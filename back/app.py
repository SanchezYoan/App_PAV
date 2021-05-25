from flask import Flask
import logging
import os
from .functions import user_account

app = Flask(__name__)

@app.route('/')
def main():
    return user_account.hello()


if __name__ == '__main__':
    logging.basicConfig(filename="prog.log", level=logging.DEBUG)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)