# version 3.0 beta 7 (commited again)
# Added functionality for labeling string during spam operation
# Added functionality for changing the order of spamming (fixed or randomized)
# author Andrew1013

#import pip (this will never be ded)
import pyautogui
import keyboard
import psutil
import time
import os
import platform
import sys
import random
import string
import datetime
import tkinter as tk

module_list = ["pyautogui","keyboard","psutil","time","os","platform","sys","string","datetime","tkinter"]
module_missing = False
for ele in module_list :
    try:       
        __import__(ele)   
    except ImportError as e:
        module_missing = True
        os.system('pip install {}'.format(ele))
        print("module {} installed!".format(ele))
if module_missing == True :
    print("restart the program to use it")
    exit()
else :
    pass

module_list = None

#function lines
def clear_screen() :
    os.system("cls")

def string_label1(string) :
    string = "string : " + string
    return string

def order_change(string1,string2) :
    string_backup = ""
    string_backup = string1
    string1 = string2
    string2 = string_backup
    return string1,string2

def string_label2(string1,string2) :
    string1 = "string1 : " + string1
    string2 = "string2 : " + string2
    return string1,string2

def stats_report() : #statistics reporting (work in progress)
    version = "v3.0b6"
    version_type = "beta"
    os_platform = platform.system()
    os_name = platform.platform()
    current_dir = os.getcwd()
    timeout = cpu_check()
    last_run = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def string1_randgen(length) : #random generator for 1 string
    string1 = ""
    for i in range(1,length+1) :
        string1 += random.choice(string.ascii_letters)
        i += 1
    return string1

def string2_randgen(length1,length2) : #random generator for 2 strings
    string1 = ""
    string2 = ""
    for i in range(1,length1+1) :
        string1 += random.choice(string.ascii_letters)
        i += 1
    for i in range(1,length2+1) :
        string2 += random.choice(string.ascii_letters)
        i += 1
    return string1,string2

def cli_test1(spam_string,n,developer_mode,on_demand_rand,rand_len) : #cli test for 1 string
    for i in range(1,n+1) :
        if on_demand_rand == True : 
            spam_string = string1_randgen(rand_len)
        else : pass

        if developer_mode == True : 
            print(spam_string + " {}".format(i))
        else : 
            print(spam_string)
        i += 1
    return 0

def cli_test2(spam_string1,spam_string2,n,developer_mode,on_demand_rand,rand_len1,rand_len2) : #cli test for 2 string
    for i in range(1,n+1) :
        if on_demand_rand == True :
            spam_string1,spam_string2 = string2_randgen(rand_len1,rand_len2)
        else :
            pass

        if developer_mode == True : 
            print(spam_string1 + " {}".format(i))
            print(spam_string2 + " {}".format(i))
        else : 
            print(spam_string1)
            print(spam_string2)
        i += 1
    return 0

def cpu_check() : #cpu check to determine timeout
    cpu_percent = psutil.cpu_percent(interval=0.1)
    if cpu_percent < 30.0 :
        timeout = 0.1
    elif cpu_percent > 90.0 and cpu_percent <= 100.0 :
        timeout = 1.0
    else :
        timeout = round(((cpu_percent-30)/100),3) + 0.1
    return timeout

def spam1(spam_string,n,developer_mode,on_demand_rand,rand_len) : #spam for 1 string
    start = time.time()
    for i in range(1,n+1) :
        timeout = cpu_check()
        if on_demand_rand == True :
            spam_string = string1_randgen(rand_len)
        else :
            pass

        if developer_mode == True : 
            pyautogui.typewrite(spam_string + " {} \n".format(i))
        else : 
            pyautogui.typewrite(spam_string)
        time.sleep(timeout)
        pyautogui.press("enter")
        timeout = cpu_check()
        i += 1
    end = time.time()
    return round(end - start,2)

def spam2(spam_string1,spam_string2,n,developer_mode,on_demand_rand,rand_len1,rand_len2) : #spam for 2 string
    start = time.time()
    for i in range(1,n+1) :
        timeout = cpu_check()
        if on_demand_rand == True :
            spam_string1,spam_string2 = string2_randgen(rand_len1,rand_len2)
        else :
            pass
        
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
    end = time.time()
    return round(end - start,2)

clear_screen()
#variable inputs
duplication,sus,second_spam,label,on_demand_rand  = False,False,False,False,False
spam_string1,spam_string2,modify_order,modify_order_random = "","","",""
rand_len1,rand_len2 = 0,0
print("Do you want to randomly generate a message or 2?")
print("Type (Yes) to accept and type (No) to cancel")
string1_rand = input("choice : ")
if string1_rand == "Yes" or string1_rand == "YES" or string1_rand == "yes" : string1_rand = True
else : string1_rand = False

