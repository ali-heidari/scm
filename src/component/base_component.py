from abc import ABC, abstractmethod
import subprocess
from component.command_failure_error import CommandFailureError

class BaseComponent(ABC):
    '''
    Abstract class for components 
    '''

    def __init__(self):
        self.init()

    @abstractmethod
    def init(self):
        pass

    def run_command(self, command) -> tuple:
        ''' 
        Run the command using the segments passed as tuple and return Output, Error and returnCode as tuple. 
        It returns (command, output, error, returnCode)
        '''

        proc = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        o, e = proc.communicate()

        print(command)
        # print(o)
        if e:
            print(e)
            raise CommandFailureError(e)

        return (command, o, e, str(proc.returncode))
