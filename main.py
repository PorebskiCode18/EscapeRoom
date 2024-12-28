screwdriver=False
firstTime1=True
firstTime2=True
firstTime=False
firstHalfKey=False
secondHalfKey=False
firstTime3=True
glue=False
note=False
unscrewed=False
firstTime4=True
firstTime5=False
firstTime6=False
firstTime7=False
handle=False
key=True
hotWaterPercent=0
coldWaterPercent=0
screws=4
redCylinder=False
blueCylinder=False
yellowCylinder=False
cameraSet=0
lightsOn=True
storageKey=False
carKeys=False
unlocked=False
bathRoomKey=False
garageOpened=False
powerOn=False
garageKeyPrinted=False
garageCard=False
computerCardPrinted=False
computerCard=False
drawerKey=False
greenKey=False
note2=False
ranNum=0
ranNum2=0
ranNum3=0
ranNum4=0
coldWaterPercent2=0
hotWaterPercent2=0
messageShown=False
weapon=False
alienAttack=False
alienKilled=False
firstTime8=False
name=""
won=False
inCar=False
noteBookCollected=False
notes=[]
area="cell"
def noteBook():
    def noteBook():
        global notes
        print("1: Take Notes")
        print("2: Check Notes")
        print("3: Go back")
        choose = int(input())
        if choose == 1:
            NewNotes = input("Write your notes here:")
            notes.append(NewNotes)
            noteBook()
        elif choose == 2:
            print(notes)
            noteBook()
        elif choose == 3:
            if area=="cell":
                cell()
            elif area=="photoroom":
                photoRoom()
            elif area=="hallway":
                hallway()
            elif area=="office":
                office()
            elif area="bathroom":
                insideBathroom()
            elif area="security":
                insideSecurity()
            elif area="garage:":
                insideGarage()
def cell():
 global firstTime1,key,note, noteBookCollected
 if firstTime1==True:
  print("You wake up in a jell cell with no memory of what happened")
  firstTime1=False
 if firstHalfKey==True and secondHalfKey==True and glue==True and key==False:
  print("Press 1 to put together the key")
  if int(input())==1:
   print("You glued the 2 key parts together")
   print("Key Collected")
   key=True
   cell()
 print("Goal: Escape the cell")
 print("1: Poster")
 print("2: Bed")
 print("3: Steel grate")
 print("4: Toilet")
 print("5: Sink")
 print("6: Cell Door")
 if note==True:
  print("7: Inspect Note")
 if noteBook==True:
     print("8: Note Book")
 choose= int(input())
 if choose == 1:
  poster()
 elif choose == 2:
  bed()
 elif choose==3:
  grate()
 elif choose==4:
  toilet()
 elif choose==5:
  sink()
 elif choose==6:
  CellDoor()
 elif choose==7:
  noteInspect()
 elif choose==8 and noteBookCollected==True:
     noteBook()
def poster():
 global screwdriver, firstTime2,noteBookCollected
 print("You look at the poster but see nothing")
 print("Press 1 to move the poster")
 print("Press 2 to go back")
 choose=int(input())
 if choose==1:
  if firstTime2 == True:
   print("You look behind the poster and find a screwdriver and a notebook where you can take notes")
   print("Screwdriver Collected")
   print("Note Book Collected")
   firstTime2=False
   noteBookCollected=True
   screwdriver = True
  else:
   print("You already looked here")
  cell()
 if choose==2:
  cell()

def bed():
 global firstHalfKey, glue, firstTime3, note
 print("You look at the bed but see nothing")
 print("Press 1 to move the bed sheets")
 print("Press 2 to go back")
 choose = int(input())
 if choose == 1:
  if firstTime3 == True:
   print("You look under the bed and find super glue and a note")
   print("Note Collected")
   print("Super Glue Collected")
   note=True
   glue = True
   firstTime3=False
  else:
   print("You already looked here")
  cell()
 if choose == 2:
  cell()
