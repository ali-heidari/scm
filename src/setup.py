import subprocess
import os
from config import Configuration


class Setup:
    '''
    Setup csm
    '''
    # Declaring variables
    # Private variables
    _configs = ()

    def __init__(self, configs: tuple):
        self._configs = configs

    def run_command(self, command_segments: tuple) -> tuple:
        ''' 
        Run the command using the segments passed as tuple and return Output, Error and returnCode as tuple. 
        It returns (command, output, error, returnCode)
        '''

        proc = subprocess.Popen(
            command_segments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        o, e = proc.communicate()

        return (' '.join(command_segments), o, e, str(proc.returncode))

    def install_package(self, name):
        ''' Install the package '''

        self._yum_install = ['yum', 'install',  name]
        Configuration.print_wrapped(self.run_command(self._yum_install))
        return True

    def install_xampp(self):
        '''  Since XAMPP is not provided with yum, need to be installed manually using *.run file '''

        run_file = "xampp-linux-x64-" + \
            _configs['xampp_version']+"-installer.run"
        self.run_command(
            ["curl", "https://www.apachefriends.org/xampp-files/7.4.2/"+run_file])
        self.run_command(["chmod", "755", run_file])
        self.run_command(["./"+run_file])

    def check_requirements(self):
        ''' Check the required packages
        cUrl, XAMPP
        '''

        self.install_package("curl")
        self.install_xampp()
        if bool(self._configs["install_wordpress"]):
            self.run_command(
                "curl", "-XGET", "https://wordpress.org/latest.tar.gz",  "-o", "wordpress-latest.tar.gz")
            self.run_command("tar", "-xvzf", "wordpress-latest.tar.gz")    
            self.run_command("mv", "wordpress-latest", "/opt/lampp/htdocs/")    

    def run(self):
        ''' Run the setup '''

        os.chdir(os.path.expanduser("~"))
        self.run_command(["mkdir", "csm-x64"])
        os.chdir(os.path.expanduser("~/csm-x64"))
        self.check_requirements()
