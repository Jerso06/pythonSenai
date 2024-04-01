from datetime import date


ano = int(input("Insira o ano do seu nascimento: "))

if date.today().year-ano>=18:
    print("Maior de idade")
else:
    print("Menor de idade")