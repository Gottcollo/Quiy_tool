import json
import os

class QuestionLoader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_questions(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data.get('questions', [])
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON from the file: {e}")