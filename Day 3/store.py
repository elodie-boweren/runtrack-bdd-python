import mysql.connector
import os
from dotenv import load_dotenv
from tkinter import *

#importer dossier .env
load_dotenv()

#se connecter à ma BDD
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = os.getenv("password"),
    database = 'Store',
    autocommit = False,)

cursor = mydb.cursor()

def show_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in cursor:
        Result_pane.insert("", "end", values=product)
    # print("List of products")
    # for product in cursor:
    #     print(product)

def add_product():
    sql = "INSERT INTO products(name, description, price, quantity) VALUES(%s, %s, %s, %s)" 
    val = input("Name of product: "), input("Description: "), input("Price: "), input("Quantity: ")
    cursor.execute(sql, val)
    mydb.commit()
    print("Your product has been added")

def delete_product():
    sql = "DELETE FROM products WHERE id_product = %s"
    val = input("ID of product to delete: ")
    cursor.execute(sql, (val,))
    mydb.commit()
    print(f"""
          Your product {val} has been deleted from the database
          """)

def show_categories():
    cursor.execute("SELECT * FROM category")
    print("Categories")
    for category in cursor:
        print(category)

#instantiate window
window = Tk()
window.geometry("600x600")
window.title("My Store")
window.config(background="#52b2d3")
#title label centered
title = Label(window,text="Manage your store here", bg ="#52d372",font =("Comic sans MS",26, "italic"),relief = RAISED, bd = 5, padx = 4, pady = 4)
title.pack()
#button Show products
button = Button(window, text = "List of products", bg ="#52d372",font =("Comic sans MS",10),relief = RAISED, bd = 2)
button.config(command = show_products, activebackground = "black", activeforeground = "white")
button.place(x = 100, y = 100)
#button show categories
button = Button(window, text = "List of product categories", bg ="#52d372",font =("Comic sans MS",10), bd = 2)
button.config(command = show_categories, activebackground = "black", activeforeground = "white")
button.place(x = 300, y = 100)
#button add product
button = Button(window, text = "Add new product", bg = "#170fba", fg = "white", font =("Comic sans MS",10),relief = RAISED, bd = 2)
button.config(command = show_products)
button.place(x = 40, y = 150)
#button delete product
button = Button(window, text = "Delete product", bg ="#170fba", fg = "white",font=("Comic sans MS",10), bd = 2)
button.config(command = show_products)
button.place(x = 40, y = 185)
#button Modify product
button = Button(window, text = "Modify product", bg ="#170fba", fg = "white",font=("Comic sans MS",10), bd = 2)
button.config(command = show_products)
button.place(x = 40, y = 220)
#Bottom pane for query result
Result_pane = Frame(window, bg = "pink")
Result_pane.pack(side = BOTTOM)


#open window on screen
window.mainloop()



