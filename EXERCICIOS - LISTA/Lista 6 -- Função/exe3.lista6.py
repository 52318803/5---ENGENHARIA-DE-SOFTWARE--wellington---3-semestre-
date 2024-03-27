#Crie uma função que converte uma temperatura de Celsius para Fahrenheit (use a fórmula: F = C * 9/5 + 32).

def temp(celc):
    fahre = celc * 9/5 + 32
    return fahre

celc = float(input("Temperatura de Celsius: "))
                    #o resultado da função no final ---> é fahre
fahre = temp(celc)  #ele pega esse resultado da temp(celc) e coloca em fahre

print(f"Temp de Fahrenheit: {fahre}")

