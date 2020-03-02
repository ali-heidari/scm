from component import curl,xampp
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

    def install_requirements(self):
        ''' Install the required packages
        cUrl, XAMPP, wordpress
        '''

        curl_instance = curl.CURL("curl")
        xampp_instance = xampp.XAMPP(
            self._configs["xampp_version"], self._configs["mysql_root_password"])

        if bool(self._configs["install_wordpress"]):
            xampp_instance.init_wordpress(
                self._configs["wp_db_user"], self._configs["wp_db_password"])

    def run(self):
        ''' Run the setup '''

        os.chdir(os.path.expanduser("~"))
        self.run_command("mkdir csm-x64")
        os.chdir(os.path.expanduser("~/csm-x64"))
        self.install_requirements()
