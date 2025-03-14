import mysql.connector
import os
from dotenv import load_dotenv

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = os.getenv("password"),
    database = 'zoo'
)

load_dotenv()

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"connecté à MySQL, {db_info}")

cursor = mydb.cursor()

# cursor.execute("SHOW DATABASES")
# for x in cursor:
#   print("list of databases: ", x)

cursor.execute("USE zoo")


# cursor.execute("""CREATE TABLE animal
# (id_animal INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# name VARCHAR(150),
# race VARCHAR(150),
# id_cage INT,
# DoB DATE,
# country VARCHAR(150))""")
# print("TABLE animal was created")

# cursor.execute("""CREATE TABLE cage
#     (id_cage INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     surface INT,
#     capacity INT)
#     """)
# print("TABLE cage was created")

# cursor.execute("SHOW TABLES")
# for x in cursor:
#   print("list of tables: ", x)

class Animal:
    def __init__(self, name, race, id_cage, DoB, country):
        self.id_animal = int
        self.name = name
        self.race = race
        self.id_cage = int
        self.DoB = DoB
        self.country = country
        sql = ("INSERT INTO animal(name, race, id_cage, DoB, country) VALUES(%s, %s, %s, %s, %s)")
        val = name, race, id_cage, DoB, country
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "animal created")
    
class Cage:
    def __init__(self, surface, max_capacity):
        self.id_cage = int
        self.surface = surface
        self.capacity = max_capacity

def show_animals():
    cursor.execute("SELECT * FROM animal")
    print("The animals in the zoo are:")
    for x in cursor:
        print(x)


# animal1 = Animal("Balou", "panda", 2, "2023/5/10", "china")
# animal2 = Animal("Tiger", "tiger", 3, "2020/4/6", "india")
show_animals()
