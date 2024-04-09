# FiguraGeometrica com métodos para calcular área e perímetro. subclasses como Quadrado,
# Retangulo, Triangulo e Circulo

#ERRADO !!!!!!!!!!!!!!!!!!!!!!!!!!!!

class FigGeo:
    def __init__(self, lado, altura, raio, base):
        self.altura = altura
        self.lado = lado
        self.raio = raio
        self.base = base
             
        
class Quadrado(FigGeo):
    def __init__(self, lado, altura, raio, base):
        super().__init__(lado, altura, raio, base)
    
    def area(self):
        return self.lado * self.lado
        
    
    def peri(self):
        return self.lado + self.lado + self.lado + self.lado
        
    
class Circulo(FigGeo):
    def __init__(self, lado, altura, raio, base):
        super().__init__(lado, altura, raio, base)
        
    def area(self, raio):
        return 3.14 * raio**2
        
    
    def peri(self, raio):
        return 2 * raio * 3.14
        
    
    
class Retangulo(FigGeo):
    def __init__(self, lado, altura, raio, base):
        super().__init__(lado, altura, raio, base)
        
    def area(self):
        return self.lado * self.altura

    def peri(self):
        return self.lado + self.altura + self.lado + self.altura
    
    
class Triangulo(FigGeo):
    def __init__(self, lado, altura, raio, base):
        super().__init__(lado, altura, raio, base)
        
    def area(self):
        return self.base * self.altura / 2
        
    def peri(self):
        return self.lado + self.lado + self.lado
        
    

numero1 = Quadrado(21, 5, 3, 4)
numero2 = Circulo(2, 8, 3, 7)
numero3 = Retangulo(3, 5, 6, 10)
numero4 = Triangulo(2, 15, 3, 4)
#print(f"Area: {numero.area}   Perimetro:  {numero.peri}")



print(numero1.area())
print()
print(numero2.area())
print()
print(numero3.area())
print()
print(numero4.area())

