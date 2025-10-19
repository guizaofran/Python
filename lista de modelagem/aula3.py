clienteBrasil = True
comprasAcima100 = False

selecionado=not(clienteBrasil or comprasAcima100)

selecionadoDemorgan=(not clienteBrasil) and (not comprasAcima100)

print(selecionado)
print(selecionadoDemorgan)