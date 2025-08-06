import os

# Caminho para o Python e o seu script
python_path = r"C:\Users\pedro\AppData\Local\Programs\Python\Python313"
script_path = r"C:\Users\pedro\OneDrive\Área de Trabalho\Algoritimos Python\python\Projetos_Pessoais\Web_Scrapper/daily_scrapper.py"

# Comando para agendar a tarefa
comando = f'''
schtasks /Create /SC DAILY /TN "ColetarDadosLojas" /TR "{python_path} {script_path}" /ST 22:10 /F
'''

os.system(comando)