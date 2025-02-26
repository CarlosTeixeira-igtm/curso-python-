# Vamos começar criando uma classe chamda carro
# Uma classe é um molde ou planta que define como os objetos dessa classe serão
# Ela define o que um objeto pode fazer (os metodos) e o que eles tem (os atributos)

class Carro:
    # a classe carro tem dois atributos: "marca" e "modelo". E um método: acelerar.
    # o metodo especial __init__ é o que quando criamos um objeto da classe
    # ele inicializa os atributos do objeto (marca e modelo)
    def __init__(self, marca, modelo, cor):
        # os atributos do objeto serão definidos dentro do init 
        # o self refere-se ao proprio objeto que esta sendo criado
        self.modelo = modelo # atributo que armazena o modelo
        self.marca = marca # atributo que armazena a marca
        self.cor = cor

# esse é o metodo que define o comportamento do obejto, aqui estamos falando o que de fato o carro faz
    def acelerar(self):
        print(f"O {self.marca} {self.modelo} esta acelerando!")

    def parar(self):
        print(f"O {self.marca} {self.modelo} parou!")

    def direita(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou a direita!")

    def direita_parou(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou a direita e parou!")
    
    def esquerda(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou a esquerda!")

    def continuou(self):
        print(f"O {self.marca} {self.modelo} {self.cor} virou a esquerda e seguiu em frente!")

carro1 = Carro("Fusca" , "1984", "Preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.direita()
carro1.direita_parou()
carro1.esquerda()
carro1.continuou()
carro1.parar()