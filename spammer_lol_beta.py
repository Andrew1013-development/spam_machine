#version 3.0 beta 3
#added more functionailty for spamming 2 different messages
#author Andrew1013

import pyautogui
import keyboard
import psutil
import time
import os

#function lines
def cli_test1(spam_string,n,developer_mode) :
    for i in range(1,n+1) :
        if developer_mode == True : print(spam_string + " {}".format(i))
        else : print(spam_string)
        i += 1
    return 0

def cli_test2(spam_string1,spam_string2,n,developer_mode) : 
    for i in range(1,n+1) :
        if developer_mode == True : 
            print(spam_string1 + " {}".format(i))
            print(spam_string2 + " {}".format(i))
        else : 
            print(spam_string1)
            print(spam_string2)
        i += 1
    return 0

def cpu_check() :
    cpu_percent = psutil.cpu_percent()
    cpu_too_high = 0
    if cpu_percent < 60.0 :
        timeout = 0.01 
    else :
        if cpu_percent >= 97.0 :
            print("CPU usage too high!")
            cpu_too_high += 1
        else :
            timeout = cpu_percent / 100 - 0.3
    if cpu_too_high == 10 :
        print("CPU usage too high")
        pyautogui.typewrite("say goodnight")
        pyautogui.press('enter')
        print("goodnight")
        exit()
    else :
        return timeout

def spam1(spam_string,n,developer_mode) :
    for i in range(1,n+1) :
        timeout = cpu_check()
        if developer_mode == True : 
            pyautogui.typewrite(spam_string + " {} \n".format(i))
        else : 
            pyautogui.typewrite(spam_string)
        time.sleep(timeout)
        pyautogui.press("enter")
        timeout = cpu_check()
        i += 1
    return 0

def spam2(spam_string1,spam_string2,n,developer_mode) :
    for i in range(1,n+1) :
        timeout = cpu_check()
        if developer_mode == True :
            pyautogui.typewrite(spam_string1 + " {} \n".format(i))
            pyautogui.typewrite(spam_string2 + " {} \n".format(i))
        else :
            pyautogui.typewrite("{} \n".format(spam_string1))
            pyautogui.typewrite("{} \n".format(spam_string2))
        time.sleep(timeout)
        pyautogui.press("enter")
        timeout = cpu_check()
        i += 1
    return 0

#variable inputs
duplication = False
sus = False
print("What do you want to spam people with?")
spam_string1 = input("message : ")
print("Do you want to spam with a secon message?")
second_spam = input("Choice : ")
if second_spam == "yes" or second_spam == "YES" :
    print("What do you want to spam people for the second message with?")
    spam_string2 = input("message : ")
else : pass
print("How many times do you want to spam?")
n = int(input("number : "))
print("Do you want to duplicate the 2 spam texts into 2 big strings?")
print("Type (True) to confirm, (False) to bypass this, or (elando) to go into developer mode (add a counter to the string)")
e = input("Choice : ")
if e =="True" or e == "true" or e == "TRUE" : duplication = True
elif e == "False" or e == "false" or e == "FALSE" : duplication = False
elif e == "elando" or e == "ELANDO" : sus = True
else :
    print("you sus")
    duplication = False
    sus = False
if duplication == True :
    print("How much do you want to duplicate the string?")
    duplication_times = int(input(""))
    while duplication_times > 0 :
        spam_string1 = "{} {}".format(spam_string1)
        spam_string2 = "{} {}".format(spam_string2)
        duplication_times -= 1
print("Do you want to test spam it on the CLI (command line interface) first?")
print("Type (True) to confirm, (False) to bypass this")
e = input("Choice : ")
if e =="True" or e == "true" or e == "TRUE" : cli_Test = True
elif e == "False" or e == "false" or e == "FALSE" : cli_Test = False
else :
    print("you sus")
    cli_Test = False

print("Caution!")
print("Use this tool with responsibility lol.")
print("OK, Initiating...")
time.sleep(0.2)
print("")
print("Ok done!")
print("Press N to confirm.")
keyboard.wait('n')
if cli_Test == True : 
    print("CLI Test first")
    if second_spam == True :
        cli_test2(spam_string1,spam_string2,n,sus)
    else :
        cli_test1(spam_string1,n,sus)
print("Press E to confirm cleared and ready for spamming")
keyboard.wait('e')  
print("You have 5 seconds to go to your preferred website for the spam machine")
time.sleep(5.0)
print("To stop in an emergency, press Ctrl + C")
time.sleep(2.0)
os.system('cls')
print("OK get ready for spam galore boi!")
time.sleep(1.2)
try :
    start = time.time()
    if second_spam == "yes" or second_spam == "YES" :
        spam2(spam_string1,spam_string2,n,sus)
    else :
        spam1(spam_string1,n,sus)
    end = time.time()
    time_executed = round(end - start,2)
    if sus == True :
        print("time used for execution : {} seconds".format(time_executed))
except KeyboardInterrupt :
    print("emergency exit")
    end = time.time()
    time_executed = round(end - start,2)
    if sus == True :
        print("time used for execution : {} seconds".format(time_executed))
    exit()
finally :
    end = time.time()
    time_executed = round(end - start,2)
    if sus == True :
        print("time used for execution : {} seconds".format(time_executed))
