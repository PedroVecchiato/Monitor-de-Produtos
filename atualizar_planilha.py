from selenium import webdriver
from utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium_stealth import stealth
from monitor_preco import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--use-gl=desktop')

navegador = webdriver.Chrome(options=options)
dataframe = pd.read_excel("Raspagem Produto.xlsx")

for i, (link, site) in enumerate(zip(dataframe["Link"], dataframe["Site"])):
    if pd.isna(link):  
        continue

    try:
        if 'amazon' in link:
            dados = coletar_amazon(navegador, link)
        elif 'magazineluiza' in link or 'magalu' in link:
            dados = coletar_magalu(navegador, link)
        elif 'mercadolivre' in link:
            dados = coletar_mercado_livre(navegador, link)
        else:
            continue  # pula links desconhecidos

        # Atualizar a linha do DataFrame com os dados retornados
        dataframe.at[i, "Nome Produto"] = dados[0]
        dataframe.at[i, "Preco Produto"] = dados[1]
        dataframe.at[i, "Desconto Produto"] = dados[2]
        dataframe.at[i, "Site"] = dados[3]
        dataframe.at[i, "Cupom"] = dados[4]
        dataframe.at[i, "Link"] = dados[5]

    except Exception as e:
        print(f"Erro na linha {i} ({link}): {e}")
        continue


dataframe.to_excel("Raspagem Produto.xlsx", index=False)
dataframe.to_csv("Raspagem de Produto.csv",index=False, sep=";", encoding="utf-8-sig")

navegador.quit()