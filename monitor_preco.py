from selenium import webdriver

from utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
import pandas

def raspar_url(link_produto,salvar_em_csv=False):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--use-gl=desktop')
    options.add_argument("--window-size=1920,1080")  # define resolução maior
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")  # simula navegador real

    navegador = webdriver.Chrome(options=options)

    if 'magazineluiza' in link_produto:
        dados = coletar_magalu(navegador,link_produto)
    if 'amazon' in link_produto:
        dados = coletar_amazon(navegador,link_produto)
    if 'mercadolivre' in link_produto:
        dados= coletar_mercado_livre(navegador,link_produto)

    dados_dict = {
        "Nome Produto": dados[0],
        "Preco Produto":(dados[1]),
        "Desconto Produto":(dados[2]),
        "Site": dados[3],
        "Cupom": dados[4],
        "Link": dados[5]
    }

    nomes_colunas = ["Nome Produto", "Preco Produto", "Desconto Produto", "Site", "Cupom", "Link"]

    # Tenta abrir o arquivo e adicionar o novo dado
    try:
        dataframe_existente = pandas.read_excel("Raspagem Produto.xlsx")
        dataframe = pandas.concat([dataframe_existente, pandas.DataFrame([dados_dict])], ignore_index=True)
    except FileNotFoundError:
        dataframe = pandas.DataFrame([dados],columns=nomes_colunas)  # Se não existir, cria do zero

    # Salva no Excel
    dataframe.to_excel("Raspagem Produto.xlsx", index=False)
    # Salva em CSV
    if salvar_em_csv == True:
        dataframe.to_csv("Raspagem Produto.csv", index=False, sep=";", encoding="utf-8-sig")

def coletar_magalu(navegador,link_produto):
    site = 'Magazine Luiza'
    navegador.get(link_produto)
    nome_produto = esperar_elemento("//h1[@data-testid='heading-product-title']",navegador)
    preco_produto = 'R$' +esperar_elemento("//p[@data-testid='price-value']",navegador).replace("ou","").strip().replace('R$','')
    try:
        esperar_elemento("//strong[contains(text(), '% OFF')]",navegador)
        cupom_produto = 'Cupom Disponivel'
    except:
        cupom_produto = "Sem Cupom Disponivel"
    try:
        preco_produto_original = esperar_elemento("(//p[@data-testid='installment'])[1]",navegador) # CALCULO DO DESCONTO
        preco_produto_original = extrair_primeiro_preco(preco_produto_original)
        desconto_produto = desconto_magalu(preco_produto_original,extrair_primeiro_preco(preco_produto))
        if desconto_produto == '0%':
            desconto_produto = "Sem Desconto Disponivel"

    except NoSuchElementException:
        desconto_produto = "Sem Desconto Disponivel"
    return nome_produto, preco_produto, desconto_produto, site, cupom_produto, link_produto

def coletar_amazon(navegador,link_produto):
    site = 'Amazon'
    navegador.get(link_produto)
    try:
        botao_antibot = esperar_elemento_nottext("//button[@class='a-button-text']",navegador)
        botao_antibot.click()
    except (NoSuchElementException,TimeoutException,ElementNotInteractableException):
        pass
    nome_produto = esperar_elemento("//span[@id='productTitle']",navegador,10)

    preco_produto_centavos = esperar_elemento("//span[@class='a-price-fraction']",navegador)
    preco_produto = 'R$ '+ esperar_elemento("//span[@class='a-price-whole']",navegador)+','+preco_produto_centavos
    
    try:
        esperar_elemento("/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[4]/div/div/div[32]/div/span/div/span/span[2]",navegador)
        cupom_produto = 'Cupom Disponivel'  
    except (NoSuchElementException,TimeoutException):
        cupom_produto = "Sem Cupom Disponivel"
    try:
        desconto_produto = esperar_elemento("//span[@class='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage']",navegador).replace('-','')
        if desconto_produto == 'none':
            try:
                desconto_produto = esperar_elemento("(//span[@class='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'])[2]",navegador).replace('-','')
            except (NoSuchElementException,TimeoutException):
                pass
    except (NoSuchElementException,TimeoutException):
        desconto_produto = ('Sem Desconto Disponivel')

    try:
        desconto_recorrente = esperar_elemento("//span[contains(text(), 'Comprar com recorrência')]",navegador)  # CALCULO DO PRODUTO COM DESCONTO
        if desconto_recorrente:
            preco_produto = numero_to_int(preco_produto)
            desconto_produto = numero_to_int(desconto_produto)
            preco_produto = calcular_preco_final(preco_produto,desconto_produto)
            
    except (NoSuchElementException,TimeoutException,ElementNotInteractableException):
        pass
    return nome_produto, preco_produto,desconto_produto, site, cupom_produto, link_produto        

def coletar_mercado_livre(navegador,link_produto):
    site = 'Mercado Livre'
    navegador.get(link_produto)
    nome_produto = esperar_elemento("//h1[@class='ui-pdp-title']",navegador)
    try:
        preco_produto_centavos = esperar_elemento("//span[@class ='andes-money-amount__cents andes-money-amount__cents--superscript-36']",navegador)
    except(NoSuchElementException,TimeoutException):
        preco_produto_centavos ='00'
        
    preco_produto = 'R$ '+ esperar_elemento("(//span[contains(@class, 'andes-money-amount__fraction')])[2]",navegador)+','+preco_produto_centavos
    try:
        desconto_produto = esperar_elemento("//span[@class= 'andes-money-amount__discount ui-pdp-family--REGULAR']",navegador).replace('-','').replace('OFF','')
    except (NoSuchElementException,TimeoutException,ElementNotInteractableException):
        desconto_produto = "Sem Desconto Disponivel"

    cupom_produto = "Sem Cupom Disponivel"    
    try:
        esperar_elemento("//span[@class='ui-pdp-background-color--LIGHT_BLUE ui-pdp-color--BLUE ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD ui-pdp-price__volume-tags--pill']",navegador)
        cupom_produto = 'Cupom Disponivel'
    except(TimeoutException,NoSuchElementException):
        pass
    try:
        esperar_elemento("//p[@class='ui-pdp-background-color--LIGHT_BLUE ui-pdp-color--BLUE ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD ui-vpp-coupons-awareness__pill']",navegador)
        cupom_produto = 'Cupom Disponivel'
    except (NoSuchElementException,TimeoutException):
        pass
    return nome_produto, preco_produto, desconto_produto, site, cupom_produto, link_produto