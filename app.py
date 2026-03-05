from flask import Flask, render_template, request, redirect, url_for, session # Import flask framework and methods
from validators import validate_form

app = Flask(__name__) 
 
@app.route('/', methods=['GET', 'POST']) 
def start(): 
    """Renders the start page and validates user input"""
    errors = {}
    name = ""
    discipline = ""

    if (request.method == 'POST'):
        errors, valid = validate_form(request.form)
        if errors:
            return render_template(
                "start.html", 
                serviceName="STS knowledge check", 
                title="Start STS knowledge check",
                errors=errors,
                name=name,
                discipline=discipline)
        else:
            return redirect(url_for("question"))
        
    return render_template(
                "start.html", 
                serviceName="STS knowledge check", 
                title="Start STS knowledge check",
                errors=errors,
                name=name,
                discipline=discipline)

@app.route('/question', methods=['GET', 'POST'])
def question():
    """Render question pages sequentially and post user responses"""
    return render_template("question.html", serviceName="STS knowledge check", title="Question")

@app.route('/results', methods=['GET'])
def getResults():
    return render_template("results.html", serviceName="STS knowledge check", title="Results")

if __name__ == '__main__': 
    app.run(debug=True) 