# Crie uma classe base ContaEnergia com métodos para calcular o consumo de energia e gerar faturas. 
# Em seguida, crie subclasses como Residencial, Comercial, Industrial que herdem da classe base e implementem 
# os métodos de acordo com o tipo de conta.


class ContaEnergia:
    def __init__(self, consumo):
        self.consumo = consumo
        
        
class residencial(ContaEnergia):
    def __init__(self, consumo, fatura):
        super().__init__(consumo)
        self.fatura = fatura
        
    def info(self, fatura):
        print(f" {self.consumo} ")    
        fatura = self.consumo * 2
        return fatura
        print(f"{fatura}")
        
    def p(self):
        print(f" {self.consumo} | {self.fatura} ")
        
        
class comercial(ContaEnergia):
    def __init__(self, consumo, fatura):
        super().__init__(consumo)
        self.fatura = fatura
        
    def info(self, fatura):
        print(f" {self.consumo} | {fatura} ")    
        fatura = self.consumo * 3
        return fatura
     
    def p(self):
        print(f" {self.consumo} | {self.fatura} ")
        
        
        
class industrial(ContaEnergia):
    def __init__(self,consumo, fatura):
        super().__init__(consumo)
        self.fatura = fatura
        
    def info(self, fatura):
            
        fatura = self.consumo * 5
        return fatura
        
    def p(self):
        print(f" {self.consumo} | {self.fatura} ")
          

prod1 = residencial(26)
prod2 = comercial(50)
prod3 = industrial(80)


prod1.info()
prod1.p()
prod2.info()
prod2.p()
prod3.info()
prod3.p()