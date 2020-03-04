from component.base_component import BaseComponent


class BIND(BaseComponent):
    '''
    BIND component handles all BIND commands and DNS works
    '''

    def __init__(self):
        ''' Init BIND instance '''

        super().__init__()

    def init(self):
        self.run_command("yum -y install bind bind-utils")

    def listen_any(self):
        ''' Listen to any IP address '''

        with open('/etc/named.conf', 'r') as file: 
            content = file.read()
            content = content.replace("listen-on port 53 { 127.0.0.1; };","listen-on port 53 { 127.0.0.1; any; };") 

    def set_default(self):
        ''' Sets the default settings '''

        self.listen_any()
        