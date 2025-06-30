from data_handler import QuestionLoader
from quiz import Quizmanager

class QuizApp:
    def __init__(self, pfad_zur_datei='data/questions.json'):
        self.loader = QuestionLoader(pfad_zur_datei)
        self.fragen = self.loader.load_questions()
        self.quiz = Quizmanager(self.fragen)

    def auswahl_mit_optionen(self, titel, werte_liste):
        print(f'\n{titel}')
        for eintrag in werte_liste:
            print(f' - {eintrag}')
        eingabe = input('Deine Auswahl: ')
        return eingabe if eingabe else None
    
    def run(self):
        kategorien = sorted(set(f["kategorie"] for f in self.fragen if "kategorie" in f))
        schwierigkeitsgrade = sorted(set(f["schwierigkeit"] for f in self.fragen if "schwierigkeit" in f))

        kategorie = self.auswahl_mit_optionen("📚 Verfügbare Kategorien:", kategorien)
        schwierigkeitsgrad = self.auswahl_mit_optionen("🧠 Verfügbare Schwierigkeitsgrade:", schwierigkeitsgrade)

        gefilterte_fragen = self.quiz.filter_fragen(
            kategorie=kategorie,
            schwierigkeitsgrad=schwierigkeitsgrad
        )

        if not gefilterte_fragen:
            print(' Keine Fragen gefunden für die Auswahl.')
            return
        
        self.quiz.run(gefilterte_fragen)