#Gerador de Senha V1

import numpy as np

print("Gerador de Senha v2\n")

querNum = input("Deseja ter numeros? S/N: ")
querEspe = input("Deseja ter simbolos? S/N: " )
querLetrasMais = input("Deseja ter letras maisculas? S/N: ")
querLetrasMin = input("Deseja ter letras minusculas? S/N: ")

letrasMa = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letrasmi = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]
caracEspeciais = ["!","@","#","$","&","*"]
senha = []

r = np.random.randint(0, 26)
l = np.random.randint(0,10)
f = np.random.randint(0,6)

senha.append(letrasMa[r])
senha.append(letrasmi[r])
senha.append(numeros[l])
senha.append(caracEspeciais[f])

match querNum:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(numeros[l])
    case "n":
        senha.remove(numeros[l])

match querEspe:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(caracEspeciais[f])
    case "n":
        senha.remove(caracEspeciais[f])

match querLetrasMais:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(letrasMa[r])
    case "n":
        senha.remove(letrasMa[r])

match querLetrasMin:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(letrasmi[r])
    case "n":
        senha.remove(letrasmi[r])

if querEspe and querNum and querLetrasMais and querLetrasMin == "N":
    print("Ai c me quebra")

senha.sort()
print(senha)
