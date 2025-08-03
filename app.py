from flask import Flask, render_template, redirect, url_for
from delete_spam import delete_spam, empty_bin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete_spam')
def run_delete_spam():
    delete_spam()
    return redirect(url_for('index'))

@app.route('/empty_bin')
def run_empty_bin():
    empty_bin()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)