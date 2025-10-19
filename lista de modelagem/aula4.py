import random

sorteio=[random.randint(1,20) for i in range(10)]
print(sorteio)

random.seed(40)
valores=[random.random() for i in range(5)]
random.seed(40)
valores2=[random.random() for i in range(5)]

print("Primeira execução: ",valores)
print("Segunda execução: ",valores2)
print("São iguais? ",valores==valores2)