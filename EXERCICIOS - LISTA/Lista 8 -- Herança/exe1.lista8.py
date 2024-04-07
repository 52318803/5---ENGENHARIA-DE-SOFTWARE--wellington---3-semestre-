# FiguraGeometrica com métodos para calcular área e perímetro. subclasses como Quadrado,
# Retangulo, Triangulo e Circulo

class FigGeo:
    def __init__(self, lado, altura, raio, base):
        self.altura = altura
        self.lado = lado
        self.raio = raio
        self.base = base
        
       
      
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
    
        
       
        
class Quadrado(FigGeo):
    def area_Q(self):
        area = self.lado * self.lado
        return area
    
    def peri_Q(self):
        perimetro = self.lado + self.lado + self.lado + self.lado
        return perimetro
    
class Circulo(FigGeo):
    def area_C(self, raio):
        area = 3.14 * raio**2
        return area
    
    def peri_C(self, raio):
        circunferencia = 2 * raio * 3.14
        return circunferencia
    
    
class Retangulo(FigGeo):
    def area_R(self):
        area = self.lado * self.altura
        return area
    def peri_R(self):
        perimetro = self.lado + self.altura + self.lado + self.altura
        return perimetro
    
    
class Triangulo(FigGeo):
    def area_T(self):
        area = self.base * self.altura / 2
        return area
    def peri_T(self):
        perimetro = self.lado + self.lado + self.lado
        return perimetro
    

numero = Quadrado(4, 8, 4, 3)
print("Area: " + numero.area_Q() + "Perimetro: " + numero.perimetro_Q())


'''
Quadrado.info()
Circulo.info()
Retangulo.info()
Triangulo.info()

'''    