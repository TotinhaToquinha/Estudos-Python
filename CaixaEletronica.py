print("Caixa eletronico")

saque = int(input("(A caixa contem apenas notas de $10, $20 e $50)Quanto vc quer sacar? $"))
saquesave = int(saque)

nota10 = 0
nota20 = 0
nota50 = 0

while saquesave > 0:
	
	if saquesave >= 50:
		nota50  += 1
		saquesave -= 50
		
	elif saquesave >= 20:
		nota20 += 1
		saquesave -= 20
		
	elif saquesave >= 10:
		nota10 += 1
		saquesave -= 10
		
	else:
		print("Você quer sacar {}, mas so tem notas de $10, $20 e $50 na caixa eletronica.".format(saque))
		print("Aredonde seu saque")
		break
		
if saquesave == 0:
		print("sacou ${} com {} notas de $10, {} notas de $20, {} com notas de $50".format(saque, nota10, nota20, nota50)) 
