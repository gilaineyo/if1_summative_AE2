class QuizSession():
    def __init__(self, user):
        self.user = user
        self.responses = []
        self.current_question_id = None

    