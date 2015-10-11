from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)
