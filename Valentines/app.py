from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question')
def question():
    return render_template('question.html')

if __name__ == '__main__':
    app.run(debug=True)
