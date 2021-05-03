from flask import *
app = Flask(__name__)

#get method
@app.route('/login/get', methods = ['POST','GET'])
def login_get():
    if request.method == ['GET']:
        uname = request.args.get('uname')  
        passwrd = request.args.get('upass') 
        if uname == "harsh" and passwrd == "harsh":  
            return f"<html><body>Welcome %s"%uname 
        else:
            return "<html><body>invalid login</body></html>" 
    else:
        return render_template('login.html')

#post method
@app.route("/login/post", methods = ['POST', 'GET'])
def post_login():
    if request.method == ['POST']:
        if request.form['uname'] == 'appa' and request.form['pass'] == 'appa':
            return "Welcome %s"%request.form['uname']
        else:
            return "invalid entry"
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run()