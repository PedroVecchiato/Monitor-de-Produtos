# Monitor-de-Produtos
Este é um projeto EDUCACIONAL. Uma aplicação de Python com interface gráfica (CustomTkinter) que permite monitorar preços de produtos em lojas como Amazon, Magazine Luiza e Mercado Livre.  Coleta automática de dados com salvamento de dados em planilhas.

-----------------------------------------------------------------------------------------------------------------------------

Este é um **PROJETO EDUCACIONAL** desenvolvido com o objetivo de praticar e aplicar conhecimentos de **Python**, com foco em:

- Web scraping com Selenium
- Manipulação de dados com Pandas
- Criação de interfaces gráficas com CustomTkinter
- Exportação de dados em `.xlsx` e `.csv`
- Organização de código em múltiplos módulos

--------------------------------------------------

Objetivo

O projeto permite que o usuário insira um link de produto das lojas **Amazon**, **Magalu** ou **Mercado Livre** e, com isso, o sistema coleta automaticamente:

- Nome do produto
- Preço atual
- Porcentagem de desconto (se houver)
- Disponibilidade de cupom
- Link da oferta

Os dados são salvos em uma planilha para controle e comparação futura

Screenshot da Interface:
<img width="321" height="399" alt="Captura de tela 2025-08-06 013001" src="https://github.com/user-attachments/assets/f05ed071-1a49-4f69-ad20-193348b85fb6" />

--------------------------------------------------------------------------------------------------------------------------------------------------------------
Se quiser que a planilha com os preços dos produtos seja atualizada automaticamente todos os dias, você pode usar o Agendador de Tarefas do Windows:

 Passo a passo:

No menu Iniciar, pesquise por "Agendador de Tarefas" e abra.
Clique em "Criar Tarefa...".
Na aba Geral:
Dê um nome (ex: Atualizar Planilha de Produtos).
Marque "Executar com privilégios mais altos".
Na aba Disparadores (Triggers):
Clique em "Novo..." e defina o horário diário em que deseja atualizar.
Na aba Ações:
Clique em "Nova...".
Em "Programa/script", selecione o executável do Python (ex: C:\Users\SeuNome\AppData\Local\Programs\Python\PythonXX\python.exe).
Em "Argumentos", adicione o caminho do script:

plaintext
Copiar
Editar
"C:\caminho\para\seu\script\atualizar_planilha.py"
Clique em OK para finalizar.

Observações:
Certifique-se de que o script atualizar_planilha.py está no caminho correto.

OU

Use o agendar_codigo (basta mudar a 9° linha com o horario desejado)
desta forma a planilha será atualizada, no entanto sera necessario deixar o código aberto em segundo plano.

---------------------------------------------------------------------------------------------------------------------------------

Este projeto foi criado com fins estritamente educacionais, como forma de consolidar meus aprendizados em:

Web scraping
Manipulação de tabelas e dados reais
Design de interfaces simples
Modularização de código Python
Automação com arquivos Excel/CSV

Aviso legal
Este projeto não possui qualquer afiliação com Amazon, Magalu ou Mercado Livre.
Todos os dados são públicos e obtidos para fins didáticos.

Caso queira Baixar um arquivo executavel afim de facilitar o processo aqui esta o link para o release: [Releases](https://github.com/PedroVecchiato/Monitor-de-Produtos/releases).
