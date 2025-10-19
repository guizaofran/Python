eletronica=set(range(1,91))
mecanica=set(range(76,151))
informatica=set(range(126,186))

peloMenosUm=eletronica.union(mecanica,informatica)
somenteInformatica=informatica.difference(mecanica.union(eletronica))

print("Pelo menos um: ",len(peloMenosUm))
print("Somente informática: ",len(somenteInformatica))