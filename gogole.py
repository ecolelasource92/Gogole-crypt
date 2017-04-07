texte = input()
nbtexte = len(texte)

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",",":","!","?",";","à","é","è","'","\\","\"","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = 0
cle = "CODE" #modifiable
nbcle = len(cle)
quotient = 2// nbcle  #penser a changer le 2 quand on veut faire prendre + de 2 lettres en vigenere = pour le reste
reste = 2 % nbcle 

while n < (nbtexte-1) :
    lettres = texte[n:n+2] #de 2 en 2 pour chaque language
   
    
   
    if n%8 == 0 or n%8 == 1 : # + 2 dans Asci et en minuscule
        for loop in range(2) : 
            newCaractere = chr(ord(lettres[loop]) +2)
            print(newCaractere, end="")  
		
			

    elif n%8 == 2 or n%8 == 3: # - 9 dans Asci et en chiffres
        for loop in range(2) :
            newCaractere = (ord(lettres[loop]) - 9)
            print(newCaractere, end="")
			
    
    elif n%8 == 4 or n%8 == 5: # + 5 dans l'alphabet et en majuscule
        for loop in range(2):
            for eachPos in range(49): 
                if lettres[loop].upper() == alphabet[eachPos] :
                    print(alphabet[eachPos + 5], end="")
     
    elif n%8 == 6 or n%8 == 7 :  # vigenere
        for loop in range(quotient) :
            for loopi in range(nbcle) :
               for eatchpos in range(49) : 
                  if cle[loopi] == alphabet[eatchpos] :
                     nvlcle = eatchpos
                     for eachPos in range(49):
                        if lettres[loopi+nbcle*loop].upper() == alphabet[eachPos] :
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
