import sys

# following 3 lines were necessary to import SmallCLexer and SmallCParser
import os
lib_path = os.path.abspath(os.path.join('..', 'grammar'))
sys.path.append(lib_path)

from antlr4 import *
from SmallCLexer import SmallCLexer
from SmallCParser import SmallCParser
# from KeyPrinter import KeyPrinter
from AST import AST


def main(argv):
    input = FileStream(argv[1])
    lexer = SmallCLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SmallCParser(stream)
    tree = parser.smallc_program()
    #printer = KeyPrinter()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)

    ast = AST()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('ERROR: 2 arguments needed: `input.c` and `output.p`')
    main(sys.argv)