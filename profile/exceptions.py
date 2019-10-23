

class Error(Exception):
    pass

class LimitError(Error):
    def __init__(self, limit, message):
        self.limit = limit
        self.message = message

    
class SortError(Error):
    def __init__(self, sort, message):
        self.sort = sort
        self.message = message