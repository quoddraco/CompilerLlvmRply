from llvmlite import ir
import llvmlite.binding as llvm

import os


def create_global_string(builder: ir.IRBuilder, s: str, name: str) -> ir.Instruction:
    type_i8_x_len = ir.types.ArrayType(ir.types.IntType(8), len(s))
    value = ir.Constant(type_i8_x_len, bytearray(s.encode('utf-8')))

    variable = ir.GlobalVariable(builder.module, type_i8_x_len, name)
    variable.linkage = 'private'
    variable.unnamed_addr = True
    variable.global_constant = True
    variable.initializer = value
    variable.align = 1

    zero = ir.Constant(ir.types.IntType(32), 0)
    return variable.gep((zero, zero))


module = ir.Module(name="demo")

puts_type = ir.FunctionType(ir.IntType(32), (ir.IntType(8).as_pointer(),), var_arg=True)
puts_func = ir.Function(module, puts_type, "printf")

main_type = ir.FunctionType(ir.IntType(32), ())
main_func = ir.Function(module, main_type, "main")

block = main_func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)
msg = create_global_string(builder, 'Hello,world!\n', "msg")

result = builder.call(puts_func, (msg,))
builder.ret(result)

print(module)

# generate bc
module_ref = llvm.parse_assembly(str(module))
module_ref.verify()
open("test03.bc", "wb").write(module_ref.as_bitcode())

# generate obj
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine(codemodel="small")

module.triple = llvm.get_default_triple()
module.data_layout = target_machine.target_data

obj = target_machine.emit_object(module_ref)
open('demo.o', 'wb').write(obj)

print("="*25, "execute", "="*25)
os.system("clang demo.o -o demo.exe")
os.system("demo.exe")