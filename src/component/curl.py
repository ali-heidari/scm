from component.base_component import BaseComponent


class CURL(BaseComponent):
    '''
    CURL component handles all CURL commands and network requests
    '''

    def __init__(self):
        ''' Init CURL instance '''

        super().__init__()

    def init(self):
        self.run_command("yum -y install curl")
