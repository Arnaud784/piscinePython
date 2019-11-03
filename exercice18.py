
def correspondance_adn(adn, code1, code2):
    
    for i in range(len(adn)-4):
    
        bout = adn[i:i+4]
    
        if code1 == bout:
    
            resteADN = adn[:i] + adn[i+4:]
    
            for i in range(len(resteADN)-4):
    
                bout2 = resteADN[i:i+4]
    
                if code2 == bout2:
    
                    return True
    return False
                
    


code1 = "CATA"
code2 = "ATGC"
prenoms = ["colonel Moutarde", "Mlle Rose", "Mme Pervenche", "M. Leblanc"]
ADN = ["CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCADN", "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGADN", "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCCADN", "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"]
for i in range(len(ADN)):
    if correspondance_adn(ADN[i], code1, code2) == True:
        print("L'ADN de ", prenoms[i], "correspond.")
        print("Le coupable est : ", prenoms[i])
    else:
        print("L'ADN de ", prenoms[i], "ne correspond pas.")
