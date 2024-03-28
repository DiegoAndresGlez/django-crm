#Install mysql on pc
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python
#source virt/Scripts/activate - linux
#./virt/Scripts/activate
#

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='dcrm/.env')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = MYSQL_ROOT_PASSWORD,
    auth_plugin='mysql_native_password',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dcrm_db")

print("Database created successfully...")
