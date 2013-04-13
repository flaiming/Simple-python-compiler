import sys
from lexer import do_lex, TokenTypes          
            

def doStatementList(tokens):
    stmts = []
    newstmt = []
    
#    def consume(token,expected):
#        if token == expected:
#            return True
#        else:
#            print "expected " + expected + " not found" 
#            return False
    
    while len(tokens) > 0:
        token, type = tokens.pop()
        print token, type
        if type == TokenTypes.RESERVED:
            
            if token == 'DEFINE':
                token, type = tokens.pop()
                if type != TokenTypes.ID:
                    print "Syntax error! Expected ID."
                    exit(1)
                identif = token
                
                token, type = tokens.pop()
                print token, type
                if type != TokenTypes.RESERVED or token != 'AS':
                    print "Syntax error! Expected AS."
                    exit(1)
                
                newstmt = ("DEFINE", identif, None)
            
            #newstmt.append(doStatementList())
#            consume(token, "END")
        elif type == TokenTypes.ID:
            # ["if", [condition], [then part], [else part]]
            #nic zatim
            pass
        else:
            print "invalid statement: " + token
        stmts.append(newstmt)
    return stmts         

def main():
    filename = sys.argv[1]
    inputfile = open(filename, "r")
    inputstring = inputfile.read()
    tokens = do_lex(inputstring)
    print tokens
    tokens.reverse()
    print doStatementList(tokens)
    
    

if __name__ == "__main__":
    main()