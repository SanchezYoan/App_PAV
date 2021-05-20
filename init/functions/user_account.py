import sys
import logging



def hello():
    """
    fonction test hello world
    """
    logging.info("lancement fonction hello")
    return "Hello Simplon !"


if __name__ == "__main__":
    logging.basicConfig(filename="prog.log", level=logging.DEBUG)
    sys.exit()
    