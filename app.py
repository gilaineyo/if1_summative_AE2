from flask import Flask, render_template, request, redirect, url_for, session # Import flask framework and methods
from config import Config # Import secret to enable session
from validators import validate_form, validate_question # Import user input validation method
from content.quiz_repository import QuizRepository # Import quiz repository for retrieving and processing content to and from CSV 

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY 
 
@app.route('/', methods=['GET', 'POST']) 
def start(): 
    """Renders the start page and validates user input"""
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
    """Render question pages sequentially and post user responses"""
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

if __name__ == '__main__': 
    app.run(debug=True) 