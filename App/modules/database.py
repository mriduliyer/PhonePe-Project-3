import mysql.connector
import os

# get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__))
# get the file path of the file you want to access
file_path = os.path.join(dir_path, 'DigiCertGlobalRootCA.crt.pem')
pass_path = os.path.join(dir_path, 'password.txt')
password_file = open(pass_path, 'r')
dbpassword = password_file.read().strip()
password_file.close()


mydb = mysql.connector.connect(user="exampleadmin", password=dbpassword, host="my-example-mysql1.mysql.database.azure.com", port=3306, database="customerdb", ssl_ca=file_path, ssl_disabled=False)
# Connect to MySQL database

cursor = mydb.cursor()