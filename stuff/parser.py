from rply import ParserGenerator
from ast import Numb, Sum, Sub, Write, Mult, Div, Mod, ASSIGN, Id


class Parser:
    def __init__(self, module, builder, printf):
        self.variables = {}
        self.pg = ParserGenerator(
            # Список всех токенов, принятых парсером.
            ['Numb', 'Write', 'LParen', 'RParen',
             'SemiColon', 'Sum', 'Sub', 'Multi', 'Div', 'Mod', 'ID', 'ASSIGN', 'Int','Begin','End'],
            precedence=[("left", ["Sum","Sub"]),("right", ["Multi", 'Div', 'Mod'])]
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : Begin body  End')
        def program_expression(p):
            print("1====", p[1], "====")
            return p[1]

        @self.pg.production('body : stmts')
        def block(p):
            return p[0]

        @self.pg.production('stmts : stmts stmt')
        def stmts_b(p):
            if p[1] is None:
                return p[0]
            else:
                return p[0] + [p[1]]

        @self.pg.production('stmts : stmt')
        def stmts_stmt(p):
            if p[0] is None:
                return []
            else:
                return [p[0]]

        @self.pg.production('stmt : stmt_write SemiColon')
        @self.pg.production('stmt : stmt_assign SemiColon')
        def stmt(p):
            return p[0]

        @self.pg.production('stmt_write : Write LParen expression RParen')
        def prints(p):
            print("++++3 ", p)
            return Write(self.builder, self.module, self.printf, p[2])


        @self.pg.production('stmt_assign : Int ID ASSIGN expression')
        def assign(p):
            print("++++6 ", p)
            return ASSIGN(self.builder, self.module, p[1].value, p[3].value)

        @self.pg.production('expression : expression Sum expression')
        @self.pg.production('expression : expression Sub expression')
        @self.pg.production('expression : expression Multi expression')
        @self.pg.production('expression : expression Div expression')
        @self.pg.production('expression : expression Mod expression')
        def expression(p):
            print("++++4 ", p)
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'Sum':
                return Sum(self.builder, self.module,left, right)
            elif operator.gettokentype() == 'Sub':
                return Sub(self.builder, self.module,left, right)
            elif operator.gettokentype() == 'Multi':
                return Mult(self.builder, self.module,left, right)
            elif operator.gettokentype() == 'Div':
                return Div(self.builder, self.module,left, right)
            elif operator.gettokentype() == 'Mod':
                return Mod(self.builder, self.module,left, right)

        @self.pg.production('expression : LParen expression RParen')
        def paren_exp(p):
            print("++++++++8",p)
            return p[1]

        @self.pg.production('expression : Numb')
        def number(p):
            print("++++5 ", p)
            return Numb(self.builder, self.module,p[0].value)

        @self.pg.production('expression : ID')
        def id(p):
            print("++++7 ", p)
            return Id(self.builder, self.module,p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
