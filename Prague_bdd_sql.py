#!/usr/bin/python2
# coding:utf8
# auteur: cagliostro <atfield2501@gmail.com>

""" Module du bot Prague_Golem servant à la connection avec la base de données sql PragueGolem """
try:
   import mysql.connector
except:
    print("librairie msq.connector manquante")
from Constantes_secretes import *

class Prague_Connexion():
    """ Connexion à la base de données sql PragueGolem """
    def __init__(self):
        """ """
    try:
        ok = mysql.connector.connect(host=localisation,user=utilisateur,password=mdp, database=baseDonnees)
        cursor = ok.cursor(prepared=True)
        print("Connexion à la base de données  {}   OK \n").format(baseDonnees)

    except Exception as e:
        print("connexion à la base de donnée impossible . . .\nCause :: "+str(e))

    def Ecriture_messages(self,*args):
        """ Ecriture dans la table flux des messages posté sur les chan ou le bot est présent """
        try:
            # Ecriture dans la bdd
            self.trame = " INSERT INTO flux (time1,time2,messages,auteur,canal) VALUE (curdate(),current_time(),%s,%s,%s);"
            self.cursor.execute(self.trame,(args[0],args[1],args[2]))
            self.cursor.execute(""" COMMIT """)
            print("-- ECRITURE      --  OK")
        except Exception as e:
            print("Ecriture Impossible. Cause: "+str(e))


