from component import curl, xampp, environment, bind
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

        # Update yum
        self._environment_instance.update_yum()

        curl_instance = curl.CURL()
        xampp_instance = xampp.XAMPP(
            self._configs["xampp_version"], self._configs["mysql_root_password"])

        if bool(self._configs["install_wordpress"]):
            xampp_instance.init_wordpress(
                self._configs["wp_db_user"], self._configs["wp_db_password"])

        if bool(self._configs["setup_dns_server"]):
            bind_instance=bind.BIND()
                

    def run(self):
        ''' Run the setup '''

        # Create a directory for SCM
        self._environment_instance = environment.Environment()
        self._environment_instance.create_directory(
            name="/var/csm-x64", cd_into=True)
        # Install and initialize the required tools    
        # self.install_requirements()
