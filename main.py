from stuff.lexer import Lexer
from stuff.parser import Parser
from codegen import CodeGen

# fname = "input.q"
# with open(fname) as f:
#     text_input = f.read()

text_input = """

begin
int b = 22;
int f = 33;
flo e = 22.9;
if (22 > 3){ int a = 6; };
write(2);
end                                                                           
                             
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

# for token in tokens:
#     print(token)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()

# parser.parse(tokens).eval()

nodes = parser.parse(tokens)


def get_last_element(lst):
    if isinstance(lst, list):
        return get_last_element(lst[-1])
    else:
        return lst


print(nodes)
for node in nodes:
    if type(node) == type(list()):
        item = get_last_element(node)
        print('\n',item)
        item.eval()
    else:
        node.eval()

codegen.create_ir()
codegen.save_ir("output.ll")
