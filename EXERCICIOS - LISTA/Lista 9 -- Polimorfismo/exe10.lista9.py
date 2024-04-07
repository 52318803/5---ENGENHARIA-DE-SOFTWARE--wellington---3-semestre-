# Crie um sistema de reservas de hotel onde diferentes tipos de quartos 
# (por exemplo, simples, duplo, suíte) tenham diferentes métodos para calcular 
# o preço da estadia e disponibilidade.


class Hotel:
    def __init__(self, preco, qntd):
        self.preco = preco
        self.qntd = qntd
        

class simples(Hotel):
    def valor(self):
        return self.preco * self.qntd
    
class duplo(Hotel):
    def valor(self):
        return self.preco * self.qntd * 2
    
class suite(Hotel):
    def valor(self):
        return self.preco * self.qntd * 3
    
class master(Hotel):
    def valor(self):
        return self.preco * self.qntd * 8
    
    
quartos = [simples(100, 2), duplo(200, 2), suite(300, 2), master(400, 2)]

for v in quartos:
    print(v.valor())
    print()