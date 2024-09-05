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
        match self.state:
            case 0:
                if (re.match(r'[a-z]|[A-Z]',character)):
                    self.lexeme += character
                    self.state = 1   
                elif (re.match(r'[0-9]',character)):
                    self.lexeme += character
                    self.state = 2
                elif (character == '"'):
                    print("entrei aqui")
                    self.lexeme += character
                    self.state = 5
                elif (character == "'"):
                    self.lexeme += character
                    self.state = 7
                
                elif (character == "+"):
                    self.lexeme += character
                    # direcionar para estado ou salva direto
                elif (character == "-"):
                    self.lexeme += character
                    # direcionar para estado ou salva direto
                elif (character == "*"):
                    self.lexeme += character
                    # direcionar para estado ou salva direto
                elif (character == "/"):
                    self.lexeme += character
                        # direcionar para estado ou salva direto
                elif (character == "="):
                    self.lexeme += character
                        # direcionar para estado ou salva direto
                elif (character == "!"):
                    self.lexeme += character
                        # direcionar para estado ou salva direto
                elif (character == ">"):
                    self.lexeme += character
                        # direcionar para estado ou salva direto
                elif character == "<":
                    self.lexeme += character
                        # direcionar para estado
                elif character == "&":
                    self.lexeme += character
                        # direcionar para estado
                elif character == "|":
                    self.lexeme += character
                        # direcionar para estado
                elif character == ".":
                    self.lexeme += character
                        # direcionar para estado
                elif character == ";":
                    self.lexeme += character
                        # direcionar para estado
                elif character == ",":
                    self.lexeme += character
                        # direcionar para estado
                elif character == "(":
                    self.lexeme += character
                        # direcionar para estado
                elif character == ")":
                    self.lexeme += character
                        # direcionar para estado
                elif character == "{":
                    self.lexeme += character
                        # direcionar para estado
                elif character == "}":
                    self.lexeme += character
                        # direcionar para estado
                elif character == "[":
                    self.lexeme += character
                        # direcionar para estado
                elif character == "]":
                    self.lexeme += character
            
            case 1:
                if (re.match(r'[a-zA-Z0-9]',character)) or (re.match(r'_',character)):
                    self.lexeme += character
                else:
                    self.save_token_and_restart(character, line_number, TokenType.IDENTIFIER)
                    self.find_lexeme(character, line_number)
            case 2:
                if (re.match(r'[0-9]', character)) :
                    self.lexeme += character
                elif (character == "."):
                    self.lexeme += character
                    self.state = 3
                else:
                    self.save_token_and_restart(character, line_number, TokenType.NUMBER)
                    self.find_lexeme(character, line_number)
            case 3:
                if (re.match(r'[0-9]', character)) :
                    self.lexeme += character
                    self.state = 4
                else:
                    self.lexeme += character
                    self.register_error_and_restart(character, line_number,TokenType.NUMBER_ERROR)
                    #registra erro, pq depois do ponto deve ter pelo menos 1 numero
                    # volta para o estado 0
            case 4:
                if (re.match(r'[0-9]', character)) :
                    self.lexeme += character
                else:
                    self.save_token_and_restart(character, line_number, TokenType.NUMBER)
                    self.find_lexeme(character, line_number)
            # REVER A QUESTAO DE QUANDO É ERRO, JÁ QUE TEM DIVERSAS SITUAÇÕES
            case 5:
                if (character == '"'):
                    self.lexeme += character
                    self.save_token_and_restart(character, line_number, TokenType.STRING)
                elif (32<=ord(character)<=126 and character != "'"):
                    self.lexeme += character
                    print(self.lexeme)
                elif (character == "\n"):
                    self.register_error_and_restart(character, line_number,TokenType.STRING_ERROR)
                else:
                    self.lexeme += character
                    self.state = 6
            case 6:
                if character == '"':
                    self.lexeme += character
                    self.register_error_and_restart(character, line_number,TokenType.STRING_ERROR)
                    #É ERRO. OS CARACTERES DA STRING TEM QUE ESTAR DENTRO DOS SIMBOLOS PERMITIDOS
                else:
                    self.lexeme += character
            #REVER A QUESTÃO DE QUANDO É ERRO
            case 7:
                if ((32<=ord(character)<=126) and character != '"' and character != "'"):
                    self.lexeme += character
                    self.state = 8
                else:
                    self.register_error_and_restart(character, line_number,TokenType.CHARACTER_INVALID)
                    self.find_lexeme(character, line_number)
                    #Erro. Tem que ter uma letra,digito simbolo depois de '
            case 8:
                if character == "'":
                    self.lexeme += character
                    self.save_token_and_restart(character, line_number, TokenType.CHARACTER)
                else:
                    self.register_error_and_restart(character, line_number,TokenType.CHARACTER_INVALID)
                    self.find_lexeme(character, line_number)




    def save_token_and_restart(self, character, line_number, token_type):
        if token_type != TokenType.LINE_COMMENT and token_type != TokenType.BLOCK_COMMENT:
            self.token_valid_list.append(Token.get_token(self.lexeme, token_type, line_number))
        self.restart(character, line_number)

    def register_error_and_restart(self, character, line_number, token_type):
        self.error_list.append(Token.get_token(self.lexeme, token_type, line_number))
        self.restart(character, line_number)

    def restart(self, character, line_number):
        self.lexeme = ''
        self.state = 0

    def show_token_list(self):
        return self.token_valid_list

    def show_error_list(self):
        return self.error_list

    def recognize_tokens(self, file):
        for line_number, line in enumerate(file, start=1):
            for character in line:
                self.find_lexeme(character, line_number)
        