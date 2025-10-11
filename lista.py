clientes = 3
servidor_ocupado = False

ha_cliente = clientes > 0        
servidor_deve_estar_ocupado = servidor_ocupado  

proposicao = (not ha_cliente) or servidor_deve_estar_ocupado

print("Há cliente na fila:", ha_cliente)
print("Servidor deve estar ocupado:", servidor_deve_estar_ocupado)