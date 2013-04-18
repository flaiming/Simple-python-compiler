import re

class TokenTypes(object):
    RESERVED = 'RESERVED'
    DIGIT      = 'DIGIT'
    LABEL       = 'LABEL'

token_exprs = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'\:=',                   TokenTypes.RESERVED),
    (r'\(',                    TokenTypes.RESERVED),
    (r'\)',                    TokenTypes.RESERVED),
    (r';',                     TokenTypes.RESERVED),
    (r'\+',                    TokenTypes.RESERVED),
    (r'-',                     TokenTypes.RESERVED),
    (r'\*',                    TokenTypes.RESERVED),
    (r'/',                     TokenTypes.RESERVED),
    (r'<',                     TokenTypes.RESERVED),
    (r'<=',                    TokenTypes.RESERVED),
    (r'>',                     TokenTypes.RESERVED),
    (r'>=',                    TokenTypes.RESERVED),
    (r'==',                    TokenTypes.RESERVED),
    (r'!=',                    TokenTypes.RESERVED),
    (r'and',                   TokenTypes.RESERVED),
    (r'or',                    TokenTypes.RESERVED),
    (r'not',                   TokenTypes.RESERVED),
    (r'if',                    TokenTypes.RESERVED),
    (r'then',                  TokenTypes.RESERVED),
    (r'else',                  TokenTypes.RESERVED),
    (r'endif',                 TokenTypes.RESERVED),
    (r'while',                 TokenTypes.RESERVED),
    (r'endwhile',              TokenTypes.RESERVED),
    (r'print',                 TokenTypes.RESERVED),
    (r'[0-9]+',                TokenTypes.DIGIT),
    (r'[A-Za-z][A-Za-z0-9_]*', TokenTypes.LABEL),
]


def lex(characters, token_exprs):
    """Devides input text to tokens, defined by token_exprs."""
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag is not None:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            print 'Illegal character: %s' % characters[pos]
            exit(1)
        else:
            #set current position just after matched token
            pos = match.end(0)
    return tokens

def doLex(characters):
    return lex(characters, token_exprs)