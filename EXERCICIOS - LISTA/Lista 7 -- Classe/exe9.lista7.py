# Crie uma classe chamada Funcionario com atributos para nome, cargo e salário. Adicione métodos para calcular o aumento de salário.

class Funcionario:
    
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    def info(self):
        print(f"Nome: {self.nome} \n Cargo: {self.cargo} \n Salario: {self.salario}")
    
    def aumento_salario(self):
        self.salario = (self.salario * 0.2) + self.salario
        
valor = Funcionario("Nathzinha", "Jardineira" , 1200)
valor.info()

print()

valor.aumento_salario()
print("Salario com reajuste...(+20%)")
valor.info()
