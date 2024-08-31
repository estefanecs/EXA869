import re

from tokenType import TokenType
from token import Token

class LexicalFiniteAutomaton:

    def __init__(self):
        self.token_valid_list = []
        self.error_list = []
        self.lexeme = ''
        self.state = 0

#ver pagina 46(do livro msm) a questão da implementação da tabela de simbolos
    def find_lexeme(self, character, line_number):
        print(character)
        match self.state:
            case 0:
                if re.match(r'[a-z]|[A-Z]',character):
                    self.lexeme += character
                    self.state = 1        
            case 1:
                if (re.match(r'[a-zA-Z0-9]',character)) or (re.match(r'_',character)):
                    self.lexeme += character
                else:
                    self.save_token_and_restart(character, line_number, TokenType.IDENTIFIER)

    def save_token_and_restart (self, character, line_number, token_type):
        if token_type != TokenType.LINE_COMMENT and token_type != TokenType.BLOCK_COMMENT:
            self.token_valid_list.append(Token.get_token(self.lexeme, token_type, line_number))
        self.lexeme = ''
        self.state = 0
        self.find_lexeme(character, line_number)

    def show_token_list(self):
        return self.token_valid_list

    def recognize_tokens(self, file):
        for line_number, line in enumerate(file, start=1):
            for character in line:
                print(line_number)
                self.find_lexeme(character, line_number)
        