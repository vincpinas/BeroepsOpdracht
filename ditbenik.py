# Install tqdm voor volle gebruik van dit programma dat doe je door de volgende command in je terminal in te voeren: pip intall tqdm
# Geniet er van.
 
import os

os.system('cls')    				

print("Hello You!, ik ben Vincent")

print("What's your first name?")  
naam = input()

os.system('cls')

print("Hello", naam[0] .upper() + naam[1:].lower() + "!")

import time
time.sleep(1)

print("What is your surname?")
achternaam = input()

os.system('cls')

print("Wow" + " " + naam[0] .upper() + naam[1:].lower() + " " + achternaam[0] .upper() + achternaam[1:].lower() + " " + "what a nice name!")

time.sleep(2.4)

datum = time.asctime()
print("the current time is:", datum)
time.sleep(2.1)
os.system('cls')

print("I am new to Media College Amsterdam, by answering a few questions you will get to know me a little better.")
time.sleep(2)
print("Let's start with a simple test to see if everything is working right.")
time.sleep(2)
os.system("cls")


raw_input=input

while True:
    # Welcome question
    while True:
        answer = raw_input("Did you eat breakfast today" + " " + naam[0] .upper() + naam[1:].lower() + " " + achternaam[0] .upper() + achternaam[1:].lower() + "? [y/n]: ")
        if answer in ('y', 'Y') or ('n', 'N'):
            break
    if answer == 'y' or answer == 'Y':
        print("Wonderful, remember that breakfast is the most important meal of the day!")
        time.sleep(2.2)
        os.system("cls")
        break
    elif answer == 'n' or answer == 'N':
        print("Oh that's a shame don't forget that breakfast is the most important meal of the day!")
        time.sleep(2.2)
        os.system("cls")
        break
    else:
        print('Invalid input.')


print("Okay, now that we know everything is working right we can move on to the multiple choice questions.")
time.sleep(2.2)
os.system("cls")

while True:
    # Question A
    while True:
        print("Before I came to Media College Amsterdam I went to....")
        print("A: Veenlanden College Mijdrecht.")
        print("B: Alkwin College.")
        print("C: Amstelveen College")
        answer = raw_input("Pick one option" + " " + naam[0] .upper() + naam[1:].lower() + " " + "[A/B/C]: ")
        if answer in ('a', 'A') or ('b', 'B') or ('c', 'C'):
            break
    if answer == 'a' or answer == 'A':
        time.sleep(0.3)
        print("YES! I did go to Veenlanden College Mijdrecht for my last 3 years and got my diploma there for MAVO.")
        break
    elif answer == 'b' or answer == 'B':
        time.sleep(0.3)
        print("Hmm, although I did go there it was only for my first year after which I went to a different school.")
        break
    elif answer == 'c' or answer == 'C':
        time.sleep(0.3)
        print("This was one of my first options but I didn't actually go there.")
        break
    else:
        print("Invalid input.")

time.sleep(2)
os.system("cls")

while True:
    # Question B
    while True:
        answer = raw_input("Pick one option" + " " + naam[0] .upper() + naam[1:].lower() + " " + "[A/B/C]: ")
        if answer in ('a', 'A') or ('b', 'B') or ('c', 'C'):
            break
    if answer == 'a' or answer == 'A':
        time.sleep(0.3)
        print(".")
        break
    elif answer == 'b' or answer == 'B':
        time.sleep(0.3)
        print(".")
        break
    elif answer == 'c' or answer == 'C':
        time.sleep(0.3)
        print(".")
        break
    else:
        print("Invalid input.")

time.sleep(2)
os.system("cls")

while True:
    # Question C
    while True:
        answer = raw_input("Pick one option" + " " + naam[0] .upper() + naam[1:].lower() + " " + "[A/B/C]: ")
        if answer in ('a', 'A') or ('b', 'B') or ('c', 'C'):
            break
    if answer == 'a' or answer == 'A':
        time.sleep(0.3)
        print(".")
        break
    elif answer == 'b' or answer == 'B':
        time.sleep(0.3)
        print(".")
        break
    elif answer == 'c' or answer == 'C':
        time.sleep(0.3)
        print(".")
        break
    else:
        print("Invalid input.")

time.sleep(2)
os.system("cls")


print("ONE MOMENT PLEASE.")
time.sleep(1.2)
# Loading screen
from tqdm import tqdm
for i in tqdm(range(0, 100), desc="Loading", unit="bit"): 
    time.sleep(0.04)
time.sleep(0.8)
os.system("cls")


while True:
    # Restart Loop
    while True:
        answer = raw_input("Do you want to restart this program" + " " + naam[0] .upper() + naam[1:].lower() + " " + achternaam[0] .upper() + achternaam[1:].lower() + "? [y/n]: ")
        if answer in ('y', 'Y') or ('n', 'N'):
            break
    if answer == 'y' or answer == 'Y':
        os.system("cls")
        time.sleep(1)
        os.system("ditbenik.py")
    elif answer == 'n' or answer == 'N':
        print('Goodbye :(')
        time.sleep(1.6)
        os.system("taskkill /IM cmd.exe")
        break
    else:
        print('Invalid input.')

        