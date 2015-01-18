import sys

"""
    一个最简单的语法制导翻译起。
    将普通表达式转化成后缀表达式。。。
    感觉没啥用处。。
"""

def read_code(code_file_name):
    f = open(code_file_name, "r")
    code = f.read()
    f.close()
    return code

class Parser(object):
    def __init__(self, code):
        self.code = code
        self.index = 0
        self.result = ""

    def _getnext(self):
        self.index += 1
        return self.code[self.index]

    @property
    def lookahead(self):
        return self.code[self.index]
    
    def expr(self):
        self.term()
        while True:
            if self.lookahead == "+":
                self.match('+')
                self.term()
                self.result += '+'
            elif self.lookahead == '-':
                self.match('-')
                self.term()
                self.result += '-'
            else:
                print self.result
                self.result = ""
                return

    def term(self):
        if self.lookahead.isdigit():
            self.result += self.lookahead;
            self.match(self.lookahead)
        else:
            raise Exception("syntax error")

    def match(self, t):
        if self.lookahead == t:
            self._getnext()
        else:
            raise Exception("syntax error")
        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: python syntax-directed-translation.py {your filename}"
    code = read_code(sys.argv[-1])
    parser = Parser(code)
    print 'start parse'
    parser.expr()
