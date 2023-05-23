from stuff.lexer import Lexer
from stuff.parser import Parser
from codegen import CodeGen

def get_last_element(lst):
    if isinstance(lst, list):
        return get_last_element(lst[-1])
    else:
        return lst

# fname = "input.q"
# with open(fname) as f:
#     text_input = f.read()

text_input = """
begin
int t = 0;
flo a = 2.5;
int e = 3;
a = flo(e);
write(t);

end                                                                           
                             
"""

lexer = Lexer().get_lexer()
try:
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
    for node in nodes:
        if type(node) == type(list()):
            item = get_last_element(node)
            item.eval()
        else:
            node.eval()

    codegen.create_ir()
    codegen.save_ir("output.ll")
except Exception as e:
    if hasattr(e, "source_pos"):
        line = e.source_pos.lineno
        print("Parsing Error at line", line)
    else:

        print("Parsing Error:", e)





