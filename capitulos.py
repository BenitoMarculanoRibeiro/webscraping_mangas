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
        driver.quit()
        status = False
    else:
        time.sleep(2)
