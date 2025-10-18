matematica=set(range(1,41))
fisica=set(range(21,56))

todos=matematica.union(fisica)
apenasMatematica=matematica.difference(fisica)
apenasFisica=fisica.difference(matematica)

print("Total em pelo menos um curso: ", len(todos))

print("Total apenas em matemática: ",len(apenasMatematica))
print("Total apenas em física: ",len(apenasFisica))
