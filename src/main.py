from quiz_app import QuizApp




def main():
    app = QuizApp('data/questions.json')
    app.run()

if __name__ == "__main__":
    main()
