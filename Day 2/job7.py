import mysql.connector
import os
from dotenv import load_dotenv

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = os.getenv("password"),
    database = 'company',
)

load_dotenv()

if mydb.is_connected():
    db_info = mydb.get_server_info()
    # print(f"connecté à MySQL, {db_info}")

cursor = mydb.cursor()

class Company:
    def __init__(self):
        self.employee = str
    
    def show_employees(self):
        cursor.execute("SELECT * FROM employee;")
        results = cursor.fetchall()
        print(results)
    
    def get_id_employee(self, nom, prenom):
        sql = ("SELECT id_employee FROM employee WHERE nom = %s and prenom = %s;")
        val = nom, prenom
        cursor.execute(sql, val)
        results = cursor.fetchall()
        print(results)

    def delete_employee(self, id_employee):
        sql = "DELETE FROM employee WHERE id_employee = %s"
        val = id_employee
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) deleted")

    def assign_service(self, id_employee, id_service):
        sql = "UPDATE employee SET id_service = %s WHERE id_employee = %s"
        val = id_service, id_employee
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) inserted")

class Employee:
    def __init__(self, nom, prenom, salaire):
        self.id_employee = int
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        sql = "INSERT INTO employee (nom, prenom, salaire) VALUES (%s, %s, %s)"
        val = (nom, prenom, salaire)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) added")
    
    
    
# Elodie = Employee("Boweren", "Elodie", 2450)
Company = Company()
# Company.show_employees()
# Company.get_id_employee("Boweren", "Elodie")
# Company.delete_employee((5,))

Company.assign_service(2, 2)
Company.show_employees()




