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
        quiz_gui = QuizGUI(root, quiz)
        quiz_gui.grab_set()

    AuswahlFenster(root, fragen, on_quiz_start)

def main():
    root = tk.Tk()
    root.geometry('300x300')
    LoginWindow(root, on_login_success=lambda username: start_quiz(username, root))
    root.mainloop()

if __name__ == "__main__":
    main()
