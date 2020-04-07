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


print("\n  ---------------- ")
print("  - Prague_Golem - ")
print("  ---------------- ")
print("    version  1.0  \n ")

from Prague_bdd_sql import * 

## test de la presence de screen 
os.system("screen -v")
test=os.system("echo $?")
if test == '0':
    print('screen ok')
    
else:
    print('screen non installé')

class PragueGolem(ircbot.SingleServerIRCBot):
    supra = Ecriture()
    # Initialisation de la base de données
#    bdd = Prague_Connexion()
    def __init__(self): 
        ircbot.SingleServerIRCBot.__init__(self, [(server_irc_adresse, port , mdp_irc)] ,
                botname, botname)  
        
        print("\nserveur    :: {}\nport       :: {}").format(server_irc_adresse , port)

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


    # Messages du serveur
    def rapport(self , serv , ev):
        message = str(ev.arguments())
        print(message)

    def on_welcome(self, serv, ev):  #Quant le bot à rejoint le serveur.
        print("Connection :: ok \n\n")
        serv.join(chan1)
        serv.join(lymbes , mdp_lymbes)  
#        serv.join(chan2)
        # Seconde identification, la premiere échoue sur epiknet
        serv.privmsg('Themis' , 'IDENTIFY '+ mdp_irc)
    
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
        if ev.target() == chan1 and irclib.nm_to_n(ev.source()) != botname:
            lacible = ev.source() + "vient de rentrait dans le temple" 
            oulalala= "Salut à toi " + irclib.nm_to_n(ev.source())
            try:
                with open(name , "w") as fichier1:
                    fichier1.write(oulalala)
                with open(name , 'r') as fichier2:        
                    visiteur = ":::  " + fichier2.readlines()[0] + "  :::" + "\n"
                time.sleep(1)    
                serv.privmsg("#Cthulhu" , visiteur)
                serv.privmsg("#lymbes" , lacible)
                # Ecriture dans le fichier Ecran_Kontrol
                PragueGolem.supra.ecriture(visiteur)
                # Ecriture recenssement
                PragueGolem.supra.recenssement(irclib.nm_to_n(ev.source())) 
                # sortie console
                # sortie irc
            except Exception as e:
                error = str(e)
                # Sortie log
                PragueGolem.supra.mylog(error)
                print(str(e)+'  yo')
            
    def get_version(self):
        return "- Prague_Golem - écrit en Python - auteur: Cagliostro - atfield2501@gmail.com - ^(;,,;)^"
