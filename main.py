import sys

from lexer import doLex
from parsing import Parser
from executioner import Executioner
            
def main():
    
    if len(sys.argv) <= 1:
        print "Please enter file name to parse."
        exit(0)
    
    #open file
    filename = sys.argv[1]
    inputstring = ""
    try:
        inputfile = open(filename, "r")
        inputstring = inputfile.read()
    except IOError:
        print "File '%s' cannot be open for reading." % filename
        exit(1)
    
    #do lexical analysis
    tokenlist = doLex(inputstring)
    print tokenlist
    
    #parse
    parser = Parser()
    stmt = parser.parseTokens(tokenlist)
    print stmt
    print parser.getSymbolTable()
    
    #execute
    executioner = Executioner(parser.getSymbolTable())
    executioner.execStatementList(stmt)

if __name__ == "__main__":
    main()
