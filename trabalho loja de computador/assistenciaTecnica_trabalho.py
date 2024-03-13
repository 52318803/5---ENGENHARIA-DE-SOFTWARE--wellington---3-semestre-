import sqlite3
import os
import platform

so = platform.system()
if so == "Windows":
    limpa = "cls"
else:
    limpa = "clear"




    # Conectar ao banco de dados (isso criará o banco de dados se não existir)
conexao = sqlite3.connect("servicos.db")
cursor = conexao.cursor()

    # Criar a tabela tab_ordemdeservico se não existir
cursor.execute("""CREATE TABLE IF NOT EXISTS tab_ordemdeservico (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    descricao TEXT,
                    peca_def TEXT
                    );""")

    # Fechar a conexão após a criação da tabela
conexao.close()

def excluir():
    conexao = sqlite3.connect("servicos.db")
    cursor = conexao.cursor()
    os.system(limpa)
    senha=input("\nDigite sua senha para excluir")
    if senha == (5629):
        codigo = input("Qual o codigo a ser excluido ")
        cursor.execute("DELETE FROM tab_ordemdeservico WHERE id = " + codigo)
        print()
        print("Exclusão OK")
        print()
        input("Tecle Enter para continuar")
        conexao.commit()
        conexao.close()
    else:
        print("senha  incorreta")
        

def cadastro():
    conexao = sqlite3.connect("servicos.db")
    cursor = conexao.cursor()
    cont="s"
    while cont =="s":
        os.system(limpa)
        nome = input("Digite o seu nome: ")
        telefone = input("Digite o telefone do serviço técnico: ")
        email = input("Digite o email do serviço técnico: ")
        peca_def = input("Qual a peça com defeito: ")
        descricao = input("Digite a descrição do problema: ")
        sql = """INSERT INTO tab_ordemdeservico(nome, telefone, email, descricao, peca_def)
                 VALUES(?, ?, ?, ?, ?);"""
        servicos = (nome, telefone, email, descricao, peca_def)
        try:
            cursor.execute(sql, servicos)
            print(f"Serviço no nome de {nome} com o telefone número {telefone} cadastrado realizado com sucesso.")
        except sqlite3.Error as e:
            print("ERRO:", e)
            break  
        print()
        cont = input("Novo cadastro(s/n)? ")
        cont = cont.lower()
    conexao.commit()
    conexao.close()

def consulta():
    os.system(limpa)
    conexao = sqlite3.connect("servicos.db")
    cursor = conexao.cursor()
    nome_consulta = input("Qual o número cadastrado: ")
    linhas = cursor.execute("""SELECT * FROM tab_ordemdeservico WHERE telefone = ?""", (nome_consulta,))
    for linha in linhas:
        print(linha)
    conexao.close()



while True:
    os.system(limpa)
    print("===============================")
    print("     Cadastro de serviços     ")
    print("1. Cadastro de serviço para manutenção")
    print("2. Consulta de serviço técnico")
    print("3. Suporte")
    print("4. Excluir ordem de servico (adm only)")
    print("5. Sair")
    print("===============================")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        consulta()
    elif opcao == 3:
        sup = input("Descreva o problema: ")
        sup_email = input("Digite o email para entrarmos em contato: ")
        sup_telefone = input("Digite o telefone para entrarmos em contato: ")
        # Aqui você pode salvar essas informações em um banco de dados ou fazer o que for necessário com elas.
    elif opcao == 4:
        print()

    elif opcao == 5:
       print("Saindo...")
       print()
       print("Saiu")
       break
    else:
        print("Opção inválida. Tente novamente.")