literatura=set(range(1,121))
ciencias=set(range(71,161))

total=literatura.union(ciencias)
apenasLiteratura=literatura.difference(ciencias)
apenasCiencias=ciencias.difference(literatura)

print("Total em pelo menos um curso: ",len(total))
print("Somente em literatura: ",len(apenasLiteratura))
print("Somente em ciências: ",len(apenasCiencias))