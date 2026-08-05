#Gerador de Senha V1

import numpy as np

print("Gerador de Senha v2\n")

numCarac = input("Numero de caracteres da senha: ")
numCarac = int(numCarac)
 
while numCarac < 4:
    print("Erro: A senha deve ter no minimo 4 caracteres")
    numCarac = input("Numero de caracteres da senha: ")
    numCarac = int(numCarac)
    if numCarac >= 4:
        break

querNum = input("Deseja ter numeros? S/N: ")
querEspe = input("Deseja ter simbolos? S/N: " )
querLetrasMais = input("Deseja ter letras maisculas? S/N: ")
querLetrasMin = input("Deseja ter letras minusculas? S/N: ")

letrasMa = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letrasmi = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
caracEspeciais = ["!","@","#","$","&","*"]
senha = []

x = np.random.randint(0, 26)
y = np.random.randint(0,10)
z = np.random.randint(0,6)
w = np.random.randint(0,4)

Listas = [letrasMa[x], letrasmi[x], numeros[y], caracEspeciais[z]]


senha.append(letrasMa[x])
senha.append(letrasmi[x])
senha.append(numeros[y])
senha.append(caracEspeciais[z])

'''
for i in range(0,numCarac):
    senha.extend(Listas[w])
'''

match querNum:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(numeros[y])
        Listas.remove(numeros[y])
        senha.append(Listas[w])
    case "n":
        senha.remove(numeros[y])
        Listas.remove(numeros[y])
        senha.append(Listas[w])

match querEspe:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(caracEspeciais[z])
        Listas.remove(caracEspeciais[z])
        senha.append(Listas[w])
    case "n":
        senha.remove(caracEspeciais[z])
        Listas.remove(caracEspeciais[z])
        senha.append(Listas[w])

match querLetrasMais:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(letrasMa[x])
        Listas.remove(letrasMa[x])
        senha.append(Listas[w])
    case "n":
        senha.remove(letrasMa[x])
        Listas.remove(letrasMa[x])
        senha.append(Listas[w])

match querLetrasMin:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(letrasmi[x])
        Listas.remove(letrasmi[x])
        senha.append(Listas[w])
    case "n":
        senha.remove(letrasmi[x])
        Listas.remove(letrasmi[x])
        senha.append(Listas[w])

if querEspe and querNum and querLetrasMais and querLetrasMin == "N":
    print("Ai c me quebra")

senha.sort()
print(senha)
