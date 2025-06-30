from data_handler import QuestionLoader

def main():
    loader = QuestionLoader('data/questions.json')
    fragen = loader.load_questions()

    for frage in fragen:
        print(f'Frage: {frage['frage']}')
        for i, antwort in enumerate(frage['antworten']):
            print(f' {i+1}. {antwort}')
        print(f'Richtige Antwort: {frage['antworten'][frage['richtig']]}')
        print()

if __name__ == "__main__":
    main()
