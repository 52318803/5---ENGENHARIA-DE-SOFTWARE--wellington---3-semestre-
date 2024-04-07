# FiguraGeometrica com métodos para calcular área e perímetro. subclasses como Quadrado,
# Retangulo, Triangulo e Circulo

class FigGeo:
    def __init__(self, lado, altura, raio, base):
        self.altura = altura
        self.lado = lado
        self.raio = raio
        self.base = base
        
       
'''     
#Quadrado  
    def quad(self):
        pass
        
#Retangulo
    def retan(self):
        pass
    
#Circulo
    def circ(self):
        pass

#Triangulo
    def trian(self):
        pass
    
 '''    
       
        
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
        
    

numero = FigGeo(4, 8, 4, 3)
#print(f"Area: {numero.area}   Perimetro:  {numero.peri}")



print(Quadrado.area())
print()
print(Circulo.area())
print()
print(Retangulo.area())
print()
print(Triangulo.area())

