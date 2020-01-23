import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    if file != None and file.filename != '':
        path = 'static/' + file.filename
        file.save(path)
        return redirect('/static/' + file.filename)
    else:
        return 'Something happen, cannot upload file. Please try again'
app.run(debug=True)
