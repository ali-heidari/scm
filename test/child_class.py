
# import sys 
# sys.path.insert(1, './src')
from component.base_component import BaseComponent


class ChildClass(BaseComponent):
    ''' A child class with absolute nothing to do. Can be used in tests   '''

    def __init__(self):
        ''' Init '''

        super().__init__()
        
    def init(self):
        pass