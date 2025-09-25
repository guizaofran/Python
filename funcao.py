def lernotas():
    nota=float(input("Digite a nota do aluno: "))
    return nota
    
    
def calculo(n1,n2):
        media=(n1+n2)/2
        print("Nota 1: ",n1)
        print("Nota 2: ",n2)
        print("Media: ", media," - ",end="")
        if media >= 6:
            print("aprovado")
        else:
            print ("reprovado")
        
        
x=lernotas()
y=lernotas()
calculo(x,y)