#Dada uma lista de palavras, crie uma nova lista com o comprimento de cada palavra

lista = ["carne moida", "arroz caseiro", "saladinha"]
lista_vazio = []

for i in lista:   #i pega uma palavra em lista
    lista_vazio.append(len(i))
    #e conta(len) o qnts caracteres possui, add(append) em lista vazia

print(lista_vazio)
