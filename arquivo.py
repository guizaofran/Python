arquivo=open('arqText.txt','w')

arquivo.write('curso python\n')
arquivo.write('curso python\n')
arquivo.write('teste\n')
arquivo.close()

leitura=open('arqText.txt','r')
print(leitura.read())
leitura.close