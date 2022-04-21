#       <CoconutMonkey, Recursive file consolidator, v0.01,Github,EffortlessTurtle>


#This is a python language CLI port for a program I wrote in C# (https://github.com/EffortlessTurtle/Wanorexia)
#This is supposed to walk down to the bottom of a file tree and recursively
#Move the files to the containing pathway OR a target directory

#Imports

import shutil
import os
import sys
from os.path import abspath, dirname

            
    

def POBox():    #Determines destination
    """Takes input from user for destination folder. Then tests to ensure the destination is a legitimate path. 
    Kicks an error and a 'do it again' message if destination target isn't legit."""
    
    #Shows default path
    dest = dirname(abspath(__file__))
    print()
    print('Current target: ' + str(dest))
    choices = ('y', 'n', 'q', 'h')
    #choose is a variable used to check the user's target folder
    choose = input('Send somewhere else? Y/N or Q to exit: ')
    if choose.lower() in choices:
        if choose.lower() == choices[0]:
            #If user chooses y
            dest = input('Where would you like to send this (path): ') 
            #Checks path validity
            valid_check = os.path.lexists(str(dest))
            if valid_check == True:
                print('Purge target: ' + str(dest))
                return dest
            else:
                print('path not valid')
                POBox()        
        elif choose.lower() == choices[1]:
            #If user chooses n
            print('Purge target: ' + dest)
            return dest  
        elif choose.lower() == choices[2]:
            #If user chooses q
            print('The monkey leaves the coconut tree')
            sys.exit()
        elif choose.lower() == choices[3]:
            #If user chooses h  
            print('--help option under construction--')
            POBox()
            #This is dead and left here on purpose, in case I add anything truly complicated  
    else:
        print('not a valid respose')
        POBox()

def MailRoom():     #Determine Target
    src = dirname(abspath(__file__))
    print('current source is: ' + str(src))
    confirm = input('Pull files from here? Y/N/Q: ')
    choices = ('y', 'n', 'q', 'h', '') #Tuple used to make choices a bit smoother
    #Goes through logic to decide what the user has told the program
    if confirm.lower() in choices:
        if confirm.lower() == choices[0]:
            #If user chooses Y
            return src
        elif confirm.lower() == choices[1]:
            #If user chooses N
            while True: #Loop for user to amend SOURCE folder 
                correction = input('Please enter new source (path): ')
                #NOTE: LOGIC ERROR: Valid paths not considered valid               
                correction_valid_check = os.path.lexists(correction)
                if correction_valid_check == True:
                    #If the new path to target is valid return that correction
                    print('New source: ' + correction)
                    src = correction
                    return src
                elif correction.lower() == choices[4]:
                    #if user just hits enter
                    print('current source: ' + src)
                    return src
                elif correction.lower() == choices[2]:
                   #if the user chooses q
                    sys.exit()    
                else:
                    print('Not a valid path')              
        elif confirm.lower() == choices[2]:
            #If the user chooses q
            print('The monkey leaves the coconut tree')
            sys.exit()
        elif confirm.lower() == choices[3]:     
            #If the user needs help
            print('--help option under construction--')
            MailRoom()
            #This is dead and left here on purpose, in case I add anything truly complicated


def Motor():
    while True: #Loop for multiple targets
        src = MailRoom()
        dest = POBox()
        srcList = list(os.walk(src))
        print(srcList) # type = list
        for file in srcList: #18MAR2022: For now this copies the whole file structure
           # print(file)
            full_file =  os.path(file) + file
            print(full_file)
            shutil.move(file, dest, copy_function = shutil.copy(full_file, dest))
            print(file, dest)
            
        choice = ('y', 'n')
        print('sent to ' + str(dest))
        again = input('again? Y/N ') #Determine if user wants to do it again
        again2 = again.lower()
        if again2 in choice:
            if again2 == choice[0]:
                continue
            elif again2 == choice[1]:
                print('The monkey leaves the coconut tree')
                sys.exit()

        
    
Motor()
        

        
    
    
    
    

    
    
    

    
  