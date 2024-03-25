nomeCompleto = str(input("Insira o nome:"))

separadoNome = nomeCompleto.split()

print(f"Primeiro nome: {separadoNome[0]}\nÚltimo nome: {separadoNome[len(separadoNome)-1]}")