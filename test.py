import tkinter as tk

# Fonction appelée lors du mouvement de la souris
def suivi_souris(event):
    print(f"Coordonnées : {event.x}, {event.y}")

# Fonction appelée lors d’un clic gauche
def clic_gauche(event):
    print("Bonjour !")

# Fonction appelée lors d’une pression de touche
def touche_pressee(event):
    print(f"Bonjour, {event.keysym} !")

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Fenêtre interactive")
fenetre.geometry("400x300")

# Lier les événements
fenetre.bind("<Motion>", suivi_souris)
fenetre.bind("<Button-1>", clic_gauche)
fenetre.bind("<Key>", touche_pressee)

# Met le focus sur la fenêtre pour capter les touches clavier
fenetre.focus_set()

# Boucle principale
fenetre.mainloop()
