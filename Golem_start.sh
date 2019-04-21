#!/bin/bash
#Script de lancement du Schtrouf_Golem.
#Fonction boucle pour contrer une défaillance de la bibliothèque python irclib (le bot se relance toutes les dix minutes)

ROUGE="\\033[1;31m"
JAUNE="\\033[1;33m"
VERT="\\033[1;32m"

echo -e "$VERT" "******* Caglio-Script ********"
echo -e "$ROUGE" "****   PRague_Golem    ****"
echo -e "$JAUNE" "          PID="$$
echo -e "$VERT" "******************************"




while ((i <= 10))
do

python Prague_Golem.py >Ecran_Kontrol.txt 2>> schtrouf_log.txt & sleep 6000
killall python
done






