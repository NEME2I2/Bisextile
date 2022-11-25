"""

Description : Ce programme a pour but de définir les années bisextiles
Version : v01
Prgrammeur : VeNoM
Licence : MIT 3.0

"""

année= 0 #les années

while année< 2000 : #création de la boucle pour tester toute les année jusqu'à 2000
    if (année%4 == 0 and année%4 != 100 or année%4 == 400): #conditions pour évaluer si l'année est bisextile
        print(année,"est bisextile") #affiche l'année bisextile
    else:
        pass
    année+=1 #incrémetation de la variable année
