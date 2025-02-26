# isso é um comentário


''' a próxima linha mostra meu nome! '''

print("Carlos")

print("Meu nome é: Carlos \nMeu curso é: Python")

"""""
Trabalhando com tipificação e variaveis

"""""
nome = "Carlos" #string
sobrenome = "Teixeira" 
idade = 49 #integer
altura = 1.80 #float
bermuda = False #boolean

print(nome + " " + sobrenome + " tem " + str(idade))

print(idade + 2)

textoVariasLinhas = '''
Operadores
soma +
subtração -
divisão /
potência ^
exponenciação **
multiplicação *
'''
print(textoVariasLinhas)


# Detalhamento strings e usando formato
nomeCompleto = "Carlos Teixeira"
inicio = 5
fim = inicio + 6
print(nomeCompleto [inicio:fim])


qNome = input("Insira seu nome :")
qSobrenome = input("Insira seu sobre nome :")
print("Seu nome é: " + qNome + " " + qSobrenome)
