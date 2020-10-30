# Add your Python code here. E.g.
from microbit import *
import speech, random

LengteWoordArray = 3

onderwerp = random.choice(["he", "she", "vincent"])
werkwoord = random.choice(["walks", "sings", "dances"])
rest = random.choice(["street", "school", "city"])

box1 = Image("00000:00000:00900:00000:00000")
box2 = Image("00000:09990:09090:09090:00000")
box3 = Image("99999:90009:90009:90009:99999")
all_boxes = [box1, box2, box3]

def SayTheWords1(word):
    speech.say(word, speed=100, pitch=150, throat=120, mouth=140)
    sleep(500)

def SayTheWords2():
    willekeurigGetal1 = random.randint(0, LengteWoordArray - 1)
    willekeurigGetal2 = random.randint(0, LengteWoordArray - 1)
    willekeurigGetal3 = random.randint(0, LengteWoordArray - 1)
    display.show(willekeurigGetal1 + willekeurigGetal2 + willekeurigGetal3)
    SayTheWords1(onderwerp[willekeurigGetal1])
    SayTheWords1(werkwoord[willekeurigGetal2])
    SayTheWords1(rest[willekeurigGetal3])
    
def SayTheWords3(word):
    wordspeed = random.randint(10, 200)
    wordpitch = random.randint(10, 200)
    speech.say(word, speed=wordspeed, pitch=wordpitch, throat=100, mouth=200)
    
    
while True:
    if button_a.is_pressed():
        display.show(Image.SKULL)
        SayTheWords1("are you okay")
        sleep(100)
    elif button_b.is_pressed():
        display.show(Image.DUCK)
        SayTheWords1("you are cool")
        sleep(100)
    elif accelerometer.was_gesture('shake'):
        SayTheWords2()
    else:
        display.show(all_boxes)