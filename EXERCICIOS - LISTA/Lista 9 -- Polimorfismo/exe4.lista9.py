# Implemente um sistema que simule um zoológico, onde diferentes tipos de animais
# (por exemplo, mamíferos, aves, répteis) tenham diferentes comportamentos 
# (como alimentação, reprodução) utilizando polimorfismo.


class Animais:
    def __init__(self, nome):
        self.nome = nome
        
        
class Reptil(Animais):
    def alimentacao(self):
        print("Insetos, flores, algas e sementes, peixes e outros animais.")
    
    def reproducao(self):
        print("Reprodução sexuada, fecundação é interna")
      
    
class Mamiferos(Animais):
    def alimentacao(self):
        print("Exixte Herbívoros, carnívoros ou onívoros")
    
    def reproducao(self):
        print("Forma sexuada, entre macho e fêmea")
        
             
class Aves(Animais):
    def alimentacao(self):
        print("Sementes, frutas, néctar... e carniça.")
        
    def reproducao(self):
        print("Botão ovo")
        
        
class Plantinha(Animais):
    def alimentacao(self):
        print("Fotossintese")
        
    def reproducao(self):
        print("Brotamento, Divisão binária, Fragmentação")
        
        
    
curiosidades = [Reptil("Angelica"), Mamiferos("Cleitinho"), Aves("Cloves"), Plantinha("Robertinha")]

for curio in curiosidades:
    print(f"Nome: {curio.nome}  |  Alimentação: {curio.alimentacao()}  |  Reprodução: {curio.reproducao()}")
    print()