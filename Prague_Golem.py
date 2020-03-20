#!/usr/bin/python2.7
# -*- coding: utf8 
# Bot IRC <atfield2501@gmail.com>

import os
import irclib
import ircbot
import time

from Constantes_secretes import *
from PragueConstantes import *
from PragueClasses import *
#from BotFonctionslib import *
#from Prague_bdd_sql import * 




print"  ---------------- "
print"  - Prague_Golem - "
print"  ---------------- "
print"    version  1.0   "

class BotModeration(ircbot.SingleServerIRCBot):
    supra = Ecriture()
    # Initialisation de la base de données
#    bdd = Prague_Connexion()

    def __init__(self): 
        try:
            ircbot.SingleServerIRCBot.__init__(self, [(server_irc_adresse, port , mdp_irc)] , 
                                           botname, botname)  
            print("\n   Connexion \n ")
            print("serveur  :: {}\nport      :: {}\n").format(server_irc_adresse , port)

        except Exception as e:
            print("\n Connexion Impossible :: {}").format(str(e))
        
        ## Variables propre à l'objet
        self.goto = ["!goto"]
        self.die = ["!die"]
        self.conge = ["!conge"]
        self.bene = ["!help"]
        self.http = ["http"]
        self.iss = ["!iss"]
        self.son = ["!son"]
        self.addson = ["!addson"]
        self.tson = ["!tson"]
        self.dico = ["!dico"]
        self.lame1 = ["!lame_1"]
        self.lame2 = ["!lame_2"]
        self.lame3 = ["!lame_3"]
        self.lame4 = ["!lame_4"]
        self.lame5 = ["!lame_5"]
        self.oracle = ["!oracle"]
        self.ultimatum = ["!ultimatum"]

        
    def on_welcome(self, serv, ev):  #Quant le bot à rejoint le serveur.
#        serv.join(chan1)
        serv.join(lymbes , mdp_lymbes)  
