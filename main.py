# Load packages
import src.config
import yaml 

# Show a message for introduction of SCM
def show_intro():
    print("The SCM")
    print("Simple Cent-os Management")

# Load YAML configuration file
def load_configs():
    with open('config.yml','r') as file:
        configs = yaml.load(file, Loader=yaml.Loader)
        for item in configs:
            print(item + ": "+ str(configs[item]))


if __name__ == "__main__":
    show_intro()
    load_configs()