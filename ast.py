from llvmlite import ir

variables = {}
class Numb():
    def __init__(self, builder, module, value):
        self.value = value
        self.builder = builder
        self.module = module

    def eval(self):
        i = ir.Constant(ir.IntType(32), int(self.value))
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


class ASSIGN():
    def __init__(self, builder, module, id, value):
        self.builder = builder
        self.module = module
        self.id = id
        self.value = value

    def eval(self):
        i = self.builder.alloca(ir.IntType(32), name=self.id)
        variables[self.id] = i
        self.builder.store(ir.Constant(ir.IntType(32), self.value), i)

class Write():
    def __init__(self, builder, module, printf, value):
        self.value = value
        self.builder = builder
        self.module = module
        self.printf = printf

    def eval(self):
        value = self.value.eval()

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
