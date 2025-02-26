# função para criar um carro com marca e modelo
def criar_carro(marca, modelo):
    return{"marca": marca, "modelo": modelo}

# Função para acelerar
def acelerar(carro):
    print(f"O {carro['marca']} {carro['modelo']} esta acelerando.")

# Função para parar
def parar(carro):
    print(f"O {carro['marca']} {carro['modelo']} parou.")

# Função para criar um carro com cor adicional
def criar_carro_com_cor(marca, modelo, cor):
    carro = criar_carro(marca, modelo) #crie um carro basico
    carro["cor"]= cor 
    return carro

#exibir a cor do carro
def exibir_cor(carro):
    print(f"O carro é da cor {carro['cor']}.")

#virar para esquerda e virar para a direita

def virar_para_esquerda(carro):
    print(f"O {carro['marca']} {carro['modelo']} virou para a esquerda.")

def virar_para_direita(carro):
    print(f"O {carro['marca']} {carro['modelo']} virou para a direita.")
    

# criando carros
carro1 = criar_carro("Fusca", "1984")
carro2 = criar_carro("Suzuki", "Jimmy" )

# acelerando e parando os carros
print(carro1["marca"]) # acessando as marcas
print(carro1["modelo"]) # acessando os modelos

#criando o carro com cor
carro3 = criar_carro_com_cor("Toyota" , "Etios" , "Branco")
print(carro3["marca"])
print(carro3["modelo"])
print(carro3["cor"])
exibir_cor(carro3)

print('----------------Corrida----------------------')
acelerar(carro3)
parar(carro3)

print(carro2["marca"])
acelerar(carro2["modelo"]) #bug aqui
print(carro2) #bug aqui
virar_para_direita(carro2)
virar_para_esquerda(carro2)
parar(carro2)


