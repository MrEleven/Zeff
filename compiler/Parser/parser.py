class Tag(object):
    NUM = 256
    ID = 257
    TRUE = 258
    FALSE = 259

class Token(object):
    tag = ""
    def __init__(self, t):
        self.tag = t

class Num(Token):
    value = ""
    def __init__(self, v):
        super(Num, self).__init__(Tag.NUM)
        self.value = v

class Word(Token):
    lexeme = ""
    def __init__(self, t, s):
        super(Word, self).__init__(t)
        self.lexeme = s

class Lexer(object):
    def __init__(self):
        self.line = 1
        self.code = ""
        self.words = {}
        self.words[Tag.TRUE] = "True"
        self.words[Tag.FALSE] = "False"

    def set_code(self, code):
        self.code = code
        self.index = 0
        
    def reserve(self, t):
        self.words[t.lexeme] = t

    def read(self):
        if len(self.code) > self.index + 1:
            self.index += 1
            self.peek = self.code[self.index]
            return self.peek
        return None
        
    def scan(self):
        while True:
            self.peek = self.read()
            if self.peek == ' ' or self.peek == '\t':
                continue
            elif self.peek == '\n':
                self.line += 1
            else:
                break
        if self.peek.isdigit():
            v = 0
            while self.peek.isdigit():
                v = 10 * v + int(self.peek)
                self.peek = self.read()
            return Num(v)
        if self.peek.isalpha():
            s = ""
            while self.peek.isalnum():
                s += self.peek
                self.peek = self.read()
            if self.words.has_key(s):
                return self.words[s]
            w = Word(Tag.ID, s)
            self.words[s] = w
            return w
        t = Token(self.peek)
        self.peek = ' '
        return t

if __name__ == '__main__':
    f = open("code.txt", "r")
    code = f.read()
    f.close()
    lexer = Lexer()
    lexer.set_code(code)
    while lexer.index + 1 < len(lexer.code):
        lexer.scan()
    print lexer.words
    print lexer.words.keys()
        
    
