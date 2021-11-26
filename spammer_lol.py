#spam machine ver2.1
#author : Andrew 1013

import pyautogui
import keyboard
import psutil
import time
import os

duplication = bool()
spam_string = str()
timeout = None

print("What do you want to spam people with?")
spam = input("")
print("Time between messages?")
time_between_message = input("")

if float(time_between_message) / 1 == 0:
    time_between_message = int(time_between_message)
else :
    time_between_message = float(time_between_message)

print("Do you want to duplicate the spam text into a big string?")
print("Type (True) to confirm, (False) to bypass this, or (elando) to go into developer mode (add a counter to the string)")

e = input("Choice : ")
if e =="True" or e == "true" or e == "TRUE" :
    duplication = True
elif e == "False" or e == "false" or e == "FALSE" :
    duplication = False
elif e == "elando" or e == "ELANDO" :
    sus = True
else :
    print("you sus")
    duplication = False
    sus = False

print("Do you want to test spam it on the CLI (command line interface) first?")
print("Type (True) to confirm, (False) to bypass this")
e = input("Choice : ")
if e =="True" or e == "true" or e == "TRUE" :
    cli_test = True
elif e == "False" or e == "false" or e == "FALSE" :
    cli_test = False
else :
    print("you sus")
    cli_test = False

time.sleep(0.2)
if duplication == True :
    print("How many times do you want to duplicate? please type a number less than or equal 30 lol.")
    duplication_times = input("")
    if duplication_times.isdigit() == True :
        spam_string_list = []
        if int(duplication_times) > 30 :
            print("Too high, exiting...")
            time.sleep(0.2)
            exit()
        else :
            for i in range(0,int(duplication_times)+1) :
                spam_string_list.append(spam)
                spam_string_list.append(" ")
                i += 1
            spam_string = spam_string.join(spam_string_list)
    else :
        print("Invaild input,exiting...")
        time.sleep(0.2)
        exit()
else :
    spam_string = spam

print("How many times do you want to spam people?")
n = int(input(""))
print("Caution!")
print("Use this tool with responsibility lol.")
print("OK, Initiating...")
time.sleep(0.2)
print("")
print("Ok done!")
print("Press N to confirm.")
keyboard.wait('n')
if cli_test == True :
    print("CLI test first")
    for i in range(1,n+1) :
        if sus == True :
            spam_string = spam + " " + str(i)
        else :
            spam_string = spam
        print(spam_string)
        i += 1
else :
    pass
print("Press E to confirm cleared and ready for spamming")
keyboard.wait('e')  
print("You have 5 seconds to go to your preferred website for the spam machine")
time.sleep(5)
print("To stop in an emergency, press Ctrl + C")
time.sleep(2)
os.system('cls')
print("OK get ready for spam galore boi!")
time.sleep(1.2)
try :
    for i in range(1,n+1) :
        if sus == True :
            spam_string = spam + " " + str(i)
        else :
            spam_string = spam
        #check for cpu usage 1
        cpu_percent = psutil.cpu_percent()
        if cpu_percent < 60.0 :
            timeout = 0.01 
        else :
            if cpu_percent >= 97.0 :
                print("CPU usage too high!")
            else :
                timeout = cpu_percent / 100 - 0.3
        # main code of the spam
        pyautogui.typewrite(spam_string)
        time.sleep(time_between_message)
        pyautogui.press("enter")
        time.sleep(timeout)
        i += 1
        #check for cpu usage 2
        cpu_percent = psutil.cpu_percent()
        if cpu_percent < 60.0 :
            timeout = 0.01 
        else :
            if cpu_percent >= 97.0 :
                print("CPU usage too high!")
            else :
                timeout = cpu_percent / 100 - 0.3
        i += 1
except KeyboardInterrupt :
    print("emergency exit")
    exit()
    
