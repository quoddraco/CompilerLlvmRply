import os
from llvmlite import ir, binding


class CodeGen():
    def __init__(self):
        self.mod = None
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._config_llvm()
        self._create_execution_engine()
        self._declare_print_function()

    def _config_llvm(self):
        # Config LLVM
        self.module = ir.Module(name=__file__)
        self.module.triple = self.binding.get_default_triple()
        func_type = ir.FunctionType(ir.VoidType(), [], False)
        base_func = ir.Function(self.module, func_type, name="main")
        block = base_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def _create_execution_engine(self):
        """
        Create an ExecutionEngine suitable for JIT code generation on
        the host CPU.  The engine is reusable for an arbitrary number of
        modules.
        """
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        # And an execution engine with an empty backing module
        backing_mod = binding.parse_assembly("")
        engine = binding.create_mcjit_compiler(backing_mod, target_machine)
        self.engine = engine
        
    def optimization(self,module_ref):
        pass_manager_builder = binding.create_pass_manager_builder()

        module_pass_manager = binding.create_module_pass_manager()

        module_pass_manager.add_constant_merge_pass()
        module_pass_manager.add_dead_arg_elimination_pass()
        module_pass_manager.add_function_attrs_pass()
        module_pass_manager.add_function_inlining_pass(5)
        module_pass_manager.add_global_dce_pass()
        module_pass_manager.add_global_optimizer_pass()
        module_pass_manager.add_ipsccp_pass()
        module_pass_manager.add_dead_code_elimination_pass()
        module_pass_manager.add_cfg_simplification_pass()
        module_pass_manager.add_gvn_pass()
        module_pass_manager.add_instruction_combining_pass()
        module_pass_manager.add_licm_pass()
        module_pass_manager.add_sccp_pass()
        module_pass_manager.add_sroa_pass()
        module_pass_manager.add_type_based_alias_analysis_pass()
        module_pass_manager.add_basic_alias_analysis_pass()

        pass_manager_builder.populate(module_pass_manager)

        module_pass_manager.run(module_ref)
        

    def _declare_print_function(self):
        # Функция Printf
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")
        self.printf = printf

    def _compile_ir(self):
        """
        Compile the LLVM IR string with the given engine.
        The compiled module object is returned.
        """
        # Создание LLVM модуля
        self.builder.ret_void()
        llvm_ir = str(self.module)
        self.mod = self.binding.parse_assembly(llvm_ir)
        self.mod.verify()

        return self.mod

    def _apply_optimizations(self):
        # Создание пасс-менеджера для оптимизаций
        pm = self.binding.ModulePassManager()

        # Добавление оптимизаций в пасс-менеджер
        pm_builder = self.binding.PassManagerBuilder()
        pm_builder.opt_level = 3
        pm_builder.populate(pm)

        # Применение пасс-менеджера к модулю
        pm.run(self.mod)

    def create_ir(self):
        self._compile_ir()
        self._apply_optimizations()

    def save_ir(self, filename):
        with open(filename, 'w') as output_file:
            output_file.write(str(self.module))
        self.try_ir()

    def try_ir(self):
        self.mod = self.binding.parse_assembly(str(self.module))
        self.optimization(self.mod) \
            if input("Нужна оптимизация:(y/n)").lower() == "y"\
            else print(" Код без оптимизации")
        self.mod.verify()

        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()

        target = binding.Target.from_default_triple()
        target_machine = target.create_target_machine(codemodel="small")

        self.module.triple = binding.get_default_triple()
        self.module.data_layout = target_machine.target_data

        print(self.mod)
        print("Assembler:")
        asm = target_machine.emit_assembly(self.mod)
        print(asm)


        obj = target_machine.emit_object(self.mod)
        open("tester.o","wb").write(obj)
        os.system("gcc tester.o -no-pie -o output")
        os.system("./output")
