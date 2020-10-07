import time, sys, os
respect = 0
maximumRespect = 330

welcome = "Welkom bij het interactive verhaal van een nieuwkomer, wat is jouw naam?"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)

naam = input(": ")

welcome = "Welkom " + naam[0] .upper() + naam[1:] .lower() + "."
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(0.8)
welcome = "\nDit verhaal is gebaseerd op het verhaal van Akram, een vluchteling uit Iran, je kunt haar verhaal bekijken op https://vluchtelingenwerk.nl"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(1.7)
welcome = "\nLaten we maar beginnen."
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(0.8)
os.system("cls")
time.sleep(1)
        # End welcome
    

from tqdm import tqdm
for i in tqdm(range(0, 100), desc="Loading", unit="bit"): 
    time.sleep(0.0050)
time.sleep(1.2)
os.system("cls")
        # End Loading

#Question 1 Loop
while True:
    while True:
        answer = input("[1] De Sjah werd kortgeleden afgezet in Iran, maar is nu een nieuw regime onder de naam van Ayatollah Khomein die veel aan onderdrukking doet en de mensen bang maakt.\nJe besluit om...\n\033[2;33;40m1. Aan te sluiten bij het verzet.\n2. Niks te doen.\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        message = "\033[2;33;40mJe hebt je aangesloten bij het verzet en hebt andere mensen met een gelijke mening gevonden. RESPECT +80\033[0;37;40m"
        respect = respect + 80
        time.sleep(1.5)
        os.system("cls")
        break
    elif answer == '2':
        message = "\033[2;33;40mJe hebt ervoor gekozen om niks te doen maar wordt nog steeds opgepakt voor verdenking van verzet, wanneer je vrij komt ga je het verzet in.\nRESPECT -20\033[0;37;40m"
        respect = respect - 20
        time.sleep(1.5)
        os.system("cls")
        break
    else:
        print('Invalid input.')
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
time.sleep(1)
os.system("cls")

#Question 2 Loop
while True:
    while True:
        answer = input("[2]Een van je kamerraden wordt op straat op gepakt tijdens een protest door Iraanse soldaten je weet zelf ook al dat hij daar gemarteld zal worden in een kamp voor informatie. Je besluit om...\n\033[2;33;40m1. Hem proberen te redden.\n2. Hem te vergeten en doorgaan met protesteren.\033[0;37;40m\nKeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        message = "\033[2;33;40mJe probeert hem te redden, maar nu word je zelf ook opgepakt, dagelijks gemarteld en in isolatie gestopt. RESPECT +100\033[0;37;40m"
        respect = respect + 100
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        message = "\033[2;33;40mJe bent nog even vrij, maar op een dag word je verraden door de kamerraad die was opgepakt en word je nu zelf ook in de gevangenis gegooid. RESPECT -50\033[0;37;40m"
        respect = respect - 50
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
time.sleep(1)
os.system("cls")

#Question 3 Loop
while True:
    while True:
        answer = input("[3] Deze gevangenis is geen vriendelijke plek, je wordt hier dagelijks gemarteld, uit gescholden en je ziet hier ook zelfs kinderen zonder pardon vermoord worden. Je bent nu in de gevangenis. Je besluit om......\n\033[2;33;40m1. Van uit de gevangenis door te vechten.\n2. Opgeven\n\033[0;37;40mKeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        message = "\033[2;33;40mJe hebt besloten in een groep sterk te staan en van uit de gevangenis door proberen te vechten voor je rechten je hebt hier door het respect van velen verdiend en overleefd het voor nu. RESPECT +100\033[0;37;40m"
        respect = respect + 100
        time.sleep(1)
        os.system("cls")
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        message = "\033[2;33;40mJe hebt het net als vele anderen vooral jongere mensen opgegeven en gaat helaas zonder pardon dood in gevangenis, je verhaal eindigt hier.\033[0;37;40m"
        time.sleep(1.3)
        os.system("cls")
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)
        end = "\n\033[2;31;40mJammer genoeg is je verhaal hier al afgelopen, bedankt voor het spelen."
        for char in end:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.07)
        while True:
            while True:
                restart = input("\n\033[2;31;40m1. Restart\n2. Sluit af\n: \033[0;37;40m")
                if restart in ("1") or ("2"):
                    break
            if restart == "1":
                restartMessage = "\033[2;33;40mLaten we het weer proberen!\033[0;37;40m"
                for char in restartMessage:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.07)
                time.sleep(0.8)
                os.system("cls")
                time.sleep(1)
                os.system("eindopdracht.py")
            elif restart == "2":
                closeMessage = "\033[2;33;40mow... :( tot volgende keer..\033[0;37;40m"
                for char in closeMessage:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.07)
                time.sleep(0.6)
                os.system("taskkill /IM cmd.exe")
                break
            else:
                print('Invalid input.')
        break
    else:
        print('Invalid input.')

#Question 4 Loop
while True:
    while True:
        answer = input("[4] Je raakt in een argument met een van de soldaten die in de gevangenis werkt en hij begint je te slaan, omdat hij boos wordt. Je ziet dat niemand je helpt, je besluit om... \n\033[2;33;40m1. Terug te vechten \n2. Wachten tot hij klaar is en hopen dat hij niet te ver gaat\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        message = "\033[2;33;40mDe andere bewakers komen hem helpen waarna je in isolatie wordt gegooid voor de volgende paar maanden. RESPECT +50\033[0;37;40m"
        respect = respect + 50
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        message = "\033[2;33;40mJe hebt geluk en de andere bewakers komen laat om je te helpen maar je overleeft het wel. RESPECT +40\033[0;37;40m"
        respect = respect + 40
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
time.sleep(1)
os.system("cls")

respectPrint = "Respect: " + str(respect) + " / " + str(maximumRespect)
for char in respectPrint:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
time.sleep(5)