from flask import Flask, render_template, request, redirect, url_for, session # Import flask framework and methods
from config import Config # Import secret to enable session
from validators import validate_form, validate_question # Import user input validation method
from content.quiz_repository import QuizRepository # Import quiz repository for retrieving and processing content to and from CSV 

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY 
 
@app.route('/', methods=['GET', 'POST']) 
def start(): 
    '''
    Renders the start page and validates user input.

            Parameters:
                    none

            Returns:
                    str: rendered HTML for start page
    '''
    errors = {}

    if (request.method == 'POST'):
        errors, valid = validate_form(request.form)
        if errors:
            return render_template(
                "start.html", 
                serviceName="STS knowledge check", 
                title="Start STS knowledge check",
                errors=errors)
        else:
            session["name"] = valid["name"]
            session["discipline"] = valid["discipline"]
            session["submitted_answers"] = []
            return redirect(url_for("question", index=1))
    
    return render_template(
                "start.html", 
                serviceName="STS knowledge check", 
                title="Start STS knowledge check",
                errors=errors)

@app.route('/question/<int:index>', methods=['GET', 'POST'])
def question(index):
    '''
    Renders the questions pages and processes answer submissions.

    The GET method returns rendered HTML for the appropriate question page.
    
    The POST response validates the answer selection input, returning the rendered HTML with error components if invalid.

    If the input is valid, the function stores the submitted answer in the session, increments the index and determines whether to redirect back to this route for the next question (if one exists) or redirect to the results page if all questions answered.

            Parameters:
                    index(int): index of the question to be displayed (starting at 1 for url readability)

            Returns:
                    str or flask.wrappers.Response: either rendered HTML for question page or redirect response for next indexed question page or results page
    '''
    quiz = QuizRepository("questions.csv", "answers.csv")
    user_questions, user_answers = quiz.get_questions_and_answers_for_user(session["discipline"])

    current_question = user_questions[int(index)-1]

    current_answers = {}
    for answer in user_answers:
        if answer.question_id == current_question.id:
            current_answers[str(answer.id)] = answer

    if (request.method == 'POST'):
        error = validate_question(request.form)
        if error:
            return render_template("question.html", 
                            serviceName="STS knowledge check", 
                            title="Question",
                            questionText=current_question.text,
                            questionId=current_question.id,
                            answers=current_answers,
                            error=error,
                            index=index
                            )
        else:
            submitted_answers = session.get("submitted_answers", [])
            submitted_answers.append(request.form.get("answerInput"))
            session["submitted_answers"] = submitted_answers
            new_index = int(index) + 1
            if new_index > len(user_questions):
                return redirect(url_for('results'))
            return redirect(url_for('question', index=new_index)) 
            

    return render_template("question.html", 
                           serviceName="STS knowledge check", 
                           title="Question",
                           questionText=current_question.text,
                           questionId=current_question.id,
                           answers=current_answers,
                           index=index
                           )

@app.route('/results', methods=['GET'])
def results():
    '''
    Processes answers given and renders the results page.

    Gets each question and answer based on the submitted answer ids stored in session and creates a list of each question and answer in order.

    Adds a point to the `correct` count for each correct answer based on its is_correct attribute. Passes information to the QuizRepository to write results to CSV.

            Parameters:
                    none

            Returns:
                    str: rendered HTML for results page
    '''
    answer_ids = session["submitted_answers"]
    quiz = QuizRepository("questions.csv", "answers.csv")

    questions_with_answers = []
    for id in answer_ids:
        question, answer = quiz.get_question_answer_by_answer_id(int(id))
        questions_with_answers.append({ "question": question, "answer": answer })

    total_questions = len(questions_with_answers)
    correct = 0
    for item in questions_with_answers:
        if item["answer"].is_correct == True:
            correct = correct + 1

    quiz.write_results_to_csv(session["name"], session["discipline"], correct, total_questions)

    return render_template("results.html", 
                           serviceName="STS knowledge check", 
                           title="Results",
                           correct=correct,
                           total_questions=total_questions,
                           questions_with_answers=questions_with_answers)

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template("error.html", e=e), 500
    
if __name__ == '__main__': 
    app.run(debug=True) 