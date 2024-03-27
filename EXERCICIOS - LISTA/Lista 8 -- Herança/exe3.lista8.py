''' Crie uma classe base Produto com atributos como nome, preço e categoria. 
Em seguida, crie subclasses como Eletronico, Alimento, Vestuario que herdem da classe
base e adicionem atributos específicos a cada tipo de produto.'''


class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
    

class eletronico(Produto):
    def __init__(self, nome, preco, categoria, loja):
        super().__init__(nome, preco, categoria)
        self.loja = loja
        
    def info_eletro(self):
        return f"[ Nome do Produto: {self.nome} ]  [ Preço do Produto: {self.preco} ]  [ Categoria do Produto: {self.categoria} ]  [ Nome da Loja: {self.loja} ]"
    

class alimento(Produto):
    def __init__(self, nome, preco, categoria, validade, mercado):
        super().__init__(nome, preco, categoria)
        self.validade = validade
        self.mercado = mercado
    
    def info_alim(self):
        return f"[ Nome do Alimento: {self.nome} ]  [ Preço do Alimento: {self.preco} ]  [ Categoria do Alimento: {self.categoria} ]  [ Nome do Mercado: {self.mercado} ]  [ Validade do Alimento: {self.validade} ]"
                 
                 
class vestuario(Produto):
    def __init__(self, nome, preco, categoria, marca):
        super().__init__(nome, preco, categoria)
        self.marca = marca
        
    def info_vestu(self):
        return f"[ Nome da Roupa: {self.nome} ]  [ Preço da Roupa: {self.preco} ]  [ Categoria da Roupa: {self.categoria} ]  [ Marca da Roupa: {self.marca} ]" 
                 
                 
                 
                 
produto1 = eletronico("Iphone_Pro_Max_Ultra_LG_TV_168", 185.752, "Celular", "Magalu e Eletros")
produto2 = alimento("Paçoca", 1.90, "Doce", "05/2025", "Carrefur")
produto3 = vestuario("Calça Cargo", 426, "Roupa de baixo", "Vans")

produto1.info_eletro()
produto2.info_alim()
produto3.info_vestu()                 