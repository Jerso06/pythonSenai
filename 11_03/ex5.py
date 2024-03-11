valor = float(input("Insira o valor: "))
taxa = float(input("Insira a taxa: "))
tempo = int(input("Insira o tempo: "))

def calcPrest():
    prestacao = valor +(valor*(taxa/100) * tempo)
    print("Prestação: ",prestacao)
    
calcPrest()