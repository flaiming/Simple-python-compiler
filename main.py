import sys
from lexer import *
from parsing import Parser
from executioner import Executioner
            
def main():
    parser = Parser()
    stmt = parser.parseFile(sys.argv[1])
    print stmt
    print parser.getSymbolTable()
    executioner = Executioner(parser.getSymbolTable())
    executioner.execStatementList(stmt)

if __name__ == "__main__":
    main()
