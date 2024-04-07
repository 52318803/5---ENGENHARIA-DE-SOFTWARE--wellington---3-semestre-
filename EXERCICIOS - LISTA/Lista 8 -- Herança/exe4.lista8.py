# Crie uma classe base Comida com atributos como nome, sabor e calorias. 
# Em seguida, crie subclasses como Fruta, Vegetal, Doce que herdem da classe base 
# e adicionem atributos específicos a cada tipo de comida.


class Comida:
    def __init__(self, nome, sabor, calorias):
        self.nome = nome
        self.sabor = sabor
        self.calorias = calorias
    

class Fruta(Comida):
    def __init__(self, nome, sabor, calorias):
        super().__init__(nome, sabor, calorias)


class Vegetal(Comida):
    def __init__(self, nome, sabor, calorias):
        super().__init__(nome, sabor, calorias)            
                 
                 
class Doce(Comida):
    def __init__(self, nome, sabor, calorias):
        super().__init__(nome, sabor, calorias)            
                 
                 
                
produto1 = Fruta("Iphone_Pro_Max_Ultra_LG_TV_168", 185.752, "Celular", "Magalu e Eletros")
produto2 = Vegetal("Paçoca", 1.90, "Doce", "05/2025", "Carrefur")
produto3 = Doce("Calça Cargo", 426, "Roupa de baixo", "Vans")

produto1.info_eletro()
produto2.info_alim()
produto3.info_vestu()  

'''



'''