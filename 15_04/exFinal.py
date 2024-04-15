

valorEmprestimo = float(input("Informe o valor do Empréstimo: "))
salLiquido = float(input("Informe o seu salário líquido: "))
mesesPagamento = int(input("Informe o número de meses para o pagamento: "))

nome = input("Informe o seu nome completo: ")
while(nome != nome.title() or nome.isalpha() == False):
    nome = input("Informe o nome corretamente: ")

cpf = input("Informe o seu CPF: ")
while(len(cpf) != 11 or cpf.isdigit() == False):
    cpf = (input("Informe o CPF corretamente: "))

telefone = input("Informe o telefone: ")
while(telefone != telefone.strip() or telefone.isdigit() == False):
    telefone = (input("Informe o telefone corretamente (sem espaçoes e caracteres especiais): "))

endereco = input("Informe o endereço: ")

cep = input("Informe o CEP: ")
while(len(cep) != 8 or cep != cep.strip() or cep.isdigit() == False):
    cep = (input("Informe o CEP corretamente: "))

email = input("Informe o email: ")
while(email != email.lower() or email.find("@gmail.com") == -1):
    email = input("Informe o email (gmail) corretamente: ")

prestMensal = valorEmprestimo/mesesPagamento
if(prestMensal > salLiquido*0.3):
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado!")