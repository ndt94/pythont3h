from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    name = request.args.get('name') # args dung cho GET
    gender = request.args.get('gender')
    return render_template('hello.html', name=name, gender=gender)

@app.route('/hello2', methods=['POST'])
def hello2():
    name = request.form.get('name') # form dung cho POST
    gender = request.form.get('gender')
    return render_template('hello.html', name=name, gender=gender)
app.run(debug=True)