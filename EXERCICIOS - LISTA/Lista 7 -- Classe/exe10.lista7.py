# Produto com atributos para nome, preço e quantidade em estoque. Atualizar o preço e a quantidade, exibir informações sobre o produto.

class Produto:
    
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def atual_preco(self):
        self.preco = self.preco + 1.90
        
    def atual_qnt(self):
        self.quantidade = self.quantidade - 1
        
    def info(self):
        print(f"Nome: {self.nome}  |  Preço: R${self.preco}  |  {self.quantidade} qntds no estoque")
        
        
produto1 = Produto("Paçoca", 2.40, 58)
produto2 = Produto("Balinha de velho", 0.60, 43)

produto1.info()
produto2.info()

print()
print("PREZADO CLIENTE  \n Produtos com reajuste de preço!!!!")
print()


produto1.atual_preco()
produto1.info()

produto2.atual_preco()
produto2.info()

