import sys, os
import mysql, mysql.connector


def create_schema(cursor):
    """Cette fonction sert a créer la table 'Tradders' si inexistante"""
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS "Account" (
    "Id"	TEXT,
    "Name"	TEXT,
    "Email" TEXT,
    "Password" TEXT
    );""")


def create_user():
    
    """cette fonction permet de créer un compte dans la db"""

    cursor.execute(""" INSERT INTO 'ACOUNT' ('Id', 'Name', 'Email', 'Password') 
        VALUES ('%', '%', '%', '%')""")

def main():
    
    conn=mysql.connector.connect("Blockchaine.db")
    c=conn.cursor()
    create_schema(c)
    conn.commit()
    conn.close()

if __name__=="__main__": 
    main()