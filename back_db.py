import sys, os
import mysql, mysql.connector


def create_schema():
    """Cette fonction sert a créer la table 'Tradders' si inexistante"""
    
    c.execute("""CREATE TABLE IF NOT EXISTS "Account" (
    "Id"	TEXT,
    "Name"	TEXT,
    "Email" TEXT,
    "Password" TEXT
    );""")


def create_user():
    
    """cette fonction permet de créer un compte dans la db"""

    c.execute( """CREATE USER 'nouveau_utilisateur'@'localhost' IDENTIFIED BY 'mot_de_passe'""");


def register_user():

    c.execute(""" INSERT INTO 'ACOUNT' ('Id', 'Name', 'Email', 'Password') 
        VALUES ('%', '%', '%', '%')""")

def main():

    mysql.connector.connect("Blockchaine.db")
    c=conn.cursor()
    create_user()
    create_schema(c)
    conn.commit()
    conn.close()

if __name__=="__main__": 
    main()