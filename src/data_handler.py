import json
import os

class QuestionLoader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_questions(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, dict) and 'questions' in data:
                return data['questions']
            elif isinstance(data, list):
                return data
            else:
                return []
