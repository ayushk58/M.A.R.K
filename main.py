from assistant import contain,pre_initial,digital_assistant
import os
from functions.Response import say,listen
import functions.check_user
import functions.device_stats
import functions.browser
import time

if __name__=="__main__":
    functions.check_user.check()
    while True:
        data=listen().lower()
        if (data==0):
            continue
        if contain(data,["shut down","kill","stop","sleep"]):
            say("I am going to sleep Sir, Have a good day")
            break
        digital_assistant(data)
        time.sleep(2)

        
            
            
            
