#4) Desenvolva um programa que solicite dois números inteiros, mostre a soma destes números, e avise se a soma é maior, menor ou igual a 1000


a = int(input("numero1: "))
b = int(input("numero2: "))

some = a + b

if some > 1000:
    print(f"{some} e MAIOR+ que 1000")
    
elif some == 1000:
    print(f"{some} e IGUAL= que 1000")
    
else:
    print(f"{some} e MENOR- que 1000")