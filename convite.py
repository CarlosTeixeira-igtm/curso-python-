from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as imgx

nomes = ['Jeferson', 'Vitor', 'Mariana']
evento = 'Formatura do Python'
data = '27 de Fevereiro 2025'
local = 'Av Paulista, na Clarify'

for nome in nomes:
    # criando uma imagem em rgb com fundo branco (600x400px) 
    img = Image.new("RGB", (600,400), (255,255,255)) # é criada a imagem com fundo branco
    draw = ImageDraw.Draw(img) # preparando a ferramenta para desenhar a imagem

    #fontes que serão usadas no texto
    font_title = ImageFont.truetype("arial.ttf", 36) # fonte do titulo e tamanho
    font_text = ImageFont.truetype("arial.ttf", 24) # fonte para o texto do evento e tamanho

    # adiconando o texto principal na imagem (titulo do convite com nome)

    draw.text((70,100), f'convite para {nome}', (0,0,0), font=font_title)

    draw.text((70,150), evento, (0,0,0), font=font_text)

    draw.text((70,200), data, (0,0,0), font=font_text)

    draw.text((70,250), local, (0,0,0), font=font_text)

    draw.rectangle ([(45,45), (555,355)], outline=(0,0,0), width=5)

    img.save(f"{nome}.jpg")


