class Login:
    def _init_(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class Pessoa:  
    def _init_(self, usuario, senha, nome, cpf, email):
        self.login = Login(usuario, senha)  
        self.nome = nome 
        self.cpf = cpf
        self.email = email
    
    def validar_login(self, senha):
        if senha == self.login.senha:
            self.bem_vindo()
        else:
            print("Credenciais inválidas. Tente novamente.")
            menu()

    def bem_vindo(self):
        print(f"Bem vindo ao Sistema, {self.nome}!")
        if isinstance(self, Funcionario):
            menu1()

    def atualizar_nome(self, novo_nome):
        self.idade = novo_nome


class Funcionario(Pessoa):
    def _init_(self, nome, cpf, email, cargo, usuario, senha):
        super()._init_(usuario, senha, nome, cpf, email)
        self.cargo = cargo

def menu1():
    print("Bem Vindo Ao Hub De Funcionario")

def menu():

    print("Bem vindo ao Sistema X")
    print("Opções:")
    print("1. Entrar")
    print("2. Comprar")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        fazer_login()
    elif opcao =="2":
        venda.realizar_venda()
    elif opcao == "3":
        print("Saindo do Sistema...")
    else:
        print("Opção inválida. Tente novamente.")
        menu()

def fazer_login():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if usuario == pessoa1.login.usuario:  
        pessoa1.validar_login(senha)
    elif usuario == pessoa2.login.usuario:  
        pessoa2.validar_login(senha)
    else:
        print("Usuário não encontrado.")
        menu()


class Produto:
    def _init_(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Feijao(Produto):
    def _init_(self, quantidade):
        super()._init_("Feijão", 29.90)
        self.quantidade = quantidade

    def calcular_total(self):
        return self.quantidade * self.valor

class Arroz(Produto):
    def _init_(self, quantidade):
        super()._init_("Arroz", 19.90)
        self.quantidade = quantidade

    def calcular_total(self):
        return self.quantidade * self.valor

class Venda:
    def _init_(self, produto):
        self.produto = produto

    def realizar_venda(self):
        print("Estoque:")
        print("1. Feijão - R$29.90")
        print("2. Arroz - R$19.90")

        escolha = int(input("Escolha o produto: "))
        quantidade = int(input("Digite a quantidade: "))

        if escolha == 1:
            produto = Feijao(quantidade)
        elif escolha == 2:
            produto = Arroz(quantidade)
        else:
            print("Opção inválida")
            return

        total = produto.calcular_total()
        print(f"Total a pagar: R${total}")


venda = Venda(None)