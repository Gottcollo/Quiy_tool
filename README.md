# Quiy_tool


Quiz für Einfache Quizabfragen

title: "Quiz Tool"

description: |
  Ein einfaches Quiz-Tool mit JSON-basierten Fragen, grafischer Benutzeroberfläche (GUI) und Highscore-Verwaltung.

project_overview: |
  Dieses Python-Projekt ist ein interaktives Quiz mit GUI auf Basis von Tkinter.
  Es lädt Fragen aus JSON-Dateien, zeigt sie im Quiz an, wertet die Antworten aus und speichert die Ergebnisse inklusive Highscores.

features:
  - "Login-Funktion: Nutzer melden sich mit einem Benutzernamen an."
  - "Fragenverwaltung: Fragen werden aus JSON-Dateien geladen."
  - "Quiz-Auswahl: Auswahl von Kategorie und Schwierigkeitsgrad vor dem Quizstart."
  - "Quiz-GUI: Anzeige der Fragen mit Radiobutton-Antworten."
  - "Feedback: Sofortige Rückmeldung (richtig/falsch) direkt im Quizfenster."
  - "Highscores: Speicherung der Ergebnisse mit Benutzername, Punktzahl und Datum in results.json."
  - "Highscore-Anzeige: Übersicht der besten Ergebnisse in einem separaten Fenster."
  - "Modulares Design: Aufgeteilt in mehrere Module für bessere Wartbarkeit."

project_structure: |
  projektordner/
    ├── data/
    │    ├── questions.json      # Fragen mit Kategorie und Schwierigkeitsgrad
    │    └── results.json        # Gespeicherte Spielergebnisse und Highscores
    ├── gui.py                 # GUI-Komponenten: QuizGUI, AuswahlFenster, Highscore-Anzeige
    ├── quiz.py                # Quizmanager: Logik und Ablauf des Quiz
    ├── login.py               # Login-Fenster und Nutzerverwaltung
    ├── data_handler.py        # Laden und Verwalten der Fragen aus JSON
    ├── main.py                # Programmstart, Koordination von Login, Auswahl und Quiz
    ├── highscore.py           # Highscore-Management
    └── README.md              # Dieses Dokument

installation_and_usage:
  steps:
    - "Python 3 installieren (getestet mit Version 3.8+)."
    - "Benötigte Bibliotheken: Standardbibliotheken (tkinter, json, os, datetime)."
    - "Projekt starten mit: python main.py"
    - "Programmablauf:"
      - "Benutzernamen eingeben und einloggen."
      - "Quiz-Kategorie und Schwierigkeitsgrad auswählen."
      - "Quizfragen beantworten, Feedback wird direkt angezeigt."
      - "Am Ende wird das Ergebnis angezeigt und gespeichert."
      - "Highscores können über einen Button eingesehen werden."

file_formats:
  questions_json:
    description: "Enthält die Fragen als Liste von Objekten mit folgenden Feldern:"
    fields:
      - frage: "String mit der Frage"
      - antworten: "Liste der Antwortmöglichkeiten"
      - richtig: "Index der richtigen Antwort"
      - kategorie: "Kategorie-Name (z.B. 'Mathe')"
      - schwierigkeit: "Schwierigkeitsgrad (z.B. 'leicht')"
  results_json:
    description: "Speichert die Quiz-Ergebnisse als Liste mit:"
    fields:
      - user: "Benutzername"
      - score: "Anzahl der richtig beantworteten Fragen"
      - total: "Gesamtanzahl der Fragen"
      - date: "Zeitstempel des Quizabschlusses"

customization_and_extensions:
  - "Neue Kategorien oder Fragen können einfach in questions.json hinzugefügt werden."
  - "GUI kann beliebig erweitert oder angepasst werden (z.B. Layout, weitere Feedbackmöglichkeiten)."
  - "Datenbankanbindung als Alternative zu JSON-Dateien ist möglich."
  - "Erweiterungen wie Zeitlimits oder zusätzliche Quizmechaniken können integriert werden."
