import speech_recognition as sr 
import random
import functions.Response as speech
import functions.device_stats
import num2words
import sys,os
import functions.check_user
from functions.Response import say,listen
from datetime import datetime
import functions.Time
import functions.web_search
import webbrowser

webbrowser.register('chrome',
	            None,
	            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                

def pre_initial():
    say("Starting Program")
    say("Initializing modules")
    say("Performing System Checks")
    say("Modules Intialized")
    say("System Checks Done")
    say("Starting happy protocol")
    
def contain(data,words):
    for word in words:
        if word in data:
            return True
    return False

def word2num(data):
    num={"first":1,"Second":2,"third":3,"four":4,"five":5}
    return num[data]

def digital_assistant(data):
    if contain(data,["Mark","mark","hey mark","hi","hello"]):
        if contain(data,["battery","status","charge","charging","current","brightness"]):
            functions.device_stats.System_specs(data)

        elif contain(data,["date","time","year","month","day"]):
            functions.Time.time_check(data)

        elif "open" in data or "start" in data:
            functions.browser.Open_Browser(data)
    
        elif "search" in data:
            functions.web_search.Search(data)
    