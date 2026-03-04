class QuizContent():
    def __init__(self, id, text):
        self.id = int(id)
        self.text = text.strip()

class Question(QuizContent):
    def __init__(self, id, text, answer_ids, discipline, wiki_topic, wiki_href, advice_text):
        QuizContent.__init__(self, id, text)    
        self.answer_ids = list(map(int, answer_ids.split(',')))
        self.discipline = discipline.strip()
        self.wiki_topic = wiki_topic.strip()
        self.wiki_href = wiki_href.strip()
        self.advice_text = advice_text.strip()


class Answer(QuizContent):
    def __init__(self, id, text, question_id, is_correct):
        QuizContent.__init__(self, id, text)
        self.question_id = int(question_id)
        self.is_correct = bool(is_correct == 'TRUE')