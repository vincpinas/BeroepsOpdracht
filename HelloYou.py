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

from datetime import datetime
datum = datetime.now()
print("the current time is:", datum)
