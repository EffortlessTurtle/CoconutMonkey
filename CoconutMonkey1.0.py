#       <CoconutMonkey, Recursive file consolidator, v1.0,Github,EffortlessTurtle>


#This is a python language CLI port for a program I wrote in C# (https://github.com/EffortlessTurtle/Wanorexia)
#This is supposed to walk down to the bottom of a file tree and recursively
#Move the files to the containing pathway OR a target directory

# Imports
import shutil
import time
import os
import sys
from os.path import abspath, dirname
    
# Functions
def POBox():    #Determines TARGET
    """---Takes input from user for destination folder. Then tests to ensure the destination is a 
    legitimate path. Prompts user and a 'do it again' message if destination target isn't legit.---"""
    #Shows defauld path
    dest = dirname(abspath(__file__))  #finds dir and abs path to file's parent
    print()
    print('Current target: ' + str(dest))
    choices = ('y', 'n', 'q', 'h')
    #choose is a variable used to check the user's target folder
    choose = input('Send somewhere else? Y/N or Q to exit: ')
    if choose.lower() in choices:
        
        if choose.lower() == choices[0]:
            
            #If user chooses y
            dest2 = input('Where would you like to send? (path): ')
            valid_check = os.path.lexists(dest2)
            
            #Checks path validity
            if valid_check == True:
                print('Purge target: ' + str(dest2))
                return dest2
            else:
                print('path not valid')
                POBox()
        
        elif choose.lower() == choices[1]:
            #If user chooses n
            return abspath(dest)  
        
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
        print('Program reseting')
        POBox()

def MailRoom():     #Determine SOURCE
    """File's path as default SOURCE. This checks user's source, and takes correction (if needed).
    This then validates paths given by user, the returns the Source Directory path
    """
    
    src = dirname(abspath(__file__))
    print('current source is: ' + str(src))
    confirm = input('Pull files from here? Y/N/Q: ')
    choices = ('y', 'n', 'q', 'h', '') #Tuple used to make choices a bit smoother
    
    #Goes through logic to decide what the user has told the program
    if confirm.lower() in choices:
        
        if confirm.lower() == choices[0]:
            #If user chooses Y
            print('Source: ' + str(src))
            return abspath(src)
        
        elif confirm.lower() == choices[1]:
            #If user chooses N
            while True: #Loop for user to amend SOURCE folder 
                
                correction = input('Please enter new source (path): ')               
                correction_valid_check = os.path.lexists(str(correction))
                if correction_valid_check == True:
                    #If the new path to target is valid return that correction
                    print('New source: ' + correction)
                    src = correction
                    return abspath(src)
                
                elif correction.lower() == choices[4]:
                    #if user just hits enter
                    print('current source: ' + src)
                    return abspath(src)
                
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
            print('--help option under construction--')  #Dead, but left on purpose
            MailRoom()
            
def Mover():    #moves files
    """---This goes recursively into a user defined file tree and moves them to a user defined target 
    folder. This handles most common exceptions"""
    
    src = MailRoom()
    dest = POBox()    
    i = 0
    
    while True: #Loop for multiple targets
        for root, dirs, files in os.walk(src):  
            for file in files:
                
                try:
                    src_path = os.path.join(root,file)
                    dest_path = os.path.join(dest,file)
                    shutil.move(src_path, dest_path)
                    print(str(src_path) + ' > ' + str(dest_path))
                    
                except FileNotFoundError as fe:
                    #let the user know there isn't a file here
                    print(str(fe))
                    
                except shutil.SameFileError:
                    #if the same file is found add an _1 (i.e., <file_name>_1.<ext>) at the end
                    src_path = os.path.join(root,file)
                    spl = os.path.split(file)
                    spl2 = str(spl[0]) + '_1'
                    file2 = os.path.join(spl2,spl[1])
                    dest_path = os.path.join(dest, file2)
                    shutil.move(src_path, dest_path)
                    print(str(src_path) + ' > ' + str(dest_path))
                    
                except:
                    #catching everything else, let user know
                    print('error occured at file: ' + str(src_path))
                    
        #Repeat this or exit? code chunk
        i += 1   
        if i == 10:
            print('race condition detected, exiting program')
            break
        else:                 
            choice = ('y', 'n')
            print()  #Just for readability
            print('sent to: ' + str(dest))
            again = input('again? Y/N ') #Determine if user wants to do it again
            again2 = again.lower()

            if again2 in choice:
                if again2 == choice[0]:
                    #allows user to retarget different folders
                    Mover()
                elif again2 == choice[1]:
                    print('The monkey leaves the coconut tree')
                    sys.exit()
        
def Main():    #Shows intro, eventually allows for settings
    
    print('\t'*4 +"---Coconut Monkey v1.0---")
    print('\n'*2)
    print('\t'*2 +"---Made by Effortless Turtle---" + '\n' *3)
    start = input("<Enter> to continue / H for help / S for settings / Q to quit: ")
    time.sleep(.1)  #fixes a race condition
    choices = [ '', 'h','s','q']
    i = 0
    
    while True:
        if start.lower() in choices:
            
            if start.lower() == choices[0]:
                #If user presses enter
                Mover()
                
            elif start.lower() == choices[1]:
                #if user chooses h
                print("--- Help section under Construction---")
                continue
                
            elif start.lower() == choices[3]:
                #if user chooses q
                print('You have quit')
                sys.exit()
                
            elif start.lower() == choices[2]:
                #if user chooses S
                print("--- Settings under construction---")    
                continue
                #could I do some wizardry with a number somewhere? maybe an list index?
        else:  #safety mechanism, leftover from early in development. Kept b/c it's a good idea
            print("That isn't a valid response")
            i += 1
            
            if i == 10:
                print('race condition detected, exiting program')
                break
            else:
                continue
        i += 1
    sys.exit()
  
# ---Running parts---
Main()
