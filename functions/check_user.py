import functions.Response
import os
import time
import random

class UserCheck:
    def __init__(self):
        pass
    def add_user(self,command):
        f=open("functions/Text_file/user.txt","a")
        f.write(command)
        f.close()

    
def rand():
    lines=open("functions/Text_file/greetings.txt","r").read().splitlines()
    greetings=str(random.choice(lines)).split(",")
    return greetings

def check():
    user=UserCheck()
    if (os.stat("functions/Text_file/user.txt").st_size==0):
        functions.Response.say("Greetings Sir, I just checked my database and I can't seem to recognize you")
        functions.Response.say("What should i call you then?please state your name only")
        command=functions.Response.listen()
        user.add_user(command)
        functions.Response.say("Welcome Mister" + command)
    else:
        f=open("functions/Text_file/user.txt")
        name=f.readline()
        greet=rand()
        functions.Response.say(greet[0] + name)
        time.sleep(0.05)
        functions.Response.say(greet[1])
        
