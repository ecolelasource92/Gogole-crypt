Cryptage :

texte = input() # le texte a taper 
nbtexte = len(texte) # renvoie le nombre de caracteres qui composent le texte (soit le nombre de lettres)

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",",":","!","?",";","à","é","è","'","\\","\"","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = 0
cle = "CODE" #modifiable
nbcle = len(cle) # decouper la cle en 4 caracteres car il y a 4 lettres dans CODE
quotient = 2// nbcle  # le quotient de la division du nombres de caracteres afilies a chaque programme de cryptage par le nombre de caracteres de la cle
reste = 2 % nbcle # le reste de la division du nombre de caracteres afilies a chaque programme de cryptage par le nombre de caracteres de la cle

while n < (nbtexte-1) : # tant que la variable n est inferieure au nombre de caracteres du texte 
    lettres = texte[n:n+2] #de 2 en 2 pour chaque language
       

    if n%8 == 0 or n%8 == 1 : # si le reste de la division de la position du caractere dans le texte par 8 (2 lettre pour 4 programmes) vaut 0 ou 1
        for loop in range(2) : 
            newCaractere = chr(ord(lettres[loop]) +2) # + 2 rang ordre alphabetique dans Asci et en minuscule
            print(newCaractere, end="")  
		
			

    elif n%8 == 2 or n%8 == 3 :  # et si le reste de la division de la position du caractere dans le texte par 8 vaut 2 ou 3
        for loop in range(2) :
            newCaractere = (ord(lettres[loop]) - 9) # - 9 rang dans tableau Asci et en chiffre
            print(newCaractere, end="")
			    
    elif n%8 == 4 or n%8 == 5: 
        for loop in range(2):
            for eachPos in range(49):                 if lettres[loop].upper() == alphabet[eachPos] :
                    print(alphabet[eachPos + 5], end="") # + 5 dans notre aplbate qui comprend lettres et caracteres speciaux et en majuscule

		
    elif n%8 == 6 or n%8 == 7 :  # vigenere
        for loop in range(quotient) :
            for loopi in range(nbcle) :
               for eatchpos in range(49) : 
                  if cle[loopi] == alphabet[eatchpos] :
                     nvlcle = eatchpos
                     for eachPos in range(49):                        if lettres[loopi+nbcle*loop].upper() == alphabet[eachPos] :
                            print(alphabet[eachPos + nvlcle],end="") 
                        
        for loopi in range(reste) :  
           for eatchpos in range(49):
              if cle[loopi] == alphabet[eatchpos] :
                 nvlcle = eatchpos
                 for eachPos in range(49): 
                    if lettres[loopi+nbcle*quotient].upper() == alphabet[eachPos] :
                        print(alphabet[eachPos + nvlcle],end="")
    n = n + 2

if nbtexte %2 == 1 : #nbr de caractere du mot impaire
    dernierelettre = chr(ord(texte[nbtexte-1]) +6)
    print(dernierelettre, end="")

	
Décryptage :
	
texte = int(input)
nbtexte = len(texte)

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", " ", ".", ",", ":", "!", "?", ";", "à", "é", "è", "'", "\\", "\"", "1", "2", "3",
            "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n = 0
cle = "CODE"  # modifiable
nbcle = len(cle)
quotient = 2 // nbcle  # penser a changer le 2 quand on veut faire prendre + de 2 lettres en vigenere = pour le reste
reste = 2 % nbcle

def asci_lettres() :
    for loop in range(2) :
            newCaractere = chr(ord(lettres[loop]) - 2)
            print(newCaractere, end="")

def asci_chiffres() :
    for loop in range(2):
        newCaractere = (ord(lettres[loop]) + 9)
        print(newCaractere, end="")

def notre_alphabet() :
    for loop in range(2):
        for eachPos in range(49):
            if lettres[loop].upper() == alphabet[eachPos]:
                print(alphabet[eachPos - 5], end="")

def vige_nere() :
    for loop in range(quotient):
        for loopi in range(nbcle):
            for eatchpos in range(49):
                if cle[loopi] == alphabet[eatchpos]:
                    nvlcle = eatchpos
                    for eachPos in range(49):
                        if lettres[loopi - nbcle * loop].upper() == alphabet[eachPos]:
                            print(alphabet[eachPos - nvlcle], end="")

    for loopi in range(reste):
        for eatchpos in range(49):
            if cle[loopi] == alphabet[eatchpos]:
                nvlcle = eatchpos
                for eachPos in range(49):
                    if lettres[loopi - nbcle * quotient].upper() == alphabet[eachPos]:
                        print(alphabet[eachPos - nvlcle], end="")

while n < (nbtexte - 1):
    lettres = texte[n:n + 2]

    if n % 8 == 0 or n % 8 == 1:
        asci_lettres()

    elif n % 8 == 2 or n % 8 == 3:
        asci_chiffres()

    elif n % 8 == 4 or n % 8 == 5:
        notre_alphabet()

    elif n % 8 == 6 or n % 8 == 7:
        vige_nere()

