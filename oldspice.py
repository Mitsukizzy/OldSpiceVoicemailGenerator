#ITP 125 Final Programming Project
#Written by: Isabella Benavente

import platform #for determining OS
import subprocess #for using commands
import os #for using commands
import urllib.request #for downloading the mp3
import math #integer division using math.floor
import argparse #for command line methods

#set some global variables
gender = ""
number = ""
reasonList = []
reasonTxt = []
endingList = []
endingTxt = []
clipNum = 0 #greetings, number, reasons, endings, jingle
outputName = ""

#dictionary of the corresponding mp3 files to download
mp3Dict = {'0':'0.mp3', '1':'1.mp3', '2':'2.mp3', '3':'3.mp3', '4':'4.mp3', '5':'5.mp3', '6':'6.mp3', '7':'7.mp3', '8':'8.mp3', '9':'9.mp3',
           'm1':'m-b1-hello.mp3', 'm2':'m-b2-have_dailed.mp3', 'm3':'m-r0-cannot_come_to_phone.mp3', 'm4':'m-leave_a_message.mp3',
           'mr1':'m-r4-ripping_weights.mp3', 'mr2':'m-r3-polishing_monocole.mp3', 'mr3':'m-r2-cracking_walnuts.mp3', 'mr4':'m-r1-building.mp3',
           'e1':'m-e1-horse.mp3' , 'e2':'m-e3-on_phone.mp3' , 'e3':'m-e4-swan_dive.mp3' , 'e4':'m-e5-voicemail.mp3',
           'f1':'f-b1-hello_caller.mp3', 'f2':'f-b2-lady_at.mp3', 'f3':'f-r0.1-unable_to_take_call.mp3', 'f4':'f-r0.2-she_is_busy.mp3',
           'f5':'f-e1-she_will_get_back_to_you.mp3', 'f6':'f-e2-thanks_for_calling.mp3',
           'fr1':'f-r1-ingesting_old_spice.mp3', 'fr2':'f-r1-ingesting_old_spice.mp3', 'fr3':'f-r4-moon_kiss.mp3', 'fr4':'f-r3-lobster_dinner.mp3',
           'jingle':'m-e2-jingle.mp3'}

def promptGender():
    #indicate that the variables are global, not local
    global gender

    while True:
        #Prompt for gender until m or f is chosen
        gender = input("\nGender (M/F): ")
        if gender.upper() == 'M' or gender.upper() == 'F':
                break #break out of loop 
        else:
                #display an error message
                print ("Invalid input. Please enter M or F.")
#Ends the promptGender function

def promptNumber():
    #indicate that the variables are global, not local
    global number

    #indicate that the variables are global, not local
    global number

    while True:
        number = input("Phone Number:")
        
        #remove all dashes, spaces, parentheses, and periods from the number
        number = number.replace('-','').replace(' ', '').replace('(','').replace(')','').replace('.','')

        #check if the input now contains all digits
        try:
                val = int(number)
        except ValueError:
                print("That is not a valid number. Try again.\n")
                continue #go back to the start of the loop
            
        print(number)

        #verify that there are 10 digits in the number
        if len(number) > 10:
                print ("Invalid input. More than 10 digits.")
        elif len(number) < 10:
                print ("Invalid input. Less than 10 digits.")
        else:
                #correctly formatted phone number
                break
#Ends the promptNumber function
    
