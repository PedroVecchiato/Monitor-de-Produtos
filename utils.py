from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
import re

def extrair_primeiro_preco(texto):
    padrao = r'(?:R\$ ?)?([\d\.]+,\d{2})'  # "R$" agora é opcional
    match = re.search(padrao, texto)
    if match:
        preco_br = match.group(1)
        preco_float = float(preco_br.replace('.', '').replace(',', '.'))
        return preco_float
    return None

def esperar_elemento(xpath, navegador,tempo=6):
    return WebDriverWait(navegador, tempo).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    ).text

def esperar_elemento_nottext(xpath, navegador,tempo=10):
    return WebDriverWait(navegador, tempo).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

def numero_to_int(numero):
    numero = (numero).replace(',','.').strip()
    numero = float(numero)
    return numero
   
def calcular_preco_final(preco,desconto):
    preco = (preco/100)*(100-desconto)
    return preco

def desconto_magalu(precoo_original,preco):
    desconto_real = (precoo_original-preco)/precoo_original
    desconto_real *=100
    desconto_real = str(f'{desconto_real:.0f}'+'%')
    return desconto_real



