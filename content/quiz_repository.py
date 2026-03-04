import csv # Read and write csv module
from pathlib import Path # To determine path to question and answer csv files
from .quiz_content import Question, Answer # Import classes for creating Question and Answer objects

class QuizRepository():
    def __init__(self, questions_file, answers_file):
        self.questions_file = questions_file
        self.answers_file = answers_file
        self.questions = []
        self.answers = []

    def read_questions_from_csv(self):
        project_root = Path(__file__).parent.parent
        questions_path = project_root / "data" / self.questions_file
        with open(questions_path, newline='') as f:
            rows = csv.DictReader(f, delimiter=',')
            for row in rows:
                question = Question(
                    row['id'],
                    row['text'],
                    row['answer_ids'],
                    row['discipline'],
                    row['wiki_topic'],
                    row['wiki_href'],
                    row['advice_text'],
                )
                self.questions.append(question)

    def read_answers_from_csv(self):
        project_root = Path(__file__).parent.parent
        answers_path = project_root / "data" / self.answers_file
        with open(answers_path, newline='') as f:
            rows = csv.DictReader(f, delimiter=',')
            for row in rows:
                answer = Answer(
                    row['id'],
                    row['text'],
                    row['question_id'],
                    row['is_correct']
                )
                self.answers.append(answer)