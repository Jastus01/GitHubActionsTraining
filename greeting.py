class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")

greeting = Greeting("Dominic")

greeting.say_hello()
