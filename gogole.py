texte = input()
nbtexte = len(texte)

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = 0
cle = "CODE" 
nbcle = len(cle)

quotient = 2// nbcle 
reste = 2 % nbcle

if nbtexte == 8 :
    while n < nbtexte :
      lettres = texte[n:n+2] 
   
      if n == 0 or n == 8 or n== 16 or n== 32 : 
         for loop in range(2) :
            newCaractere = chr(ord(lettres[loop]) +2)

            print(newCaractere, end="")

      elif n == 2 or n== 10 or n== 18 or n== 26 : 
         for loop in range(2):

            newCaractere = (ord(lettres[loop]) - 9)

            print(newCaractere, end="")

      elif n == 4 or n== 12 or n== 20 or n== 28 : 
        for loop in range(2) :


            for eachPos in range(26): 

                if lettres[loop].upper() == alphabet[eachPos] :

                    
				print(alphabet[eachPos + 5], end="")
				
      elif n == 6 or n== 14 or n== 22 or n == 30: 
        for loop in range(quotient) :
            for loopi in range(nbcle) :
               for eatchpos in range(26): 
                  if cle[loopi] == alphabet[eatchpos] :
                     nvlcle = eatchpos
                     for eachPos in range(26):
                        if lettres[loopi+nbcle*loop].upper() == alphabet[eachPos] :
                            print(alphabet[eachPos + nvlcle],end="") 
                        
        for loopi in range(reste) :
           for eatchpos in range(26):
              if cle[loopi] == alphabet[eatchpos] :
                 nvlcle = eatchpos
                 for eachPos in range(26): 
                    if lettres[loopi+nbcle*quotient].upper() == alphabet[eachPos] :
                        print(alphabet[eachPos + nvlcle],end="")
    
      n = n + 2
else :
    for loop in range (nbtexte // 8) :
        while n < nbtexte :
           lettres = texte[n:n+2] 
   
           if n == 0 or n == 8 or n== 16 or n==32 : 
              for loop in range(2) :
                 newCaractere = chr(ord(lettres[loop]) +2)

                 print(newCaractere, end="")

           elif n == 2 or n== 10 or n== 18 or n== 26: 
              for loop in range(2) :

                 newCaractere = (ord(lettres[loop]) - 9)

                 print(newCaractere, end="")

           elif n == 4 or n== 12 or n== 20 or n== 28 : 
              for loop in range(2) :

			     for eachPos in range(26): 

                    if lettres[loop].upper() == alphabet[eachPos] :

                       print(alphabet[eachPos + 5], end="")
           
		   elif n == 6 or n== 14 or n== 22 or n == 30: 
              for loop in range(quotient) :
                 for loopi in range(nbcle) :
                    for eatchpos in range(26): 
                       if cle[loopi] == alphabet[eatchpos] :
                          nvlcle = eatchpos
                          for eachPos in range(26):
                             if lettres[loopi+nbcle*loop].upper() == alphabet[eachPos] :
                               print(alphabet[eachPos + nvlcle],end="") 
                        
              for loopi in range(reste) :
                 for eatchpos in range(26):
                    if cle[loopi] == alphabet[eatchpos] :
                       nvlcle = eatchpos
                       for eachPos in range(26): 
                          if lettres[loopi+nbcle*quotient].upper() == alphabet[eachPos] :
                             print(alphabet[eachPos + nvlcle],end="")
    
        n = n + 2
