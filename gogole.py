texte = input()

nbLettres = len(texte)



i = 0
for loop in range(nbLettres) :
    if i <= 1 :
        newCaractere = chr(ord(texte[loop]) +2)
        print(newCaractere, end="")
        i = i + 1
    else : 
        break

k = 0
for loop in range(nbLettres) :
    if k <= 1 :
        newCaractere = (ord(texte[loop]) - 9)
        print(newCaractere, end="")
        k = k + 1 
    else :
      break

texte = texte.upper()
g = 0
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for loop in range(nbLettres) :
    if g <= 1 :
        for eachPos in range(26):
            if texte[loop] == alphabet[eachPos] :
                print(alphabet[eachPos + 5], end="")
                break
    g = g +1	
