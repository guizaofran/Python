futebol = set(range(1, 36))
volei = set(range(26, 56))
basquete = set(range(46, 71))


peloMenosUm = futebol.union(volei, basquete)
somenteBasquete = basquete.difference(futebol.union(volei))

print("Pelo menos um esporte:", len(peloMenosUm))
print("Somente basquete:", len(somenteBasquete))