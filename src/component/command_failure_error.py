
class CommandFailureError(Exception):
    ''' Exception for the shell command failure '''
    
    def __init__(self, message):
        super().__init__(message)