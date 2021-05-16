from flask import Flask, render_template
from flask_cors import CORS
import logging
app = Flask(__name__)
CORS(app)

@app.route('/')
def entry_point():
    return render_template('acceuil.html')

@app.route('/hello_world')
def hello_world():
    # logging.info("Lancement Hello_word" )
    print("Hello Simplon World")

@app.route('/register')
def new_user():
    return render_template("profil.html")

# @app.route('/new')
# def profil():


if __name__=="__main__":
    app.run(debug=True)