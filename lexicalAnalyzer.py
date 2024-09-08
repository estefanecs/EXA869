#Lista de erros: Delimitadores que abrem sem fechar: (){}[], abertura sem fechamento de comentários: /**/
# Abertura sem fechamento de aspas simples e aspas duplas, inserção de simbolos não aceitos: ♫ » etc. (altcode),
# Inserção de caracteres com acento: â ü etc (Consideraremos isso erro?).
from finiteAutomaton import LexicalFiniteAutomaton

def lexical_analise():
	file_name = input("Digite o nome do arquivo de leitura (ex: './input/teste.txt'): ")

	file = open_file(file_name)
	if (file):
		finiteAutomaton = LexicalFiniteAutomaton()
		finiteAutomaton.recognize_tokens(file)
		file.close()

	write_file("tokens_list.txt", finiteAutomaton.show_token_list(), "Nenhum Token foi encontrado.")
	write_file("error_token_list.txt", finiteAutomaton.show_error_list(), "Sucesso. Nenhum erro foi encontrado.")
	for item in finiteAutomaton.show_token_list():
		print(item)

	print("----------- erro")
	for item in finiteAutomaton.show_error_list():
		print(item)

def open_file(file_name):
	try:
		file = open(file_name, "r")
	except FileNotFoundError:
		print("O Arquivo não foi encontrado.")
	else:
		return file
	
def write_file(file_name, list, message):
	with open(file_name, "w") as file:
		if not list:
			file.write(message)
			return
		for item in list:
			file.write(f"Lexeme: {item['lexeme']}, Category: {item['category']}, Line: {item['line']}\n")

if __name__ == "__main__":
    lexical_analise()