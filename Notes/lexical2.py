import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []
        self.keywords = ['if', 'else', 'while', 'for', 'break', 'continue', 'return']
        self.preprocessor_directives = ['#include', '#define', '#ifdef', '#ifndef', '#endif']

    def tokenize(self):
        while self.pos < len(self.code):
            if self.code[self.pos].isdigit():
                self.tokenize_number()
            if self.code[self.pos].isalpha() or self.code[self.pos] == '_':
                self.tokenize_identifier()
            elif self.code[self.pos] == '#':
                self.tokenize_preprocessor_directive()
            elif self.code[self.pos].isspace():
                self.pos += 1
            else:
                # self.tokens.append(('symbol', self.code[self.pos]))
                self.pos += 1

    def tokenize_number(self):
        num = ''
        while self.pos < len(self.code) and self.code[self.pos].isdigit():
            num += self.code[self.pos]
            self.pos += 1
        self.tokens.append(('number', int(num)))

    def tokenize_identifier(self):
        identifier = ''
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == '_'):
            identifier += self.code[self.pos]
            self.pos += 1
        if identifier not in self.keywords:
            self.tokens.append(('identifier', identifier))
        # else:
        #     self.tokens.append(('identifier', identifier))

    def tokenize_preprocessor_directive(self):
        directive = ''
        while self.pos < len(self.code) and not self.code[self.pos].isspace():
            directive += self.code[self.pos]
            self.pos += 1
        if directive in self.preprocessor_directives:
            self.tokens.append(('preprocessor', directive))
        else:
            self.tokens.append(('symbol', '#'))

    def display_tokens(self):
        for token in self.tokens:
            print(token)

# Example usage
code = '''
#include <stdio.h>

int main() {
    int x = 123;
    printf("x = %d", x);
    return 0;
}
'''

lexer = Lexer(code)
lexer.tokenize()
lexer.display_tokens()