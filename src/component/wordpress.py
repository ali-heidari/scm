from component.base_component import BaseComponent


class Wordpress(BaseComponent):
    '''
    Wordpress component handles all Wordpress commands
    '''

    def __init__(self):
        ''' Init Wordpress instance with provided user and password '''
        super().__init__()

    def init(self):
        self.install()

    def install(self):
        self.run_command(
            "curl -XGET https://wordpress.org/latest.tar.gz -o wordpress-latest.tar.gz")
        self.run_command("tar -xvzf wordpress-latest.tar.gz")
        self.run_command("mv wordpress-latest /opt/lampp/htdocs/")
        
