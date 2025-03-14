import mysql.connector
import os

# def load_env(file_path):
#     with open(file_path) as file:
#         for line in file:
#             key, value = line.strip().split("=", 1)
#             os.environ[key] = value

# load_env(".env")
# password = os.getenv("password")

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ecole2024!',
    database = 'laplateforme',
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    # print(f"connecté à MySQL, {db_info}")

cursor = mydb.cursor()
#job 4:
# cursor.execute("SELECT nom,capacite FROM salle;")
# print(results)

#job 5:
# cursor.execute("SELECT superficie FROM etage;")
# results = cursor.fetchall()
# print(results)
# superficie_totale = sum(result[0] for result in results)
# print(f"La superficie de La Plateforme est de {superficie_totale} m2")

#job 6:
cursor.execute("SELECT capacite FROM salle;")
results = cursor.fetchall()
capacite_totale = sum(result[0] for result in results)
print(f"La capacité de toutes les salles est de {capacite_totale}")


results = cursor.fetchall()
result = cursor.fetchone()
# print(results)

# print("-----------------")
# print(result)

cursor.close()
mydb.close()