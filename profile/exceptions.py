

class LimitError(Exception):
    def __init__(self, limit, message):
        self.limit = limit
        self.message = message

    
class SortError(Exception):
    def __init__(self, sort, message):
        self.sort = sort
        self.message = message