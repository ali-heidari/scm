
class Configuration:
    def __init__(self):
        super().__init__()

    # Wrap several messages between sequences of *, to distinguish from other prints
    @staticmethod
    def print_wrapped(messages: tuple):
        print("*****************************\t"+messages[0])
        for message in messages[1:]:
            print(message)
        print("********************************************************\n")
