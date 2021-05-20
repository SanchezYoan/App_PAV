from flask import Flask
import logging
from .functions import user_account

app = Flask(__name__)

@app.route('/')
def main():
    return user_account.hello()


if __name__ == '__main__':
    logging.basicConfig(filename="prog.log", level=logging.DEBUG)
    app.run(host='0.0.0.0',port=5000, debug=True, use_reloader=True)