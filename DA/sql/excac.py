import mysql.connector
from mysql.connector import Error
import pandas as pd

# B1: Khoi tao connector
connection = mysql.connector.connect(host='14.225.44.220',
                                        database= "classicmodels",
                                        user="hocvien",
                                        password="CodeGym")




