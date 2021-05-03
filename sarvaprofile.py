from flask import *
app = Flask(__name__)

@app.route('/mahabali')
def sarva_profile():
    return render_template('sarvaProfile.html')

if __name__ == '__main__':
    app.run()