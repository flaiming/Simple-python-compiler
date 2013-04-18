import sys
import re

#operators = {
#             ':=': r'\:=',
#             '(': r'\(',
#             '}': r'\}',
#             ';': r';',
#             '+': r'\+',
#             '-': r'-',
#             '*': r'\*',
#             '/': r'/',
#             }
#
#conditions = {'==': r'==',
#              '!=': r'!=',
#              '<': r'<',
#              '<=': r'<=',
#              '>': r'>',
#              '>=': r'>=',
#              }
#
#keywords = {
#            'if': r'if',
#            'else': r'else',
#            'endif': r'endif',
#            'while': r'while',
#            'endwhile': r'endwhile',
#            'print': r'print',
#            }
#
#number = {
#           'digit': r'[0-9]+'
#           }
#
#identifier = {
#           'label': r'[A-Za-z][A-Za-z0-9_]*'
#           }
#
#blanks = {
#          '1': r'[ \n\t]+',
#          '2': r'#[^\n]*',
#          }

class TokenTypes(object):
    RESERVED = 'RESERVED'
    INT      = 'INT'
    ID       = 'ID'

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
    (r'==',                     TokenTypes.RESERVED),
    (r'!=',                    TokenTypes.RESERVED),
    (r'and',                   TokenTypes.RESERVED),
    (r'or',                    TokenTypes.RESERVED),
    (r'not',                   TokenTypes.RESERVED),
    (r'if',                    TokenTypes.RESERVED),
    (r'then',                  TokenTypes.RESERVED),
    (r'else',                  TokenTypes.RESERVED),
    (r'endif',                 TokenTypes.RESERVED),
    (r'while',                 TokenTypes.RESERVED),
    (r'endwhile',                 TokenTypes.RESERVED),
    (r'print',                 TokenTypes.RESERVED),
    (r'[0-9]+',                TokenTypes.INT),
    (r'[A-Za-z][A-Za-z0-9_]*', TokenTypes.ID),
]

def lex(characters, token_exprs):
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
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

#def transform():
#    exprs = operators.values() + conditions.values() + keywords.values()
#    reserved = []
#    for e in exprs:
#        reserved.append((e, TokenTypes.RESERVED))
#    
#    none = []
#    for b in blanks.values():
#        none.append((b, None))
#        
#    return none + reserved + [(number.values()[0], TokenTypes.INT)] + [(identifier.values()[0], TokenTypes.ID)]

def do_lex(characters):
#    exprs = transform()
#    print exprs
    return lex(characters, token_exprs)