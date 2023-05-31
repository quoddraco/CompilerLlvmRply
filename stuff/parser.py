from rply import ParserGenerator
from rply.errors import ParserGeneratorWarning
import warnings

import ast
from ast import *

class Parser:
    def __init__(self, module, builder, printf):
        self.variables = {}
        self.pg = ParserGenerator(
            ['Numb', 'Write', 'LParen', 'RParen','LBracket','RBracket','LogicEquality','LessThan','GreaterThan',
             'LogicalNegation', 'Func', 'While', 'Return','Comma',
             'SemiColon', 'Sum', 'Sub', 'Multi', 'Div', 'Mod', 'ID', 'ASSIGN', 'Int','Begin','End','Float','NumbFlo',
             'If'],
            precedence=[("left", ["Sum","Sub"]),("right", ["Multi", 'Div', 'Mod'])]
        )
        self.module = module
        self.builder = builder
        self.printf = printf
        self.idfstr=0

    def parse(self):
        @self.pg.production('program : Begin body  End')
        def program_expression(p):
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
        @self.pg.production('stmt : stmt_if SemiColon')
        @self.pg.production('stmt : stmt_while SemiColon')
        @self.pg.production('stmt : stmt_pereassign SemiColon')
        @self.pg.production('stmt : stmt_func SemiColon')
        @self.pg.production('stmt : stmt_return SemiColon')
        def stmt(p):
            return p[0]

        @self.pg.production('stmt_func : Func ID LParen ID RParen LBracket stmts RBracket')
        def funcs(p):
            return FuncStatement(self.builder, self.module, p[1].value, p[3] , p[6])

        @self.pg.production('stmt_if : If LParen expression RParen LBracket stmts RBracket')
        def ifs(p):
            return IfStatement(self.builder, self.module, p[2], p[5], [])

        @self.pg.production('stmt_while : While LParen expression RParen LBracket stmts RBracket')
        def whiles(p):
            return WhileStatement(self.builder, self.module, p[2], p[5])

        @self.pg.production('stmt_write : Write LParen expression RParen')
        def prints(p):
            self.idfstr +=1
            return Write(self.builder, self.module, self.printf, p[2],self.idfstr)

        @self.pg.production('stmt_assign : Int ID ASSIGN expression')
        @self.pg.production('stmt_assign : Float ID ASSIGN expression')
        def assign(p):

            if isinstance(p[3], ast.Numb):
                return ASSIGN(self.builder, self.module, p[1].value, p[3].value)
            else:
                return ASSIGN(self.builder, self.module, p[1].value, p[3])

        @self.pg.production('stmt_pereassign : ID ASSIGN expression')
        def pereassign(p):

           if isinstance(p[2], ast.Numb):
               return PereASSIGN(self.builder, self.module, p[0].value, p[2].value)
           else:
               return PereASSIGN(self.builder, self.module, p[0].value, p[2])

        @self.pg.production('stmt_return : Return expression')
        def ruturn_func(p):
            return ReturnStatement(self.builder, p[1])

        @self.pg.production('expression : expression Sum expression')
        @self.pg.production('expression : expression Sub expression')
        @self.pg.production('expression : expression Multi expression')
        @self.pg.production('expression : expression Div expression')
        @self.pg.production('expression : expression Mod expression')
        @self.pg.production('expression : expression LogicEquality expression')
        @self.pg.production('expression : expression LessThan expression')
        @self.pg.production('expression : expression GreaterThan expression')
        @self.pg.production('expression : expression LogicalNegation expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'Sum':
                return Sum(self.builder, left, right)
            elif operator.gettokentype() == 'Sub':
                return Sub(self.builder, left, right)
            elif operator.gettokentype() == 'Multi':
                return Mult(self.builder, left, right)
            elif operator.gettokentype() == 'Div':
                return Div(self.builder, left, right)
            elif operator.gettokentype() == 'Mod':
                return Mod(self.builder, left, right)
            elif operator.gettokentype() == 'LogicEquality':
                return Equality(self.builder, left, right)
            elif operator.gettokentype() == 'LessThan':
                return LessThan(self.builder, left, right)
            elif operator.gettokentype() == 'GreaterThan':
                return GreaterThan(self.builder, left, right)
            elif operator.gettokentype() == 'LogicalNegation':
                return LogicalNegation(self.builder, left, right)

        @self.pg.production('expression : LParen expression RParen')
        def paren_exp(p):
            return p[1]

        @self.pg.production('expression : Numb')
        @self.pg.production('expression : NumbFlo')
        def number(p):
            return Numb(self.builder,p[0].value)

        @self.pg.production('expression : Float LParen ID RParen')
        @self.pg.production('expression : Int LParen ID RParen')
        def typecast(p):
            return Typecast(self.builder, self.module, p[0].value, p[2].value)

        @self.pg.production('expression : ID')
        def id(p):
            return Id(self.builder, self.module,p[0].value)

        @self.pg.production('expression : ID LParen expression RParen')
        def idfunc(p):
            return CallFunc(self.builder, p[0].value, p[2])

        @self.pg.error
        def error_handle(token):
            warnings.filterwarnings("ignore", category=ParserGeneratorWarning)
            raise ValueError("Syntax error at token {0} at line {1}".format(token.gettokentype(),token.source_pos.lineno-1))

    def get_parser(self):
        warnings.filterwarnings('ignore')

        return self.pg.build()
