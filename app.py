import customtkinter as ctk
from monitor_preco import raspar_url
import os
from time import sleep

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Monitor de Preço')
app.geometry('300x350')

# Texto do campo
texto_da_url = ctk.CTkLabel(master=app, text='Link do Produto', height=40, width=150, justify='center')
texto_da_url.place(x=80, y=40)

# Campo de entrada
campo_da_url = ctk.CTkEntry(master=app, placeholder_text='Cole a URL do Produto', justify='center', height=40, width=200)
campo_da_url.place(x=60, y=80)

# Opcao para salvar em CSV

salvar_csv = ctk.CTkSwitch(master=app,text='Salvar em CSV')
salvar_csv.place(x=80,y=140)

# Função que será chamada ao clicar no botão
def url_produto():
    link_produto = campo_da_url.get()
    salvar_em_csv = salvar_csv.get()
    raspar_url(link_produto,salvar_em_csv)

# Botão Pesquisar produto
campo_botao_pesquisa = ctk.CTkButton(master=app, text='Monitorar Produto', width=150, height=35, command=url_produto)
campo_botao_pesquisa.place(x=80, y=220)


# Texto do Campo 2
erro_caminho_pasta = ctk.CTkLabel(master=app,text='',justify='center',height=40,width=150)
erro_caminho_pasta.place(x=80,y=285)

def abrir_planilha():
    abriu = False

    if os.path.exists('Raspagem Produto.csv'):
        os.startfile('Raspagem Produto.csv')
        abriu = True
    if os.path.exists('Raspagem Produto.xlsx'):
        os.startfile('Raspagem Produto.xlsx')
        abriu = True
    if abriu:
        erro_caminho_pasta.configure(text='')
    else:
        erro_caminho_pasta.place(x=55,y=310)
        erro_caminho_pasta.configure(text='Caminho para pasta não encontrado') 

# Botão Abrir Planilha
campo_botao_planilha = ctk.CTkButton(app,text='Abrir Planilha',width=150,height=35,command=abrir_planilha)
campo_botao_planilha.place(x=80,y=270)

        
        
app.mainloop()
