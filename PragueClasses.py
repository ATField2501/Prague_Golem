# -*- coding: utf8 

""" Classes et Fonctions du bot Prague_Golem """


import urllib2
import json
import random
import smtplib

def compta():  
    """
    Compte les lignes du fichier ListeAddSon.txt
    """      
    f = open('ListeAddSon.txt', 'r')        
    NumberOfLine = 0
    for line in f:
        NumberOfLine += 1          
    return NumberOfLine 

def Iss():
    """
    Appel de l'api pour position orbitale de la station spatial ISS
    """
    fichierTMP1 =open(".tmp_iss", "w") 
    req = urllib2.Request( "http://api.open-notify.org/iss-now.json" )
    response = urllib2.urlopen(req)
    obj = json.loads(response.read())                    
    armadda = "Position Actuelle de la station orbitale ISS:  timestamp >>",obj[ "timestamp" ] ,"latidude >>" ,obj[ "iss_position" ][ "latitude" ],"longitude >>",obj[ "iss_position" ][ "longitude" ]                   
    fichierTMP1.write(json.dumps(armadda))
    fichierTMP1.close()
    fichierTMP1 =open(".tmp_iss", "r")
    position_orbitale=fichierTMP1.readlines()[0]
    return position_orbitale

def Traduction(cible959):
    """
    Traduction des url youtube en titres
    """
    response555 = urllib2.urlopen(cible959)
    obj889 = response555.read()
    fichier02 =open(".tmp_recherche.txt", "w")
    fichier02.write(obj889)
    fichier02.close()
    with open(".tmp_recherche.txt", "r") as f:
        for line in f.readlines():
            if '<title>' in line:
                iioonnn = line.split('<title>')
                iii= iioonnn[1]
                ii= iii.split('</title>')                       
                folio=str(ii[0]) 
                spirale= folio.replace('&quot;' , '"')
                spirale= folio.replace('&#39;' , "'")
                url=format(spirale)
    return url

def Son():
    """
    Fait tomber une url au hasard prise dans le fichier ListAddSon.txt
    """
    fichierSon =  open("ListeAddSon.txt", "r") 
    NumberOfLine=compta()                
    from random import randrange
    risop = random.randint(0,NumberOfLine)
    musique = fichierSon.readlines()[risop]
    fichierSon.close()
    return musique

def Addson(slurP):
    """
    Ajoute une entree au fichier
    """
    ya=False
    fichierSon =  open("ListeAddSon.txt", "a")                 
    if len(slurP) == 51 or len(slurP) == 36 or len(slurP) == 60 or len(slurP) == 44:
        fichierSon.write(slurP)  
        ya = True                            
    elif len(slurP) != 51 or len(slurP) != 36 or len(slurP) != 60:
        fichierSon.close()           
    return slurP , ya  

def Message(auteur666, pigeon, stars , adresse_mail , mdp_mail , botname):
    """
    Envois message reçus en privé sur boit mail renseignée
    """  
    msg = ":::  Maître.. Je reçois un méssage  :::"
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    message455 = stars + "    >>> " + pigeon + "\n" # On recupére le message
    sting = open("Boite_Reception.txt", "a")
    sting.write(message455)
    sting.close()
    Data = msg + message455
    server.starttls()
    server.login(adresse_mail , mdp_mail)
    data = botname + "\n" + message455
    server.sendmail(adresse_mail , adresse_mail , data)  #Envoi du message par mail
    server.quit()
    return msg
