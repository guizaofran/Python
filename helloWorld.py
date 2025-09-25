codigo=int(input("Seu codigo: "))
salario=float(input("Seu salario: "))
nome=input("Insira seu nome: ")
situacao=True

tipo=type(situacao)

print('Codigo: %i '%codigo)
print('\nSalario: $%i'%salario)
print('\nNome: %s'%nome)
print('\nSituacao: %r\n'%situacao)
print(tipo)