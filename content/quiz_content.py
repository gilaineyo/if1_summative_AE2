class QuizContent():
    """
    A parent class for question and answer content.
    ...

    Attributes
    ----------
    id : int
        id of the content item
    text : str
        text content of the item
    """
    def __init__(self, id, text):
        """
        Constructs all the necessary attributes for the QuizContent object.

        Parameters
        ----------
            id : int or str
                id of the content item, converted to int by this contructor
            text : str
                text content of the item
        """
        self.id = int(id)
        self.text = text.strip()

class Question(QuizContent):
    """
    A class representing a question. Inherits from QuizContent.
    ...

    Attributes
    ----------
    id : int
        id of the Question
    text : str
        text content of the Question
    answer_ids : [int]
        a list of integers representing the ids of the Question's answer options
    discipline : str
        the user discipline to which the question relates (may be None)
    wiki_topic : str
        the section of the wiki to which the Question maps
    wiki_href : str
        the href of the relevant wiki entry
    advice_text : str
        text to be displayed to the user in the event of an incorrect answer
    """
    def __init__(self, id, text, answer_ids, discipline, wiki_topic, wiki_href, advice_text):
        """
        Constructs all the necessary attributes for the Question object.

        Parameters
        ----------
            id : int or str
                id of the Question
            text : str
                text content of the Question
            answer_ids : [str]
                a list of strings representing the ids of the Question's answer options, converted to [int] by this constructor
            discipline : str
                the user discipline to which the question relates (may be None)
            wiki_topic : str
                the section of the wiki to which the Question maps
            wiki_href : str
                the href of the relevant wiki entry
            advice_text : str
                text to be displayed to the user in the event of an incorrect answer
        
        Notes
        ----------
            This constructor invokes the parent `QuizContent` constructor to construct the shared classes `id` and `text`.
        """
        QuizContent.__init__(self, id, text)    
        self.answer_ids = list(map(int, answer_ids.split(',')))
        self.discipline = discipline.strip()
        self.wiki_topic = wiki_topic.strip()
        self.wiki_href = wiki_href.strip()
        self.advice_text = advice_text.strip()


class Answer(QuizContent):
    """
    A class representing an answer. Inherits from QuizContent.
    ...

    Attributes
    ----------
    id : int
        id of the Question
    text : str
        text content of the Question
    question_id : int
        id of the corresponsing Question
    is_correct : str
    """
    def __init__(self, id, text, question_id, is_correct):
        """
        Constructs all the necessary attributes for the Answer object. Inherits from QuizContent.

        Parameters
        ----------
            id : int
                id of the Answer
            text : str
                text content of the Answer
            question_id : int or str
                id of the corresponsing Question, converted to int by this constructor
            is_correct : str
                string read from CSV containing the text 'TRUE' or 'FALSE', converted to boolean by this constructor                 
        
        Notes
        ----------
            This constructor invokes the parent `QuizContent` constructor to construct the shared classes `id` and `text`.
        """
        QuizContent.__init__(self, id, text)
        self.question_id = int(question_id)
        self.is_correct = bool(is_correct == 'TRUE')