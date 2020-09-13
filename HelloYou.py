# Install tqdm voor volle gebruik van dit programma dat doe je door de volgende command in je terminal in te voeren: pip intall tqdm
# Geniet er van.
 
import os

os.system('cls')    				

print("Hello You!, ik ben Vincent")

print("What's your name?")  
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

raw_input=input

while True:
    # If else statement
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



from tqdm import tqdm
for i in tqdm(range(0, 100), desc="Loading", unit="bit"): 
    time.sleep(0.04)
time.sleep(0.8)
os.system("cls")



while True:
    # If else statement
    while True:
        answer = raw_input("Do you want to restart this program" + " " + naam[0] .upper() + naam[1:].lower() + " " + achternaam[0] .upper() + achternaam[1:].lower() + "? [y/n]: ")
        if answer in ('y', 'Y') or ('n', 'N'):
            break
    if answer == 'y' or answer == 'Y':
        os.system("cls")
        time.sleep(1)
        os.system("HelloYou.py")
    elif answer == 'n' or answer == 'N':
        print('Goodbye :(')
        time.sleep(1.6)
        os.system("taskkill /IM cmd.exe")
        break
    else:
        print('Invalid input.')

        
