def sauda(nome):
	print ("ola , " + nome)
	sauda2(nome)
	print ("preparando para dizer tchau...")
	tchau()


def sauda2(nome):
	print ("ola, como vai " + nome + "?")


def tchau():
	print("tchau...")

print (sauda("maria"))

#pilha: estrutura de dados que segue o principio de LIFO (last in, first out), primeiro a entrar, ultimo a sair
#exemplo: pilha de anotaçoes, pilha de pratos