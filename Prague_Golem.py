#!/usr/bin/env python2
# -*- coding: utf8 
# Bot IRC <atfield2501@gmail.com>


import irclib
import ircbot

from Constantes_secretes import *
from PragueConstantes import *
from PragueClasses import *
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
        self.bene = ["Prague_Golem"]
        self.http = ["http"]
        self.iss = ["!iss"]

    def on_welcome(self, serv, ev):  #Quant le bot à rejoint le serveur.
        serv.join(chan1)
        serv.join("#lymbes" , 'dead')  

    def on_join(self, serv, ev): #Quant kk rejoint le canal               
	masque_auteur = irclib.nm_to_n(ev.source())
        try:		######## Salut le visiteur sur le chan1 et fait un rapport sur le chan #lymbes													
            fichier1 = open("name_visiteur.txt", "w" )
            if ev.target() == chan1 and irclib.nm_to_n(ev.source()) != botname:
                lacible = ev.source() + "vient de rentrait dans le temple" 
                oulalala= "Salut à toi " + irclib.nm_to_n(ev.source()) 
                fichier1.write(oulalala)
                fichier1.close() 
                rar44 = open("name_visiteur.txt", "r")
                visiteur = ":::  " + rar44.readlines()[0] + "  :::" + "\n"
                serv.privmsg("#lymbes" , lacible)
                kiku =  open("Ecran_Kontrol.txt", "a")           
                kiku.write(visiteur)
                kiku.close()
                # sortie console
                print(visiteur)
                # sortie irc
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
        # Sortie console
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
                   url=Traduction(cible959)
                   serv.privmsg( canal , url)   
            except Exception as e:
                   print(str(e))

        for iss in self.iss: # utilise API pour donner position de la station spatial ISS
            try:
                if iss in message:
                    position_orbitale=Iss()
                    serv.privmsg( canal , position_orbitale) 
            except Exception as e:
                   print(str(e))
                   serv.privmsg( canal ,"Erreur..")               
                   break

if __name__ == "__main__":
    BotModeration().start()


    
