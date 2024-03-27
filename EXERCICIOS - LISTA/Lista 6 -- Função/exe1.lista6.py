#Crie uma função que recebe uma lista de números e retorna a soma dos números pares contidos na lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def soma_pares(lista):
    soma = 0
    for x in lista:    # se cada elemento estiver na lista
        if x % 2 == 0:  #pega só os pares
            soma += x   #faz as somas

    return soma  

print(soma_pares(lista))  #resultado da soma da lista dentro da função  