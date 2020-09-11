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

time.sleep(1.9)

os.system('cls')

from tqdm import tqdm
for i in tqdm(range(0, 100), desc="Loading", unit="bit"): 
    time.sleep(0.04)

raw_input = input

while True:
    # If else statement
    while True:
        answer = raw_input("Do you want to restart this program" + " " + naam[0] .upper() + naam[1:].lower() + " " + achternaam[0] .upper() + achternaam[1:].lower() + "? [y/n]: ")
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        os.system("cls")
        time.sleep(1)
        os.system("HelloYou.py")
    else:
        print('Goodbye :(')
        time.sleep(1.6)
        os.system("taskkill /IM cmd.exe")
        break
        
