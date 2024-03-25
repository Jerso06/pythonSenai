frase = str(input("Insira a frase: "))

letrasA = frase.count("a")
primeiroA = frase.find("a")
ultimoA = frase.rfind("a")

print(f"Quantidades de 'a': {letrasA}\nPrimeira posição: {primeiroA}\nÚltima posição: {ultimoA}")