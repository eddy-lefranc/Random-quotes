# Imports

import tkinter as tk
import requests
from threading import Thread

# Variables

api = "https://api.quotable.io/random"
quotes = []
quote_number = 0

# Fenêtre Tkinter

window = tk.Tk()
window.geometry("900x250")
window.title("Générateur de citations")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="#502F36")

# Fonction qui précharge 10 citations de l'API.

def preload_quotes():
    global quotes

    for x in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + author
        quotes.append(quote)
        
preload_quotes()

# Fonction qui récupère et affiche une citation aléatoire.

def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number = quote_number + 1
    print(quote_number)

    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=preload_quotes)
        thread.start()

# ******** UI ******** 
        
# Fenêtre de la citation

quote_label = tk.Label(window, text="Cliquez sur le bouton pour générer une citation.",
                       height=6,
                       pady=10,
                       wraplength=800,
                       font=("Times New Roman", 14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)

# Bouton

button = tk.Button(text_="Nouvelle citation",
                   command=get_random_quote,
                   bg='#1C161A',
                   fg="#FFFFFF",
                   activebackground="#FFFFFF",
                   font=("Times New Roman", 14))
button.grid(row=1, column=0, stick="WE", padx=20, pady=10)

# Lancement du programme

if __name__ == "__main__":
    window.mainloop()