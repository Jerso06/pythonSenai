valor = str(input("Insira um número de 0 a 9999: "))
milhar = "0"
centena = "0"
dezena = "0"
unidade = "0"

if(len(valor) == 4):
    milhar = valor[0]
    centena = valor[1]
    dezena = valor[2]
    unidade = valor[3]

elif(len(valor) == 3):
    centena = valor[0]
    dezena = valor[1]
    unidade = valor[2]

elif(len(valor) == 2):
    dezena = valor[0]
    unidade = valor[1]

elif(len(valor) == 1):
    unidade = valor[0]

else:
    print("Número inválido")

print(f"Milhar: {milhar}\nCentena: {centena}\nDezena: {dezena}\nUnidade: {unidade}")