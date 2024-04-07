# Crie uma calculadora polimórfica que pode realizar diferentes operações matemáticas
# (adição, subtração, multiplicação, etc.) com base nos operandos fornecidos.

class CalculadoraPolimorfica:
    @staticmethod         #não tem necessidade de criar uma instancia especifica
    def adicao(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

    @staticmethod
    def multiplicacao(a, b):
        return a * b

    @staticmethod
    def divisao(a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    @staticmethod
    def potencia(a, b):
        return a ** b

# Exemplo de uso
op = input("Escolha a operação (+, -, *, /, **): ")

if op in ('+', '-', '*', '/', '**'):
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if op == '+':
        resultado = CalculadoraPolimorfica.adicao(x, y)
    elif op == '-':
        resultado = CalculadoraPolimorfica.subtracao(x, y)
    elif op == '*':
        resultado = CalculadoraPolimorfica.multiplicacao(x, y)
    elif op == '/':
        resultado = CalculadoraPolimorfica.divisao(x, y)
    elif op == '**':
        resultado = CalculadoraPolimorfica.potencia(x, y)

    print("Resultado:", resultado)
else:
    print("Operação inválida")