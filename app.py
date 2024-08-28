from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/preview')
def preview():
    return render_template('preview.html')

@app.route('/merge')
def merge():
    return render_template('fusion.html')

@app.route('/organize')
def organize():
    return render_template('reorganization.html')

@app.route('/conflicts')
def conflicts():
    return render_template('conflict.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/clean')
def clean():
    return render_template('cleaning.html')

if __name__ == '__main__':
    app.run(debug=True)
