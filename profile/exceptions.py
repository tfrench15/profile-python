

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, limit, message):
        self.limit = limit
        self.message = message

    