#Lista de erros: Delimitadores que abrem sem fechar: (){}[], abertura sem fechamento de comentários: /**/
# Abertura sem fechamento de aspas simples e aspas duplas, inserção de simbolos não aceitos: ♫ » etc. (altcode),
# Inserção de caracteres com acento: â ü etc (Consideraremos isso erro?).
from finiteAutomaton import LexicalFiniteAutomaton

def lexical_analise():
	file_name = './input/teste.txt'
	file = open_file(file_name)
	if (file):
		finiteAutomaton = LexicalFiniteAutomaton()
		finiteAutomaton.recognize_tokens(file)
		file.close()

	for item in finiteAutomaton.show_token_list():
		print(item)

def open_file(file_name):
	try:
		file = open(file_name, "r")
	except FileNotFoundError:
		print("O Arquivo não foi encontrado.")
	else:
		return file
	
if __name__ == "__main__":
    lexical_analise()