def promptReason():
    #indicate that the variables are global, not local
    global gender
    global reasonList
    global reasonTxt
    global clipNum

    #clear the lists
    del reasonList[:]
    del reasonTxt[:]
    
    print("\nChoose a reason:")
    
    while True:
        if gender.upper() == 'F':
            print ("1 - ingesting my delicious Old Spice man smell.")
            print ("2 - listening to me read romantic poetry while I make a bouquet of paper flowers from each read page.")
            print ("3 - being serenaded on the moon with the view of the earth while surviving off the oxygen of lungs via a passionate kiss.")
            print ("4 - enjoying a lobster dinner I prepared just for her while carrying her on my back safely through piranha infested waters.")
        elif gender.upper() == 'M':
            print ("1 - Ripping out mass loads of weights.")
            print ("2 - Polishing their monocle smile.")
            print ("3 - Cracking walnuts with their man mind.")
            print ("4 - Building an orphanage with their barehands while playing a sweet, sweet lulluby for those children with two mallets against their abs xylophone.")
        #get a value from user
        userInput = input("\nEnter the reasons you want in your voicemail (1-4): ")

        #check if the input is a number, not other characters
        try:
                val = int(userInput)
        except ValueError:
                print("That is not a valid number or string of numbers. Try again.\n")
                continue #go back to the start of the loop
            
        reason = int(userInput)

        while reason > 0:
            digit = reason % 10 #get the end digit
            reason =  math.floor(reason / 10) #cut off the end digit
           
            if digit > 0 and digit <= 4:
                #reasons for female
                if gender.upper() == 'F':
                    #set the contents of reasonTxt to the actual text
                    if digit == 1:
                        reasonList.append(1)
                        reasonTxt.append("ingesting my delicious Old Spice man smell.")
                    elif digit == 2:
                        reasonList.append(2)
                        reasonTxt.append("listening to me read romantic poetry while I make a bouquet of paper flowers from each read page.")
                    elif digit == 3:
                        reasonList.append(3)
                        reasonTxt.append("being serenaded on the moon with the view of the earth while surviving off the oxygen of lungs via a passionate kiss.")
                    elif digit == 4:
                        reasonList.append(4)
                        reasonTxt.append("enjoying a lobster dinner I prepared just for her while carrying her on my back safely through piranha infested waters.")
                #reasons for male
                elif gender.upper() == 'M':
                    #set the contents of reasonTxt to the actual text
                    if digit == 1:
                        reasonList.append(1)
                        reasonTxt.append("Ripping out mass loads of weights.")
                    elif digit == 2:
                        reasonList.append(2)
                        reasonTxt.append("Polishing their monocle smile.")
                    elif digit == 3:
                        reasonList.append(3)
                        reasonTxt.append("Cracking walnuts with their man mind.")
                    elif digit == 4:
                        reasonList.append(4)
                        reasonTxt.append("Building an orphanage with their barehands while playing a sweet, sweet lulluby for those children with two mallets against their abs xylophone.")
            else:
                print("You have entered an invalid input. Try again.\n")
                promptReason() #call the function again

        #reverse the lists since the numbers were taken from the singles digit first
        reasonList.reverse()
        reasonTxt.reverse()
        break #break out of loop, valid input entered                
#Ends the promptReason function

def promptEnding():
    #indicate that the variables are global, not local
    global endingList
    global endingTxt

    #clear the lists
    del endingList[:]
    del endingTxt[:]
    
    print ("\nChoose an ending:")

    while True:
        print ("1 - I'm on a horse.")
        print ("2 - I'm on a phone.")
        print ("3 - SWAN DIVE.")
        print ("4 - This voicemail is now diamonds.")
        userInput = input("Enter the endings you want in your voicemail (1-4): ")

        #check if the input is a number, not other characters
        try:
                val = int(userInput)
        except ValueError:
                print("That is not a valid number or string of numbers. Try again.")
                promptEnding() #calls this function again

        ending = int(userInput)

        while ending > 0:
            digit = ending % 10 #get the end digit
            ending =  math.floor(ending / 10) #cut off the end digit

            if digit > 0 and digit <= 4:
                #set the contents of endingTxt to the actual text
                if digit == 1:
                    endingList.append(1)
                    endingTxt.append("I'm on a horse.")
                elif digit ==2:
                    endingList.append(2)
                    endingTxt.append("I'm on a phone.")
                elif digit == 3:
                    endingList.append(3)
                    endingTxt.append("SWAN DIVE.")
                elif digit == 4:
                    endingList.append(4)
                    endingTxt.append("This voicemail is now diamonds.")              
            else:
                print("You have entered an invalid input. Try again.")
                promptEnding() #calls this function again

        #reverse the lists since the numbers were taken from the singles digit first
        endingList.reverse()
        endingTxt.reverse()
        break #break out of loop, valid input entered            
#Ends the promptEnding function

def summary():
    print("\nSummary\n--------")
    print("Gender : " + gender.upper())
    print("Phone Number: " + number)
    print("\nReason: " )
    for r in reasonTxt:
        print(r)
    print("\nEnding: ")
    for e in endingTxt:
        print(e)

    while True:
        confirm = input("Would you like to create a voicemail with these settings? (Y/N): ")

        if confirm.upper() == "Y":
            break #continue
        elif confirm.upper() == "N":
            #restart from the beginning
            promptUser() #call function again
            #should still continue this loop until Y is entered
        else:
            print("The input you entered is invalid. Please try again.")