def grate():
 global screwdriver,screws, firstHalfKey
 if screwdriver==False:
  print("The grate has 4 screws, looks like you need to find a screwdriver")
  cell()
 if screwdriver==True and unscrewed==False:
  print("Press 1 to unscrew a screw")
  print("Press 2 to go back")
  choose = int(input())
  if choose == 1:
   if screws>0:
       print("You unscrewed a screw")
       screws-=1
       print("There are " + screws.__str__() + " screws left")
       if screws==0:
           firstHalfKey=True
           print("You opened the grate")
           print("You found half a key inside")
           print("1/2 Key Collected")
       grate()
   else:
    print("You have already done this")
    grate()
  if choose == 2:
   cell()
def toilet():
 global firstTime4,handle, secondHalfKey
 if firstTime4==True:
    print("You look at the toilet")
    print("There seems to be something in the toilet")
    print("The handle on the side seems to be missing")
    firstTime4=False
    cell()

 else:
  if handle==False:
   print("Find the toilet handle")
   cell()
  else:
   print("Press 1 to put the handle in")
   print("Press 2 to go back")
   choose = int(input())
   if choose==1:
    print("You put the handle in the toilet and flush it")
    print("Half of a key shows up in the toilet")
    print("1/2 Key Collected")
    secondHalfKey=True
    cell()
   elif choose==2:
    cell()
def CellDoor():
 global area
 if key==True:
  print("Press 1 to open the cell door")
  print("Press 2 to go back")
  choose=int(input())
  if choose==1:
   print("You opened the cell door")
   print("You are now in the photo room")
   photoRoom()
   area="photoroom"
  elif choose==2:
   cell()
 else:
  print("You need a key to open the door")
  cell()
def sink():
 global hotWaterPercent, coldWaterPercent, handle
 if handle==False:
  print("The sink has 2 handles: hot and cold")
  print("Press 1 to increase hot water")
  print("Press 2 to increase cold water")
  print("Press 3 to go back")
  choose = int(input())
  if choose == 1:
   print("You increased the hot water percent by 5%")
   hotWaterPercent += 5
   if hotWaterPercent>100:
    hotWaterPercent=0
   print("Hot water percent is " + hotWaterPercent.__str__() + "%")
   if hotWaterPercent == 40 and coldWaterPercent == 75:
    print("A toilet handle came out of the water")
    print("Toilet Handle Collected")
    handle = True
   sink()
  elif choose == 2:
   print("You increased the cold water percent by 5%")
   coldWaterPercent += 5
   if coldWaterPercent>100:
    coldWaterPercent=0
   print("Cold water percent is " + coldWaterPercent.__str__() + "%")
   if hotWaterPercent == 40 and coldWaterPercent == 75:
    print("A toilet handle came out of the water")
    print("Toilet Handle Collected")
    handle = True
   sink()
  elif choose == 3:
   cell()
 else:
  print("You've already collected the handle")
  cell()
def noteInspect():
 print("You see some writing on the note")
 print("Hot: (2x+y)%")
 print("Cold: (3x+2y)%")
 print("X=5, Y= 30")
 cell()
def photoRoom():
 global lightsOn, area
 print("Goal: Escape the police station")
 if lightsOn==True:
  print("1: Cell 1")
  print("2: Cell 2")
  print("3: Cell 3")
 print("4: Camera")
 if lightsOn==True:
  print("5: Board")
  print("6: Hallway")
  print("7: Car Key Storage")
 print("8: Lights")
 print("9: Note Book")
 choose=int(input())
 if choose==1 and lightsOn==True:
  area = "cell"
  cell()

 elif choose==2 and lightsOn==True:
  cell2()
 elif choose == 3 and lightsOn==True:
  cell3()
 elif choose == 4:
  camera()
 elif choose == 5 and lightsOn==True:
  board()
 elif choose == 6 and lightsOn==True:
  area = "hallway"
  hallway()

 elif choose == 7 and lightsOn==True:
  KeyStorage()
 elif choose == 8:
  lights()
 elif choose==9:
     noteBook()
