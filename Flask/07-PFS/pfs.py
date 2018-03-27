# pfs : problem feedback system

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/feedback/')
def feedback():
    return render_template('post.html')

if __name__ == '__main__':
    app.run()
