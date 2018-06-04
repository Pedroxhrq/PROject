import csv
import os

def mainMenu():
	os.system('cls')
	print("\nMENU PRINCIPAL\n\n1- Pesquisar\n2- Inserir\n3- Listar\n4- Sair\n")
	escolha = int(input("Escolha: "))
	if escolha == 1:
		subMenu()
	elif escolha == 2:
		inserir()
	elif escolha == 3:
		listar()
	elif escolha == 4:
		sair()
	else:
		print("Escolha invalida!")

def subMenu():
	os.system('cls')
	print("\nOpções de pesquisa:\n\n1- Processo\n2- Pessoa responsável\n3- Data de retirada\n4- Data de devolução\n5- Motivo da retirada\n6- Voltar para o menu principal\n")
	escolha = int(input("Escolha: "))
	if escolha == 1:
		pesquisarProcesso()
	elif escolha == 2:
		pesquisarPessoa()
	elif escolha == 3:
		pesquisarRetirada()
	elif escolha == 4:
		pesquisarDevolucao()
	elif escolha == 5:
		pesquisarMotivo()
	elif escolha == 6:
		mainMenu()
	else:
		print("Escolha invalida!")

# subMenu

def pesquisarProcesso():
	with open("retirada_de_pastas.csv","r") as arquivo:
		registro = csv.reader(arquivo)
		processo = input("Número do processo: ")
		for row in registro:
			if row[0] == processo:
				print(row)
		pesquisarProcesso()
		input()

# def pesquisarPessoa():
# 	with open("retirada_de_pastas.csv","r") as arquivo:
# 		registro = csv.reader(arquivo)
# 		pessoa_responsavel = input("Nome da pessoa responsável: ").capitalize()
# 		for row in registro:
# 			if row[1] == pessoa_responsavel:
# 				print(row)
# 				break
# 	subMenu()
#
# def pesquisarRetirada():
# 	with open("retirada_de_pastas.csv","r") as arquivo:
# 		registro = csv.reader(arquivo)
# 		data_retirada = input("Data de retirada: ")
# 		for row[2] == data_retirada:
# 			print(row)
# 			break
# 	subMenu()
#
# def pesquisarDevolucao():
# 	with open("retirada_de_pastas.csv","r") as arquivo:
# 		registro = csv.reader(arquivo)
# 		data_devolucao = input("Data de devolução: ")
# 		for row[3] == data_devolucao:
# 			print(row)
# 			break
# 	subMenu()
#
# def pesquisarMotivo():
# 	with open("retirada_de_pastas.csv","r") as arquivo:
# 		registro = csv.reader(arquivo)
# 		motivo_retirada = input("Motivo da retirada: ").upper()
# 		for row[4] == motivo_retirada:
# 			print(row)
# 			break
# 	subMenu()
#
# mainMenu
#
# def inserir():
# 	processo = input("Processo: ")
# 	pessoa_responsavel = input("Pessoa responsável: ")
# 	data_retirada = input("Data de retirada: ")
# 	data_devolucao = input("Data de devolução: ")
# 	motivo_retirada = input("Motivo da retirada: ")
#  	controle_pastas = [processo,pessoa_responsavel,data_retirada,data_devolucao,motivo_retirada]
# 	arquivo = open("retirada_de_pastas.csv","ab+")
#  	novaLinha = "\n" + processo + ", " + pessoa_responsavel + ", " + data_retirada + ", " + data_devolucao + ", " + motivo_retirada
#  	arquivo.write(bytes(novaLinha,"UTF-8"))
# 	print("Cadastro realizado com sucesso!")
# 	arquivo.close()
# 	mainMenu()
#
# def listar():
# 	controle_listar = []
# 	arquivo = open("retirada_de_pastas.csv","rU")
# 	registro = csv.reader(arquivo)
# 	registro.__next__()
# 	print("\t\t############################\n\t\t#    Listagem de Registros:    #\n\t\t############################\n\n")
# 	for processo,pessoa_responsavel,data_retirada,data_devolucao,motivo_retirada in registro:
# 		print("Processo: " + processo)
# 		print("Pessoa responsável: " + pessoa_responsavel)
# 		print("Data de retirada: " + data_retirada)
# 		print("Data de devolução: " + data_devolucao)
# 		print("Motivo da retirada: " + motivo_retirada)
# 		print("\n------------------------------\n")
# 		controle_listar.append([processo,pessoa_responsavel,data_retirada,data_devolucao,motivo_retirada])
# 	listar()
# 	mainMenu()

