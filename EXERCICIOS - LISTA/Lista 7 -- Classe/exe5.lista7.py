# Crie uma classe chamada Triangulo com métodos para calcular a área e o perímetro do triângulo, dados os valores dos lados.

class Triangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
                
    def Area(self, base, altura):
        return self.base * self.altura / 2
    

valor = Triangulo(2, 6)

valor.Area()