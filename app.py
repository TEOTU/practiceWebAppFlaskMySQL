'''
About the project: It's just a practice thing for me to learn how websites are built.
 Here I use:
 Flask
 HTML, CSS
 BootStrapping
 Dynamic Data using templates
'''
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'AI Scientist Engineer',
        'location': 'Ukraine, Kiev',
        'salary': 'Not needed'
    },
    {
        'id': 2,
        'title': 'Unemployed',
        'location': 'The Earth',
    }]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Michael's")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
