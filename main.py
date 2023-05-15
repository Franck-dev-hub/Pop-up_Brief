import tkinter as tk
import datetime


def popup_matin():
    popup = tk.Toplevel(root)
    popup.title("Brief")  # Ajout d'un titre à la fenêtre
    popup.configure(bg="grey")  # Modification de la couleur d'arrière plan de la fenêtre
    popup.attributes("-fullscreen", True)  # Affiche en plein écran
    popup_matin.popup_exists = True  # Indique qu'une fenêtre contextuelle est ouverte

    # Définition du texte à afficher en fonction de la taille de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if screen_width > screen_height:
        font_size = int(screen_width / 20)
    else:
        font_size = int(screen_height / 20)
    text = "Attention brief à 9H00"
    label = tk.Label(popup, text=text, font=("Helvetica", font_size), bg="grey")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    # Définition de la logique de fermeture de la fenêtre contextuelle
    def close_matin():
        popup.destroy()
        popup_matin.popup_exists = False

    # Ajouter un bouton "Fermer la fenêtre"
    button = tk.Button(popup, text="Fermer la fenêtre", font=("Helvetica", int(font_size/8)), command=close_matin, width=40, height=5)
    button.pack(side="bottom", pady=20, fill="both")

    popup.protocol("WM_DELETE_WINDOW", close_matin)


def popup_aprem():
    popup = tk.Toplevel(root)
    popup.title("Brief")  # Ajout d'un titre à la fenêtre
    popup.configure(bg="grey")  # Modification de la couleur d'arrière plan de la fenêtre
    popup.attributes("-fullscreen", True)  # Affiche en plein écran
    popup_matin.popup_exists = True  # Indique qu'une fenêtre contextuelle est ouverte

    # Définition du texte à afficher en fonction de la taille de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if screen_width > screen_height:
        font_size = int(screen_width / 20)
    else:
        font_size = int(screen_height / 20)
    text = "Attention brief à 15H00"
    label = tk.Label(popup, text=text, font=("Helvetica", font_size), bg="grey")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    # Définition de la logique de fermeture de la fenêtre contextuelle
    def close_aprem():
        popup.destroy()
        popup_aprem.popup_exists = False

    # Ajouter un bouton "Fermer la fenêtre"
    button = tk.Button(popup, text="Fermer la fenêtre", font=("Helvetica", int(font_size/8)), command=close_aprem)
    button.pack(side="bottom", pady=20)

    popup.protocol("WM_DELETE_WINDOW", close_aprem)


def schedule_popup():
    now = datetime.datetime.now()
    if now.weekday() == 2:
        if now.hour == 8 and now.minute == 45:
            popup_matin()
        elif now.hour == 14 and now.minute == 45:
            popup_aprem()
        else:
            root.after(60000, schedule_popup)  # Réessaie dans 1 minute (60 000 millisecondes)
    else:
        root.after(43200000, schedule_popup)  # Réessaie dans 12H (43 200 000 millisecondes)


root = tk.Tk()
root.withdraw()

popup_matin.popup_exists = False
popup_aprem.popup_exists = False

schedule_popup()
root.mainloop()
