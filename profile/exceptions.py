

class LimitError(Exception):
    """ LimitError is raised when bad input is passed to the limit parameter. """
    def __init__(self, limit, message):
        self.limit = limit
        self.message = message

    
class SortError(Exception):
    """ SortError is raised when bad input is passed to the sort parameter. """
    def __init__(self, sort, message):
        self.sort = sort
        self.message = message