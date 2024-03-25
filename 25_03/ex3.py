cidade = str(input("Informe o nome da cidade: "))

comeco = cidade.find("Santo")

if(comeco == 0):
    print("Começa com 'Santo'")

else:
    print("Não começa com 'Santo'")