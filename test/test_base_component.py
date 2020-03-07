import unittest 
import subprocess
import sys 
sys.path.insert(1, './src/')
from component import *
from child_class import ChildClass

class BaseComponentTest(unittest.TestCase):

    child_class = ChildClass()

    def test_run_command(self):
        self.assertTrue(len(self.child_class.run_command("ls -la")[2])==0) 


    def test_fail_run_command(self):
        ''' Test invalid command '''
        try:
            self.assertFalse(len(self.child_class.run_command(("la"))[2])==0) 
            self.fail("It didn't raise exception? Weird!?")
        except command_failure_error.CommandFailureError as error:
            pass
        


if __name__ == "__main__":
    unittest.main()