from flask import Flask, render_template # Import flask framework

app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    return render_template("test.html", title="Test") 
 
if __name__ == '__main__': 
    app.run(debug=True) 