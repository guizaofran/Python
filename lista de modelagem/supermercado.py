frutas=set(range(1,101))
laticinios=set(range(71,151))
carnes=set(range(126,186))

peloMenosUm=frutas.union(laticinios,carnes)
somenteFrutas=frutas.difference(laticinios.union(carnes))

print("Pelo menos um: ",len(peloMenosUm))
print("Somente frutas: ",len(somenteFrutas))