def man():
    global name, firstTime8, weapon, won
    import random
    if firstTime8==False:
        print("John: Who.. who are you?")
        name= input("Enter your name: ")
        print("I am " + name)
        print("What happened here")
        print("John: Once the aliens attacked the police station got over run")
        print("John:I managed to lock them out for the time being and hid away must the things to keep them from learning our secrets")
        print("John: Is there anything you need from me")
        print("I found a way out of the police station but I need a weapon to get past one of the aliens in the garage")
        print("John: I can give you a weapon but it wont help")
        print("John: Before the human race is extinct I want to be able to have fun one more time")
        print("John: Beat me in a game of rock paper scissors and i'll give you my gun")
        firstTime8=True
        man()
    else:
        print("Choose 1) Rock 2) Paper 3) Scissors")
        JohnChoice=random.randrange(1,4)
        choose=int(input())
        if choose==1 and JohnChoice==1:
            print("Man: Rock")
            print("Tie, try again")
            man()
        elif choose==1 and JohnChoice==2:
            print("Man: Paper")
            print("You lose, try again")
            man()
        elif choose==1 and JohnChoice==3:
            print("Man: Scissors")
            print("You win, here's your weapon")
            print("Weapon Collected")
            weapon=True
            won=True
            cell2()
        elif choose==2 and JohnChoice==1:
            print("Man: Rock")
            print("You win, here's your weapon")
            print("Weapon Collected")
            weapon = True
            won = True
            cell2()
        elif choose == 2 and JohnChoice == 2:
            print("Man: Paper")
            print("Tie, try again")
            man()
        elif choose==2 and JohnChoice==3:
            print("Man: Scissors")
            print("You lose, try again")
            man()
        elif choose==3 and JohnChoice==1:
            print("Man: Rock")
            print("You lose, try again")
            man()
        elif choose == 3 and JohnChoice == 2:
            print("Man: Paper")
            print("You win, here's your weapon")
            print("Weapon Collected")
            weapon = True
            won = True
            cell2()
        elif choose == 3 and JohnChoice == 3:
            print("Man: Scissors")
            print("Tie, try again")
            man()
def cell2():
 global alienAttack,won
 print("Goal: Escape the police station")
 print("1: Bed")
 print("2: Go back")
 if alienAttack==True and won==False:
     print("3: Talk to man")
 choose= int(input())
 if choose == 1:
  print("You move the bed sheets and find a newspaper under the bed")
  print("Title: Amertec Labs Commissions Creation Of Laboratories In The Mountains ")
  print("Amertec Labs a government run corporation sets up base in the mines based on rumors of mysterious object")
  print("The government is keeping this project top secret and will not release any more information at this time")
  cell2()
 elif choose==2:
  photoRoom()
 elif choose==3 and alienAttack==True and won==False:
     man()
def cell3():
 global redCylinder
 print("Goal: Escape the police station")
 print("1: Bed")
 print("2: Go back")
 choose = int(input())
 if choose == 1:
  print("You move the bed sheets and red cylinder under the bed")
  print("Red Cylinder Collected")
  redCylinder=True
  cell3()
 elif choose == 2:
  photoRoom()
def camera():
 global redCylinder, blueCylinder, yellowCylinder, cameraSet, firstTime5, firstTime6, firstTime7, lightsOn
 if redCylinder==False or blueCylinder==False or yellowCylinder==False:
  print("The camera has 3 holes on top: One red hole, one blue, and one yellow")
  print("Find the 3 cylinders for the camera to work")
  photoRoom()
 else:
  if cameraSet<3:
   print("Press 1 to put the red cylinder in the camera")
   print("Press 2 to put the blue cylinder in the camera")
   print("Press 3 to put the yellow cylinder in the camera")
   choose=int(input())
   if choose==1:
    print("You put the red cylinder in the camera")
    if firstTime5==False:
     cameraSet+=1
     firstTime5=True
   elif choose==2:
    print("You put the blue cylinder in the camera")
    if firstTime6 == False:
     cameraSet += 1
     firstTime6 = True
   elif choose == 2:
    print("You put the yellow cylinder in the camera")
    if firstTime7 == False:
     cameraSet += 1
     firstTime7 = True
   camera()
  else:
   if lightsOn==True:
    print("You cant see what's projected with the lights on")
    photoRoom()
   else:
    print("The camera projects a image of a prisoner named Adam")
    photoRoom()


