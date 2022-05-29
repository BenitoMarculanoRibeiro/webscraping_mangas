import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from PyPDF2 import PdfFileMerger
from PIL import Image


options = webdriver.ChromeOptions()
options.add_argument("--headless")

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico, options=options)

driver.get("https://mangayabu.top/manga/omniscient-reader-s-viewpoint/")
all_links = []
status = True
while(status):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = WebDriverWait(driver, timeout=120).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@class,"chaps-content")]')))
    if element.is_displayed():
        dados = driver.find_elements(
            By.XPATH, '//a[contains(@class,"chaps-content")]')
        for i in dados:
            link = i.get_attribute('href')
            all_links.append(link)
        print(all_links)
        print(len(all_links))
        # driver.quit()
        status = False
    else:
        time.sleep(2)


for url in all_links:

    driver.get(url)
    links = []
    status = True
    while(status):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        element = WebDriverWait(driver, timeout=120).until(
            EC.presence_of_element_located((By.XPATH, '//img[contains(@alt,"Página")]')))
        if element.is_displayed():
            dados = driver.find_elements(
                By.XPATH, '//img[contains(@alt,"Página")]')
            for i in dados:
                link = i.get_attribute('data-src')
                links.append(link)
            print(links)
            # driver.quit()
            status = False
        else:
            time.sleep(2)

    paths = []
    for i in links:
        paths = i.split('/')
        # print(f'{paths[-4]}/{paths[-3]}/{paths[-2]}/{paths[-1]}')
        try:
            os.makedirs(f'{paths[-4]}/{paths[-3]}/{paths[-2]}')
            print('Caminho criado.')
        except OSError:
            print('Caminho já existe.')
        status = True
        while(status):
            try:
                with open(f'{paths[-4]}/{paths[-3]}/{paths[-2]}/{paths[-1]}', 'wb') as imagem:
                    resposta = requests.get(i, stream=True)
                    if not resposta.ok:
                        print("Ocorreu um erro, status:", resposta.status_code)
                    else:
                        for dado in resposta.iter_content(1024):
                            if not dado:
                                break
                            imagem.write(dado)
                        status = False
                        print("Imagem salva!")
            except OSError:
                time.sleep(2)
                print('Tentando novamente.')

    path = f'{paths[-4]}/{paths[-3]}/{paths[-2]}'
    lista_arquivos = os.listdir(path)
    path_pdf = path.replace("mangas", "pdfs")
    print(path_pdf)
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

    #path = f'pdfs/{paths[-3]}/{paths[-2]}'
    #print(path)
    x = [str(f'{path_pdf}/{a}') for a in os.listdir(path_pdf) if a.endswith(".pdf")]
    merger = PdfFileMerger()
    for pdf in x:
        print(pdf)
        merger.append(open(pdf, 'rb'))
    print(f"{path_pdf}/{paths[-2]}.pdf")
    with open(f"{path_pdf}/{paths[-2]}.pdf", "wb") as fout:
        merger.write(fout)
