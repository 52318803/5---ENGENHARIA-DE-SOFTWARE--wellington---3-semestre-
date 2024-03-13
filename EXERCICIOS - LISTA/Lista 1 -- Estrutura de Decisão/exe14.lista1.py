
# 14) Faça um programa que leia três números e mostre o maior e o menor deles.


num1 = int(input("Digite um numero : "))
num2 = int(input("Digite um numero : "))
num3 = int(input("Digite um numero : "))


# Encontrar o maior número
if num1 >= num2 and num1 >= num3:
    maior = num1

elif num2 >= num1 and num2 >= num3:
    maior = num2

else:
    maior = num3

print("Maior = ", maior)



# Encontrar o menor número
if num1 <= num2 and num1 <= num3:
    menor = num1

elif num2 <= num1 and num2 <= num3:
    menor = num2

else:
    menor = num3

print("Menor = ", menor)