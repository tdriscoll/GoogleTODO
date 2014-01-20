
class MissingTaskException(Exception): pass

class EmailCreator(object):

    def __init__(self, task):
        pass
    
    def run(self):
        raise MissingTaskException()