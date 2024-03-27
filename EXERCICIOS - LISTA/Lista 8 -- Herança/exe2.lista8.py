"""Crie uma classe base Funcionario com atributos como nome, idade e salário. 
Em seguida, crie subclasses como Gerente, Analista, Desenvolvedor que herdem da classe base e
adicionem atributos específicos a cada tipo de funcionário."""


class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
        
class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, beneficios):
        super().__init__(nome, idade, salario)
        self.beneficios = beneficios
        
    def info_gerente(self):
        return f"Nome: {self.nome} -- Idade: {self.idade} -- Salario: {self.salario} -- Beneficios: {self.beneficios}"
    

class Analista(Funcionario):
    def __init__(self, nome, idade, salario, curriculo):
        super().__init__(nome, idade, salario)
        self.curriculo = curriculo
        
    def info_analista(self):
        return f"Nome: {self.nome} -- Idade: {self.idade} -- Salario: {self.salario} -- Info de Curriculo: {self.curriculo}"
    
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, salario, pet):
        super().__init__(nome, idade, salario)
        self.pet = pet
        
    def info_desenv(self):
        return f"Nome: {self.nome} -- Idade: {self.idade} -- Salario Desejado: {self.salario} -- Tem Pet? {self.pet}"
    
    

nome1 = Gerente("Natasha", 19, 18.500, "Vale Combustivel, Vale Alimentação, GymPass")
nome2 = Analista("Gio", 21, 15.300, "Formação em ser grande gostosa")
nome3 = Desenvolvedor("Paloma", 15, 800, "Tenho, o nome é Cacau")

nome1.info_gerente()
nome2.info_analista()
nome3.info_desenv()

    