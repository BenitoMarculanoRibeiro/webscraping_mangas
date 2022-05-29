from PIL import Image
import os
path = "mangas/omniscient-reader-s-viewpoint/capitulo-03"
lista_arquivos = os.listdir(path)
path_pdf = path.replace("mangas", "pdfs")
try:
    os.makedirs(path_pdf)
    print('Caminho criado.')
except OSError:
    print('Caminho já existe.')
for arquivo in lista_arquivos:
    # abrir arquivo
    imagem = Image.open(f"{path}/{arquivo}").convert("RGB")

    # salvar o arquivo com outro formato
    imagem.save(f'{path_pdf}/{arquivo.replace("jpg", "pdf")}')
