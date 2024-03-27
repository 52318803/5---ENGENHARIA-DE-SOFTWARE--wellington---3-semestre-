#Escreva uma função que calcula a média dos elementos em uma lista de números.

lista = [45, 62, 31, 78, 17, 50]

def media(lista):
    soma = 0
    for y in lista:
        soma += y     #ele pega um elemento e soma com outro elemento
        media = soma / len(lista)
    return media
    
print(media(lista))