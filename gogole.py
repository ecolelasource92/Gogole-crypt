
caractere = input()
newCaractere = chr(ord(caractere) +2)
print(newCaractere)

caractere = input()
newCaractere = (ord(caractere) - 9)
print(newCaractere)

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
