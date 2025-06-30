import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
from highscore import HighscoreManager

def zeige_highscores_fenster(master):
    manager = HighscoreManager()
    top = manager.top_scores(10)

    if not top:
        messagebox.showinfo("Highscores", "Noch keine Einträge vorhanden.")
        return

    fenster = tk.Toplevel(master)
    fenster.title("Highscores")

    text = tk.Text(fenster, width=60, height=20)
    text.pack(padx=10, pady=10)

    text.insert("end", f"{'Name':<15}{'Punkte':<10}{'Gesamt':<10}{'Prozent':<10}{'Datum'}\n")
    text.insert("end", "-" * 60 + "\n")

    for eintrag in top:
        prozent = (eintrag["score"] / eintrag["total"]) * 100
        zeile = f"{eintrag['user']:<15}{eintrag['score']:<10}{eintrag['total']:<10}{prozent:>7.1f}%   {eintrag['date'][:10]}\n"
        text.insert("end", zeile)

    text.config(state="disabled")


def save_result(username, score, total):
    result = {
        "user": username,
        "score": score,
        "total": total,
        "date": datetime.now().isoformat()
    }

    pfad = "data/results.json"
    if os.path.exists(pfad):
        with open(pfad, "r", encoding="utf-8") as f:
            daten = json.load(f)
    else:
        daten = []

    daten.append(result)

    with open(pfad, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=2, ensure_ascii=False)


class QuizGUI(tk.Toplevel):
    def __init__(self, master, quizmanager, username):
        super().__init__(master)
        self.title("Quiz")
        self.quiz = quizmanager
        self.username = username
        self.current_index = 0
        self.punkte = 0

        self.columnconfigure(0, weight=1)  # Für zentriertes Layout

        self.frage_label = tk.Label(self, text="", wraplength=400, font=("Arial", 14))
        self.frage_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.var_antwort = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.var_antwort, value=i, font=("Arial", 12))
            rb.grid(row=i + 1, column=0, sticky="w", padx=40, pady=2)
            self.radio_buttons.append(rb)

        self.feedback_label = tk.Label(self, text="", font=("Arial", 12))
        self.feedback_label.grid(row=5, column=0, padx=20, pady=(10, 20), sticky="w")

        self.next_button = tk.Button(self, text="Antwort prüfen", command=self.check_answer)
        self.next_button.grid(row=6, column=0, pady=(0, 20))

        self.show_question()

    def show_question(self):
        if self.current_index >= len(self.quiz.fragen):
            self.show_result()
            return

        frage = self.quiz.fragen[self.current_index]
        self.frage_label.config(text=frage['frage'])
        self.var_antwort.set(-1)
        self.feedback_label.config(text="", fg="black")  # Feedback leeren
        
        for i, antwort in enumerate(frage['antworten']):
            self.radio_buttons[i].config(text=antwort, state="normal")

        self.next_button.config(state="normal")

    def check_answer(self):
        selected = self.var_antwort.get()
        if selected == -1:
            messagebox.showwarning("Keine Antwort", "Bitte wähle eine Antwort aus.")
            return

        # Buttons deaktivieren, um weitere Eingaben während Feedback zu verhindern
        for rb in self.radio_buttons:
            rb.config(state="disabled")
        self.next_button.config(state="disabled")

        frage = self.quiz.fragen[self.current_index]
        if selected == frage['richtig']:
            self.punkte += 1
            self.feedback_label.config(text='RICHTIG!', fg='green')
        else:
            richtige_antwort = frage['antworten'][frage['richtig']]
            self.feedback_label.config(text=f"Falsch! Die richtige Antwort ist:\n{richtige_antwort}", fg='red')

        self.current_index += 1
        self.after(1500, self.show_question)

    def show_result(self):
        gesamt = len(self.quiz.fragen)
        prozent = (self.punkte / gesamt) * 100

        if prozent >= 90:
            feedback = "Ausgezeichnet! Du hast ein sehr gutes Verständnis der Themen."
        elif prozent >= 70:
            feedback = "Gut gemacht! Du beherrschst die Grundlagen, aber es gibt noch Luft nach oben."
        elif prozent >= 50:
            feedback = "Du hast einige Fragen richtig beantwortet. Etwas mehr Übung hilft dir weiter."
        else:
            feedback = "Du solltest die Themen nochmals wiederholen. Lass dich nicht entmutigen!"
        save_result(self.username, self.punkte, len(self.quiz.fragen))

        # Fenster leeren
        for widget in self.winfo_children():
            widget.destroy()

        result_text = f"Du hast {self.punkte} von {gesamt} Fragen richtig beantwortet ({prozent:.0f}%).\n\n{feedback}"
        result_label = tk.Label(self, text=result_text, font=("Arial", 14), wraplength=500, justify="left")
        result_label.grid(row=0, column=0, padx=20, pady=40)

        close_btn = tk.Button(self, text="Schließen", command=self.destroy)
        close_btn.grid(row=1, column=0, pady=10)





class AuswahlFenster(tk.Toplevel):
    def __init__(self, master, fragen, on_start_quiz):
        super().__init__(master)
        self.title("Auswahl Quiz-Kategorie & Schwierigkeit")
        self.fragen = fragen
        self.on_start_quiz = on_start_quiz
        self.geometry("600x500")
        
        self.columnconfigure(0, weight=1)

        # Kategorien und Schwierigkeitsgrade sammeln
        kategorien = sorted(set(f['kategorie'] for f in fragen))
        schwierigkeiten = sorted(set(f['schwierigkeit'] for f in fragen))

        # Label Kategorie
        lbl_kategorie = tk.Label(self, text="Kategorie:")
        lbl_kategorie.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))

        self.kategorie_var = tk.StringVar(value=kategorien[0] if kategorien else "")

        # Radiobuttons Kategorien
        for i, k in enumerate(kategorien):
            rb = tk.Radiobutton(self, text=k, variable=self.kategorie_var, value=k)
            rb.grid(row=i+1, column=0, sticky="w", padx=40)

        # Label Schwierigkeit
        start_row = len(kategorien) + 1
        lbl_schwierigkeit = tk.Label(self, text="Schwierigkeitsgrad:")
        lbl_schwierigkeit.grid(row=start_row, column=0, sticky="w", padx=20, pady=(20, 5))

        self.schwierigkeit_var = tk.StringVar(value=schwierigkeiten[0] if schwierigkeiten else "")

        # Radiobuttons Schwierigkeit
        for j, s in enumerate(schwierigkeiten):
            rb = tk.Radiobutton(self, text=s, variable=self.schwierigkeit_var, value=s)
            rb.grid(row=start_row + j + 1, column=0, sticky="w", padx=40)

        # Button Quiz starten
        btn_start = tk.Button(self, text="Quiz starten", command=self.start_quiz)
        btn_start.grid(row=start_row + len(schwierigkeiten) + 2, column=0, pady=30)

    def start_quiz(self):
        kategorie = self.kategorie_var.get()
        schwierigkeitsgrad = self.schwierigkeit_var.get()
        gefilterte = [f for f in self.fragen if f['kategorie'] == kategorie and f['schwierigkeit'] == schwierigkeitsgrad]
        if not gefilterte:
            messagebox.showwarning("Keine Fragen", "Für die Auswahl wurden keine Fragen gefunden.")
            return
        self.destroy()
        self.on_start_quiz(gefilterte)


