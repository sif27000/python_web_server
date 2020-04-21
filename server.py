from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('/index.html')

@app.route('/index_univers.html')
@app.route('/univers')
@app.route('/index.html')
def univers():
    return render_template('/index_univers.html')


@app.route('/works.html')
def works():
    return render_template('/works.html')

@app.route('/about.html')
def about():
    return render_template('/about.html')

@app.route('/contact.html')
def contact():
    return render_template('/contact.html')

@app.route('/components.html')
def components():
    return render_template('/components.html')