def board():
 print("You look at the board")
 print("There are newspapers on the board")
 print("Title: Mysterious Mystical Object Found In The Mines")
 print("3 miners reported missing and pronounced dead after encounter with a mysterious orb")
 print("Details on the reason of death are not yet available")
 photoRoom()
def KeyStorage():
 global storageKey, carKeys
 if storageKey==False:
  print("You need to find the key for the car key storage")
  photoRoom()
 elif storageKey==True:
  print("You opened the storage")
  print("Press 1 to pick up the car keys")
  if int(input())==1:
   carKeys=True
   photoRoom()
def lights():
 global lightsOn
 print("Press 1 to turn on the lights")
 print("Press 2 to turn off the lights")
 print("Press 3 to go back")
 choose=int(input())
 if choose==1:
  lightsOn=True
  print("You turned the lights on")
  lights()
 elif choose==2:
  lightsOn= False
  print("You turned the lights off")
  lights()
 elif choose==3:
  cell()
def wall():
 global bathRoomKey
 print("You move toward the wall")
 print("Theres a bathroom card on the wall")
 print("Press 1 to pick up the card")
 print("Press 2 to go back")
 choose=int(input())
 if choose==1:
  print("You picked up the card")
  print("Bathroom Card Collected")
  bathRoomKey=True
  wall()
 elif choose==2:
  office()
def computer1():
 global powerOn, computerCardPrinted
 if powerOn==False:
  print("Theres a post it on the computer: Locker Combo: 12 54 39")
  print("You press the power button but it doesnt work")
  print("Find a way to turn the power on first")
  office()
 else:
     print("Press 1 to turn on the computer")
     if int(input()) == 1:
         print("John's computer needs a password to unlock")
         print("The password is John's password is his favorite animal (lower case) + a 4 digit code")
         print("Enter Password:")
         if input()=="pig6243":
             print("You unlock the computer")
             print("There's a file on the computer")
             print("Press 1 to open file")
             print("Press 2 to go back")
             choose = int(input())
             if choose == 1:
                 print("You open the file")
                 print("The file contains a card for access to the security computer")
                 print("Press 1 to print the card")
                 if int(input()) == 1:
                     print("You printed the computer card pick it up at the printer")
                     computerCardPrinted = True
                     office()
             elif choose == 2:
                 office()
def computer2():
 global powerOn, garageKeyPrinted
 if powerOn == False:
  print("You press the power button but it doesnt work")
  print("Find a way to turn the power on first")
  office()
 else:
  print("Press 1 to turn on the computer")
  if int(input())==1:
   print("The computer doesn't have a password")
   print("You unlock the computer")
   print("There's a file on the computer")
   print("Press 1 to open file")
   print("Press 2 to go back")
   choose=int(input())
   if choose==1:
    print("You open the file")
    print("The file contains a card to open the garage door inside the garage")
    print("Press 1 to print the card")
    if int(input())==1:
     print("You printed the garage card pick it up at the printer")
     garageKeyPrinted=True
     office()
   elif choose==2:
    office()

def drawer():
    global drawerKey
    if drawerKey==False:
        print("You need to get a key to open the drawer")
        office()
    else:
        print("Press 1 to insert the key and open the drawer")
        if int(input())==1:
            print("You've opened the drawer")
            insideDrawer()
def insideDrawer():
    print("There is multiple files")
    print("1: File 1")
    print("2: File 2")
    print("3: File 3")
    print("4: Go back")
    choose= int(input())
    if choose==1:
        file1()
    elif choose==2:
        file2()
    elif choose==3:
        file3()
    elif choose==4:
        office()
