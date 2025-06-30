import tkinter as tk
from tkinter import messagebox

class QuizGUI(tk.Toplevel):
    def __init__(self, master, quizmanager):
        super().__init__(master)
        self.title("Quiz")
        self.quiz = quizmanager
        self.current_index = 0
        self.punkte = 0

        self.frage_label = tk.Label(self, text="", wraplength=400, font=("Arial", 14))
        self.frage_label.pack(pady=20)

        self.var_antwort = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.var_antwort, value=i, font=("Arial", 12))
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(self, text="Antwort prüfen", command=self.check_answer)
        self.next_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.current_index >= len(self.quiz.fragen):
            self.show_result()
            return

        frage = self.quiz.fragen[self.current_index]
        self.frage_label.config(text=frage['frage'])
        self.var_antwort.set(-1)
        for i, antwort in enumerate(frage['antworten']):
            self.radio_buttons[i].config(text=antwort)

    def check_answer(self):
        selected = self.var_antwort.get()
        if selected == -1:
            messagebox.showwarning("Keine Antwort", "Bitte wähle eine Antwort aus.")
            return

        frage = self.quiz.fragen[self.current_index]
        if selected == frage['richtig']:
            self.punkte += 1
            messagebox.showinfo("Richtig!", "Deine Antwort ist richtig!")
        else:
            richtige_antwort = frage['antworten'][frage['richtig']]
            messagebox.showinfo("Falsch", f"Falsch! Die richtige Antwort ist:\n{richtige_antwort}")

        self.current_index += 1
        self.show_question()

    def show_result(self):
        messagebox.showinfo("Ergebnis", f"Du hast {self.punkte} von {len(self.quiz.fragen)} Fragen richtig beantwortet!")
        self.destroy()




class AuswahlFenster(tk.Toplevel):
    def __init__(self, master, fragen, on_start_quiz):
        super().__init__(master)
        self.title("Auswahl Quiz-Kategorie & Schwierigkeit")
        self.fragen = fragen
        self.on_start_quiz = on_start_quiz
        self.geometry("400x300")

        # Dynamisch Kategorien und Schwierigkeitsgrade sammeln und sortieren
        kategorien = sorted(set(f['kategorie'] for f in fragen))
        schwierigkeiten = sorted(set(f['schwierigkeit'] for f in fragen))

        tk.Label(self, text="Kategorie:").pack()
        self.kategorie_var = tk.StringVar(value=kategorien[0] if kategorien else "")
        for k in kategorien:
            tk.Radiobutton(self, text=k, variable=self.kategorie_var, value=k).pack(anchor="w")

        tk.Label(self, text="Schwierigkeitsgrad:").pack()
        self.schwierigkeit_var = tk.StringVar(value=schwierigkeiten[0] if schwierigkeiten else "")
        for s in schwierigkeiten:
            tk.Radiobutton(self, text=s, variable=self.schwierigkeit_var, value=s).pack(anchor="w")

        start_btn = tk.Button(self, text="Quiz starten", command=self.start_quiz)
        start_btn.pack(pady=10)

    def start_quiz(self):
        kategorie = self.kategorie_var.get()
        schwierigkeitsgrad = self.schwierigkeit_var.get()
        gefilterte = [f for f in self.fragen if f['kategorie'] == kategorie and f['schwierigkeit'] == schwierigkeitsgrad]
        if not gefilterte:
            messagebox.showwarning("Keine Fragen", "Für die Auswahl wurden keine Fragen gefunden.")
            return
        self.destroy()
        self.on_start_quiz(gefilterte)

