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
print("You have 5 seconds to go to your preferred website for the spam machine")
time.sleep(5)
print("To stop in an emergency, press E")
time.sleep(2)
os.system('cls')
print("OK get ready for spam galore boi!")
time.sleep(1.2)
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
    #emergency execution code
    if keyboard.is_pressed("e") == True :
        exit()
    else :
        continue