def file1():
    print("File 1 has a newspaper inside")
    print("Title: ALIENS INVADE EARTH")
    print("At approximately 3 p.m. eastern time on February 5th the mysterious object found in the mountains went active")
    print("Soon after violent creatures came through the portal in massive hoards")
    print("Over whelmed the military was over run and forced to retreat")
    print("Meetings around the world are being set up as global leaders are in shambles to gain order")
    print("The government has urged people to lock their doors and stay indoors")
    insideDrawer()
def file2():
    print("File 2 contains a prisoners file")
    print("The prisoner name is scrubbed but the file number remains")
    print("The file number is: 695461")
    insideDrawer()
def file3():
    print("File 3 contains officer John's information")
    print("Name: John")
    print("Badge #: 6243")
    insideDrawer()
def printer():
 global garageCard, garageKeyPrinted, computerCardPrinted, computerCard
 if garageKeyPrinted==True or computerCardPrinted==True:
    if garageKeyPrinted==True:
        print("The garage card is waiting at the printer")
    if computerCardPrinted==True:
        print("The computer card is waiting at the printer")
    print("Press 1 to pick it up")
    print("Press 2 to go back")
    choose= int(input())
    if choose==1:
        if garageCard==False:
            print("You pick up the garage card")
            print("Garage Card Collected")
            garageCard=True
        else:
            print("You've already done this")
        if computerCard==False:
            print("You pick up the computer card")
            print("Computer Card Collected")
            computerCard = True
        else:
            print("You've already done this")
        office()
    elif choose==2:
        office()
def office():
 global area
 print("Goal: Escape the police station")
 print("1: Hallway")
 print("2: Wall")
 print("3: John's Computer")
 print("4: Alex's Computer")
 print("5: File Drawer")
 print("6: Printer")
 print("7: Note Book")
 choose= int(input())
 if choose==1:
  area = "hallway"
  hallway()

 elif choose==2:
  wall()
 elif choose==3:
  computer1()
 elif choose==4:
  computer2()
 elif choose==5:
  drawer()
 elif choose==6:
     printer()
 elif choose==7:
     noteBook()
def security():
 global unlocked, area
 if unlocked==False:
  print("This door needs a word code")
  print("Enter The Code:")
  code=int(input())
  if code.lower()=="hole":
   print("The door unlocked")
   unlocked=True
   hallway()
  else:
   print("Wrong code, find the right one")
   hallway()
 else:
    print("You enter the security room")
    area = "security"
    insideSecurity()

def securityComputer():
    global garageOpened
    print("You look at the security computer its locked")
    print("You need a computer key card to give access to the keyboard")
    if computerCard==True:
        print("You can use the keyboard")
        print("You need a prisoner name and a prisoner file number to open the computer")
        print("Enter prisoner name")
        prisonerName=input("")
        print("Enter prisoner file number")
        fileNumber = int(input(""))
        if prisonerName.lower()=="adam" and fileNumber=="695461":
            print("You unlocked the computer")
            print('Press 1 to open the door to the garage')
            if int(input())==1:
                print("You opened the door to the garage")
                garageOpened=True
                insideSecurity()
        else:
            print("Wrong prisoner name or prisoner file number, try again")
            securityComputer()
    else:
        print("Find the computer card to use the keyboard")
        insideSecurity()
def table():
    global yellowCylinder
    print("You look at the table")
    print("1: Yellow Cylinder")
    print("2: Newspapers")
    print("3: Go back")
    choose=int(input())
    if choose==1:
        print("Press 1 to pick up the yellow cylinder")
        if int(input())==1:
            print("You picked up the yellow cylinder")
            yellowCylinder=True
            table()
    elif choose==2:
        print("Title: Mysterious Object Connects Dimensions?")
        print("Information leaks revealed that the mysterious object is active and is able to set up stable portals between dimensions")
        print("So far there has been no contact from the other side of the portal")
        print("The government has denied any of this information and urges people to remain calm")
        table()
    elif choose==3:
        insideSecurity()
def lockerList():
    print("Lockers")
    print("111: Alex")
    print("112: John")
    print("113: Bert")