#        serv.join(chan2)

    def on_join(self, serv, ev): #Quant kk rejoint le canal               
	masque_auteur = irclib.nm_to_n(ev.source())
        ####### Administre le canal #lymbes en refoulant tout intrus
        try:  
           if ev.target() == lymbes and masque_auteur != botname and irclib.nm_to_n(ev.source()) != nickperso:
              serv.kick( lymbes , masque_auteur, phrase_lymbes_1)
              serv.privmsg( lymbes , phrase_lymbes_2) 
              serv.privmsg( lymbes , ":::    {} tente de pénétrer dans les lymbes   :::".format(masque_auteur)) 
        except:
              serv.privmsg(lymbes , phrase_lymbes_3) 

        ######## Salut le visiteur sur le chan1 et fait un rapport sur le chan #lymbes													
        fichier1 = open( name , "w" )
        try:
            if ev.target() == chan1 and irclib.nm_to_n(ev.source()) != botname:
                lacible = ev.source() + "vient de rentrait dans le temple" 
                oulalala= "Salut à toi " + irclib.nm_to_n(ev.source()) 
                fichier1.write(oulalala)
                fichier1.close() 
                rar44 = open( name, "r")
                visiteur = ":::  " + rar44.readlines()[0] + "  :::" + "\n"
                serv.privmsg("#Cthulhu" , visiteur)
                serv.privmsg("#lymbes" , lacible)
                # Ecriture dans le fichier Ecran_Kontrol
                BotModeration.supra.ecriture(visiteur)
                # Ecriture recenssement
                BotModeration.supra.recenssement(irclib.nm_to_n(ev.source())) 
                # sortie console
                print(visiteur)
                # sortie irc
                serv.privmsg("#Cthulhu",visiteur)
        except Exception as e:
                error = str(e)
                # Sortie log
                BotModeration.supra.mylog(error)
                print(str(e))

    def get_version(self,serv,ev):
        serv.privmsg("","- Prague_Golem - écrit en Python - auteur: Cagliostro - atfield2501@gmail.com - atfield2501.free.fr")
 
    def on_nick(self,sev,ev):
        # Ecriture recenssement
        BotModeration.supra.recenssement(irclib.nm_to_n(ev.source())) 

    def on_kick(self, serv, ev): # Rejoindre automatiquement le salon apres un kick
        serv.join(ev.target())  
     
    def on_privmsg(self, serv, ev): # Quand le bot recoit un message en privé 
       try:   
           auteur666 = irclib.nm_to_n(ev.source()) # On recupére l'auteur du message 
           pigeon = ev.arguments()[0] # Ainsi que le méssage 
           stars = ev.source() 
           ## Appel de la fonction Message() 
           msg = Message(auteur666 , pigeon , stars, adresse_mail , mdp_mail , botname)
           serv.privmsg(auteur666, "::: Méssage Enregistré :::") # On réponds à la personne
           serv.privmsg(nickperso , msg) # On informe le Maître
       except Exception as e:
           error = str(e)
           # Sortie log
           BotModeration.supra.mylog(error)


    def on_action(self, serv, ev):
        """ Quant un utilisteur fait une action """
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        message = "[Action] "+ev.arguments()[0].lower() 
        masque_auteur = ev.source()
        # Ecriture dans la bdd sql
        BotModeration.bdd.Ecriture_messages(message,auteur,canal)


    def on_pubmsg(self, serv, ev): # Quant un message est posté
        
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        message = ev.arguments()[0].lower() 
        masque_auteur = ev.source()

        # Ecriture de tous les posts dans un fichier  
        kontrole = ev.target() + "/" + auteur + " >>> " + ev.arguments()[0] + "\n"
        # Ecriture dans le fichier Ecran_Kontrol
        BotModeration.supra.ecriture(kontrole)   
        # Ecriture dans la bdd sql
     #   BotModeration.bdd.Ecriture_messages(message,auteur,canal)

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
           
           

        for bene in self.bene:    #Réagi à son nom pour indiquer qu'il n'est pas humain et donner la liste de ses commandes...
            if bene in message:
               try:
                   serv.privmsg( canal ,"::: je ne suis qu'un bot :::")
                   with open("/home/cagliostro/Documents/Prague_Golem/fichier_help.txt") as helpyou:
                       for line in helpyou:                                        
                           serv.privmsg( auteur , line)
               except Exception as e:
                   error = str(e)
                   # Sortie log
                   BotModeration.supra.mylog(error) 

                   
        for http in self.http:     #traduis les url youtube et autres en titres de chansons...                          
            if http in message:
               try:
                   cible959 = ev.arguments()[0] or ev.arguments()[0][8:]                    
                   url=Traduction(cible959)
                   serv.privmsg( canal , url)   
               except: 
                   pass ## Ne fais rien et évite de levé une erreur avec la fonction Addson           

        for iss in self.iss: # utilise API pour donner position de la station spatial ISS
            if iss in message:
               try:
                    position_orbitale=Iss()
                    serv.privmsg( canal , position_orbitale) 
               except Exception as e:
                    serv.privmsg( canal ,"Erreur..")               
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error) 

        for son in self.son: # Fait tomber une url youtube au hasard
            if son in message:
                try:
                    serv.privmsg( canal , " * son *")
                    musique= Son()
                    serv.privmsg( canal , musique)
                    cible959=musique
                    titre=Traduction(cible959) 
                    serv.privmsg( canal , titre)      
                except Exception as e:
                    serv.privmsg( canal ,"Erreur..") 
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error) 

        for addson in self.addson: # Ajoute une url youtube au fichier
            if addson in message:
                try:
                    slurP = ev.arguments()[0][8:]+ "\n"
                    serv.privmsg( canal , slurP)
                    musique, ya , presente= Addson(slurP) 
                    if ya == True:
                        serv.privmsg( canal , " * addson *") 
                        cible959=musique
                        titre=Traduction(cible959)
                        serv.privmsg( canal , titre)     
                    else:
                        serv.privmsg( canal , " * Mauvaise entree *")    
                    if presente == True:
                        serv.privmsg(canal, " * url déjà présente dans la bdd *")
                except Exception as e:
                    error = str(e)
                    print(error)
                    # Sortie log
                    BotModeration.supra.mylog(error) 

        for tson in self.tson:
            if tson in message:
                try:                
                    serv.privmsg( canal , " * Totalson *")
                    total = compta()
                    serv.privmsg( canal , total)    
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error)           
                    serv.privmsg( canal ,"Erreur..") 

        for dico in self.dico: # Utilise API pour deffinition des mots par wikipédia
            if dico in message:
                try:	
                    addr = ev.arguments()[0][6:]
                    definition = Dico(addr)
                    fichierTMP =open("/tmp/tmp_wikipedia", "r")  
                    for line in fichierTMP:     
                        longueur=len(line)    # je cherche le moyen de faire des lignes courtes         
                        serv.privmsg( canal , line[:longueur/2])  
                        time.sleep(0.3) ## Une petite pause pour ne pas effrayer le serveur irc
                        serv.privmsg( canal , line[longueur/2:])  
                        time.sleep(0.3)
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error)
                    serv.privmsg( canal ,"Erreur..")

        for lame1 in self.lame1:
            if lame1 in message and irclib.mask_matches(masque_auteur,masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    with open("/home/cagliostro/Documents/Prague_Golem/ascii_attack/ascii01.txt") as ll:
                        for line in ll:
                            serv.privmsg(cible, line)
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error)

        for lame2 in self.lame2:
            if lame2 in message and irclib.mask_matches(masque_auteur,masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    with open("/home/cagliostro/Documents/Prague_Golem/ascii_attack/ascii02.txt") as ll:
                        for line in ll:
                            serv.privmsg(cible, line)
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error)


        for lame3 in self.lame3:
            if lame3 in message and irclib.mask_matches(masque_auteur,masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    with open("/home/cagliostro/Documents/Prague_Golem/ascii_attack/ascii03.txt") as ll:
                        for line in ll:
                            serv.privmsg(cible, line)
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error)

        for lame4 in self.lame4:
            if lame4 in message and irclib.mask_matches(masque_auteur,masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    with open("/home/cagliostro/Documents/Prague_Golem/ascii_attack/ascii04.txt") as ll:
                        for line in ll:
                            serv.privmsg(cible, line)
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    BotModeration.supra.mylog(error)

        for lame5 in self.lame5:
            if lame5 in message and irclib.mask_matches(masque_auteur,masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    with open("/home/cagliostro/Documents/Prague_Golem/ascii_attack/ascii05.txt") as ll:
                        for line in ll:
                            serv.privmsg(cible, line)
                except Exception as e:
                     serv.privmsg(canal,"* Impossible *")
                     error = str(e)
                     # Sortie log
                     BotModeration.supra.mylog(error)



        for oracle in self.oracle:
            if oracle in message and irclib.mask_matches(masque_auteur,masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    serv.privmsg(canal,"cible : "+str(cible))
                    os.system("python3 "+Tao+" > /tmp/tmp_Oracle.txt")
                    with open("/tmp/tmp_Oracle.txt","r") as wheed:
                        for line in wheed:
                            serv.privmsg(cible, line)
                            time.sleep(0.8)
                except Exception as e:
                     serv.privmsg(canal,"* Impossible *")
                     error = str(e)
                     print(e)
                     # Sortie log
                     BotModeration.supra.mylog(error)

        for ultimatum in self.ultimatum:
            if ultimatum in message:
                pass



if __name__ == "__main__":
    BotModeration().start()


