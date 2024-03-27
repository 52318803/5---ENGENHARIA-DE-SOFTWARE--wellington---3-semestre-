#Implemente uma função que conta o número de vogais em uma palavra.

def tabule(palavra):
    vogais = 0

    for i in palavra:
        if i in "aeiou":
            vogais += 1  #conta cada a/e/i/o/u
    return vogais

palavra = input("Escreva uma palavra: ")
vogais = tabule(palavra)

print(vogais)
