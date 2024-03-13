
# 9) velocidade do veículo e apresente na tela a penalidade



veloc = float(input("Digite a valocidade: "))
 
# F2 Rename Symbol 

if veloc <= 60:
    print("Sem Penalidade")

elif veloc <= 80:
    print("Multa Leve")

elif veloc <= 100:
    print("Multa Grave")

elif veloc <= 120:
    print("Multa Gravissima")

else:
    print("Detenção do Condutor")