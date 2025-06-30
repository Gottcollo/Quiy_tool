import json
import os

class HighscoreManager:
    def __init__(self, pfad="data/results.json"):
        self.pfad = pfad

    def lade_highscores(self):
        if not os.path.exists(self.pfad):
            return []
        with open(self.pfad, "r", encoding="utf-8") as f:
            return json.load(f)

    def top_scores(self, limit=10):
        daten = self.lade_highscores()
        daten.sort(key=lambda r: r['score'] / r['total'], reverse=True)
        return daten[:limit]