#Ends the summary function

def promptUser():
    #calls the functions that prompt the user for all required info
    promptGender()
    promptNumber()
    promptReason()
    promptEnding()    
    summary()    
#End of the promptUser function

#Main part of the code, outside of functions
os.system("copy del *1?.*mp3 & del *2?.*mp3 & del *3?.*mp3 & del *1?.*mp3") #delete all numbered mp3s in the directory            
promptUser() #calls the function to prompt the user

outputName = input("Name of outputted mp3 file: ")

userPlatform = platform.system()
print("You are running " + userPlatform)

#downloading all the needed files
if gender.upper() == 'M':
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['m1'], '10.mp3')
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['m2'], '11.mp3')
    clipNum = 12

    #phone number
    for num in number:
        urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict[num], str(clipNum) + '.mp3')
        clipNum += 1
        
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['m3'], '22.mp3')
    clipNum = 23

    #reason
    for reason in reasonList:
        if reason == 1:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['mr1'], str(clipNum) + '.mp3')
        elif reason == 2:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['mr2'], str(clipNum) + '.mp3')
        elif reason == 3:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['mr3'], str(clipNum) + '.mp3')
        elif reason == 4:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['mr4'], str(clipNum) + '.mp3')
        clipNum += 1 #increment each time
            
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['m4'], str(clipNum) + '.mp3')
    clipNum += 1 #increment each time
    
elif gender.upper() == 'F':
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['f1'], '10.mp3')
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['f2'], '11.mp3')
    clipNum = 12

    #phone number
    for num in number:
        urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict[num], str(clipNum) + '.mp3')
        clipNum += 1
        
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['f3'], '22.mp3')
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['f4'], '23.mp3')

    clipNum = 24

    #reason
    for reason in reasonList:
        if reason == 1:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['fr1'], str(clipNum) + '.mp3')
        elif reason == 2:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['fr2'], str(clipNum) + '.mp3')
        elif reason == 3:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['fr3'], str(clipNum) + '.mp3')
        elif reason == 4:
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['fr4'], str(clipNum) + '.mp3')
        clipNum += 1 #increment each time
    
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['f5'], str(clipNum) + '.mp3')
    clipNum += 1 #increment each time
    urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['f6'], str(clipNum) + '.mp3')
    clipNum += 1 #increment each time
    
#ending
for ending in endingList:
    if ending == 1:
        urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['e1'], str(clipNum) + '.mp3')
    elif ending == 2:
        urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['e2'], str(clipNum) + '.mp3')
    elif ending == 3:
        urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['e3'], str(clipNum) + '.mp3')
    elif ending == 4:
        urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['e4'], str(clipNum) + '.mp3')
    clipNum += 1 #increment each time

while True:
        confirm = input("Want to add the Old Spice jingle at the end? (Y/N): ")

        if confirm.upper() == "Y":
            urllib.request.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + mp3Dict['jingle'], str(clipNum) + '.mp3')
            break #continue
        elif confirm.upper() == "N":
            break #continue without adding jingle
        else:
            print("The input you entered is invalid. Please try again.")


if userPlatform == 'Windows':
    os.system("copy /b *.mp3 " + outputName + ".mp3") #join multiple mp3 files in windows
else: #Linux or MAC
    os.system("cat *.mp3 > " + outputName + ".mp3") #join multiple mp3 files in linux or mac

'''
#start of command line code
parser = argparse.ArgumentParser()
parser.add_argument("gender", type=str, help="holds the gender")
parser.add_argument("-g", "--gender", action="store_true", help="flag for gender")
parser.add_argument("number", type=str, help="holder the phone number")
parser.add_argument("-n", "--number", action="store_true", help="flag for phone number")
parser.add_argument("gender", type=str, help="holds the numbers corresponding to the reasons wanted in the voicemail")
parser.add_argument("-r", "--reason", action="store_true", help="flag for reason")
parser.add_argument("ending", type=str, help="holds the numbers corresponding to the endings wanted in the voicemail")
parser.add_argument("-e", "--ending", action="store_true", help="flag for ending")
parser.add_argument("output", type=str, help="the name that the user wants to name the output voicemail file")
parser.add_argument("-o", "--output", action="store_true", help="flag for output file name")
args = parser.parse_args()

if args.gender:
    print("Gender: " + gender)
if args.number:
    print("Number: " + number)
    '''

