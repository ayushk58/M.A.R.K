import psutil
import num2words
import inflect
import functions.Response
import screen_brightness_control as sbc


def contain(data,words):
    for word in words:
        if word in data:
            return True
    return False

class Battery:
    def __init__(self):
        pass
    
    def status(self):
        battery=psutil.sensors_battery()
        functions.Response.say("Your battery is at" + str(battery.percent) + "percent")
        if(battery.percent<30):
            functions.Response.say("The battery is too low Sir, I suggest you should plug it in to avoid shut down of the system")

class Battery_charge:
    def __init__(self):
        pass
    
    def status(self):
        battery=psutil.sensors_battery()
        if(battery.power_plugged):
            functions.Response.say("The system is currently charging sir")
        else:
            functions.Response.say("The System in not connected to any output power source")


class Screen_Brightness:
    def __init__(self):
        pass
    def status(self):
        current=sbc.get_brightness()
        return current

    def Increase(self):
        try:  
            current_brightness=sbc.get_brightness()
            if current_brightness >= 100:
                ("Sorry sir, I can't further increase brightness as it is already in maximum state")
            else:
                sbc.set_brightness('+20')
                functions.Response.say("Brightness Increased")
        except:
            functions.Response.say("Sorry sir, I can't further increase brightness as it is already in maximum state")
    
    def Decrease(self):
        try:
            current_brightness = sbc.get_brightness()
            if current_brightness-20>=0:
                sbc.set_brightness('-20')
            else:
                sbc.set_brightness(0)
            functions.Response.say("Brightness Decreased")
        except:
            functions.Response.say("Sorry sir, I can't further decrease brightness as it is already in minimum state")
    
    def set_brightness(self,data):
        try:
            if data>100 or data<0:
                functions.Response.say("The value is outside the machine's current capacity")
            else:
                if sbc.get_brightness()==data:
                    functions.Response.say("Sorry Sir but the birghtness is already at what you specified")
                else:
                    sbc.set_brightness(data)
                    functions.Response.say("The brightness is set at what you desired sir")
        except:
            functions.Response.say("Some error occured, you can try setting the brightness again")

            
        


    

def System_specs(data):
    if "battery" in data:
        battery=Battery()
        if "status" in data:
            battery.status()
        
    elif contain(data,["charge","charging","power"]):
        battery=Battery_charge()
        battery.status()

    elif "brightness" in data:
        brightness=Screen_Brightness()
        if "status" in data or "current" in data:
            current=brightness.status()
            functions.Response.say("The current brightness is at" + str(current) + "percent")
        elif "increase" in data:
            brightness.Increase()
        elif "decrease" in data:
            brightness.Decrease()
        elif "set" in data:
            data=data.split(" ")
            val=data[-2]
            brightness.set_brightness(val)

    return
