# Escreva uma função que recebe uma matriz e retorna o maior elemento presente nela

def maior(matriz):
    maior = matriz[0][0]   #como se tudo 0

    for linhas in range(len(matriz)):  #começa com a 1ªlinha --- depois 2ª linha

        for coluna in range(len(matriz[linhas])):  #pega o 1ª coluna --- depois 2ª coluna
            
            if matriz[linhas][coluna] > maior:   #ele vai vendo qual é o maior num, qnd lê a lista de matriz...
                maior = matriz[linhas][coluna]   #aqui ele vai mudando o num caso seja maior q o anterior 
                
    return maior            

#lista de matriz
minha_matriz = [
    [1, 2, 3],
    [4, 20, 6],
    [7, 8, 9]
]

print(maior(minha_matriz))
