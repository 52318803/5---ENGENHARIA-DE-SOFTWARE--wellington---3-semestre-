# Crie uma classe base Comida com atributos como nome, sabor e calorias. 
# Em seguida, crie subclasses como Fruta, Vegetal, Doce que herdem da classe base 
# e adicionem atributos específicos a cada tipo de comida.


class Comida:
    def __init__(self, nome, sabor, calorias):
        self.nome = nome
        self.sabor = sabor
        self.calorias = calorias
    

class Fruta(Comida):
    def __init__(self, nome, sabor, calorias, tipos_F):
        super().__init__(nome, sabor, calorias)
        self.tipos_F = tipos_F

    def tipos(self):
        print(f"nome: {self.nome}  | sabor: {self.sabor}  | calorias: {self.calorias}  | alguns tipos: {self.tipos_F}")
        



class Vegetal(Comida):
    def __init__(self, nome, sabor, calorias, tipos_V):
        super().__init__(nome, sabor, calorias)            
        self.tipos_V = tipos_V         
                 
    def tipos(self):
        print(f"nome: {self.nome}  | sabor: {self.sabor}  | calorias: {self.calorias}  | alguns tipos: {self.tipos_V}")
        
        
                 
class Doce(Comida):
    def __init__(self, nome, sabor, calorias, tipos_D):
        super().__init__(nome, sabor, calorias)            
        self.tipos_D = tipos_D             
                 
    def tipos(self):
        print(f"nome: {self.nome}  | sabor: {self.sabor}  | calorias: {self.calorias}  | tipos de doce: {self.tipos_D}")
        
                    
                
produto1 = Fruta("Laranja", "suculenta", 12.50, "Lima / Pera / Bahia / Rubi...")
produto2 = Vegetal("Pepino", "de mato", 0.2, "Caipira / Japones / Aonaga / Conserva")
produto3 = Doce("Fantastíc", "uma delica", 40.000, "Leite / Amargo / Azedo / com Fruta / Amendoin...")


produto1.tipos()
produto2.tipos()
produto3.tipos()  

