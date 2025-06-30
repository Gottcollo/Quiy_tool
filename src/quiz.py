import random


class Quizmanager:
    def __init__(self, fragen_liste):
        self.fragen = fragen_liste
        self.punkte = 0


    def filter_fragen(self, kategorie=None, schwierigkeitsgrad=None):
        gefiltert = self.fragen
        if kategorie:
            gefiltert = [f for f in gefiltert if f.get('kategorie', '').lower() == kategorie.lower()]
        if schwierigkeitsgrad:
            gefiltert = [f for f in gefiltert if f.get('schwierigkeit', '').lower() ==schwierigkeitsgrad.lower()]
        return gefiltert
    
    def run(self, gefilterte_fragen=None):
        fragen = gefilterte_fragen if gefilterte_fragen else self.fragen
        random.shuffle(self.fragen)

        for frage in fragen:
            print(f"\nFrage: {frage['frage']}")
            for i, antwort in enumerate(frage['antworten']):
                print(f' {i+1}. {antwort}')

            try:
                auswahl = int(input('Deine Antwort (1-4): ')) - 1
            except ValueError:
                print('Total Falsche Eingabe. Frage wird Übersprungen.')
                continue

            if auswahl == frage['richtig']:
                print('Richtig!')
                self.punkte += 1
            
            else:
                print(f"Falsch! Die richtige Antwort ist: {frage['antworten'][frage['richtig']]}")
        
        print(f'\n Du hast {self.punkte} von {len(self.fragen)} Fragen richtig beantwortet.')