if string1_rand == True :
    print("Do you want to randomly generate a second message?")
    print("Note that you can't use the new random order feature when you're only spamming with 1 message")
    print("Type (Yes) to accept and type (No) to cancel")
    string2_rand = input("choice : ")
    if string2_rand == "Yes" or string2_rand == "YES" or string2_rand == "yes" : 
        string2_rand = True
        second_spam = True
    else : 
        string2_rand = False
        second_spam = False
    
    print("Do you want to generate new strings on-demand or generate once?")
    print("Type (Yes) to generate a new string on-demand and (No) to generate once only")
    on_demand_rand = input("choice : ")
    if on_demand_rand == "Yes" or on_demand_rand == "yes" or on_demand_rand == "YES" : on_demand_rand = True
    else : on_demand_rand = False
    
    print("Length for the generation of string1?")
    rand_len1 = int(input("value : "))
    if string2_rand == True :
        print("Length for the generation of string2?")
        rand_len2 = int(input("value : "))

    if on_demand_rand == False and string1_rand == True : 
        spam_string1 = string1_randgen(rand_len1)
    elif on_demand_rand == False and string2_rand == True : 
        spam_string1,spam_string2 = string2_randgen(rand_len1,rand_len2)
    else : 
        pass
else :
    print("What do you want to spam people with?")
    spam_string1 = input("message : ")
    print("Do you want to spam with a second message?")
    print("Note that you can't use the new random order feature when you're only spamming with 1 message")
    print("Type (Yes) to accept or (No) to bypass")
    second_spam = input("Choice : ")
    if second_spam == "yes" or second_spam == "YES" or second_spam == "Yes":
        second_spam = True
        print("What do you want to spam people for the second message with?")
        spam_string2 = input("message : ")
    else : second_spam = False


print("Do you want to label the strings?")
print("Type (Yes) to label the strings or (No) to bypass")
label = input("choice : ")
if label.lower() == "yes" : 
    label = True
else : 
    label = False
print("Do you want to change the order of spamming?")
print("Type (Yes) to accept and (No) to bypass.")
e2 = input("choice : ")
if e2.lower() == "yes" :
    print("Do you want to randomly change the order of spamming or just change it once?")
    print("Type (fixed) to change the order for once only or (random) to randomly change the order")
    modify_order = input("choice : ")

print("How many times do you want to spam?")
n = int(input("number : "))
print("Do you want to duplicate the 2 spam texts into 2 big strings?")
print("Note : if you want to duplicate your string, you will have to settle for generating for once only.")
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
    on_demand_rand = False
    print("How much do you want to duplicate for string1?")
    duplication_times1 = int(input("value : "))
    print("How much do you want to duplicate for string2?")
    duplication_times2 = int(input("value : "))
    
    while duplication_times1 > 0 :
        spam_string1 += spam_string1
        duplication_times1 -= 1
    while duplication_times2 > 0 :
        spam_string2 += spam_string2
        duplication_times2 -= 1
    
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
print()

if modify_order.lower() == "fixed" :
    spam_string1,spam_string2 = order_change(spam_string1,spam_string2)
else :
    pass

if cli_Test == True : 
    if modify_order.lower() == "random" :
        modify_order_choice = ["0","1"]
        modify_order_random = random.choice(modify_order_choice)

    print("CLI Test first")
    if second_spam == True : 
        if modify_order_random == "1" : 
            spam_string1,spam_string2 = order_change(spam_string1,spam_string2)   
        if label == True :
            spam_string1,spam_string2 = string_label2(spam_string1,spam_string2)
        cli_test2(spam_string1,spam_string2,n,sus,on_demand_rand,rand_len1,rand_len2)
    else : 
        if label == True :
            spam_string1 = string_label1(spam_string1)
        cli_test1(spam_string1,n,sus,on_demand_rand,rand_len1)

print("Press E to confirm cleared and ready for spamming")
keyboard.wait('e')  
print("You have 5 seconds to go to your preferred website for the spam machine")
time.sleep(5.0)
print("To stop in an emergency, press Ctrl + C")
time.sleep(2.0)
clear_screen()
print("OK get ready for spam galore boi!")
time.sleep(1.2)

try :    
    if modify_order.lower() == "random" :
        modify_order_choice = ["0","1"]
        modify_order_random = random.choice(modify_order_choice)

    if second_spam == "yes" or second_spam == "YES" or second_spam == "Yes": 
        if modify_order_random == "1" : 
            spam_string1,spam_string2 = order_change(spam_string1,spam_string2)    
        if label == True :
            spam_string1,spam_string2 = string_label2(spam_string1,spam_string2)
        time_executed = spam2(spam_string1,spam_string2,n,sus,on_demand_rand,rand_len1,rand_len2)
    else : 
        if label == True :
            spam_string1 = string_label1(spam_string1)
        time_executed = spam1(spam_string1,n,sus,on_demand_rand,rand_len1)
    
    if sus == True : print("time for execution : {} seconds".format(time_executed))
except :
    print("emergency exit")
    if sus == True : print("time for execution : {} seconds".format(time_executed))
    exit()

#watch some Jenny Huynh son
#link : https://www.youtube.com/watch?v=I7epHzh0q_w