def sair():
	sys.exit()

def main():
	mainMenu()
	subMenu()
	pesquisarProcesso()
	sair()

main()

# import csv
# import os
#
# over = 0
# opcao = 0
# while over == 0:
# 	os.system('cls')
# 	print("\n")
# 	opcao = int(input("Opções:\n\n1- Cadastrar Cliente\n2- Cadastrar Funcionário\n3- Listar Clientes\n4- Listar Funcionários\n5- Sair\n\nEscolha: "))
# 	print("\n")
#
# 	if opcao == 1:
# 		nome = input("Nome: ")
# 		endereco = input("Endereco: ")
# 		cidade = input("Cidade: ")
# 		telefone = input("Telefone: ")
# 		cpf = input("CPF: ")
# 		eMail = input("E-mail: ")
# 		dataNascimento = input("Data de Nascimento: ")
# 		cliente = [nome,endereco,cidade,telefone,cpf,eMail,dataNascimento]
# 		arquivo = open("cliente.csv","ab+")
# 		novaLinha = "\n" + nome + ", " + endereco + ", " + cidade + ", " + telefone + ", " + cpf + ", " + eMail + ", " + dataNascimento
# 		arquivo.write(bytes(novaLinha,"UTF-8"))
# 		print("Cadastro de cliente realizado com sucesso!")
# 		arquivo.close()
#
# 	if opcao == 2:
# 		nome = input("Nome: ")
# 		endereco = input("Endereco: ")
# 		cidade = input("Cidade: ")
# 		telefone = input("Telefone: ")
# 		cpf = input("CPF: ")
# 		eMail = input("E-mail: ")
# 		dataNascimento = input("Data de Nascimento: ")
# 		cargo = input("Cargo: ")
# 		setor = input("Setor: ")
# 		funcionario = [nome,endereco,cidade,telefone,cpf,eMail,dataNascimento,cargo,setor]
# 		arquivo = open("funcionario.csv","ab+")
# 		novaLinha = "\n" + nome + ", " + endereco + ", " + cidade + ", " + telefone + ", " + cpf + ", " + eMail + ", " + dataNascimento + ", " + cargo + ", " + setor
# 		arquivo.write(bytes(novaLinha,"UTF-8"))
# 		print("Cadastro de funcionário realizado com sucesso!")
# 		arquivo.close()
#
# 	if opcao == 3:
# 		def listarClientes():
# 			cliente = []
# 			arquivo = open("cliente.csv","rU")
# 			registro = csv.reader(arquivo)
# 			registro.__next__()
# 			print("\t\t############################\n\t\t#    Lista de Clientes:    #\n\t\t############################\n\n")
# 			for nome,endereco,cidade,telefone,cpf,eMail,dataNascimento in registro:
# 				print("Nome: " + nome)
# 				print("Endereco: " + endereco)
# 				print("Cidade: " + cidade)
# 				print("Telefone: " + telefone)
# 				print("CPF: " + cpf)
# 				print("Email: " + eMail)
# 				print("Data de Nascimento: " + dataNascimento)
# 				print("\n------------------------------\n")
# 				cliente.append([nome,endereco,cidade,telefone,cpf,eMail,dataNascimento])
# 		listarClientes()
# 		input()
#
# 	if opcao == 4:
# 		def listarFuncionarios():
# 			funcionario = []
# 			arquivo = open("funcionario.csv","rU")
# 			registro = csv.reader(arquivo)
# 			registro.__next__()
# 			print("\t\t############################\n\t\t#  Lista de Funcionarios:  #\n\t\t############################\n\n")
# 			for nome,endereco,cidade,telefone,cpf,eMail,dataNascimento,cargo,setor in registro:
# 				print("Nome: " + nome)
# 				print("Endereco: " + endereco)
# 				print("Cidade: " + cidade)
# 				print("Telefone: " + telefone)
# 				print("CPF: " + cpf)
# 				print("Email: " + eMail)
# 				print("Data de Nascimento: " + dataNascimento)
# 				print("Cargo: " + cargo)
# 				print("Setor: " + setor)
# 				print("\n------------------------------\n")
# 				funcionario.append([nome,endereco,cidade,telefone,cpf,eMail,dataNascimento,cargo,setor])
# 		listarFuncionarios()
# 		input()
#
# 	if opcao == 5:
# 		over = 1;
