import pip._internal as pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    try:
        from tqdm import tqdm
        import time, sys, os
    except ImportError:
        install('tqdm')
        from tqdm import tqdm
        import time, sys, os
        time.sleep(3)
        os.system("cls")
        
respect = 0
maximumRespect = 895
geld = 0

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

def typewelcome(welcome):
    lengte = len(welcome)
    i = 0
    calc = lengte * 0.00020
    wacht = 0.05 - calc
    while i < lengte:
        for char in welcome:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(wacht)
            i += 200
# End import & func

typewelcome("Welkom bij het interactive verhaal van een nieuwkomer, wat is jouw naam?")
naam = input(": ")
typewelcome("Welkom " + naam[0] .upper() + naam[1:] .lower() + ".")
time.sleep(0.8)
typewelcome("\nDit verhaal is gebaseerd op het verhaal van Akram, een vluchteling uit Iran, je kunt haar verhaal bekijken op https://vluchtelingenwerk.nl")
time.sleep(1.7)
typewelcome("\nLaten we maar beginnen.")
time.sleep(0.8)
os.system("cls")
time.sleep(1)
        # End welcome

for i in tqdm(range(0, 100), desc="Loading", unit="bit"): 
    time.sleep(0.0069)
time.sleep(1.2)
os.system("cls")
        # End Loading

