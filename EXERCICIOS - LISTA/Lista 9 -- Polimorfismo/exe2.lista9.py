# Desenvolva um sistema de loja virtual onde diferentes tipos de produtos
# (por exemplo, livros, eletrônicos, roupas) tenham diferentes métodos para
# calcular o preço com base em descontos e promoções.


class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        

class Livros(Produtos):
    def desconto(self):
        return self.preco * 0.2
    
    def promocao(self):
        return self.preco * 0.8
    
    
class Eletro(Produtos):
    def desconto(self):
        return self.preco * 0.1
    
    def promocao(self):
        return self.preco * 0.4
    

class Roupas(Produtos):
    def desconto(self):
        return self.preco * 0.5
    
    def promocao(self):
        return self.preco * 0.2
    
    
    
loja = [Livros("A culpa das estrelas", 80), Eletro("Iphone14plusX500", 5800900), Roupas("Calça Cargo", 400)]

for novo in loja:
    print(f"Nome: {novo.nome}  |  Desc: {novo.desconto()}%  |  Promo: {novo.promocao()}% ")
    print()       #não utiliza ()             utiliza ()
