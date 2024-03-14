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

load_dotenv()
PASS = os.getenv('PASS')

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = PASS,
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE humaninstrumentality")

print("Database created successfully...")