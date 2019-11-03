
def distance_hamming(mot1, mot2):
 
    distance = 0
    
    for i in range(len(mot1)):
    
        if mot1[i] != mot2[i]:
    
            distance += 1
    
    print("La distance entre les deux mots est de", distance)
    
    
mot1 = input('Entrez un mot: ')
mot2 = input('Entrez un deuxième mot: ')
distance_hamming(mot1, mot2)