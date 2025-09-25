quantidade=0
soma=0
media=0

valor=int(input("Insira um valor: "))

while (valor>=0):
    soma=soma+valor
    quantidade=quantidade+1
    valor=int(input("Insira um valor: "))

    media=soma/quantidade

    print("\nTotal da soma: %i"%soma)
    print("\nQuantidade de valores: %i"%quantidade)
    print("\nMedia total: %.2f"%media)
