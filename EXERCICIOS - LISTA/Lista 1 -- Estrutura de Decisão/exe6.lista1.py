#6) Escreva um programa para ler as três notas obtidas por um aluno durante
#o semestre. Calcular a sua média (aritmética) e informar a sua menção Aprovado (media
#>= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 e 6.9)


a = float(input("nota1: "))
b = float(input("nota1: "))
c = float(input("nota1: "))

media = (a + b + c)/3

if media >= 7:
    print("aprovado")
    
elif media >= 5.1 and media <= 6.9:
    print("recuperacao")
    
else:
    print("reprovado")