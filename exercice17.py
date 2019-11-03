def verif_palindrome(mot):

    inverseMot = ''
    
    for i in range(len(mot)):
    
        inverseMot = mot[i] + inverseMot
    
    if inverseMot == mot:
    
        print(mot, "est un palindrome")
        
    else:
        print(mot, "n'est pas un palindrome")
        
mot = input('Entrez un mot: ')
verif_palindrome(mot)