def locker111():
    print("Enter the locker combo")
    right=int(input("Turn Right:"))
    left=int(input("Turn Left:"))
    right2=int(input("Turn Right:"))
    if right==12 and left==54 and right2==39:
        print("Locker combo, didn't work")
        lockerRoom()
    else:
        print("Locker combo, didn't work")
        lockerRoom()
def insideLocker():
    global drawerKey
    print("1: Picture")
    print("2: Key")
    print("3: Go back")
    choose=int(input())
    if choose==1:
        print("You see a picture of John and his pet pig")
        insideLocker()
    elif choose==2:
        print("You see the key to the file drawer in the office")
        print("Press 1 to pick it up")
        if int(input())==1:
            print("You pick up the drawer key")
            print("Drawer Key Collected")
            drawerKey=True
            insideLocker()
    elif choose==3:
        lockerRoom()
def locker112():
    print("Enter the locker combo")
    right = int(input("Turn Right:"))
    left = int(input("Turn Left:"))
    right2 = int(input("Turn Right:"))
    if right == 12 and left == 54 and right2 == 39:
        print("The locker opened")
        insideLocker()
    else:
        print("Locker combo, didn't work")
        lockerRoom()
def locker113():
    print("Enter the locker combo")
    right = int(input("Turn Right:"))
    left = int(input("Turn Left:"))
    right2 = int(input("Turn Right:"))
    if right == 12 and left == 54 and right2 == 39:
        print("Locker combo, didn't work")
        lockerRoom()
    else:
        print("Locker combo, didn't work")
        lockerRoom()
def lockerRoom():
    global area
    print("Goal: escape the police station")
    print("1: Locker list")
    print("2: Locker 111")
    print("3: Locker 112")
    print("4: Locker 113")
    print("5: Security room")
    print("6: Note Book")
    choose=int(input())
    if choose==1:
        lockerList()
    elif choose==2:
        locker111()
    elif choose==3:
        locker112()
    elif choose==4:
        locker113()
    elif choose==5:
        area = "security"
        insideSecurity()
    elif choose==6:
        noteBook()
def insideSecurity():
    global area
    print("Goal: escape the police station")
    print("1: Security Computer")
    print("2: Table")
    print("3: Locker Room")
    print("4: Hallway")
    print("5: Note Book")
    choose=int(input())
    if choose==1:
        securityComputer()
    elif choose==2:
        table()
    elif choose==3:
        area = "locker"
        lockerRoom()

    elif choose==4:
        area = "hallway"
        hallway()
    elif choose==5:
        noteBook()
def bathroom():
    global bathRoomKey,area
    if bathRoomKey==True:
        print("Press 1 to use the bathroom card")
        if int(input())==1:
            print("The bathroom door opens")
            area = "bathroom"
            insideBathroom()

    else:
        print("The door needs a key card to open")
        print("Find the bathroom card")
        hallway()
def insideBathroom():
    global note2, area
    print("Goal: Escape the police station")
    print("1: Electric Box")
    print("2: Bathroom Stall 1")
    print("3: Bathroom Stall 2")
    print("4: Sink")
    print("5: Go back")
    if note2==True:
        print("6: Inspect note")
    print("7: Note Book")
    choose=int(input())
    if choose==1:
        electricBox()
    elif choose==2:
        stall1()
    elif choose==3:
        stall2()
    elif choose==4:
        sink()
    elif choose==5:
        area = "hallway"
        hallway()

    elif choose==6 and note2==True:
        noteInspect2()
    elif choose==7:
        noteBook()
def electricBox():
    global greenKey, powerOn, note2
    if greenKey==False:
        print("The electric box has a green key hole")
        print("Find a green key to open the box")
        insideBathroom()
    else:
        print("Press 1 to open the electric box")
        if int(input())==1:
            print("You've opened the electric box")
            print("Press 1 to interact with electric switch")
            print("Press 2 to pick up the note")
            print("Press 3 to go back")
            choose=int(input())
            if choose==1:
                print("You flipped the switch")
                if powerOn==False:
                    print("The power is on, you can use the computers in the office now")
                    powerOn=True
                else:
                    print("You turned the power off")
                    powerOn=False
                insideBathroom()
            elif choose==2:
                print("You pick up the note")
                print("Inspect the note in the bathroom")
                note2=True
                insideBathroom()
            elif choose==3:
                insideBathroom()
