from component.base_component import BaseComponent
import os


class Environment(BaseComponent):
    '''
    Environment component handles all Environment and shell commands 
    '''

    def __init__(self):
        ''' Init Environment instance '''

        super().__init__()

    def init(self):
        pass

    def change_directory(self, directory):
        ''' Change the shell to given directory path. The cd command in shell. Note that if directory exists, no error will raise '''
        
        os.chdir(os.path.expanduser(directory))

    def create_directory(self, name, cd_into=False):
        ''' Create a directory in current path '''

        self.run_command(command="mkdir -p "+name)
        # If needed, change path inside the created directory
        if cd_into:
            self.change_directory(name)

    def update_yum(self):
        ''' Excute 'yum update' command '''
        
        self.run_command(command="yum update")
