#api_ibge.py

import json
import requests as rq

resposta = rq.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/ovidio')

dados_json = json.loads(resposta.text)
print(dados_json[0]['res'][0])
    