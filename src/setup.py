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
            self._configs["xampp"]["version"], self._configs["mysql"]["root_password"])

        if bool(self._configs["mysql"]["install"]):
            xampp_instance.init_wordpress(
                self._configs["wordpress"]["db_user"], self._configs["wordpress"]["db_password"])

        if bool(self._configs["dns_server"]["setup"]):
            bind_instance=bind.BIND()
            bind_instance.set_default()
            bind_instance.add_domain(self._configs["domain"],self._configs["ip"])
                

    def run(self):
        ''' Run the setup '''

        # Create a directory for SCM
        self._environment_instance = environment.Environment()
        self._environment_instance.create_directory(
            name="~/scm-x64", cd_into=True)
        # Install and initialize the required tools    
        self.install_requirements()
