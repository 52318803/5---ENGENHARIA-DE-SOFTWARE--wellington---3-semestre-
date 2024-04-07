# Crie uma calculadora polimórfica que pode realizar diferentes operações matemáticas
# (adição, subtração, multiplicação, etc.) com base nos operandos fornecidos.


class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
        
class Adicao(Calculadora):
    def result(self):                   #tenho q usar 'mesma' função em todos
        return self.num1 + self.num2
    
    
class Subtracao(Calculadora):
    def result(self):
        return self.num1 - self.num2
    
    
class Multiplicacao(Calculadora):
    def result(self):
        return self.num1 * self.num2


class Divisao(Calculadora):
    def result(self):
        return self.num1 / self.num2
    
    
operacao = [Adicao(10, 2), Subtracao(10, 2), Multiplicacao(10, 2), Divisao(10, 2)] 

for resultado in operacao:
    print(f"{resultado.result()}")
    
    
    
    
    
'''
numero1 = Adicao(10, 2)
numero2 = Subtracao(10, 2)
numero3 = Multiplicacao(10, 2)
numero4 = Divisao(10, 2)


print(numero1.soma())
print(numero2.sub())
print(numero3.multi())
print(numero4.div())


----------------------------------------------------------------

Se fosse pra utilizar Polimorfismo...

- tiraria todos os  'def __init__(self, num1, num2):
                        super().__init__(num1, num2)'

-------------------------------------------------------


- incluiria em calcularoda...

def operacao(self):
        raise NotImplementedError("Método operacao() não implementado na classe base Calculadora")


- incluiria no final...


numero1 = Calculadora(10, 2)
numero2 = Calculadora(8, 6)


operacoes = [Adicao, Subtracao, Multiplicacao, Divisao]

for operacao in operacoes:
    resultado = operacao(numero1.num1, numero1.num2).operacao()
    print(resultado)

'''