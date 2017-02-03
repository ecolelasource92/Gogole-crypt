
texte = input()
newCaractere = chr(ord(texte) +2)
print(newCaractere)

texte = input()
nblettres= len(texte)
for loop in range(nblettres) :
   newCaractere = (ord(texte[loop]) - 9)
   print(newCaractere, end="")

texte = input().upper()
i = 0
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for loop in range(len(texte)) :
	if i <= 1 :
		for eachPos in range(26):
			if texte[loop] == alphabet[eachPos] :
				print(alphabet[eachPos + 5], end="")
				break
	i = i +1	
