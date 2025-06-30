import random
import tkinter as tk
from login import LoginWindow
from quiz import Quizmanager
from data_handler import QuestionLoader
from gui import QuizGUI, AuswahlFenster, zeige_highscores_fenster

def start_quiz(username, root):
    root.withdraw()
    fragen = QuestionLoader('data/questions.json').load_questions()

    def on_quiz_start(gefilterte_fragen):
        MIN_FRAGEN = 5
        MAX_FRAGEN = 10

        alle_fragen = QuestionLoader('data/questions.json').load_questions()

        # Wenn gefilterte Fragen zu wenig sind, ergänze aus anderen Fragen, ohne Duplikate
        if len(gefilterte_fragen) < MIN_FRAGEN:
            fehlende_anzahl = MIN_FRAGEN - len(gefilterte_fragen)
            # Filtere aus allen Fragen diejenigen, die nicht in gefilterte_fragen sind
            rest = [f for f in alle_fragen if f not in gefilterte_fragen]

            # Wähle zufällig fehlende Fragen aus rest
            if len(rest) > 0:
                ergänzung = random.sample(rest, min(fehlende_anzahl, len(rest)))
                ausgewählte_fragen = gefilterte_fragen + ergänzung
            else:
                ausgewählte_fragen = gefilterte_fragen
        else:
            anzahl = min(len(gefilterte_fragen), random.randint(MIN_FRAGEN, MAX_FRAGEN))
            ausgewählte_fragen = random.sample(gefilterte_fragen, anzahl)

        quiz = Quizmanager(ausgewählte_fragen)
        quiz_gui = QuizGUI(root, quiz, username)
        quiz_gui.grab_set()


    auswahl_fenster = AuswahlFenster(root, fragen, on_quiz_start)
    auswahl_fenster.grab_set()  # Fokus bleibt auf Auswahlfenster

def on_login_success(username, root):
    start_quiz(username, root)
    # Highscore-Button im Hauptfenster anzeigen
    btn_highscore = tk.Button(root, text="Highscores anzeigen", command=lambda: zeige_highscores_fenster(root))
    btn_highscore.grid(row=1, column=0, pady=10, sticky="w")


def main():
    root = tk.Tk()
    root.geometry('300x300')
    # Übergib root zusätzlich, damit on_login_success ihn nutzen kann
    LoginWindow(root, on_login_success=lambda username: on_login_success(username, root))
    root.mainloop()

if __name__ == "__main__":
    main()
