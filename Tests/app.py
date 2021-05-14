from flask import Flask
from flask_cors import CORS
import logging
app = Flask(__name__)
CORS(app)

@app.route('/')
def entry_point():
    return render_template('acceuil.html')

@app.route('/hello_world')
def hello_world():
    logging.info("Lancement Hello_word" )
    print("Hello Simplon World")
    