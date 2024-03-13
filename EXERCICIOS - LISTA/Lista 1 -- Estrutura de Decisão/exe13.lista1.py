
# 13) se um ano é bissexto. Observação


ano = float(input("Digite o ano: "))


if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano Bissesto")

else:
    print("Ano Normal")