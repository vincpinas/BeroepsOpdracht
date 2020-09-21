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
        print("Before I came to Media College Amsterdam I went to")
        print("A: Veenlanden College Mijdrecht.")
        print("B: Alkwin College.")
        print("C: Amstelveen College.")
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
        print("No, this was one of my first options but I didn't actually go there.")
        break
    else:
        print("Invalid input.")

time.sleep(4.5)
print("Let's move on.")
time.sleep(1.3)
os.system("cls")


while True:
    # Question B
    while True:
        print("When I finish school I want to become a")
        print("A: Data Architect.")
        print("B: Security Engineer.")
        print("C: Media Developer.")
        answer = raw_input("Pick one option" + " " + naam[0] .upper() + naam[1:].lower() + " " + "[A/B/C]: ")
        if answer in ('a', 'A') or ('b', 'B') or ('c', 'C'):
            break
    if answer == 'a' or answer == 'A':
        time.sleep(0.3)
        print("My father did this job but I'm not really interested in programming languages like php.")
        break
    elif answer == 'b' or answer == 'B':
        time.sleep(0.3)
        print("This seems interesting but that's not what I picked this course for.")
        break
    elif answer == 'c' or answer == 'C':
        time.sleep(0.3)
        print("YES! Media Development seems really fun to me although I have yet to see what it's actually like working as a Media developer.")
        break
    else:
        print("Invalid input.")

time.sleep(4.5)
print("Alright, last question.")
time.sleep(1.3)
os.system("cls")

while True:
    # Question C
    while True:
        print("I live in")
        print("A: Uithoorn.")
        print("B: Amstelveen.")
        print("C: Amsterdam.")
        answer = raw_input("Pick one option" + " " + naam[0] .upper() + naam[1:].lower() + " " + "[A/B/C]: ")
        if answer in ('a', 'A') or ('b', 'B') or ('c', 'C'):
            break
    if answer == 'a' or answer == 'A':
        time.sleep(0.3)
        print("YES! I live in Uithoorn right now and have lived here for about 7 years now.")
        break
    elif answer == 'b' or answer == 'B':
        time.sleep(0.3)
        print("I have lived here, before my parents got seperated.")
        break
    elif answer == 'c' or answer == 'C':
        time.sleep(0.3)
        print("No, I have never lived here before and I think I wouldn't want to live here either.")
        break
    else:
        print("Invalid input.")

time.sleep(2.8)
os.system("cls")

while True:
    # KuezeVraag1
    while True:
        print("Now it's your turn, tell me a litte about yourself")
        answer = raw_input("How was your day" + " " + naam[0] .upper() + naam[1:].lower() + "? ")
        if answer in ('bad', 'Bad') or ('idk', 'IDK') or ('good', 'GOOD'):
            break
    if answer == 'bad' or answer == 'Bad':
        time.sleep(0.3)
        input("I see, do you want to talk about it?. ")
        break
    elif answer == 'idk' or answer == 'IDK':
        time.sleep(0.3)
        print("I see, then we will not talk about it any further?")
        break
    elif answer == 'good' or answer == 'GOOD':
        time.sleep(0.3)
        input("Oh, that's quite nice to hear, tell me more! ")
        break
    else:
        print("I don't know how to respond to that please respond with either: 'bad', 'idk' or good.")


if answer == 'bad' or answer == 'Bad':
    print("Oh, that's quite sad to hear.")
    time.sleep(1)
    input("You know what always helps me?")
    print("It always helps when I listen to some music and just get some rest.")
    time.sleep(1)
    print("You should go and do that")

elif answer == 'good' or answer == 'GOOD':
    print("Oh that's always good to hear")
    time.sleep(1)
    input("Anything else you want to add?")
    time.sleep(0.7)
    print("Nice, nice anyways.")


time.sleep(4.5)
print("That's all folks.")
time.sleep(3)
print("You can go now..")
time.sleep(2.6)
print("Or do you want to stay?")
time.sleep(2.6)
print("I'll give you a choice now.")
time.sleep(1.8)
os.system("cls")


print("ONE MOMENT PLEASE.")
time.sleep(1.2)
# Loading screen
from tqdm import tqdm
for i in tqdm(range(0, 100), desc="Loading", unit="bit"): 
    time.sleep(0.04)
time.sleep(0.8)


while True:
    # Restart Loop
    while True:
        answer = raw_input("Do you want to restart this program" + " " + naam[0] .upper() + naam[1:].lower() + " " + achternaam[0] .upper() + achternaam[1:].lower() + "? [y/n]: ")
        if answer in ('y', 'Y') or ('n', 'N'):
            break
    if answer == 'y' or answer == 'Y':
        print("Alright, NICE.")
        time.sleep(1)
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