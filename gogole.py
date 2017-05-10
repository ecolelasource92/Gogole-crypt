#Cryptage 	
texte = input() #utilisateur doit rentrer le texte qu'il souhaite coder
nbtexte = len(texte) # fonction qui permet de retourner la longueur de la chaine de caracteres


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",

            "V", "W", "X", "Y", "Z", " ", ".", ",", ":", "!", "?", ";", "#", "(", ")", "'", "\\", "\"", "-", "1", "2", "3",

            "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",

            "O", "P", "Q", "R", "S", "T"] # notre alphabet specifique

n = 0 # variable ou curseur qui selon son reste par la division euclidienne permet de definir le caractere du texte a coder 
cle = "CODE"  # utile pour le programme de Vigenere
nbcle = len(cle) # retourner la longueur de la chaine de caracteres
quotient = 2 // nbcle  # on divise le nombre le nombre de lettres codees dans un meme programme de codage par le nombre de caracteres de la cle  




def asci_lettres() : #fonction qui transforme deux caracteres cote a cote en deux lettres contenues dans le tableau ASCII

    for loop in range(2) : #boucle qui tourne deux fois pour coder les deux caracteres

            newCaractere = chr(ord(lettres[loop]) -3) 
		# ord = fonction qui transforme la lettre associee au caractere a son chiffre complementaire dans ASCII
		# chr = fonction qui transforme chaque caractere en associant le chiffre du tableau ASCII en sa lettre associee
		# -3 = reculer de 3 rangs pour avoir une nouvelle lettre


            print(newCaractere, end="") # sortir les 2 nouveaux caracteres codes 



def asci_diminu() : # meme fonction mais cette fois sous forme de soustraction

    for loop in range(2):

        newCaractere = chr(ord(lettres[loop]) + 2) # meme chose que precedemment en utilisant le tableau ASCII
						   # mais cette fois on fait + 3 rangs pour avoir une nouvelle lettre

        print(newCaractere, end="") # sortir les 2 nouveaux caracteres codes 



def notre_alphabet() : # fontion qui se refere au tableau que nous avons cree, qui compte les caracteres speciaux

    for loop in range(2):

        for eachPos in range(70): # boucle qui tourne entierement dans notre tableau unique de 70 caracteres

            if lettres[loop].upper() == alphabet[eachPos]: # condition
							   # si le caractere dans le texte sous forme majuscule 
							   # est identique a un des 70 caracteres dans notre tableau

                print(alphabet[eachPos + 5], end="") # afficher 2 nouveaux caracteres de 5 rang superieur



def vige_nere() :

    for loop in range(quotient):

        for loopi in range(nbcle):

            for eatchpos in range(70):

                if cle[loopi] == alphabet[eatchpos]:

                    nvlcle = eatchpos

                    for eachPos in range(70):

                        if lettres[loopi + nbcle * loop].upper() == alphabet[eachPos]:

                            print(alphabet[eachPos + nvlcle], end="")



  



def texte_impaire() : # puisque chaque programme code pour 2 caracteres cote a cote, si le texte est impair alors 
		      # le dernier caractere va etre code selon une fonction specifique

    dernierelettre = chr(ord(texte[nbtexte - 1]) + 6) # selon le tableau ASCII, convertir en chiffre puis en lettre 
						      # puis avancer de 6 rangs

    print(dernierelettre, end="") # afficher le dernier caractere code 


# programme principal de codage qui appelle les 5 methodes :

while n < (nbtexte - 1): # boucle tant que conditonnelle
			 # tant que la variable curseur est inferieur a la longueur du texte a coder - 1 (car on compte le 0)

    lettres = texte[n:n + 2] # chaque methode de cryptage code 2 caracteres cote a cote dans le texte



    if n % 8 == 0 or n % 8 == 1: # si le reste de la variable n divise par 8 (nombre de methodes de codage) vaut 0 ou 1
				 
        asci_lettres() # alors on appelle la methode 1 (pour les 2 premiers caracteres)



    elif n % 8 == 2 or n % 8 == 3: # si le reste de la variable n divise par 8 vaut 2 ou 3

        asci_diminu() # on appelle la methode 2 (pour les 2 caracteres suivants)


    elif n % 8 == 4 or n % 8 == 5: #si le reste de la variable n divise par 8 vaut 4 ou 5

        notre_alphabet() # on appelle la methode 3 (pour les 2 caracteres suivants)



    elif n % 8 == 6 or n % 8 == 7: #si le reste de la variable n divise par 8 vaut 6 ou 7

        vige_nere() # on appelle la methode 4 (pour les 2 caracteres suivants)


	n = n + 2 # n prend des nouvelles valeurs de 2 en 2 pour appeler differentes methodes de cryptage (ca change le reste)



if nbtexte % 2 == 1: # si le texte est impair car le reste vaut 1

    texte_impaire() # appeler pour le tout dernier caractere du texte la derniere methode de cryptage 

	
#Décryptage :
	

texte = input()
nbtexte = len(texte)


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",

            "V", "W", "X", "Y", "Z", " ", ".", ",", ":", "!", "?", ";", "#", "(", ")", "'", "\\", "\"", "-", "1", "2", "3",

            "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",

            "O", "P", "Q", "R", "S", "T"]# notre alphabet specifique

n = 0
cle = "CODE"  # modifiable
nbcle = len(cle)
quotient = 2 // nbcle  # penser a changer le 2 quand on veut faire prendre + de 2 lettres en vigenere = pour le reste

def asci_lettres() :
    for loop in range(2) :
	newCaractere = chr(ord(lettres[loop]) + 3)
        print(newCaractere, end="")

def asci_diminue() :
    for loop in range(2):
        newCaractere = chr(ord(lettres[loop]) - 2)
        print(newCaractere, end="")

def notre_alphabet() :
    for loop in range(2):
        for eachPos in range(50):
            if lettres[loop].upper() == alphabet[eachPos]:
                print(alphabet[eachPos - 5].lower(), end="")

def vige_nere() :
    for loop in range(quotient):
        for loopi in range(nbcle):
            for eatchpos in range(70):
                if cle[loopi] == alphabet[eatchpos]:
                    nvlcle = eatchpos
                    for eachPos in range(70):
                        if lettres[loopi - nbcle * loop].upper() == alphabet[eachPos]:
                            print(alphabet[eachPos - nvlcle].lower(), end="")



def texte_impaire() :
    dernierelettre = chr(ord(texte[nbtexte - 1]) - 6)
    print(dernierelettre.lower(), end="")

# progrmme principal de decryptage :	
while n < (nbtexte - 1):
    lettres = texte[n:n + 2]

    if n % 8 == 0 or n % 8 == 1:
        asci_lettres()

    elif n % 8 == 2 or n % 8 == 3:
        asci_diminue()

    elif n % 8 == 4 or n % 8 == 5:
        notre_alphabet()

    elif n % 8 == 6 or n % 8 == 7:
        vige_nere()

    n = n + 2

if nbtexte % 2 == 1:
    texte_impaire()