def noteInspect2():
    global ranNum, ranNum2, ranNum3, ranNum4
    # random each game
    print("You see some writing on the note")
    print("Hot: (" + ranNum.__str__() + "+" + ranNum2.__str__() +")%")
    print("Cold: ("+ ranNum3.__str__() + "+" + ranNum4.__str__() + ")%")
    insideBathroom()
def stall1():
    global greenKey
    print("You enter the first stall")
    print("Press 1 to inspect the toilet")
    print("Press 2 to go back")
    choose=int(input())
    if choose==1:
        if greenKey==False:
            print("You inspect the toilet")
            print("You find a green key behind the toilet")
            print("Press 1 to pick up the key")
            if int(inpuyt())==1:
                print("You pick up the key")
                print("Green Key Collected")
                greenKey=True
            stall1()
        else:
            print("You've already done this")
            stall1()
    elif choose==2:
        insideBathroom()
def stall2():
    global blueCylinder
    print("You enter the first stall")
    print("Press 1 to inspect the toilet")
    print("Press 2 to go back")
    choose = int(input())
    if choose == 1:
        if blueCylinder == False:
            print("You inspect the toilet")
            print("You find a blue cylinder behind the toilet")
            print("Press 1 to pick up the cylinder")
            if int(inpuyt()) == 1:
                print("You pick up the key")
                print("Blue Cylinder Collected")
                blueCylinder = True
            stall2()
        else:
            print("You've already done this")
            stall2()
    elif choose == 2:
        insideBathroom()
def sink2():
    global hotWaterPercent2, coldWaterPercent2, messageShown
    if messageShown == False:
        print("The sink has 2 handles: hot and cold")
        print("Press 1 to increase hot water")
        print("Press 2 to increase cold water")
        print("Press 3 to go back")
        choose = int(input())
        if choose == 1:
            print("You increased the hot water percent by 5%")
            hotWaterPercent2 += 5
            if hotWaterPercent2 > 100:
                hotWaterPercent2 = 0
            print("Hot water percent is " + hotWaterPercent2.__str__() + "%")
            if hotWaterPercent == ranNum+ranNum2 and coldWaterPercent2 == ranNum3+ ranNum4:
                print("A fog from the water forms")
                print("The fog rises and is absorbed into the mirror")
                print("A message appears on the mirror")
                print("Security door: What gets bigger the more you take away?")
                print("Hint: Emptiness")
                print("PS: just use the word")
                messageShown = True
            sink2()
        elif choose == 2:
            print("You increased the cold water percent by 5%")
            coldWaterPercent2 += 5
            if coldWaterPercent2 > 100:
                coldWaterPercent2 = 0
            print("Cold water percent is " + coldWaterPercent2.__str__() + "%")
            if hotWaterPercent == ranNum + ranNum2 and coldWaterPercent2 == ranNum3 + ranNum4:
                print("A fog from the water forms")
                print("The fog rises and is absorbed into the mirror")
                print("A message appears on the mirror")
                print("Security door: What gets bigger the more you take away?")
                print("Hint: Emptiness")
                print("PS: just use the word")
                messageShown = True
            sink2()
        elif choose == 3:
            insideBathroom()
    else:
        print("A message appears on the mirror")
        print("Security door: What gets bigger the more you take away?")
        print("Hint: Emptiness")
        print("PS: just use the word")
        cell()
