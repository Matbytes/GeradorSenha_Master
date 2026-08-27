#Gerador de Senha V2
import random

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
universo = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","&","*"]
senha = []


f = 4
x = random.randint(0, 25)
b = random.randint(0,25)
y = random.randint(0,9)
z = random.randint(0,5)
w = random.randint(0,f)

Listas = [letrasMa[x], letrasmi[b], numeros[y], caracEspeciais[z]]


senha.append(letrasMa[x])
senha.append(letrasmi[b])
senha.append(numeros[y])
senha.append(caracEspeciais[z])

if numCarac > 4:
    numCarac -= 4
    for i in range(0,numCarac):
        t = random.choice(universo)
        if t in senha:
            t = random.choice(universo)
            senha.append(t)
        else:
            senha.append(t)
    random.shuffle(senha)
else:
    pass

match querNum:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(numeros[y])
        Listas.remove(numeros[y])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])
    case "n":
        senha.remove(numeros[y])
        Listas.remove(numeros[y])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])

match querEspe:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(caracEspeciais[z])
        Listas.remove(caracEspeciais[z])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])
    case "n":
        senha.remove(caracEspeciais[z])
        Listas.remove(caracEspeciais[z])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])

match querLetrasMais:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(letrasMa[x])
        Listas.remove(letrasMa[x])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])
    case "n":
        senha.remove(letrasMa[x])
        Listas.remove(letrasMa[x])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])

match querLetrasMin:
    case "S":
        pass
    case "s":
        pass
    case "N":
        senha.remove(letrasmi[b])
        Listas.remove(letrasmi[b])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])
    case "n":
        senha.remove(letrasmi[b])
        Listas.remove(letrasmi[b])
        f -= 1
        Listas.append(Listas[w])
        senha.append(Listas[w])

if f == 0:
    print("Ai c me quebra")

random.shuffle(senha)

Senha_Final = "".join(senha)
print(Senha_Final)
