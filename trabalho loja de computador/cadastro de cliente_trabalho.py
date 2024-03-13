

class Cliente:
    def __init__(self, nome, telefone, endereco, email): #construtor da classe - novo objeto da classe oe criado
        self.nome = nome   #recebe 4 parametros
        self.telefone = telefone     #atribui esses parametros as variaveis de instancia
        self.endereco = endereco
        self.email = email



def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    email = input("Digite o email do cliente: ")

    novo_cliente = Cliente(nome, telefone, endereco, email)  #cria um novo obj(cliente) q chama as informaçoes
    return novo_cliente  #e retorna






def main():
    clientes = []  #lista vazia
    continuar = True
 
    while continuar:
        novo_cliente = cadastrar_cliente()  #chama cadastro para obter um novo cliente e 
        clientes.append(novo_cliente)   #add na lista de novo cliente

        opcao = input("Deseja cadastrar outro cliente? (s/n): ")
        if opcao.lower() != 's':   #tudo minusculo
            continuar = False  #encerra


    print("\nLista de Clientes Cadastrados:")   
    for cliente in clientes:          #printa todos os clientes da lista 
        print("Nome:", cliente.nome)
        print("Telefone:", cliente.telefone)
        print("Endereço:", cliente.endereco)
        print("Email:", cliente.email)
        print()
        
        
        
        

if __name__ == "__main__":  #Verifica se o script está sendo executado diretamente e não sendo importado como um módulo.
    main()    #Se for o caso, chama a função main() para iniciar a execução do programa.