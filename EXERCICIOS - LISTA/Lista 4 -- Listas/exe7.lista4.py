#Crie uma lista com os valores pares e outra com os ímpares de 1 a 10

lista = [1,2,3,4,5,6,7,8,9,10]

impar = [x for x in lista if x % 2 != 0]

par = [x for x in lista if x % 2 == 0] 

print(par)
print(impar)