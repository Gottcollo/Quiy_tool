from data_handler import QuestionLoader
from quiz import Quizmanager

class QuizApp:
    def __init__(self, pfad_zur_datei='data/questions.json'):
        self.loader = QuestionLoader(pfad_zur_datei)
        self.fragen = self.loader.load_questions()
        self.quiz = Quizmanager(self.fragen)

    def auswahl_mit_optionen(self, titel, werte_liste):
        if not werte_liste:
            print(f"Keine Optionen verfügbar für {titel}")
            return None

        print(f'\n{titel}')
        for i, eintrag in enumerate(werte_liste, 1):
            print(f'{i}. {eintrag}')
    
        while True:
            eingabe = input('Deine Auswahl (Nummer): ')
            if not eingabe:
                return None
            if eingabe.isdigit():
                index = int(eingabe) - 1
                if 0 <= index < len(werte_liste):
                    return werte_liste[index]
            print("Ungültige Eingabe, bitte eine Zahl aus der Liste eingeben.")

    
    def run(self):
        kategorien = sorted(set(f.get("kategorie", "") for f in self.fragen if "kategorie" in f))
        schwierigkeitsgrade = sorted(set(f.get("schwierigkeit", "") for f in self.fragen if "schwierigkeit" in f))

        print(f"[DEBUG] Kategorien: {kategorien}")
        print(f"[DEBUG] Schwierigkeitsgrade: {schwierigkeitsgrade}")

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
