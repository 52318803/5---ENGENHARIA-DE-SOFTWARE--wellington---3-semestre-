# Crie uma classe base chamada AnimalEstimacao com atributos como nome, idade e especie.
# Em seguida, crie subclasses como Cachorro, Gato, Pássaro que herdem da classe base e
# adicionem atributos específicos a cada tipo de animal de estimação.


from telnetlib import GA


class AnimalEstimacao:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        
        
        
        
class Cachorro(AnimalEstimacao):
    def __init__(self, nome, idade, especie, pelagem):
        super().__init__(nome, idade, especie)
        self.pelagem = pelagem
        
    def info(self):
        print(f"{self.nome} tem {self.idade} anos  | {self.especie} e pelagem {self.pelagem}")   
        
        
        
        
class Gato(AnimalEstimacao):
    def __init__(self, nome, idade, especie, crias):
        super().__init__(nome, idade, especie)
        self.crias = crias
        
    def info(self):
        print(f"{self.nome} tem {self.idade} anos  | {self.especie} com {self.crias} crias")
        
            
     
class Passaro(AnimalEstimacao):
    def __init__(self, nome, idade, especie, ovos):
        super().__init__(nome, idade, especie)
        self.ovos = ovos

    def info(self):
        print(f"{self.nome} tem {self.idade} ano  | {self.especie} com {self.ovos} ovos")
     
     
     
animal1 = Cachorro("Ruffus", 8, "caramelo", "fofinha")  
animal2 = Gato("Hime", 2, "da rua", 0)
animal3 = Passaro("Bird", 1, "Voador", 5)

animal1.info()   
animal2.info()
animal3.info()