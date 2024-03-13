
# 15 ) fórmula IMC = peso / altura2.


peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / altura ** 2

print("IMC: ", imc)

if imc < 20:
    print("Abaixo do peso")

elif imc <= 25:
    print("Normal")

elif imc <= 30:
    print("Exceso de Peso")

elif imc <= 35:
    print("Obesidade")

else:
    print("Obesidade Morbida")