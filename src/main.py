import random
import tkinter as tk
from login import LoginWindow
from quiz import Quizmanager
from data_handler import QuestionLoader
from gui import QuizGUI, AuswahlFenster

def start_quiz(username, root):
    root.withdraw()
    fragen = QuestionLoader('data/questions.json').load_questions()

    def on_quiz_start(gefilterte_fragen):
        quiz = Quizmanager(gefilterte_fragen)
        quiz_gui = QuizGUI(root, quiz, username)
        # Begrenze auf 5–10 zufällige Fragen (falls genug vorhanden)
        if len(gefilterte_fragen) >= 5:
            anzahl = min(len(gefilterte_fragen), random.randint(5, 10))
            ausgewählte_fragen = random.sample(gefilterte_fragen, anzahl)
        else:
            ausgewählte_fragen = gefilterte_fragen  # Weniger als 5 → nimm alle

        quiz = Quizmanager(ausgewählte_fragen)
        quiz_gui = QuizGUI(root, quiz, username)
        quiz_gui.grab_set()

    auswahl_fenster = AuswahlFenster(root, fragen, on_quiz_start)
    auswahl_fenster.grab_set()  # Fokus bleibt auf Auswahlfenster

def main():
    root = tk.Tk()
    root.geometry('300x300')
    LoginWindow(root, on_login_success=lambda username: start_quiz(username, root))
    root.mainloop()

if __name__ == "__main__":
    main()
