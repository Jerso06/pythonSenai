teste = input("Insira algo: ")

print("Tipo primitivo: ",type(teste))
print("tamanho da variável: ",len(teste))
print("Apenas espaços: ", teste.isspace())
print("Número: ", teste.isnumeric())
print("Alfabético: ", teste.isalpha())
print("Alfanumérico: ", teste.isalnum())
print("Está maiúsculo: ", teste.isupper())
print("Esta minúsculo: ", teste.islower())
print("Está capitalizada: ", teste.istitle())
