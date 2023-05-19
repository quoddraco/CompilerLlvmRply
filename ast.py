from llvmlite import ir

variables_return_func = {}
variables = {}
class Numb():
    def __init__(self, builder, value):
        self.value = value
        self.builder = builder

    def eval(self,builder):
        if '.' not in self.value:
          i = ir.Constant(ir.IntType(32), int(self.value))
        else:
          i = ir.Constant(ir.DoubleType(), float(self.value))
        return i

class Id():
    def __init__(self, builder, module, id):
        self.id = id
        self.builder = builder
        self.module = module

    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        if self.id not in variables:
            raise NameError(f"Variable '{self.id}' is not defined")
        r = builder.load(variables[self.id])
        print(r)
        return r

class Sum():
    def __init__(self, builder, left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.add(self.left.eval(builder), self.right.eval(builder))
        return i


class Sub():
    def __init__(self, builder, left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.sub(self.left.eval(builder), self.right.eval(builder))
        return i


class Mult():
    def __init__(self, builder, left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.mul(self.left.eval(builder), self.right.eval(builder))
        return i


class Div():
    def __init__(self, builder,left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.sdiv(self.left.eval(builder), self.right.eval(builder))
        return i


class Mod():
    def __init__(self, builder,left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.srem(self.left.eval(builder), self.right.eval(builder))
        return i

class Equality():
    def __init__(self, builder,left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.icmp_signed('==', self.left.eval(builder), self.right.eval(builder))
        return i

class LessThan():
    def __init__(self, builder,left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.icmp_signed('<', self.left.eval(builder), self.right.eval(builder))
        return i

class GreaterThan():
    def __init__(self, builder,left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.icmp_signed('>', self.left.eval(builder), self.right.eval(builder))
        return i

class LogicalNegation():
    def __init__(self, builder,left, right):
        self.builder = builder
        self.left = left
        self.right = right
    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        i = builder.icmp_signed('!=', self.left.eval(builder), self.right.eval(builder))
        return i

class WhileStatement:
    def __init__(self, builder, module, condition, body):
        self.builder = builder
        self.module = module
        self.condition = condition
        self.body = body

    def eval(self,builder = None):
        if builder == None:
            builder = self.builder

        w_cond_head = builder.append_basic_block("w_cond_head")
        w_body_block = builder.append_basic_block("w_body")
        w_after_block = builder.append_basic_block("w_after")

        builder.branch(w_cond_head)
        builder.position_at_start(w_cond_head)

        condition_val = self.condition.eval(builder)
        builder.cbranch(condition_val, w_body_block, w_after_block)

        builder.position_at_start(w_body_block)

        for statement in self.body:
            statement.eval(builder)
        condition_val = self.condition.eval(builder)
        builder.cbranch(condition_val, w_body_block, w_after_block)
        # self.builder.branch(w_after_block)

        builder.position_at_start(w_after_block)

class IfStatement:
    def __init__(self, builder, module, condition, if_body, else_body=None):
        self.builder = builder
        self.module = module
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        # вычисляем значение условного выражения
        condition_val = self.condition.eval(builder)

        # создаем блоки базовых блоков для тела if и else
        if_bb = builder.append_basic_block("if")
        else_bb = builder.append_basic_block("else")
        merge_bb = builder.append_basic_block("merge")

        # создаем инструкцию условного перехода в блок if, если значение условия истинно,
        # и в блок else в противном случае
        builder.cbranch(condition_val, if_bb, else_bb)

        # выполняем тело if
        builder.position_at_start(if_bb)
        for statement in self.if_body:
            statement.eval(builder)
        builder.branch(merge_bb)

        # выполняем тело else, если оно есть
        builder.position_at_start(else_bb)
        if self.else_body is not None:
            for statement in self.else_body:
                statement.eval(builder)
        builder.branch(merge_bb)

        # переходим к блоку слияния
        builder.position_at_start(merge_bb)

        # self.builder.position_at_start(self.module.get_function("main").entry_basic_block)

class PereASSIGN():
    def __init__(self, builder, module, id, value):
        self.builder = builder
        self.module = module
        self.id = id
        self.value = value

    def eval(self,builder = None):
        if builder == None:
            builder = self.builder
        if isinstance(self.value, str):
            builder.store(ir.Constant(ir.IntType(32), self.value), variables[self.id])

        else:
            value = self.value.eval(builder)
            builder.store(value, variables[self.id])


class ASSIGN():
    def __init__(self, builder, module, id, value):
        self.builder = builder
        self.module = module
        self.id = id
        self.value = value

    def eval(self,builder = None):
        if builder == None:
            builder = self.builder

        if isinstance(self.value, str):

           if "." not in self.value:
              i = builder.alloca(ir.IntType(32), name=self.id)
              variables[self.id] = i
              builder.store(ir.Constant(ir.IntType(32), self.value), i)

           elif "." in self.value:
               i = builder.alloca(ir.DoubleType(), name=self.id)
               variables[self.id] = i
               builder.store(ir.Constant(ir.DoubleType(), self.value), i)
        else:
            i = builder.alloca(ir.IntType(32), name=self.id)
            variables[self.id] = i
            value = self.value.eval(builder)
            builder.store(value, i)


class FuncStatement():
    def __init__(self, builder, module, name, body):
        self.builder = builder
        self.module = module
        self.name = name
        self.body = body

    def eval(self):
        func_type = ir.FunctionType(ir.VoidType(), [])
        func = ir.Function(self.module, func_type, name=self.name)

        # Генерируем тело функции
        block = func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        for statement in self.body:
            statement.eval(self.builder)

        self.builder.ret_void()

class ReturnStatement():
    def __init__(self, builder,id):
        self.builder = builder
        self.id = id

    def eval(self,builder = None):
        if builder == None:
            builder = self.builder

        id_value = self.id.eval(builder)
        print(id_value)
        variables_return_func[builder] = id_value
        print(variables_return_func)





class Write():
    def __init__(self, builder, module, printf, value, idfstr):
        self.value = value
        self.builder = builder
        self.module = module
        self.printf = printf
        self.idfstr = idfstr

    def eval(self):
        value = self.value.eval()

        # Объявление списка аргументов
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        namefstr = f"fstr{self.idfstr}"
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=namefstr)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Вызов ф-ии Print
        self.builder.call(self.printf, [fmt_arg, value])


