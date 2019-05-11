#!/usr/bin/python2.7
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
        ircbot.SingleServerIRCBot.__init__(self, [(server_irc_adresse, port , mdp_irc)] , 
                                           botname, botname)  
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

    def on_welcome(self, serv, ev):  #Quant le bot à rejoint le serveur.
        serv.join(chan1)
        serv.join("#lymbes" , 'dead')  

    def on_join(self, serv, ev): #Quant kk rejoint le canal               
	masque_auteur = irclib.nm_to_n(ev.source())

        try:  ## Si kk tente de pénétrer sur le chan # lymbes, on le refoule
           if ev.target() == "#lymbes" and masque_auteur != botname and irclib.nm_to_n(ev.source()) != nickperso:
              serv.kick("#lymbes", masque_auteur, 'Les Lymbes vous sont interdites, réjouissez-vous.')
              serv.privmsg("#lymbes" , ":::    ..... - (;,,;) - .....    :::") 
              serv.privmsg("#lymbes" , ":::    {} tente de pénétrer dans les lymbes   :::".format(masque_auteur)) 
        except:
              serv.privmsg("#lymbes" , "je n'ai pas les niveaux de privilège requis pour effectuer le kick..") 

        try:		######## Salut le visiteur sur le chan1 et fait un rapport sur le chan #lymbes													
            fichier1 = open("/tmp/name_visiteur.txt", "w" )
            if ev.target() == chan1 and irclib.nm_to_n(ev.source()) != botname:
                lacible = ev.source() + "vient de rentrait dans le temple" 
                oulalala= "Salut à toi " + irclib.nm_to_n(ev.source()) 
                fichier1.write(oulalala)
                fichier1.close() 
                rar44 = open("/tmp/name_visiteur.txt", "r")
                visiteur = ":::  " + rar44.readlines()[0] + "  :::" + "\n"
                serv.privmsg("#lymbes" , lacible)
                # Ecriture dans le fichier Ecran_Kontrol
                Ecriture(visiteur)
                # sortie console
                print(visiteur)
                # sortie irc
                serv.privmsg("#Cthulhu",visiteur)
        except Exception as e:
                error = str(e)
                # Sortie log
                Log(error)

  
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
           Log(error)

    def on_pubmsg(self, serv, ev): # Quant un message est posté
        auteur = irclib.nm_to_n(ev.source())
        canal = ev.target()
        message = ev.arguments()[0].lower() 
        masque_auteur = ev.source()
        # Ecriture de tous les posts dans un fichier  
        kontrole = ev.target() + "/" + auteur + " >>> " + ev.arguments()[0] + "\n"
        # Ecriture dans le fichier Ecran_Kontrol
        Ecriture(kontrole)   
        
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
                   with open("/home/cagliostro/Documents/Prague_Golem/fichier_help.txt") as helpyou:
	               for line in helpyou:                                        
                           serv.privmsg( auteur , line)
               except Exception as e:
                   error = str(e)
                   # Sortie log
                   Log(error)


                   
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
                    Log(error)


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
                    Log(error)



  

        for addson in self.addson: # Ajoute une url youtube au fichier
            if addson in message:
                try:
                    slurP = ev.arguments()[0][8:]+ "\n"
                    serv.privmsg( canal , slurP)
                    musique, ya = Addson(slurP) 
                    if ya == True:
                        serv.privmsg( canal , " * addson *") 
                        cible959=musique
                        titre=Traduction(cible959)
                        serv.privmsg( canal , titre)  
                    else:
                        serv.privmsg( canal , " * Mauvaise entree *")       
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    Log(error)



        for tson in self.tson:
            if tson in message:
                try:                
                    serv.privmsg( canal , " * Totalson *")
                    total = compta()
                    serv.privmsg( canal , total)    
                except Exception as e:
                    error = str(e)
                    # Sortie log
                    Log(error)
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
                    Log(error)     
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
                    Log(error)
              

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
                    Log(error)

                

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
                    Log(error)
                 
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
                    Log(error)

                  

        for lame5 in self.lame5:
            if lame5 in message and irclib.mask_matches(masque_auteur,masque_perso):
                try:
                    cible = ev.arguments()[0][8:]
                    with open("/home/cagliostro/Documents/Prague_Golem/ascii_attack/ascii05.txt") as ll:
                        for line in ll:
                            serv.privmsg(cible, line)
                except Exception as e:
                     error = str(e)
                     # Sortie log
                     Log(error)
                   

if __name__ == "__main__":
    BotModeration().start()


 
