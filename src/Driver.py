import sys
from antlr4 import *
from LangGrammarLexer import LangGrammarLexer
from LangGrammarParser import LangGrammarParser
from LangGrammarListener import LangGrammarListener
from colorama import Fore

def printErr(error_msg: str):
    print(Fore.RED + "Error: " + Fore.RESET + error_msg)
    exit()

def main(argv):
    input_stream = FileStream(argv[1])

    lexer = LangGrammarLexer(input_stream)
    
    stream = CommonTokenStream(lexer)
    
    parser = LangGrammarParser(stream)
    
    tree = parser.prog()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        printErr("The program contains syntax errors")
    
    else:
        listener = LangGrammarListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)