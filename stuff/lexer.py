from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('Begin', r'begin')
        self.lexer.add('End', r'end')

        # Print
        self.lexer.add('Write', r'write')
        # Скобки
        self.lexer.add('LParen', r'\(')
        self.lexer.add('RParen', r'\)')
        self.lexer.add('LBracket', r'\{')
        self.lexer.add('RBracket', r'\}')

        # Точка с запятой
        self.lexer.add('SemiColon', r'\;')
        self.lexer.add('Comma', r',')

        # Операторы
        self.lexer.add('Sum', r'\+')
        self.lexer.add('Sub', r'\-')
        self.lexer.add('Multi', r'\*')
        self.lexer.add('Div', r'div')
        self.lexer.add('Mod', r'mod')
        self.lexer.add('LogicEquality', r'==')
        self.lexer.add('ASSIGN', r'=')


        self.lexer.add('LessThan', r'\<')
        self.lexer.add('GreaterThan', r'\>')
        self.lexer.add('LogicalNegation', r'\!=')
        self.lexer.add('LogicalAnd', r'\and')
        self.lexer.add('LogicalOr ', r'\|\|')

        self.lexer.add('While', r'while')
        self.lexer.add('Return', r'return')
        self.lexer.add('If', r'if')
        self.lexer.add('Func', r'func')

        # Числа
        self.lexer.add('NumbFlo', r'\d+\.\d+')
        self.lexer.add('Float', r'flo')
        self.lexer.add('Numb', r'\d+')
        self.lexer.add('Int', r'int')
        self.lexer.add('String', r'str')
        self.lexer.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')


        # Игнорируем пробелы
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()