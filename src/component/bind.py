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
