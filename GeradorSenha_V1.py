#Gerador de Senha V1

import random

print("Pressione ENTER para gerar uma senha:\n")
input()

letrasMa = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letrasmi = ["a","b","c","d","e","f","g","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
caracEspeciais = ["!","@","#","$","&","*"]
senha = []

r = random.randint(0, 26)
l = random.randint(0,10)
f = random.randint(0,6)

senha.append(letrasMa[r])
senha.append(letrasmi[r])
senha.append(numeros[l])
senha.append(caracEspeciais[f])
senha.sort()

print(senha)


