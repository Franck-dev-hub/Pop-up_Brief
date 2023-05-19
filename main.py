import tkinter as tk
import datetime
import configparser

# Chargement du fichier .conf
config = configparser.ConfigParser()
config.read('main.conf')

# Lecture des paramètres du fichier .conf
day = int(config.get('Configuration', 'day'))
heure_rappel_am = int(config.get('Configuration', 'heure_rappel_am'))
minute_rappel_am = int(config.get('Configuration', 'minute_rappel_am'))
heure_rappel_pm = int(config.get('Configuration', 'heure_rappel_pm'))
minute_rappel_pm = int(config.get('Configuration', 'minute_rappel_pm'))
brief_am = config.get('Configuration', 'brief_am')
brief_pm = config.get('Configuration', 'brief_pm')


def popup_am():
    popup = tk.Toplevel(root)  # Ouvre la fenêtre par-dessus tout
    popup.title("Brief")  # Ajout d'un titre à la fenêtre
    popup.configure(bg="grey")  # Modification de la couleur d'arrière-plan de la fenêtre
    popup.attributes("-fullscreen", True)  # Affiche en plein écran
    popup_am.popup_exists = True  # Indique qu'une fenêtre contextuelle est ouverte

    # Définition du texte à afficher en fonction de la taille de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if screen_width > screen_height:
        font_size = int(screen_width / 20)
    else:
        font_size = int(screen_height / 20)
    text = "Attention brief à " + brief_am
    label = tk.Label(popup, text=text, font=("Helvetica", font_size), bg="grey")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    # Définition de la logique de fermeture de la fenêtre contextuelle
    def close_am():
        popup.destroy()
        popup_am.popup_exists = False

    # Ajouter un bouton "Fermer la fenêtre"
    button = tk.Button(popup, text="Fermer la fenêtre", font=("Helvetica", int(font_size/8)), command=close_am,
                       width=40, height=5)
    button.pack(side="bottom", pady=20, fill="both")

    popup.protocol("WM_DELETE_WINDOW", close_am)


def popup_pm():
    popup = tk.Toplevel(root)  # Ouvre la fenêtre par-dessus tout
    popup.title("Brief")  # Ajout d'un titre à la fenêtre
    popup.configure(bg="grey")  # Modification de la couleur d'arrière-plan de la fenêtre
    popup.attributes("-fullscreen", True)  # Affiche en plein écran
    popup_pm.popup_exists = True  # Indique qu'une fenêtre contextuelle est ouverte

    # Définition du texte à afficher en fonction de la taille de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    if screen_width > screen_height:
        font_size = int(screen_width / 20)
    else:
        font_size = int(screen_height / 20)
    text = "Attention brief à " + brief_pm
    label = tk.Label(popup, text=text, font=("Helvetica", font_size), bg="grey")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    # Définition de la logique de fermeture de la fenêtre contextuelle
    def close_pm():
        popup.destroy()
        popup_pm.popup_exists = False

    # Ajouter un bouton "Fermer la fenêtre"
    button = tk.Button(popup, text="Fermer la fenêtre", font=("Helvetica", int(font_size/8)), command=close_pm)
    button.pack(side="bottom", pady=20)

    popup.protocol("WM_DELETE_WINDOW", close_pm)


def schedule_popup():
    now = datetime.datetime.now()
    if now.weekday() == day:
        if now.hour == heure_rappel_am and now.minute == minute_rappel_am:
            popup_am()
        elif now.hour == heure_rappel_pm and now.minute == minute_rappel_pm:
            popup_pm()
        else:
            root.after(60000, schedule_popup)  # Réessaie dans 1 minute (60 000 millisecondes)
    else:
        root.after(43200000, schedule_popup)  # Réessaie dans 12H (43 200 000 millisecondes)


root = tk.Tk()
root.withdraw()

popup_am.popup_exists = False
popup_pm.popup_exists = False

schedule_popup()
root.mainloop()
