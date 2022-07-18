# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import datetime as dt
from cryptography.fernet import Fernet
import pyodbc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import csv


class DataSynchronisation(models.Model):
    _name = 'data.synchronisation'


    def synchronize_customer(self) :
        # Load log file
        basepath = os.path.dirname( os.path.dirname( __file__ ) )
        log_filename = os.path.join( basepath, 'static', 'server.log' )
        try :
            log_handle = open(log_filename , "a")
            log_handle.write( "{} NOTE: Lancement du programme. \n".format( dt.datetime.now() ) )
        except Exception as e :
            raise UserError(e)

        # Load parameter and Decrypt password
        _KEY_ = self.env['ir.config_parameter'].sudo().get_param('data.synchronisation.crypto_fernet_key')
        dbpassword = self.env['ir.config_parameter'].sudo().get_param('data.synchronisation.sage_database_password')
        server = self.env['ir.config_parameter'].sudo().get_param('data.synchronisation.sage_server_name')
        dbuser = self.env['ir.config_parameter'].sudo().get_param('data.synchronisation.sage_database_user')
        dbname = self.env['ir.config_parameter'].sudo().get_param('data.synchronisation.sage_database_name')

        if _KEY_ and dbpassword and server and dbuser and dbname:

            try :
                fernet = Fernet( bytes(_KEY_, 'utf-8') )
                dbpassword = fernet.decrypt( bytes(dbpassword, 'utf-8') )
                dbpassword = dbpassword.decode('utf-8')
                log_handle.write( "{} NOTE: Password decrypted. \n".format( dt.datetime.now() ) )
            except Exception as e:
                log_handle.write( "{} ERROR: Unable to descrypt password. \n".format( dt.datetime.now() ) )
                raise UserError("Unable to descrypt password")

            # db connexion
            state_db_connexion, cursor = self.databaseConnexion(server,dbname,dbuser,dbpassword, log_handle)

            # synchronize partner
            if state_db_connexion : 
                customers = process_partner_synchronisation(cursor, log_handle)  

                raise UserError(customers)



        else :
            log_handle.write( "{} ERROR: Unable to load parameter. \n".format( dt.datetime.now() ) )
            raise UserError("Unable to load parameter")


    # 
    # Save data to file
    def saveDataToFile(filename, header, data, path, log_handle) :
		
        fullpath = os.path.join(path, filename)
        with open(fullpath, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(header)
            for line in data:
                writer.writerow(line)
        log_handle.write( "{} NOTE: Géneration du CSV terminé avec succès.\n".format( dt.datetime.now() ) )

    #
    # Synchronize customer
    def process_partner_synchronisation(self, cursor, dbname, log_handle) :
        log_handle.write( "{} NOTE: Load customer... \n".format( dt.datetime.now() ) )



        

        # Database Query
        Query = """SELECT [CT_Num]
        ,[CT_Intitule]
        ,[CT_Type]
        ,[CG_NumPrinc]
        ,[CT_Qualite]
        ,[CT_Classement]
        ,[CT_Contact]
        ,[CT_Adresse]
        ,[CT_Complement]
        ,[CT_CodePostal]
        ,[CT_Ville]
        ,[CT_CodeRegion]
        ,[CT_Pays]
        ,[CT_Raccourci]
        ,[BT_Num]
        ,[N_Devise]
        ,[CT_Ape]
        ,[CT_Identifiant]
        ,[CT_Siret]

        ,[CT_Commentaire]
        ,[CT_Encours]
        ,[CT_Assurance]
        ,[CT_NumPayeur]
        ,[N_Risque]
        ,[CO_No]
        ,[cbCO_No]
        ,[N_Condition]
        ,[CT_DateCreate]
        ,[CT_Saut]
        ,[CT_Lettrage]
        ,[CT_ValidEch]
        ,[CT_Sommeil]
        ,[DE_No]
        ,[cbDE_No]
        ,[CT_ControlEnc]
        ,[CT_NotRappel]
        ,[N_Analytique]
        ,[cbN_Analytique]
        ,[CA_Num]
        ,[cbCA_Num]
        ,[CT_Telephone]
        ,[CT_Telecopie]
        ,[CT_EMail]
        ,[CT_Site]
    FROM [{}].[dbo].[F_COMPTET]""".format(dbname)
        cursor.execute(Query)

        #       ,[NIF]
        #   ,[STAT]
        #   ,[TP]
        #   ,[RESP]

        data = cursor.fetchall()

        basepath = os.path.dirname( os.path.dirname( __file__ ) )
        filename = "{}_Clients.csv".format(dbname)
        filepath = os.path.join( basepath, 'static')

        headers = [
            "CT_Num"
            ,"CT_Intitule"
            ,"CT_Type"
            ,"CG_NumPrinc"
            ,"CT_Qualite"
            ,"CT_Classement"
            ,"CT_Contact"
            ,"CT_Adresse"
            ,"CT_Complement"
            ,"CT_CodePostal"
            ,"CT_Ville"
            ,"CT_CodeRegion"
            ,"CT_Pays"
            ,"CT_Raccourci"
            ,"BT_Num"
            ,"N_Devise"
            ,"CT_Ape"
            ,"CT_Identifiant"
            ,"CT_Siret"

            ,"CT_Commentaire"
            ,"CT_Encours"
            ,"CT_Assurance"
            ,"CT_NumPayeur"
            ,"N_Risque"
            ,"CO_No"
            ,"cbCO_No"
            ,"N_Condition"
            ,"CT_DateCreate"
            ,"CT_Saut"
            ,"CT_Lettrage"
            ,"CT_ValidEch"
            ,"CT_Sommeil"
            ,"DE_No"
            ,"cbDE_No"
            ,"CT_ControlEnc"
            ,"CT_NotRappel"
            ,"N_Analytique"
            ,"cbN_Analytique"
            ,"CA_Num"
            ,"cbCA_Num"
            ,"CT_Telephone"
            ,"CT_Telecopie"
            ,"CT_EMail"
            ,"CT_Site"
            ,"NIF"
            ,"STAT"
            ,"TP"
            ,"RESP"
        ]
        
        saveDataToFile(filename, headers, data, filepath, log_handle)

        return data

    # 
    #  Connexion à la base de données
    def databaseConnexion(self, server_name, database, username, password, log_handle) :
        state_ss_connection = False
        sscustomercursor = None
        connect_str = "DRIVER={ODBC Driver 17 for SQL Server};" + \
            "Server={server};".format(server=server_name) + \
            "Database={database};".format(database=database) + \
            "uid={uid};".format(uid=username) + \
            "pwd={{{pwd}}};".format(pwd=password)+ \
            "Encrypt=yes;TrustServerCertificate=yes;"
            
        # raise UserError(connect_str)
        try :
            ssconexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};Server=127.0.0.1\SAGE;Database=HYGEA;uid=sa;pwd={@ebp78EBP};Encrypt=yes;TrustServerCertificate=yes;")
            sscustomercursor = ssconexion.cursor()
            log_handle.write( "{} NOTE: Connexion établie sur la base de données SQL Server.\n".format( dt.datetime.now() ) )

            state_ss_connection = True

        except Exception as e :
            raise UserError(e)
            log_handle.write( "{} ERROR: {}\n".format(dt.datetime.now(), e))
            log_handle.write( "{} ERROR: Impossible d'établir une connexion à la base SQL Server.\n".format( dt.datetime.now() ) )

            # email_subject = "ALTHEA  ".format(_CONFIG_['client']['nom'])
            # email_text = "{} ERROR: {}".format( dt.datetime.now(), e )

            # send_email(_CONFIG_['mail']['sender'], _CONFIG_['mail']['recipient'], email_subject, email_text)

        return state_ss_connection,sscustomercursor