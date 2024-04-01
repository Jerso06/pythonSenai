n1 = int(input("informe o número de gols do primeiro time: "))
n2 = int(input("informe o numero de gols do segundo time: "))

if n1>n2:
    print("O time 1 ganhou")
elif n2>n1:
    print("O time 2 ganhou")
else:
    print("O jogo empatou")