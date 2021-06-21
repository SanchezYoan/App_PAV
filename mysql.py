import sys
import mysql.connector
#import argparse

cnx = mysql.connector.connect(user='yoan'@'192.168.163.1', password='AzErTy123*',
                              host='localhost',
                              database='blockchaine.db')
cnx.close()


#parser.add_argument("-au", "--ajouter_user", help="ajouter un utilisateur à mysql")
#parser.add_argument("-af", "--ajouter_facture", nargs="*", help="Ajouter une facture à la base de donnee")

def add_client(cursor):
#Ajouter les informations d'un client
    cursor.execute("""INSERT INTO Clients VALUES (%s,%s,%s,%s,%s);""", (addc[0], addc[1], addc[2], addc[3], addc[4]))
    logging.info("lancement de la fonction d'ajout de client")
    return 0

def add_achat(cursor):
    #Ajouter une ligne achat à la bdd
    cursor.execute('INSERT INTO Users (id_Clients, id, DATE_EMISSION) VALUES (%s,%s,%s)', (addf[0], addf[1], addf[2]))
    logging.info("lancement de la fonction d'ajout d'Achats ")
    return 0

def add_crypto(cursor):
#Ajouter une crypto à la bdd
    cursor.execute('INSERT INTO Lignes (MONAME, QUANTITE, PRIX_UNITE, TOTAL) VALUES (%s;%s,%s,%s)', (addf[0],addf[1],addf[2],addf[3]))
    logging.info("lancement de la fonction d'ajout de produit")
    return 0

def main():
    
    cursor.execute("""CREATE DATABASE GESTION""")
    # Créé un utilisateur 
    cursor.execute("""CREATE USER '?' IDENTIFIED WITH mysql_native_password""", (addu))
    conn = mysql.connector.connect(host='192.168.163.1', database='blockchaine', user='yoan', password='AzErTy123*')
    c = conn.cursor()
    add_client()
