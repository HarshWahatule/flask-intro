from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return 'about run'

@app.route('/post/<day>')
def get_post(day):
    query = f'Select * from table where day = {day}'
    return query

@app.route('/calc/<int:num1>/<int:num2>')
def calc(num1,num2):
    return f'<h1> sum : {num1 + num2} <br> difference : {num1 - num2} <br> product : {num1 * num2} <br> quotient : {num1 / num2}</h1>'

@app.route('/table/<int:num>')
def print_table(num):
    return render_template('table.html',num=num*num)


if __name__ == '__main__':
    app.run()