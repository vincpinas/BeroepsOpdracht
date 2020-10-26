import time, sys, os
respect = 500
maximumRespect = 790
geld = 2000
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

while True:
    while True:
        os.system("cls")
        answerQuestion16 = input("[16] Je bent nu een tijdje in nederland geweest en hebt veel vrienden gemaakt, maar je woont nog steeds alleen. Je besluit om...\n\033[2;33;40m1. Te gaan daten\n2. Een huisdier te nemen\n\033[0;37;40mkeuze: ")
        if answerQuestion16 in ('1') or ('2'):
            break
    if answerQuestion16 == '1':
        typewriter("\033[2;33;40mJe gaat daten en door je vrienden vind je iemand leuk, jullie besluiten 2 jaar later om te gaan trouwen. RESPECT +100\033[0;37;40m")
        respect += 100
        time.sleep(1.3)
        os.system("cls")
        break
    elif answerQuestion16 == '2':
        typewriter("\033[2;33;40mJe besluit om een huisdier te nemen. RESPECT +40, GELD -55\033[0;37;40m")
        respect += 40
        geld -= 55
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")

if answerQuestion16 == "2":
    typewriter("Je bent naar lokale dieren winkel gegaan voor een huisdier, ze hebben hier van alles. je kiest voor...\n")
    huisdier = input("type dier: ")
    time.sleep(1)
    typewriter("Je hebt besloten op een " + huisdier + ", je moet hem/haar alleen nog een naam geven\n")
    huisdierNaam = input("naam van huisdier: ")
    time.sleep(1.3)
    typewriter("Je leeft een prettig leven uit in Nederland samen met je " + huisdier + " " + huisdierNaam)
    

if answerQuestion16 == "1":
    typewriter("Je leeft je leven uit samen met je geliefde en jullie twee kinderen")

time.sleep(2)
os.system("cls")
typewriter("\nFinal stats:\n")
time.sleep(1.5)
respectPrint = "Respect: " + str(respect) + " / " + str(maximumRespect)
for char in respectPrint:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
time.sleep (1.5)
typewriter("\nGeld: " + str(geld))
time.sleep(2)
os.system("cls")
typewriter("\nDit was het einde van het verhaal jammer genoeg, we hopen je weer een keer te zien.")
time.sleep(0.7)
typewriter("\nWil je meer informatie over vluchtelingen en hoe alles werkt?")
typewriter("\nGa dan naar https://vluchtelingenwerk.nl/")
time.sleep(0.4)
typewriter("\nTot volgende keer!")
time.sleep(5)