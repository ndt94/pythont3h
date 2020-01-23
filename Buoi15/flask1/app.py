from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/hello/<name>')

def hello(name):
    return render_template('hello.html', name=name)

@app.route('/hello2')
def hello2():
    name = request.args.get('name', '')
    gender = request.args.get('gender')
    return render_template('hello.html', name=name, gender=gender)

@app.route('/students')

def getStudents():
    students = [
        {'id': 1, 'name': 'Student 1'},
        {'id': 2, 'name': 'Student 2'},
    ]
    return render_template('students.html', students=students)
app.run(debug=True)