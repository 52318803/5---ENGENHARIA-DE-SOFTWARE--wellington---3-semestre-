# Crie uma classe chamada Retangulo que tenha métodos para calcular a área e o perímetro do retângulo, dados os valores dos lados

class Retang:
    
    def __init__(self, area, perimetro): #quando um objeto da classe é criado, são usados para inicializar os atributos do objeto
        self.area = area
        self.perimetro = perimetro  #SELF -- É uma referência ao próprio objeto, acessa os atributos e métodos do objeto dentro da classe
                                    #ATRIBUTO -- variáveis associadas aos objetos da classe, armazenam dados específicos do objeto
    
   #METODO -- é a função dentro da classe
    def calculaArea(self):
        area_retangulo = self.area * self.perimetro
        return area_retangulo
       
    def calculaPeri(self):
        perimetro_retangulo = (self.area + self.perimetro) * 2 
        return perimetro_retangulo
    
    
retangulo = Retang(5, 5)

print("Area: ", retangulo.calculaArea())
print("Perimetro: ", retangulo.calculaPeri())