#Question 1 Loop (stukje 1)
while True:
    while True:
        os.system("cls")
        answer = input("[1] De Sjah werd kortgeleden afgezet in Iran, maar is nu een nieuw regime onder de naam van Ayatollah Khomein die veel aan onderdrukking doet en de mensen bang maakt, je besluit om...\n\033[2;33;40m1. Aan te sluiten bij het verzet.\n2. Niks te doen.\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe hebt je aangesloten bij het verzet en hebt andere mensen met een gelijke mening gevonden. RESPECT +80\033[0;37;40m")
        respect += 80
        time.sleep(1.5)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe hebt ervoor gekozen om niks te doen maar wordt nog steeds opgepakt voor verdenking van verzet, wanneer je vrij komt ga je het verzet in. RESPECT -20\033[0;37;40m")
        respect -= 20
        time.sleep(1.5)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 2 Loop (stukje 2)
while True:
    while True:
        os.system("cls")
        answer = input("[2]Een van je kamerraden wordt op straat op gepakt tijdens een protest door Iraanse soldaten je weet zelf ook al dat hij daar gemarteld zal worden in een kamp voor informatie. Je besluit om...\n\033[2;33;40m1. Hem proberen te redden.\n2. Hem te vergeten en doorgaan met protesteren.\033[0;37;40m\nKeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe probeert hem te redden, maar nu word je zelf ook opgepakt, dagelijks gemarteld en in isolatie gestopt. RESPECT +100\033[0;37;40m")
        respect += 100
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe bent nog even vrij, maar op een dag word je verraden door de kamerraad die was opgepakt en word je nu zelf ook in de gevangenis gegooid. RESPECT -50\033[0;37;40m")
        respect -= 50
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 3 Loop (death "maybe") (stukje 3)
while True:
    while True:
        os.system("cls")
        answer = input("[3] Deze gevangenis is geen vriendelijke plek, je wordt hier dagelijks gemarteld, uit gescholden en je ziet hier ook zelfs kinderen zonder pardon vermoord worden. Je bent nu in de gevangenis. Je besluit om...\n\033[2;33;40m1. Van uit de gevangenis door te vechten.\n2. Opgeven\n\033[0;37;40mKeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe hebt besloten in een groep sterk te staan en van uit de gevangenis door proberen te vechten voor je rechten je hebt hier door het respect van velen verdiend en overleefd het voor nu. RESPECT +100\033[0;37;40m")
        respect += 100
        time.sleep(1)
        os.system("cls")
        time.sleep(1.3)
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe hebt het opgegeven en dat straal je ook uit.\033[0;37;40m\n")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
#Question [3] -2 Follow up Question (escape death or not) (stukje 4)
if answer == '2': 
    while True:
        while True:
            answer2 = input("Een man(Bahram) ziet dat je het hebt op gegeven en wilt je zijn hulp verlenen, je besluit om...\n\033[2;33;40m1. Accepteren.\n2. Weigeren\n\033[0;37;40mKeuze: ")
            if answer2 in ('1') or ('2'):
                break
        if answer2 == '1':
            typewriter("\033[2;33;40mJe accepteert de mans hulp en houd jezelf sterk. RESPECT +10\033[0;37;40m")
            respect += 10
            time.sleep(1.3)
            os.system("cls")
            break
        elif answer2 == '2':
            typewriter("\033[2;33;40mJe weigert de man zijn hulp, hij loopt weg terwijl hij zijn hoofd schudt. Je hebt het nu totaal opgegeven en zal hier dood gaan.\033[0;37;40m")
                # RESTART
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
                    os.system("py hetverhaalvanAkram.py")
                elif restart == "2":
                    closeMessage = "\033[2;33;40mow... :( tot volgende keer..\033[0;37;40m"
                    for char in closeMessage:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.07)
                    time.sleep(0.6)
                    os.system("taskkill /IM cmd.exe")
                else:
                    print('Invalid input.')
                    time.sleep(0.7)
                    os.system("cls")
            break
        else:
            print('Invalid Input')
            time.sleep(1.3)  
#Question [3 -2] Follow up (uitbreiding) (stukje 5)
if answer == '2' and answer2 == '1':
    while True:
        while True:
            answer3 = input("Terwijl Bahram je door de gevangenis leidt en verteld hoe alles werkt komen jullie langs een groepje dat jullie vies aan kijkt, je besluit om...\n\033[2;33;40m1. Hun aan te spreken \n2. Negeren\n\033[0;37;40mkeuze: ")
            if answer in ('1') or ('2'):
                break
        if answer3 == '1':
            typewriter("\033[2;33;40mJe spreekt hun aan en meteen beginnen ze terug te praten, er breekt een gevecht uit en de bewaking moet komen. RESPECT -10\033[0;37;40m")
            respect -= 10
            time.sleep(1.3)
            os.system("cls")
            break
        elif answer3 == '2':
            typewriter("\033[2;33;40mJe houd je zelf rustig en houd rekening met waar je bent. RESPECT +30\033[0;37;40m")
            respect += 30
            time.sleep(1.3)
            os.system("cls")
            break
        else:
            print('Invalid input.')
            time.sleep(0.7)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 4 Loop (stukje 6)
while True:
    while True:
        os.system("cls")
        answer = input("[4] Je raakt in een argument met een van de soldaten die in de gevangenis werkt en hij begint je te slaan, omdat hij boos wordt. Je ziet dat niemand je helpt, je besluit om... \n\033[2;33;40m1. Terug te vechten \n2. Wachten tot hij klaar is en hopen dat hij niet te ver gaat\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mDe andere bewakers komen hem helpen waarna je in isolatie wordt gegooid voor de volgende paar maanden. RESPECT +50\033[0;37;40m")
        respect += 50
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe hebt geluk en de andere bewakers komen laat om je te helpen maar je overleeft het wel. RESPECT +40\033[0;37;40m")
        respect += 40
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 5 Loop (death) (stukje 7)
while True:
    while True:
        os.system("cls")
        answer = input("[5] Na 8 jaar in de gevangenis word je spontaan geblinddoekt door een aantal bewakers en naar buiten genomen bang voor je leven besluit je om...\n\033[2;33;40m1. Jezelf los proberen te worstelen.\n2. Het gewoon te laten gebeuren.\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mBang voor je leven probeerde je jezelf los te worstelen, de bewakers schrikken zich en uit schok schieten ze je neer, je verhaal eindigt hier.\033[0;37;40m")
        time.sleep(1.3)
        os.system("cls")
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
                os.system("py hetverhaalvanAkram.py")
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
                print('Invalid Input')
                time.sleep(0.7)
                os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mDe bewakers namen je mee naar buiten de gevangenis, hier doen ze de blinddoek af en word je naar buiten geduwd. Je bent nu weer uit de gevangenis. RESPECT +30\033[0;37;40m")
        respect += 30
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 6 Loop (death) (stukje 8)
while True:
    while True:
        os.system("cls")
        answer = input("[6] Je bent nu net weer vrij op de straat en je moet snel een keuzen maken, blijf of vlucht. Je besluit om...\n\033[2;33;40m1. Blijf in Iran \n2. Vlucht\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe hebt besloten om in Iran te blijven wonen, maar dit was niet een slimme keuze. Nog altijd onderdrukt en in gevaar krijg je hierna niet meer de kans om het land te verlaten en ga je hier op een vroege leeftijd al dood.\033[0;37;40m")
        time.sleep(1.3)
        os.system("cls")
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
                os.system("py hetverhaalvanAkram.py")
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
                print('Invalid Input')
                time.sleep(0.7)
                os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe hebt besloten om naar een veilig land te vluchten, de trip zal moeilijk worden. RESPECT +15 \033[0;37;40m")
        respect += 15
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 7 Loop (stukje 9)
while True:
    while True:
        os.system("cls")
        answer = input("[7] Je bent op de vlucht, er zijn een paar opties om het land uit te komen maar niks is zeker, je besluit om...\n\033[2;33;40m1. Met de auto te gaan\n2. Met een klein bootje aan de kust te gaan\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mDe auto wordt aan de grens kort geïnspecteerd, gelukkig kijken ze niet naar wat erin zit en krijgen de smokkelaars je buiten het land. RESPECT +60\033[0;37;40m")
        respect += 60
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mDe boot is heel krap met de hoeveelheid vluchtelingen die hetzelfde idee hadden, je besluit in een hoekje van de boot de te gaan zitten waar nu nog de meeste ruimte is. RESPECT +90\033[0;37;40m")
        respect += 90
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 8 Loop (expanded) (stukje 10)
while True:
    while True:
        os.system("cls")
        answer = input("[8] Je komt net in Nederland aan en wordt verwezen naar het IND om een asielverzoek aan te vragen je besluit om...\n\033[2;33;40m1. Het zelf te zoeken\n2. De instructies goed te volgen\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe probeert het zelf te zoeken maar na een tijdje raak je verdwaald en moet je iemand zoeken die jou kan helpen. RESPECT -30\033[0;37;40m")
        respect -= 30
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe hebt de instructies goed gevolgd en de aanvraag naar een asielprocedure gaat goed. RESPECT +20\033[0;37;40m")
        respect += 20 
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
#Question 8 expansion (stukje 11)
if answer == '1':
    while True:
        while True:
            os.system("cls")
            answer2 = input("Je bent verdwaald en moet hulp vragen aan iemand, je besluit om...\n\033[2;33;40m1. Hulp vragen aan een agent.\n2. Hulp vragen aan iemand die Iraans lijkt.\n\033[0;37;40mkeuze: ")
            if answer2 in ('1') or ('2'):
                break
        if answer2 == '1':
            typewriter("\033[2;33;40mJe vraagt hulp aan de agent, maar omdat hij je niet begrijpt moet je mee met hem naar het bureau om iemand te zoeken die het kan vertalen. RESPECT -30\033[0;37;40m")
            respect -= 30
            time.sleep(1.3)
            os.system("cls")
            break
        elif answer2 == '2':
            typewriter("\033[2;33;40mGelukkig had je het goed en kon hij echt Iraans spreken, hij helpt je verder naar het IND. RESPECT +20\033[0;37;40m")
            respect += 20 
            time.sleep(1.3)
            os.system("cls")
            break
        else:
            print('Invalid input.')
            time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 9 Loop (stukje 12)
while True:
    while True:
        os.system("cls")
        answerQuestion9 = input("[9] Je hebt een asielverzoek, nu moet je naar het COA voor opvang tijdens de procedure je besluit je om...\n\033[2;33;40m1. Schreeuwen tegen de medewerkers\n2. In slaap vallen tijdens het gesprek\n\033[0;37;40mkeuze: ")
        if answerQuestion9 in ('1') or ('2'):
            break
    if answerQuestion9 == '1':
        typewriter("\033[2;33;40mTijdens je gesprek begin je te schreeuwen tegen de medewerkers omdat je gestrestst bent, de medewerkers kunnen hier helaas geen sympathie voor tonen. RESPECT -45\033[0;37;40m")
        respect -= 45
        time.sleep(1.3)
        os.system("cls")
        break
    elif answerQuestion9 == '2':
        typewriter("\033[2;33;40mTijdens je gesprek met het COA val je door alles wat er gebeurd is en hoe weinig slaap je hebt gehad bijna in slaap, ze moeten je nu wakker proberen te houden. RESPECT -10\033[0;37;40m")
        respect -= 10  
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 10(9 -1) Loop (Gaan schreeuwen) (stukje 13)
if answerQuestion9 == "1":
    while True:
        while True:
            os.system("cls")
            answerQuestion10 = input("[10] Je bent gaan schreeuwen tegen de medewerkers en ze zijn nu boos op je, dit zal je verblijf minder leuk maken met hoe de medewerkers met je om zullen gaan. Je besluit om...\n\033[2;33;40m1. Relatie verbeteren. \n2. Het gewoon zo laten. \n\033[0;37;40mkeuze: ")
            if answerQuestion10 in ('1') or ('2'):
                break
        if answerQuestion10 == '1':
            typewriter("\033[2;33;40mJe biedt je excuses aan en ze accepteren het. RESPECT +10\033[0;37;40m")
            respect += 10 
            time.sleep(1.3)
            os.system("cls")
            break
        elif answerQuestion10 == '2':
            typewriter("\033[2;33;40mJe bied niet je excuses aan. RESPECT -10\033[0;37;40m")
            respect -= 10
            time.sleep(1.3)
            os.system("cls")
            break
        else:
            print('Invalid input.')
            time.sleep(0.7)
time.sleep(1)
os.system("cls")
#Question 11(9 -2) Loop (In slaap gevallen) (stukje 14)
if answerQuestion9 == "2":
    while True:
        while True:
            os.system("cls")
            answerQuestion11 = input("[10] De procedure voor tijdelijk verblijf is zojuist afgelopen, helaas was je wel meerdere keren bijna in slaap gevallen. Je besluit om...\n\033[2;33;40m1. Je legt uit wat er mis is, dit waarderen ze.\n2. Je zegt niks over.\033[0;37;40mkeuze: ")
            if answerQuestion11 in ('1') or ('2'):
                break
        if answerQuestion11 == '1':
            typewriter("\033[2;33;40mJe biedt je excuses aan en ze accepteren het. RESPECT +35\033[0;37;40m")
            respect += 35
            time.sleep(1.3)
            os.system("cls")
            break
        elif answerQuestion11 == '2':
            typewriter("\033[2;33;40mJe bied niet je excuses aan. RESPECT -35\033[0;37;40m")
            respect -= 35
            time.sleep(1.3)
            os.system("cls")
            break
        else:
            print('Invalid input.')
            time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 11 Loop (stukje 15)
while True:
    while True:
        os.system("cls")
        answer = input("[11] Je hebt nu wat vrije tijd in het opvangcentrum, je besluit om...\n\033[2;33;40m1. Een boek te gaan lezen\n2. Extra tijd besteden om Nederlands wat beter te leren\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe zoekt een boek om te lezen, helaas snap je er niks van omdat het boek in Nederlands geschreven is.\033[0;37;40m")
        respect = respect
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe wilt je Nederlands verbeteren, om dit te doen ga je een boek zoeken om te lezen en iemand die de woorden voor je kan vertalen.\033[0;37;40m")
        respect = respect
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 12 Loop (stukje 16)
while True:
    while True:
        os.system("cls")
        answer = input("[12] Het is je laatste dag in het kamp, je gaat morgen verplaatst worden naar een nieuwe locatie, je besluit om...\n\033[2;33;40m1. Sporten\n2. Rusten\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe bent een tijdje gaan sporten, dit haalt je zorgen een beetje weg en je komt wat meer tot rust voor de komende tijden. RESPECT +30\033[0;37;40m")
        respect += 30
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe gaat rusten, maar hierdoor ga je te ver door denken en maakt je alleen maar meer zorgen over er wat er kan gebeuren in de toekomst en hoe het met je familie gaat. RESPECT -15\033[0;37;40m")
        respect -= 15
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 13 Loop (stukje 17)
while True:
    while True:
        os.system("cls")
        answer = input("[13] De procedure is nu afgelopen, je hebt je verblijf vergunning dus je moet nu naar een huisvesting. Wanneer je er bent besluit je om...\n\033[2;33;40m1. Je zelf thuis maken en er een puin van maken.\n2. Je omgeving leren kennen.\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mHet puin blijft ophopen en is erg vies als bezoek langskomt. Je moet nu iemand betalen om je te helpen opruimen. RESPECT -40, GELD -€25\033[0;37;40m")
        respect -= 40
        geld -= 25
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe leert je omgeving kennen en wordt vrienden met de buren, als welkom cadeau geven ze je €50 om wat leuks te kopen. RESPECT +65, GELD +€50\033[0;37;40m")
        respect += 65
        geld += 50
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question 14 Loop (stukje 18)
while True:
    while True:
        os.system("cls")
        answer = input("[14] Je moet nu werk gaan zoeken om wat geld te verdienen terwijl je hier blijft, je besluit om...\n\033[2;33;40m1. Hulp te vragen vanuit de gemeente\n2. Hulp te vragen vanuit Vluchtelingenwerk\n\033[0;37;40mkeuze: ")
        if answer in ('1') or ('2'):
            break
    if answer == '1':
        typewriter("\033[2;33;40mJe vraagt hulp vanuit de gemeente, maar helaas kom je hier niet ver mee omdat de medewerkers alleen Nederlands praten, ze plannen een gesprek voor je in met iemand van vluchtelingen werk op een latere datum.\033[0;37;40m")
        respect += 10
        time.sleep(1.3)
        os.system("cls")
        break
    elif answer == '2':
        typewriter("\033[2;33;40mJe vraagt hulp van VluchtelingenWerk en ze kunnen je al snel op weg helpen. RESPECT +10\033[0;37;40m")
        respect += 10
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#Question 15 Uitbreiding op 14 (stukje 19)
while True:
    while True:
        os.system("cls")
        answerQuestion15 = input("[15] Je gaat in gesprek met een arbeid coach van Vluchtelingenwerk hier wordt vast gesteld wat je wensen zijn voor je werk en wat mogelijk is.\n\033[2;33;40m1. Het maakt je niet uit zolang je werk hebt.\n2. Je wilt de bouw in gaan.\n\033[0;37;40mkeuze: ")
        if answerQuestion15 in ('1') or ('2'):
            break
    if answerQuestion15 == '1':
        typewriter("\033[2;33;40mJe coach zoekt naar een bedrijf waar je zo snel mogelijk kan werken. RESPECT +5\033[0;37;40m")
        respect += 5
        time.sleep(1.3)
        os.system("cls")
        break
    elif answerQuestion15 == '2':
        typewriter("\033[2;33;40mJe wilt de bouw in gaan, je verdient hier €2700 per maand. RESPECT +20, GELD +€2700\033[0;37;40m")
        respect += 20
        geld += 2700
        time.sleep(1.3)
        os.system("cls")
        break
    else:
        print('Invalid input.')
        time.sleep(0.7)
time.sleep(1)
os.system("cls")
#Question 15 uitbreiding op stukje 19 (stukje 20)
if answerQuestion15 == "1":
    while True:
        while True:
            os.system("cls")
            answer = input("[15] Je coach heeft een paar mogelijk opties voor je gevonden je kiest om...\n\033[2;33;40m1. Vuilnisman worden\n2. Rioolwerker worden\n\033[0;37;40mkeuze: ")
            if answer in ('1') or ('2'):
                break
        if answer == '1':
            typewriter("\033[2;33;40mJe werkt als vuilnisman, hier verdien je ongeveer €2000 per maand mee. RESPECT +55, GELD +€2000\033[0;37;40m")
            respect += 55
            geld += 2000
            time.sleep(1.3)
            os.system("cls")
            break
        elif answer == '2':
            typewriter("\033[2;33;40mJe besluit down en dirty te gaan en riool werker te worden, je verdient 3000 per maand mee. RESPECT +100, GELD +€3000\033[0;37;40m")
            respect += 100
            geld += 3000
            time.sleep(1.3)
            os.system("cls")
            break
        else:
            print('Invalid input.')
            time.sleep(0.7)
time.sleep(1)
os.system("cls")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question16 (stukje 21)
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
    typewriter("Je bent naar lokale dierenwinkel gegaan voor een huisdier, ze hebben hier van alles. je kiest voor...\n")
    huisdier = input("type dier: ")
    time.sleep(1)
    typewriter("Je hebt besloten op een " + huisdier + ", je moet hem/haar alleen nog een naam geven.\n")
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
typewriter("\nDit was het einde van het verhaal jammer genoeg, we hopen je weer een keer te zien. Bedankt voor het spelen" + naam[0] .upper() + naam[1:] .lower())
time.sleep(0.7)
typewriter("\nWil je meer informatie over vluchtelingen en hoe alles werkt?")
typewriter("\nGa dan naar https://vluchtelingenwerk.nl/")
time.sleep(0.4)
typewriter("\nTot volgende keer!")
time.sleep(5)