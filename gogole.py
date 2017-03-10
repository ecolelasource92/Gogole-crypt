   
texte = input()

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = 0

while n <= len(texte) :
    lettres = texte[n:n+2]
   

    if n == 0 :
        for loop in range(2) :
            newCaractere = chr(ord(lettres[loop]) +2)

            print(newCaractere, end="")

    elif n == 2 :
        for loop in range(2) :

            newCaractere = (ord(lettres[loop]) - 9)

            print(newCaractere, end="")


    elif n == 4  :
        for loop in range(2) :


            for eachPos in range(26):

                if lettres[loop].upper() == alphabet[eachPos] :

                    print(alphabet[eachPos + 5], end="")


    n = n + 2
