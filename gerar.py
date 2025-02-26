import pandas as pd
import random 
from datetime import datetime, timedelta
# funão para gerar dados de vendas

def gerar_dados(num_linhas, in_min, in_max):
    produtos = ['Tupperware' , 'Bombril' , 'Xerox' , 'Kodac']
    cidades = ['Orlando' , 'Anahein' , 'Poá' , 'Franco da Rocha']
    dados = []
    #in_min = 0
    #in_max = 365
    for _ in range(num_linhas): # for que consegue controlar a qtdd 
        produto = random.choice(produtos)
        cidade = random.choice(cidades)
        valor = round(random.uniform(50,500), 2)
        data = datetime.today() - timedelta(days=random.randint(in_min, in_max))
        dados.append([produto, cidade, valor, data])
    return dados


# gerar 100 lihas de dados com intervalo de datas de 1 a 365 dias
dados_prontos = gerar_dados(100, 1, 365)

#criar o dataframe (efetivamente a tabela)
df_vendas = pd.DataFrame(dados_prontos, columns = ['Produto','Cidade','Valor','Data'])
#salvando em csv

df_vendas.to_csv('vendas.csv', index=False )
print("Deu tudo certo! O arquivo foi salvo!")