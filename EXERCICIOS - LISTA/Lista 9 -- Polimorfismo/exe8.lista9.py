# 8 e 6-) Implemente uma biblioteca de veículos onde diferentes tipos de veículos
# (por exemplo, carros, bicicletas, ônibus) tenham diferentes métodos para calcular 
# o custo de manutenção e consumo de combustível.


class Veiculos:
    def __init__(self, preco, gasolina):
        self.preco = preco
        self.gasolina = gasolina
        
        
        
class Carro(Veiculos):
    def manutencao(self):
        return self.preco * 3
    
    def consumo_Com(self):
        return self.gasolina * 3
      
    
class Onibus(Veiculos):
    def manutencao(self):
        return self.preco * 4
    
    def consumo_Com(self):
        return self.gasolina * 4.50
         

class Caminhao(Veiculos):
    def manutencao(self):
        return self.preco * 5
    
    def consumo_Com(self):
        return self.gasolina * 6.50         
         
         
class Moto(Veiculos):
    def manutencao(self):
        return self.preco * 2
    
    def consumo_Com(self):
        return self.gasolina * 2.50
             
             
class Bicicleta(Veiculos):
    def manutencao(self):
        return self.preco * 1
    
    def consumo_Com(self):
        return self.gasolina * 0
        
        
class Aviao(Veiculos):
    def manutencao(self):
        return self.preco * 10
    
    def consumo_Com(self):
        return self.gasolina * 8
        
        
           
valores = [Carro(15000, 3.70), Onibus(80000, 3.70), Moto(2000, 3.70), Caminhao(500000, 3.70), Bicicleta(1000, 0), Aviao(15000000, 7000)]

for tabela in valores:
    #print("Carro  |  Onibus  |  Moto  |  Caminhao  |  Bicicleta  |  Aviao")
    print(f"Tabela de Manutençao: {tabela.manutencao()}")
    
    print(f"Tabela de Consumo de Combustivel: {tabela.consumo_Com()}")
    print()