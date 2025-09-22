import os

class HistoryManager:
    def __init__(self, filename="history.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write('')

    def save_calculation(self, expression, result):
        with open(self.filename, 'a') as f:
            f.write(f"{expression} = {result}\n")

    def get_history(self):
        with open(self.filename, 'r') as f:
            return f.readlines()