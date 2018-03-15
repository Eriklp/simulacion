#listanumeros = [3521569528,1101990581,1076301704,2948418163,3792022443,2697495705,2002445460,502890592,3431775349,1040222146,3582980688,1840389745,4282906414,1327318762,2089338664,4131459930,3027134324,2835148530,1179416782,1849001581,526320344,2422121673,2517840959,2221714477,55000521,591044015,1168297933,1971159042,4039967188,4139787488,122076017,2865003221,2757324559,1140549535,244059003,4193854726,18931592,4249850126,312057759 ,3675685089]
#listanumeros = [2532366149,2716130141,587579591,2613066757,2843392329,4221221658,4239683583,3592772811,3854560696,2567938102,2486591617,2648294542,278698226,2164677367,466144040,861994134,1922126174,4242479129,1453731229,2248622845,1385042866,611840519,3891490822,3772976688,433055315,3280465593,3227309938,1058619757,3553678900,3787614684,2908544105,1391482497,1059885992,2368779363,1065576133,1307464475,3772231870,2819329938,79679761,1654303468]
from mersenne_twister import get_array
listanumeros = get_array(40)

print(listanumeros)


##PUNTO 1
# sumas = [0,0,0,0,0,0,0,0]
# for i in range(len(listanumeros)):
# 	listanumeros[i]=listanumeros[i]/float(pow(2, 32))
# 	if listanumeros[i]>=0 and listanumeros[i]<0.125:
# 		sumas[0]+=1
# 	elif listanumeros[i]>=0.125 and listanumeros[i]<0.25:
# 		sumas[1]+=1
# 	elif listanumeros[i]>=0.25 and listanumeros[i]<0.375:
# 		sumas[2]+=1
# 	elif listanumeros[i]>=0.375 and listanumeros[i]<0.5:
# 		sumas[3]+=1
# 	elif listanumeros[i]>=0.5 and listanumeros[i]<0.625:
# 		sumas[4]+=1
# 	elif listanumeros[i]>=0.625 and listanumeros[i]<0.75:
# 		sumas[5]+=1
# 	elif listanumeros[i]>=0.75 and listanumeros[i]<0.875:
# 		sumas[6]+=1
# 	elif listanumeros[i]>=0.875 and listanumeros[i]<1:
# 		sumas[7]+=1
# #print(listanumeros)
# print(sumas)
# resultado=0
# for x in sumas:
# 	resultado+= (pow(5-x,2))/5
# print(resultado)


##PUNTO 3

resultado = [0,0]
estado = ""
corridas = 0
estados = []

for i in range(len(listanumeros)-1):
	
	if(listanumeros[i] < listanumeros[i +1]):
		resultado[0] += 1
		estado = "subio"
	elif(listanumeros[i] > listanumeros[i +1]):
		resultado[1] += 1
		estado = "bajo"		
	else:
		if(estado == "subio"):
			resultado[0] += 1
		elif(estado == "bajo"):
			resultado[1] += 1
	estados.append(estado)
	
print(resultado)		

for i in range(len(estados)-1):
	if(estados[i] != estados[i+1]):
		corridas += 1


print corridas
