from lexer import TokenTypes, do_lex

class Parser():
    
    def __init__(self):
        self.tokenlist = []
        self.currtoken = ("", "", 0)
        self.symboltable = dict()
    
    def parseFile(self, filename):
        inputfile = open(filename, "r")
        inputstring = inputfile.read()
        self.tokenlist = do_lex(inputstring)
        print self.tokenlist
        self.nextToken()
        return self.doStatementList()
    
    def getSymbolTable(self):
        return self.symboltable
    
    def nextToken(self):
        if(len(self.tokenlist) > 0):
            s, type = self.tokenlist.pop(0)
            print s, type
            if type == TokenTypes.RESERVED:
                self.currtoken = (s, "", 0)
            elif type == TokenTypes.INT:
                self.currtoken = ("digit", "", int(s))
            elif type == TokenTypes.ID:
                self.symboltable[s] = 0
                self.currtoken = ("label", s, 0)
            else:
                print "syntax error: " + s
        else:
            self.currtoken = ("", "", 0)
    
    def consume(self, expected):
        if self.currtoken[0] == expected:
            self.nextToken()
        else:
            print "expected " + expected + " not found" 
    
    def doStatementList(self):
        stmts = []
        newstmt = []
        
        while self.currtoken[0] in ["while", "if", "print", "label"]:
            if self.currtoken[0] == "while":
                # ["while", [condition], [statementlist]]
                self.consume("while")
                newstmt = ["while"]
                newstmt.append(self.doCondition())
                newstmt.append(self.doStatementList())
                self.consume("endwhile")
            elif self.currtoken[0] == "if":
                # ["if", [condition], [then part], [else part]]
                self.consume("if")
                newstmt = ["if"]
                newstmt.append(self.doCondition())
                newstmt.append(self.doStatementList())
                if self.currtoken[0] == "else":
                    self.consume("else")
                    newstmt.append(self.doStatementList())
                self.consume("endif")
            elif self.currtoken[0] == "print":
                # ["print", [expression]]
                self.consume("print")
                newstmt = ["print"]
                newstmt.append(self.doExpression())
            elif self.currtoken[0] == "label":
                # ["=", [expression], [expression]]
                label = [self.currtoken[1]]
                self.nextToken()
                self.consume(":=")
                newstmt = [":="]
                newstmt.append(label)
                newstmt.append(self.doExpression())
            else:
                print "invalid statement: " + self.currtoken[0]
            stmts.append(newstmt)
        return stmts
    
    def doCondition(self):
        exp = self.doExpression()
        # ["==|!=", [left side], [right side]]
        if self.currtoken[0] in ["==", "!=", "<", "<=", ">", ">="]:
            retval = [self.currtoken[0]]
            retval.append(exp)
            self.nextToken()
            retval.append(self.doExpression())
        else:
            print "expected == or != not found"
        return retval
        
    def doExpression(self):
        term = self.doTerm()
        # carry the term in case there's no +|-
        exp = term
        # ["+|-", [left side], [right side]]
        while self.currtoken[0] in ["+", "-", "*", "/"]:
            exp = [self.currtoken[0]]
            self.nextToken()
            exp.append(term)
            exp.append(self.doExpression())
        return exp
    
    def doTerm(self):
        if self.currtoken[0] == "label":
            retval = self.currtoken[1]
            self.nextToken()
        elif self.currtoken[0] == "digit":
            retval = self.currtoken[2]
            self.nextToken()
        return [retval]