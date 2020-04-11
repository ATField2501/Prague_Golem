# -*- coding: utf8 
# auteur cagliostro <atfield2501@gmail.com>
""" Classes et Fonctions du bot Prague_Golem """

import time
import urllib2
import json
import smtplib
import random
from PragueConstantes import *

date=time.strftime("%A %d %B %Y %H:%M:%S")

def Lecture(*args):
    """ Fonction prenant en charge la lecture des fichiers """
    with open("ascii_attack/ascii0"+str(args[0])+".txt", "r") as ecran:
        sortie = ecran.readlines()
    return sortie


def compta():  
    """ Compte les lignes du fichier ListeAddSon.txt """      
    f = open(Maison+'PG_data/ListeAddSon.txt', 'r')        
    NumberOfLine = 0
    for line in f:
        NumberOfLine += 1          
    return NumberOfLine 

def Iss():
    """ Appel de l'api pour position orbitale de la station spatial ISS """
    fichierTMP1 =open(Maison+"PG_cache/tmp_iss", "w") 
    req = urllib2.Request( "http://api.open-notify.org/iss-now.json" )
    response = urllib2.urlopen(req)
    obj = json.loads(response.read())                    
    armadda = "Position Actuelle de " + \
            "la station orbitale ISS:  timestamp >>",\
            obj[ "timestamp" ] ,"latidude >>" ,\
            obj[ "iss_position" ][ "latitude" ],"longitude >>",\
            obj[ "iss_position" ][ "longitude" ]                   
    fichierTMP1.write(json.dumps(armadda))
    fichierTMP1.close()
    fichierTMP1 =open(Maison+"PG_cache/tmp_iss", "r")
    position_orbitale=fichierTMP1.readlines()[0]
    return position_orbitale

def Traduction(cible959):
    """ Traduction des url youtube en titres """
    response555 = urllib2.urlopen(cible959)
    obj889 = response555.read()
    fichier02 =open(Maison+"PG_cache/tmp_recherche.txt", "w")
    fichier02.write(obj889)
    fichier02.close()
    with open(Maison+"PG_cache/tmp_recherche.txt", "r") as f:
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
    fichierSon =  open(Maison+"PG_data/ListeAddSon.txt" , "r") 
    NumberOfLine=compta()                
    risop = random.randint(0,NumberOfLine)
    musique = fichierSon.readlines()[risop]
    fichierSon.close()
    return musique

def Addson(slurP):
    """
    Ajoute une entree au fichier en verifiant la longueur de la chaîne
    """
    ya=False
    presente = False
    boZon = open(Maison+"PG_data/ListeAddSon.txt" , "r")
    f=boZon.readlines()
    
    for e in f:
        if e.rstrip() == slurP.rstrip():
            presente = True
    boZon.close()        
    fichierSon =  open(Maison+"PG_data/ListeAddSon.txt", "a")                 
    try:
        if presente == False:
            if len(slurP) <= 200:
                fichierSon.write(slurP)  
                ya = True                            
        else:
            fichierSon.close()           
    except Exception as e:
        print(str(e))
 
    return slurP , ya , presente     
        

def Message(auteur666, pigeon, stars , adresse_mail , mdp_mail , botname):
    """
    Envois message reçus en privé sur boite mail renseignée
    """  
    msg = ":::  Maître.. Je reçois un méssage  :::"
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    # On recupére le message
    message455 = stars + "    >>> " + pigeon + "\n" 
    sting = open(Maison+"PG_data/Boite_Reception.txt", "a")
    sting.write(message455)
    sting.close()
    Data = msg + message455
    server.starttls()
    server.login(adresse_mail , mdp_mail)
    data = botname + "\n" + message455
    # Envoi du message par mail
    server.sendmail(adresse_mail , adresse_mail , data)  
    server.quit()
    return msg

def Repare(ss):
    """
    Appel la methode replace() pourquoi?? Parceque les 
    librairie que j'utilise son en 2.7. 
    Pour les noobs comme moi; vive python3
    """
    ss = ss.replace('\u00e9' , 'é')
    ss = ss.replace('\u00e7' , 'ç')
    ss = ss.replace('\u00e8' , 'è')
    ss = ss.replace('\u00e0' , 'à')
    ss = ss.replace('\u0153' , 'œ')
    ss = ss.replace('\u2019' , "'")
    ss = ss.replace('\u00ab' , "<<")
    ss = ss.replace('\u00bb' , ">>")
    ss = ss.replace('\u00f9' , "ù")
    ss = ss.replace('\u00e2' , "à")
    ss = ss.replace('\u00c9' , "ê")
    ss = ss.replace('\u00c2' , "â")
    ss = ss.replace('\u00ea' , "ê")
    ss = ss.replace('"' , '')          
    return ss



def Dico(addr):
    """
    Cherche la definition d'un mot donné à l'aide de l'api wikipédia
    """
    ss=""
     
    soft = wikipedia+addr
    response = urllib2.urlopen(soft)     
    obj1 = json.loads(response.read())
    obj2 = obj1[2]
    obj3 = obj2[0]+obj2[2]
    print("demande de la déffinition de {]".format(obj2))
    with open(Maison+"PG_cache/tmp_wikipedia.txt", "w") as fichierTTMP: 
        fichierTTMP.write(json.dumps(obj3))                   
    with open(Maison+"PG_cache/tmp_wikipedia.txt", "r") as fichierTTTMP:      
        definition = fichierTTTMP.readlines()
    for line in definition:
        ss += line
#            filtre = Repare(ss)
    with open(Maison+"PG_cache/tmp_wikipedia.txt", "w") as fichierTTTTMP: 
        fichierTTTTMP.write(ss)    

    return 


class Ecriture():
    def __init__ (self):
        """ Prends en charge l'ecriture des messages """
    def ecriture(self,*arg):
        """ Ecriture de ce que le bot vois dans le fichier Ecran_Kontrol"""
        with open(Maison+"PG_cache/Ecran_Kontrol" , "a") as ecran_k:
            ecran_k.write(date+'-'+arg[0])

    def mylog(self,error):
        """ Ecriture des erreurs dans le fichier log """
        with open(Maison+"PG_data/PragueGolem_log" , "a") as log:
            log.write(date+'-'+error+"\n")

    def recenssement(self,*arg):
        """ Recensse les visiteurs sur le chan """
        self.presente = False
        print(arg[0])
        try:
            with open(Maison+"PG_data/PragueGolem_recenssement" , "r") as ecran_re:
                f=ecran_re.readlines() 
                for e in f:
                    if e.strip() == arg[0]:
                        self.presente = True
        except IOError as e:
            print(str(e))
            pass

        if self.presente == False:
            with open(Maison+"PG_data/PragueGolem_recenssement","a") as ecran_:
                ecran_.write(arg[0]+"\n ")
                
