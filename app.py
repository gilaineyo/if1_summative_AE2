from flask import Flask, render_template # Import flask framework

app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    return render_template("start.html", serviceName="STS knowledge check", title="Start STS knowledge check")

@app.route('/question')
def getQuestion():
    return render_template("question.html", serviceName="STS knowledge check", title="Question")

if __name__ == '__main__': 
    app.run(debug=True) 