def garage():
 global garageOpened, weapon, alienAttack, alienKilled, area
 if garageOpened==False:
  print("There is no visible way to open the door")
  print("Keep on looking")
  photoRoom()
 else:
    print("Press 1 to open the garage door")
    if int(input())==1:
        if alienKilled==False:
            if weapon==False:
                print("You open the garage door and step into the garage")
                print("Right then a strong creature attacks you...")
                print("You wake up back in the cell confused")
                print("There is now a person in the cell next to you")
                print("Go talk to them")
                alienAttack=True
                area="cell"
                cell()

            else:
                print("You open the garage door and step into the garage")
                print("The creature attacks you")
                print("Press 1 to block")
                if int(input())==1:
                    print("Press 2 to shoot the creature")
                    if int(input())==2:
                        print("You shoot the creature")
                        print("The creature dies")
                        print("You can enter the garage")
                        alienKilled=True
                        area="garage"
                        insideGarage()
                    else:
                        print("Wrong button, the creature kills you")
                        print("You respawn at the garage door")
                        garage()
                else:
                    print("Wrong button, the creature kills you")
                    print("You respawn at the garage door")
                    garage()
def insideGarage():
    global area
    print("You enter the garage")
    print("Goal: Escape the police station")
    print("1: Wall")
    print("2: Car")
    print("3: Garage Door Exit")
    print("4: Hallway")
    print("5: Note Book")
    choose=int(input())
    if choose==1:
        wall2()
    elif choose==2:
        car()
    elif choose==3:
        garageExit()
    elif choose==4:
        area="hallway"
        hallway()
    elif choose==5:
        noteBook()
def wall2():
    global storageKey
    print("You look at the wall")
    print("The keys to the car key storage are hanging on the wall")
    print("Press 1 to pick them up")
    if int(input())==1:
        print("You pick up the car key storage keys")
        print("Storage Keys Collected")
        storageKey=True
        insideGarage()
def car():
    global carKeys, inCar
    if carKeys==True:
        print("Press 1 to open the car door")
        if int(input())==1:
            print("You enter the car")
            inCar=True
            insideCar()
    else:
        print("You need to find the car keys first")
        insideGarage()
def insideCar():
    print("Goal: Escape the police station")
    print("1: Drive to garage door")
    print("2: Turn on radio")
    print("3: Exit Car")
    choose=int(input())
    if choose==1:
        garageExit()
    elif choose==2:
        print("Radio: Aliens over runned the town")
        print("Stay inside yours cars or you will die")
        print("Get out of town now")
        insideCar()
    elif choose==3:
        print("You exit the car")
        insideGarage()
def garageExit():
    global inCar
    if garageCard==True
        if inCar==True:
            print("Press 1 to scan the card and open garage door")
            if int(input())==1:
                print("The garage door opens")
                print("The streets are covered in aliens")
                print("They start to attack you but your safe in the car")
                print("Press 1 to drive away")
                if int(input())==1:
                    print("You escaped")
                    print("Game Over")
                    print("To be continued...")
        else:
            print("Press 1 to scan the card and open garage door")
            print("Press 2 to go back")
            choose=int(input())
            if choose==1:
                print("The aliens attacked you and you were defenseless")
                print("You respawn in the garage")
                insideGarage()
            elif choose==2:
                insideGarage()
    else:
        print("You need to find the garage card to open the garage door")
def hallway():
 global area
 print("Goal: Escape the police station")
 print("1: Photo Room")
 print("2: Office")
 print("3: Security Room")
 print("4: Bathroom")
 print("5: Garage")
 print("6: Note Book")
 choose=int(input())
 if choose==1:
  area = "photoroom"
  photoRoom()

 elif choose==2:
  area = "office"
  office()

 elif choose == 3:
  security()
 elif choose == 4:
  bathroom()
 elif choose == 5:
  garage()
 elif choose==6:
     noteBook()
def main():
    import random
    global firstTime, ranNum, ranNum2, ranNum3, ranNum4
    if firstTime==False:
        ranNum = random.randrange(0, 50, 5)
        ranNum2 = random.randrange(0, 50, 5)
        ranNum3 = random.randrange(0, 50, 5)
        ranNum4 = random.randrange(0, 50, 5)
        firstTime = True
        cell()
main()