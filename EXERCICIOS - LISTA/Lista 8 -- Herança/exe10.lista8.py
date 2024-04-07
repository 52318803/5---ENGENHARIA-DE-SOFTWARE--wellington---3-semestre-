# Crie uma classe base chamada ProdutoLimpeza com atributos como nome, preço e finalidade.
# Em seguida, crie subclasses como Detergente, Desinfetante, Amaciante que herdem da
# classe base e adicionem atributos específicos a cada tipo de produto de limpeza.


class Limpeza:
    def __init__(self, nome, preco, finalidade):
        self.nome = nome
        self.preco = preco
        self.finalidade = finalidade
        
        
class detergente(Limpeza):
    def __init__(self, nome, preco, finalidade, tipos):
        super().__init__(nome, preco, finalidade)
        self.tipos = tipos
        
    def info(self):
        print(f"{self.nome} | {self.preco} | {self.finalidade} | {self.tipos}")    
        
        
        
class desinfetante(Limpeza):
    def __init__(self, nome, preco, finalidade, forte):
        super().__init__(nome, preco, finalidade)
        self.forte = forte
        
    def info(self):
        print(f"{self.nome} | {self.preco} | {self.finalidade} | {self.forte}")    
        
        
        
class amaciante(Limpeza):
    def __init__(self, nome, preco, finalidade, cheiro):
        super().__init__(nome, preco, finalidade)
        self.cheiro = cheiro
        
    def info(self):
        print(f"{self.nome} | {self.preco} | {self.finalidade} | {self.cheiro}")
        
          

prod1 = detergente("Ipe", 18.59, "Lavar Louça", "limpeza profunda ")
prod2 = desinfetante("Pinho Sol", 15.60, "Eliminar bacterias", "Muito forte")
prod3 = amaciante("Downy", 45.78, "Roupas cheirosas", "Muito bom")


prod1.info()

prod2.info()

prod3.info()