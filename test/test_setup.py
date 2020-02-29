import unittest 
import subprocess
import sys 
sys.path.insert(1, './src')
from setup import Setup

class SetupTest(unittest.TestCase):
    def test_run_command(self):
        setup = Setup(())
        self.assertTrue(len(setup.run_command(("ls","-la"))[2])==0) 

         
    def test_fail_run_command(self):
        setup = Setup(())
        try:
            setup.run_command(("la","-la"))
            self.fail("Did not fail!? weird...")
        except FileNotFoundError as identifier:
            pass
        


if __name__ == "__main__":
    unittest.main()