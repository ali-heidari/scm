from component import curl, xampp, environment
from config import Configuration


class Setup:
    '''
    Setup csm
    '''
    # Declaring variables
    # Private variables
    _configs = ()
    _environment_instance: environment.Environment = None

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

        self._environment_instance = environment.Environment()
        self._environment_instance.create_directory(
            name="~/csm-x64", cd_into=True)
        self.install_requirements()
