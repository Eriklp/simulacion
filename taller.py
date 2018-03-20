
# File:   taller.py
# Author: Camilo Jose Cruz Rivera 1428907
# Author: Erik Lopez Pacheco 1430406
# Author: Jesus Alberto Ramirez Otalvaro 1422554

# Created on 14 de Marzo de 2018, 16:21


from mersenne_twister import get_array
listanumeros = get_array(40)

print(listanumeros)


# PUNTO 1
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


# PUNTO 3

# resultado = [0,0]
# estado = ""
# corridas = 0
# estados = []

# for i in range(len(listanumeros)-1):

# 	if(listanumeros[i] < listanumeros[i +1]):
# 		resultado[0] += 1
# 		estado = "subio"
# 		#estados.append(estado)
# 	elif(listanumeros[i] > listanumeros[i +1]):
# 		resultado[1] += 1
# 		estado = "bajo"
# 		#estados.append(estado)
# 	else:
# 		if(estado == "subio"):
# 			resultado[0] += 1
# 			#estados.append(estado)
# 		elif(estado == "bajo"):
# 			resultado[1] += 1
# 			#estados.append(estado)
# 	estados.append(estado)

# print(resultado)

# for i in range(len(estados)-1):
# 	if(estados[i] != estados[i+1]):
# 		corridas += 1


# print corridas

# PUNTO 4

# tuplas = []
# matriz = [[0,0,0],[0,0,0],[0,0,0]]

# for i in range(len(listanumeros)):
# 	if(i%2 == 0):
# 		x = listanumeros[i]/float(pow(2, 32))
# 		y = listanumeros[i+1]/float(pow(2, 32))
# 		tupla = (x,y)
# 		tuplas.append(tupla)

# for i in range(len(tuplas)):
# 	if(tuplas[i][0] >= 0 and tuplas[i][0] < 0.33):
# 		if(tuplas[i][1] >=0 and tuplas[i][1] < 0.33):
# 			matriz[0][0] += 1
# 		elif(tuplas[i][1] >=0.33 and tuplas[i][1] < 0.66):
# 			matriz[0][1] += 1
# 		elif(tuplas[i][1] >=0.66 and tuplas[i][1] < 1):
# 			matriz[0][2] += 1
# 	elif(tuplas[i][0] >= 0.33 and tuplas[i][0] < 0.66):
# 		if(tuplas[i][1] >=0 and tuplas[i][1] < 0.33):
# 			matriz[1][0] += 1
# 		elif(tuplas[i][1] >=0.33 and tuplas[i][1] < 0.66):
# 			matriz[1][1] += 1
# 		elif(tuplas[i][1] >=0.66 and tuplas[i][1] < 1):
# 			matriz[1][2] += 1
# 	elif(tuplas[i][0] >= 0.66 and tuplas[i][0] < 1):
# 		if(tuplas[i][1] >=0 and tuplas[i][1] < 0.33):
# 			matriz[2][0] += 1
# 		elif(tuplas[i][1] >=0.33 and tuplas[i][1] < 0.66):
# 			matriz[2][1] += 1
# 		elif(tuplas[i][1] >=0.66 and tuplas[i][1] < 1):
# 			matriz[2][2] += 1

# print(matriz)


# ###PUNTO 5
# # listanumerosNormalizados = []
# matriz = [0,0,0]
# for i in listanumeros:
# 	x = i/float(pow(2, 32))
# 	# listanumerosNormalizados.append(x.split)
# 	xStr = str(x)
# 	if(xStr[2] == xStr[3] and xStr[2] == xStr[4] and xStr[3] == xStr[4] ):
# 		matriz[0] += 1
# 	elif(xStr[2] != xStr[3] and xStr[2] != xStr[4] and xStr[4] != xStr[3]):
# 		matriz[2] += 1
# 	else:
# 		matriz[1] += 1


# print matriz


### PUNTO 6

# listaGrande = get_array(120)
# listaGrandeNormalizada = []
# # IMPRIMIR listaGrande normalizada
# for i in listaGrande:
# 	val = i/float(pow(2, 32))
# 	listaGrandeNormalizada.append(val)
# 	print val

# resultado = []
# iterator = 1
# suma = 0

# for i in range(len(listaGrandeNormalizada)):
# 	if(iterator == 12):
# 		suma += listaGrandeNormalizada[i]		
# 		suma -=6
# 		resultado.append(suma)
# 		iterator = 1
# 	else:
# 		suma += listaGrandeNormalizada[i]
# 		iterator += 1

# # IMPRIMIR resultado
# for i in resultado:
# 	print i

##PUNTO 7

#fx = [0.5, 0.539, 0.579, 0.617, 0.655, 0.691, 0.725, 0.758, 0.788, 0.815, 0.841, 0.864, 0.884, 0.903, 0.919, 0.933, 0.945, 0.955, 0.964, 0.971, 0.977, 0.982, 0.986, 0.989, 0.991, 0.993, 0.995, 0.996, 0.997, 0.998]

# rfx = [0.50000, 0.84134, 0.97725, 0.53983, 0.86433, 0.98214, 0.57926, 0.88493, 0.98610, 0.61791, 0.90320, 0.98928, 0.65542, 0.91924, 0.99180, 0.69146, 0.93319, 0.99379, 0.72575, 0.94520, 0.99534, 0.75804, 0.95543, 0.99653, 0.78814, 0.96407, 0.99744, 0.81594, 0.97128, 0.99813 ,0.99865, 0.00135, 0.02872, 0.18406, 0.00187, 0.03593, 0.21186, 0.00256, 0.04457, 0.24196, 0.00347, 0.05480, 0.27425, 0.00466, 0.06681, 0.30854, 0.00621, 0.08076, 0.34458, 0.00820, 0.09680, 0.38209, 0.01072, 0.11507, 0.42074, 0.01390, 0.13567, 0.46017, 0.01786, 0.15866, 0.50000, 0.02275]
# 
# x = [-3, -2.9, -2.8, -2.7, -2.6, -2.5, -2.4, -2.3, -2,2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3]
# 
# fx= sorted(rfx)
# 
# intervalos=[]
# intervalosX=[]
# 
# for i in range(len(listanumeros)):
	# listanumeros[i]=listanumeros[i]/float(pow(2, 32))
# 
# for i in range(len(listanumeros)):
	# for j in range(len(fx)):
		# if listanumeros[i]< fx[j]:
			# aux=(fx[j-1], fx[j])
			# aux2=(x[j-1],x[j])
			# intervalos.append(aux)
			# intervalosX.append(aux2)
			# break 
			# 
# print intervalosX
# 
