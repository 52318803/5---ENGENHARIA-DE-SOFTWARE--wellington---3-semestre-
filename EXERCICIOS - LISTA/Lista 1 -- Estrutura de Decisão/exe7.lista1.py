#7) Desenvolva um programa para calcular e mostrar o desconto no valor de uma compra

compra = int(input("valor total da compra? "))

if compra > 5000.00:                                 
    desc = compra * 0.70
    print(f"desnconto de 30% ---> {desc}")

elif compra > 1000.00 and compra <= 5000.00:    #valor_descontado = valor_original * 0.2   - esse é o valor do desconto 
    desc = compra * 0.80                        #novo_valor = valor_original * 0.80        - esse é o novo valor com o desconto incluso
    print(f"desconto de 20% ---> {desc}")

else:
    desc = compra * 0.90
    print(f"desconto de 10% ---> {desc}")