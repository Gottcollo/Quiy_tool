import tkinter as tk
from tkinter import messagebox


class LoginWindow:

    def __init__(self, master, on_login_success):
        self.master = master
        self.master.title('Login')
        self.on_login_success = on_login_success

        #beispiel-user (Benutzername: Passwort)immer erweiterbar
        self.user_db = { 'admin': '1234', 
                        'sam': 'samu1234'
                        
                        }
        
        tk.Label(master, text='Benutzername:').grid(row=0, padx=10, pady=10)
        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(master, text='Passwort:').grid(row=1, column=0, padx=10, pady=10)
        self.entry_password = tk.Entry(master, show='*')
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(master, text='Login', command=self.check_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if self.user_db.get(username) == password:
            messagebox.showinfo('Erfolgreicher Login', f'Willkommen, {username}!')
            # NICHT self.master.destroy() hier aufrufen!
            # Stattdessen nur Login-Fenster verstecken oder schließen, aber root nicht zerstören!
            self.master.withdraw()  # oder self.master.quit() vermeiden!
            self.on_login_success(username)


        else:
            messagebox.showerror("Fehler", "Falscher User oder Password.")

