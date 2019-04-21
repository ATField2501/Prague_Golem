""" Classes et Fonctions du bot Prague_Golem """

import urllib2
import requests
import json
import re


def Iss():
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
 
