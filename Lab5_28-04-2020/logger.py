"""
Message logging.

Authors:
 Bartłomiej Piekarz
 Daniel Tańcula
 Tomasz Piaseczny
"""


class Logger:

    DEBUG = 0
    INFO = 1
    MESSAGE = 2

    def __init__(self, mode):
        self.mode = mode

    def msg(self, msg):
        if self.mode <= self.MESSAGE:
            print(msg)

    def info(self, msg):
        if self.mode <= self.INFO:
            print("[INFO]: " + msg)

    def debug(self, msg):
        if self.mode <= self.DEBUG:
            print("[DEBUG]: " + msg)
