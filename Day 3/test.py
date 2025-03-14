import mysql.connector
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk

# Connexion à la base de données
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("password"),
    database="Store"
)

load_dotenv()

cursor = mydb.cursor()

# Fonction pour afficher les produits
def show_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    Result_pane.delete(*Result_pane.get_children())  # Vider le tableau avant d'ajouter les nouvelles données
    for product in products:
        Result_pane.insert("", "end", values=product)

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Liste des produits")
root.geometry("600x400")

# Créer un tableau pour afficher les produits
columns = ("ID", "Nom", "Prix", "Quantité")
Result_pane = ttk.Treeview(root, columns=columns, show="headings")

# Configurer les en-têtes de colonnes
for col in columns:
    Result_pane.heading(col, text=col)

# Afficher le tableau
Result_pane.pack(fill="both", expand=True)

# Bouton pour actualiser les produits
refresh_button = tk.Button(root, text="Afficher les produits", command=show_products)
refresh_button.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
