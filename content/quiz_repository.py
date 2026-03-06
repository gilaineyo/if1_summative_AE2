import csv # Read and write csv module
from pathlib import Path # To determine path to question and answer csv files
from .quiz_content import Question, Answer # Import classes for creating Question and Answer objects
from datetime import datetime # Import datetime package for saving date to CSV
import logging # Import logging package to support exception handling

logger = logging.getLogger(__name__)

class QuizRepository():
    """
    A class for the management of all quiz content.

    ...

    Attributes
    ----------
    questions_file : str
        filename of the file from which to read questions
    answers_file : str
        filename of the file from which to read questions
    questions : list
        list of all questions, populated by methods that read from csv
    questions : list
        list of all answers, populated by methods that read from csv

    Methods
    -------
    read_questions_from_csv():
        reads questions from csv and appends Question objects to list in questions attribute
    read_answers_from_csv():
        reads answers from csv and appends Answer objects to list in answers attribute
    get_questions_and_answers_for_user(discipline):
        constructs a question set from all questions based on the user's discipline
    get_question_answer_by_answer_id(id):
        accepts an answer id and retrieves the Answer and corresponding Question objects 
    get_question_by_id(id):
        retrieves the Question object for a given id
    write_results_to_csv(name, discipline, score, total_questions):
        writes results to CSV file defined in the method, creating the file and headers if necessary
    """
    def __init__(self, questions_file, answers_file):
        """
        Constructs all the necessary attributes for the QuizRepository object.

        Parameters
        ----------
            questions_file : str
                filename from which to read questions
            answers_file : str
                filename from which to read answers
        """
        self.questions_file = questions_file
        self.answers_file = answers_file
        self.questions = []
        self.answers = []

    def read_questions_from_csv(self):
        """
        Reads the CSV according to the stored filename.
        
        Creates a Question object for each row by mapping columns to Question constructor parameters and appends this to the questions attribute.

        Throws exceptions if unsuccessful.
        
        Parameters
        ----------
        None

        Returns
        -------
        None - results are appended to questions attribute
        """
        try:
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
        
        except FileNotFoundError:
            logger.error(f"Questions file not found at {questions_path}")
        except Exception as e:
            logger.error(f"Unexpected error reading questions: {e}")

    def read_answers_from_csv(self):
        """
        Reads the CSV according to the stored filename.
        
        Creates an Answer object for each row by mapping columns to Answer constructor parameters and appends this to the answers attribute.

        Throws exceptions if unsuccessful.

        Parameters
        ----------
        None

        Returns
        -------
        None - results are appended to answers attribute
        """
        try:
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
        except FileNotFoundError:
            logger.error(f"Questions file not found at {answers_path}")
        except Exception as e:
            logger.error(f"Unexpected error reading answers: {e}")

    def get_questions_and_answers_for_user(self, discipline):
        """
        Gets questions and associated answer options for user's session based on the user's selected discipline.

        Parameters
        ----------
        discipline : str
            user's selected discipline, for which questions will be retrieved along with questions that have no discipline defined
        
        Returns
        -------
        tuple[list[Question], list[Answer]]
            A tuple ``(user_questions, user_answers)`` where:
            - user_questions : list[Question]
                questions whose discipline matches the user's discipline, or those whose discipline is None, sorted by id
            - user_answers : list[Answer] 
                answers whose question_id is found within the returned user_questions 
        """
        self.read_questions_from_csv()
        self.read_answers_from_csv()
        user_questions = []
        user_answers = []

        for question in self.questions:
            if question.discipline == "":
                user_questions.append(question)
            elif question.discipline == discipline:
                user_questions.append(question)

        for question in user_questions:
            for answer in self.answers:
                if answer.question_id == question.id:
                    user_answers.append(answer)

        user_questions.sort(key=lambda x: x.id)

        return user_questions, user_answers
    
    def get_question_answer_by_answer_id(self, id):
        """
        Gets a single answer by its id and retrieves the associated question by calling get_question_by_id().

        Parameters
        ----------
        id : int
            id for the answer to be retrieved along with its corresponding question    
        
        Returns
        -------
        tuple[Question, Answer]
            A tuple ``(question, answer)`` where:
            - question : Question
                question with the id matching the question_id of the given id's Answer
            - answer : Answer 
                answer with the matching id 
        """
        self.read_answers_from_csv()
        for answer in self.answers:
            if answer.id == id:
                question = self.get_question_by_id(answer.question_id)
                return question, answer

    def get_question_by_id(self, id):
        """
        Gets a single question by its id.

        Parameters
        ----------
        id : int
            id for the question to be retrieved
        
        Returns
        -------
        Question
            question object with matching id
        """
        self.read_questions_from_csv()
        for question in self.questions:
            if question.id == id:
                return question
            
    def write_results_to_csv(self, name, discipline, score, total_questions):
        """
        Writes user's quiz results and timestamp to CSV, creating a CSV file if none exists and adding headers.

        Parameters
        ----------
        name : str
            user's name
        discipline : str
            user's selected discipline
        score : int
            number of correct answers given
        total_questions:
            number of questions in the quiz presented to the user
        
        Returns
        -------
        None

        Notes
        -------
        This method does not return a value, it writes a new row to `results.csv`. 
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("results.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([name, discipline, score, total_questions, timestamp])