#        PragueGolem.rapport(self , serv , ev)
    
    def on_nick(self,serv,ev): 
        """ Quant un utilisateur change de nickname """
        PragueGolem.rapport(self , serv , ev)
        # Ecriture recenssement
        PragueGolem.supra.recenssement(irclib.nm_to_n(ev.source())) 

    def on_kick(self, serv, ev): 
        """  Rejoindre automatiquement le salon apres un kick """
        serv.join(ev.target())  
     
    def on_privmsg(self, serv, ev): 
        """ Quand le bot reçoit un message en privé """
        try:  
            # On recupére l'auteur du message 
            auteur666 = irclib.nm_to_n(ev.source())
            pigeon = ev.arguments()[0] # Ainsi que le méssage 
            stars = ev.source() 
            ## Appel de la fonction Message() 
            msg = Message(auteur666 , pigeon , stars, 
                    adresse_mail , mdp_mail , botname)
            # On réponds à la personne
            serv.privmsg(auteur666, phrase_3)
            # On informe le Maître
            serv.privmsg(nickperso , msg)
        except Exception as e:
            error = str(e)
            # Sortie log
            PragueGolem.supra.mylog(error)


    def on_action(self, serv, ev):
        """ Quant un utilisteur fait une action """
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        message = "[Action] "+ev.arguments()[0].lower() 
        masque_auteur = ev.source()
        # Ecriture dans la bdd sql
        PragueGolem.bdd.Ecriture_messages(message,auteur,canal)


    def on_pubmsg(self, serv, ev):
        """ Quant un message est publié sur le canal """ 
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        message = ev.arguments()[0].lower() 
        masque_auteur = ev.source()
        # Ecriture de tous les posts dans un fichier  
        kontrole = ev.target() + "/" + auteur + " >>> " + ev.arguments()[0] + "\n"
        print(kontrole)
        # Ecriture dans le fichier Ecran_Kontrol
        PragueGolem.supra.ecriture(kontrole)   
        # Ecriture dans la bdd sql
     #   BotModeration.bdd.Ecriture_messages(message,auteur,canal)

        # Commande reçus par le bot sur irc        
        ### Déplacement
        for goto in self.goto:
            if goto in message \ # line break python ;)
                    and irclib.mask_matches(masque_auteur, 
                            masque_perso):               
                cible1 = ev.arguments()[0][6:]  
                serv.privmsg( canal , phrase_1)
                serv.join(cible1)
            elif goto in message \
                    and not irclib.mask_matches(masque_auteur, 
                            masque_perso):               
                serv.privmsg( canal , phrase_2)
        ### Mourir
        for die in self.die:
            if die in message \
                    and irclib.mask_matches(masque_auteur, 
                            masque_perso):                
                serv.privmsg( canal ,phrase_4)
                self.die()
            elif die in message \
                    and not irclib.mask_matches(masque_auteur, 
                            masque_perso):               
                serv.privmsg( canal , phrase_2)
        ## Partir
        for conge in self.conge:
            if conge in message \
                    and irclib.mask_matches(masque_auteur, 
                            masque_perso):
                serv.privmsg( canal , phrase_5)
                serv.part(canal, message='::::  (;,,;)  ::::')
            elif conge in message \
                    and not irclib.mask_matches(masque_auteur, 
                            masque_perso):               
                serv.privmsg( canal , phrase_2)
        ## Evocation du nom 
        # Réagi à son nom pour indiquer qu'il n'est 
        # pas humain et donner la liste de ses commandes...
        for bene in self.bene:    
            if bene in message:
               try:
                   serv.privmsg( canal , phrase_6)
                   with open(Maison+"fichier_help.txt") \
                           as helpyou:
                       for line in helpyou:                     
                           serv.privmsg( auteur , line)
               except Exception as e:
                   error = str(e)
                   # Sortie log
                   PragueGolem.supra.mylog(error) 

        # traduction des url youtube et autres en titres                 
        for http in self.http:                             
            if http in message:
               try:
                   cible959 = ev.arguments()[0] or ev.arguments()[0][8:]                    
                   url=Traduction(cible959)
                   serv.privmsg( canal , url)   
               except:
                   # Ne fais rien et évite de levé une erreur avec la fonction Addson
                   pass

        # utilise API pour donner position de la station spatial ISS
        for iss in self.iss: 
            if iss in message:
               try:
                    position_orbitale=Iss()
                    serv.privmsg( canal , position_orbitale) 
               except Exception as e:
                    serv.privmsg( canal ,"Erreur..")               
                    error = str(e)
                    # Sortie log
                    PragueGolem.supra.mylog(error) 

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
                    PragueGolem.supra.mylog(error)
                    print(error)

        for addson in self.addson: # Ajoute une url youtube au fichier
            if addson in message:
                try:
                    slurP = ev.arguments()[0][8:]+ "\n"
                    serv.privmsg( canal , slurP)
                    musique, ya , presente= Addson(slurP) 
                    if ya == True:
                        serv.privmsg( canal , " * addson *") 
                        cible959=musique
                        titre=Traduction(str(cible959))
                        serv.privmsg( canal , titre)     
                    else:
                        serv.privmsg( canal , " * Mauvaise entree *")    
                    if presente == True:
                        serv.privmsg(canal, " * url déjà présente dans la bdd *")
                except Exception as e:
                    error = str(e)
                    print(error)
                    # Sortie log
                    PragueGolem.supra.mylog(error) 

        for tson in self.tson:
            if tson in message:
                try:                
                    serv.privmsg( canal , " * Totalson *")
                    total = compta()
                    serv.privmsg( canal , total)    
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    PragueGolem.supra.mylog(error)           
                    serv.privmsg( canal ,"Erreur..") 

        for dico in self.dico: # Utilise API pour deffinition des mots par wikipédia
            if dico in message:
                try:	
                    addr = ev.arguments()[0][6:]
                    serv.privmsg(canal , "Deffinition du mot: {}".format(str(addr)))
                    Dico(addr)
                    with open(Maison+"tmp_wikipedia.txt", "r") as fichierTTMPi:
                        for line in fichierTTMPi:     
                            longueur=len(line)    # je cherche le moyen de faire des lignes courtes         
                            serv.privmsg( canal , line[:longueur/2])  
                            ## Une petite pause pour ne pas 
                            # effrayer le serveur irc
                            time.sleep(0.3) 
                            serv.privmsg( canal , line[longueur/2:])  
                            time.sleep(0.3)
                except Exception as e:
                    error = str(e)
                    print("Erreur :: {}".format(error))
                    # Sortie log
                    PragueGolem.supra.mylog(error)
                    serv.privmsg( canal ,"Erreur..")
                serv.privmsg(canal , 'AAA YE, Fini!!')    

        for lame1 in self.lame1:
            if lame1 in message \
                    and irclib.mask_matches(masque_auteur,
                            masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    retour = Lecture('1')
                    for line in retour:
                        serv.privmsg(canal , line)
                except Exception as e:
                     serv.privmsg(canal,"* Impossible *")
                     error = str(e)
                     print(error)
                     # Sortie log
                     PragueGolem.supra.mylog(error)

        for lame2 in self.lame2:
            if lame2 in message \
                    and irclib.mask_matches(masque_auteur,
                            masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    retour = Lecture('2')
                    for line in retour:
                        serv.privmsg(canal , line)
                except Exception as e:
                     serv.privmsg(canal,"* Impossible *")
                     error = str(e)
                     print(error)
                     # Sortie log
                     PragueGolem.supra.mylog(error)


        for lame3 in self.lame3:
            if lame3 in message \
                    and irclib.mask_matches(masque_auteur,
                            masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    retour = Lecture('3')
                    for line in retour:
                        serv.privmsg(canal , line)
                except Exception as e:
                     serv.privmsg(canal,"* Impossible *")
                     error = str(e)
                     print(error)
                     # Sortie log
                     PragueGolem.supra.mylog(error)

        for lame4 in self.lame4:
            if lame4 in message \
                    and irclib.mask_matches(masque_auteur,
                            masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    retour = Lecture('4')
                    for line in retour:
                        serv.privmsg(canal , line)
                except Exception as e:
                     serv.privmsg(canal,"* Impossible *")
                     error = str(e)
                     print(error)
                     # Sortie log
                     PragueGolem.supra.mylog(error)

        for lame5 in self.lame5:
            if lame5 in message \
                    and irclib.mask_matches(masque_auteur,
                            masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    retour = Lecture('5')
                    for line in retour:
                        serv.privmsg(canal , line)
                except Exception as e:
                     serv.privmsg(canal,"* Impossible *")
                     error = str(e)
                     print(error)
                     # Sortie log
                     PragueGolem.supra.mylog(error)



        for oracle in self.oracle:
            if oracle in message \
                    and irclib.mask_matches(masque_auteur,
                            masque_perso):
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
                     PragueGolem.supra.mylog(error)

        for ultimatum in self.ultimatum:
            if ultimatum in message:
                pass



if __name__ == "__main__":
    PragueGolem().start()


