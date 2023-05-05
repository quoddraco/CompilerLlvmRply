from llvmlite import ir

variables = {}
class Numb():
    def __init__(self, builder, module, value):
        self.value = value
        self.builder = builder
        self.module = module

    def eval(self):
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

    def eval(self):
        if self.id not in variables:
            raise NameError(f"Variable '{self.id}' is not defined")
        r = self.builder.load(variables[self.id])
        return r


class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i


class Sub(BinaryOp):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i


class Mult(BinaryOp):
    def eval(self):
        i = self.builder.mul(self.left.eval(), self.right.eval())
        return i


class Div(BinaryOp):
    def eval(self):
        i = self.builder.sdiv(self.left.eval(), self.right.eval())
        return i


class Mod(BinaryOp):
    def eval(self):
        i = self.builder.srem(self.left.eval(), self.right.eval())
        return i

class Equality(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('==', self.left.eval(), self.right.eval())
        return i

class LessThan(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('<', self.left.eval(), self.right.eval())
        return i

class GreaterThan(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('>', self.left.eval(), self.right.eval())
        return i

class LogicalNegation(BinaryOp):
    def eval(self):
        i = self.builder.icmp_signed('!=', self.left.eval(), self.right.eval())
        return i

class IfStatement():
    def __init__(self,builder, module,condition, if_body, else_body=None):
        self.builder = builder
        self.module = module
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

    def eval(self):
        # Оценка условия
        condition_value = self.condition.eval()

        # Создание блоков для ветвей if и else
        if_block = self.builder.append_basic_block('if')
        else_block = self.builder.append_basic_block('else')
        merge_block = self.builder.append_basic_block('merge')

        # Переход к соответствующему блоку
        self.builder.cbranch(condition_value, if_block, else_block)

        # Генерация кода для блока if
        self.builder.position_at_end(if_block)
        if_value = self.if_body.eval()
        self.builder.branch(merge_block)

        # Генерация кода для блока else
        self.builder.position_at_end(else_block)
        if self.else_body is not None:
            else_value = self.else_body.eval()
        self.builder.branch(merge_block)

        # Генерация кода для блока merge
        self.builder.position_at_end(merge_block)
        if self.else_body is not None:
            phi = self.builder.phi(if_value.type, 'iftmp')
            phi.add_incoming(if_value, if_block)
            phi.add_incoming(else_value, else_block)
            return phi
        else:
            return if_value


class ASSIGN():
    def __init__(self, builder, module, id, value):
        self.builder = builder
        self.module = module
        self.id = id
        self.value = value

    def eval(self):
        if "." not in self.value:
           i = self.builder.alloca(ir.IntType(32), name=self.id)
           variables[self.id] = i
           self.builder.store(ir.Constant(ir.IntType(32), self.value), i)
        elif "." in self.value:
            i = self.builder.alloca(ir.DoubleType(), name=self.id)
            variables[self.id] = i
            self.builder.store(ir.Constant(ir.DoubleType(), self.value), i)
class Write():
    def __init__(self, builder, module, printf, value):
        self.value = value
        self.builder = builder
        self.module = module
        self.printf = printf

    def eval(self):
        print(self.value)
        value = self.value.eval()
        print(value.type)

        # Объявление списка аргументов
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Вызов ф-ии Print
        self.builder.call(self.printf, [fmt_arg, value])
        # if "i32" in str(value):
        #
        # # Объявление списка аргументов
        #    voidptr_ty = ir.IntType(8).as_pointer()
        #    fmt = "%i \n\0"
        #    c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
        #                     bytearray(fmt.encode("utf8")))
        #    global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        #    global_fmt.linkage = 'internal'
        #    global_fmt.global_constant = True
        #    global_fmt.initializer = c_fmt
        #    fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
        #
        # # Вызов ф-ии Print
        #    self.builder.call(self.printf, [fmt_arg, value])
        #
        # elif "double" in str(value):
        #     print("ddddddddddddd", value)
        #
        #     # Объявление списка аргументов
        #     voidptr_ty = ir.DoubleType().as_pointer()
        #     fmt = "%double \n\0"
        #     c_fmt = ir.Constant(ir.ArrayType(ir.DoubleType(), len(fmt)),
        #                         bytearray(fmt.encode("utf8")))
        #     global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        #     global_fmt.linkage = 'internal'
        #     global_fmt.global_constant = True
        #     global_fmt.initializer = c_fmt
        #     fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
        #
        #     # Вызов ф-ии Print
        #     self.builder.call(self.printf, [fmt_arg, value])


