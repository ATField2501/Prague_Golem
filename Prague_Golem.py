#!/usr/bin/env python2
# -*- coding: utf8 
# Bot IRC <atfield2501@gmail.com>


import irclib
import ircbot
import urllib2
from Constantes_secretes import *
from PragueConstantes import *
from BotFonctionslib import *


print"  ---------------- "
print"  - Prague_Golem - "
print"  ---------------- "
print"    version  1.0   "



class BotModeration(ircbot.SingleServerIRCBot):
    def __init__(self): 
        ircbot.SingleServerIRCBot.__init__(self, [(server_irc_adresse, port , mdp)] , 
                                           botname, botname)  
        ## Variables propre à l'objet
        self.goto = ["!goto"]
        self.die = ["!die"]
        self.conge = ["!conge"]
        self.bene = [botname]
        self.http = ["http"]

    def on_welcome(self, serv, ev):  #Quant le bot à rejoint le serveur.
        serv.join(chan1)
        serv.join("#lymbes" , 'dead')  

    def on_join(self, serv, ev): #Quant kk rejoint le canal               
	masque_auteur = irclib.nm_to_n(ev.source())
        try:															
            fichier1 = open("name_visiteur.txt", "w" )
            if ev.target() == "#Cthulhu" and irclib.nm_to_n(ev.source()) != "Prague_Golem":
                lacible = ev.source() + "vient de rentrait dans le temple" 
                oulalala= "Salut à toi " + irclib.nm_to_n(ev.source()) 
                fichier1.write(oulalala)
                fichier1.close() 
                fichierVisit = open("Visiteurs.txt", "r") #Repertoire des visiteurs du canal
                chaine = irclib.nm_to_n(ev.source())
                str(chaine)
            for line in fichierVisit.readlines()[0]:
                if chaine in line and ev.target() == "#Cthulhu":   #Ecrire l'entrée seulement si non présente dans le fichier                
                     fichierVisit.close                
                elif chaine not in line and ev.target() == "#Cthulhu":
                    fichierVisit = open("Visiteurs.txt", "a")
                    fichierVisit.write(irclib.nm_to_n(ev.source()) + "\n")
                    fichierVisit.close  
                    break
            rar44 = open("name_visiteur.txt", "r")
            visiteur = ":::  " + rar44.readlines()[0] + "  :::" + "\n"
            serv.privmsg("#lymbes" , lacible)
            kiku =  open("Ecran_Kontrol.txt", "a")           
            kiku.write(visiteur)
            kiku.close()
            print(visiteur)
            serv.privmsg("#Cthulhu",visiteur)
        except Exception as e:
                print(str(e))
  
    def on_kick(self, serv, ev): # Rejoindre automatiquement le salon apres un kick
        serv.join(ev.target())  
     
    def on_privmsg(self, serv, ev): # Quand le bot recoit un message en privé                 
        pass

    def on_pubmsg(self, serv, ev): # Quant un message est posté
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        message = ev.arguments()[0].lower() 
        masque_auteur = ev.source()
        # Ecriture de tous les posts dans un fichier  
        kontrole = ev.target() + "/" + auteur + " >>> " + ev.arguments()[0] + "\n"
        fichierKontrol = open("Ecran_Kontrol.txt", "a" ) 
        fichierKontrol.write(kontrole)
        fichierKontrol.close()
        # Affichage direct dans la console
        print(kontrole)    
        
        # Commande reçus par le bot sur irc               
        for goto in self.goto:
            if goto in message and irclib.mask_matches(masque_auteur, masque_perso):               
                cible1 = ev.arguments()[0][6:]  
                serv.privmsg( canal , " :::    Je m'y rends   :::")
                serv.join(cible1)
            elif goto in message and not irclib.mask_matches(masque_auteur, masque_perso):               
                serv.privmsg( canal , " :::    Je n'obéis qu'à mon Maître   :::")

        for die in self.die:
            if die in message and irclib.mask_matches(masque_auteur, masque_perso):                
                serv.privmsg( canal , " ::: Je meurt...   :::")
                self.die()
            elif die in message and not irclib.mask_matches(masque_auteur, masque_perso):               
                serv.privmsg( canal , " :::    Je n'obéis qu'à mon Maître   :::")

        for conge in self.conge:
            if conge in message and irclib.mask_matches(masque_auteur, masque_perso):
                serv.privmsg( canal , " ::: je rentre au Temple  :::")
                serv.part(canal, message='::::  (;,,;)  ::::')
            elif conge in message and not irclib.mask_matches(masque_auteur, masque_perso):               
                serv.privmsg( canal , " :::    Je n'obéis qu'à mon Maître   :::")

        ## petit bug sur celle-là
        for bene in self.bene:    #Réagi à son nom pour indiquer qu'il n'est pas humain et donner la liste de ses commandes...
            if bene in message:
               print("  OK ")
               try:
                   serv.privmsg( canal ,"::: je ne suis qu'un bot :::")
                   with open("fichier_help.txt") as helpyou:
	               for line in helpyou:                                        
                           serv.privmsg( canal , line)
               except Exception as e:
                   print(str(e))

        for http in self.http:     #traduis les url youtube et autres en titres de chansons...                          
            try:
               if http in message:
                   cible959 = ev.arguments()[0] or ev.arguments()[0][8:]                    
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
                               serv.privmsg( canal , format(spirale))                                                                    
            except Exception as e:
                   print(str(e))

if __name__ == "__main__":
    BotModeration().start()


    
