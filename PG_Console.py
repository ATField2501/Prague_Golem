#!/usr/bin/python3
# -*- coding: utf8 
# Cagliostro <atfield2501@gmail.com>

from Prague_Golem import *
from threading import Thread , RLock
from PragueConstantes import *

print("\n  ---------------- ")
print(JAUNE+"  - Prague_Golem - "+VERT)
print("  ---------------- ")
print(JAUNE+"    version  1.0  \n "+VERT)


verrou = RLock()

class Invite_Commande(Thread):
    def __init__(self):
        """ Invite de commande dans le shell """
        Thread.__init__(self)
    def run(self):
        with verrou:
            while 1:
                shell_entree = input(JAUNE+'>> '+VERT)
                if shell_entree == 'help':
                    with open('PG_data/fichier_helpshell.txt',\
                            'r') as k:
                        for i,line in enumerate(k):
                            print(JAUNE+line.rstrip()+VERT)

                elif shell_entree == 'vox':
                    print(JAUNE+'Ecriture >> '+VERT)
                    vox_mechanica = raw_input()
                    PragueGolem.privmsg('lymbes', vox_mechanica) 
                
                elif shell_entree == 'exit':
                    sys.exit(0)
                
                elif shell_entree == "connect":
                    trigger = Declencheur()
                    trigger.start()
                    trigger.join()
                
                elif shell_entree == "log":
                    with open("PG_data/PragueGolem_log","r") as k:
                        for line in k:
                            print(BLANC+str(line).strip()+VERT)
                else:
                    print(ROUGE+'erreur'+BLANC+"\n Hum, je ne reconnais pas cette commande"+VERT)




if __name__ == "__main__":
    invite=Invite_Commande()
    invite.start()
    invite.join()

