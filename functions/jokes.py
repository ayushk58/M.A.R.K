import pyjokes
import functions.Response

class Jokes:
    def __init__(self):
        pass
    def jokes(self):
        jk=str(pyjokes.get_joke(language="en",category="all"))
        functions.Response.say(jk)


def tell_joke():
    joke=Jokes()
    joke.jokes()

