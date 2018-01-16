class M2VException(BaseException):
    def __init__(self, message):
        self.message = message
