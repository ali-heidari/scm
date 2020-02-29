# Load packages
from setup import Setup
from config import Configuration
import yaml

def show_intro():
    ''' Show a message for introduction of SCM '''
    Configuration.print_wrapped(("The SCM", "Simple Cent-os Management"))


def load_configs():
    ''' Load YAML configuration file '''
    with open('config.yml', 'r') as file:
        configs = yaml.load(file, Loader=yaml.Loader)
        messages = ["Configs"] 
        for item in configs:
            messages.append(item + ": " + str(configs[item]))
        Configuration.print_wrapped(messages)
        return configs


if __name__ == "__main__":
    show_intro()
    setup = Setup(load_configs())
    setup.run()
