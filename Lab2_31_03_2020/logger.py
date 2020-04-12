class Logger:

    DEBUG = 0
    INFO = 1

    def __init__(self, mode):
        self.mode = mode

    def log_info(self, msg):
        if self.mode >= self.INFO:
            print("[INFO]: " + msg)

    def log_debug(self, msg):
        if self.mode >= self.DEBUG:
            print("[DEBUG]: " + msg)