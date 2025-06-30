import tkinter as tk
from login import LoginWindow
from quiz_app import QuizApp



def start_quiz(username):
    app = QuizApp('data/questions.json')
    app.run()

def main():
    root = tk.Tk()
    root.geometry('300x200')
    LoginWindow(root, on_login_success=start_quiz)
    root.mainloop()

if __name__ == "__main__":
    main()
