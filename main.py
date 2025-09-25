x=int(input("Digite um numero: "))

if x%2==0:
    print("%i e um numero par"%x)
else:
    print("%i e um numero impar"%x)

nota1=float(input("Informe a primeira nota: "))
nota2=float(input("Informe a segunda nota: "))

media=(nota1+nota2)/2

if media>=6:
    print("Sua media foi: %.1f - aprovado"%media)
else:
     print("Sua media foi: %.1f - reprovado"%media)
