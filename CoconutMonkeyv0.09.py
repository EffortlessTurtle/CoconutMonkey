#       <CoconutMonkey, Recursive file consolidator, v0.09,Github,EffortlessTurtle>


#This is a python language CLI port for a program I wrote in C# (https://github.com/EffortlessTurtle/Wanorexia)
#This is supposed to walk down to the bottom of a file tree and recursively
#Move the files to the containing pathway OR a target directory

# This is a python language port for a program I wrote in C#
# This is supposed to walk down to the bottom of a selected file tree and recursively
# Move the files to the containing pathway/a target directory
# Iteration 8
# I discovered that I have been trying to do this wrong the entire time, I should have been using os.rename, but I 
# made a mistake in reinforcing that failure. Mover() will have a completely new set up, but keeping the for loop.
# 
# 
# .
# Notes:
# ++os.path.splitext(), gives tuple with file name in position[0] and file ext in position[1]. 
# Maybe I can use dictionaries to compare the pos[1] and filter or sort the output files?
# ++ for filter, make 1 dir with 1 subdirectory, main directory is what you want, one subdirectory
# is all unrecognized file ext. place txt document of filtered file names WITH PATH in wanted folder.
# 
# ++TODO:
# ++ Fix false negatives on pathways (I suspect a permissions issue) (fixed? 22MAR22) [race condition, currently fixing]
# ++ Build function to MOVE files, use it as default (fixed)
# ++ make way to choose Copy or move and filtering. Use settings?
# ++ Make Dictionaries for filtering? (fixed, probably won't need)
# ++ for filter, make 1 dir with 1 subdirectory, main directory is what you want, one subdirectory is all unrecognized file ext.
# place txt document of filtered file names WITH PATH in wanted folder.
#
# ++TODO:
# ++ Make move the default and copy an option
# ++ Fix false negatives on pathways (fixed? 22MAR22) [duct tape with counter in Main()]
# ++ work out file picking, instead of copying whole tree
# ++ Work on naming files with same name try:except setup.
# ++ rework renaming scheme
# ++ make way to choose Copy or move and filtering. Use settings? (NOTE: idea, use a dictionary to hold temporary options)
# ++ Should I make move and copy and name filtering into a class?
# ++ make the purged dir again, that was a good idea.
#
#
#
#
#
#
#
#####################################################################################
# 
# (NOTE: what if I used some derivation of os.path.splitdrive(target)> os.path.join path[1] of target and name of folder> join again to path[2]
# > move file to destination folder)
#
# NOTE: Time module contains sleep() method that can be used to wait a certain period of time in python before taking input.(will this
# fix my race condition?)

# Imports
import shutil
import os
import sys
from os.path import abspath
    
# Functions
def POBox():    #Determines TARGET
    """Takes input from user for destination folder. Then tests to ensure the destination is a legitimate path. 
    Kicks an error and a 'do it again' message if destination target isn't legit. TODO: I need to make this a path plus a folder
    This will necessitate a mkdir and something else in Motor() for loop."""
    #Shows default path
 
    dest = '<target>'
    print()
    print('Current target: ' + str(dest))
    choices = ('y', 'n', 'q', 'h')
    #choose is a variable used to check the user's target folder
    choose = input('Send somewhere else? Y/N or Q to exit: ')
    if choose.lower() in choices:
        if choose.lower() == choices[0]:
            #If user chooses y
            dest2 = input('Where would you like to send this (path): ') 
            #Checks path validity
            valid_check = os.path.isdir(dest2)
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
    src = os.path.join('<target>','<target>')
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
                #NOTE: LOGIC ERROR: Sometimes valid paths not considered valid
                """There is a logic error here where valid paths are still not considered valid """                
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
            print('--help option under construction--')
            MailRoom()

def Mover():    #moves files
    """ This is an almost copy of Motor(). It just has the move function instead of the copy function """
    print('Mover')  #NOTE: signpost
    src = MailRoom()
    dest = POBox()
    # Make the thing to make a folder in the target folder
    # ++Add a check to see if there is already a Path in the target; if there is a path, just use it.
    #       if there isn't a path, make one and append that folder name onto the path. (Allows a 
    #       suitable amount of control over the path)
    
    while True: #Loop for multiple targets
        print(str(dest)+' <-dest, Mover()') #NOTE: signpost
        print(str(src) + ' <- src, Mover()\n') #NOTE: signpost
        print(src)
        list_of_files = []
        for root, dirs, files in os.walk(src):
            for file in files:
                try:
                    print(str(file) + ' <- file, Mover()')
                    src_path = os.path.join(root,file)
                    dest_path = os.path.join(dest, file)
                    shutil.move(src_path, dest_path)
                except FileNotFoundError as fe:
                    print(str(fe))
                except shutil.SameFileError as sf:
                    src_path = os.path.join(root,file)
                    spl = os.path.split(file)
                    spl2 = str(spl[0]) + '_1'
                    file2 = os.path.join(spl2,spl[1])
                    dest_path = os.path.join(dest, file2)
                except:
                    print('error occured at file: ' + str(src_path)
                           
        #Repeat this or exit? code chunk            
        choice = ('y', 'n')
        print()  # Just for readability
        print('sent to: ' + str(dest))
        again = input('again? Y/N ') #Determine if user wants to do it again
        again2 = again.lower()
        if again2 in choice:
            if again2 == choice[0]:
                continue
            elif again2 == choice[1]:
                print('The monkey leaves the coconut tree')
                sys.exit()

def Motor(): #copies files
#I'm aware this is dead code right now, I'm going to incorporate this later.
    print('Motor')  #NOTE: signpost
    while True: #Loop for multiple targets
        src = MailRoom()
        dest = POBox()
        logic_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        suf_letter = [
            'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y','z'
        ]
                          
        for root, dirs, files in os.walk((os.path.normpath(src)), topdown=False):
            i = 0
            log_count = 0
            count =0
            for name in files:
                #print(type(name))  #Type: str
                i = i + 1
                name2 = str(name)
                try:
                    SourceFolder = os.path.join(root, name2)      # NOTE: SOURCE PATH
                    TargFolder = os.path.join(dest, name2)    # NOTE: TARGET PATH             
                    NameCheck = os.path.lexists(TargFolder)    
                    if NameCheck == True:
                        Splitter = os.path.splitext(TargFolder) #Splits text for editing, gives tuple output (<path>)
                        spl_list = list(Splitter)  #OUTPUT: 
                        fil_nm = spl_list[0]
                        shutil.copy2(SourceFolder, TargFolder)
                        print(str(SourceFolder) + '  >  ' + str(TargFolder))
                    else:
                        #This will iterate through 'shutil.SameFileError's until file name : 'filename_<num><num><letter>.ext'
                        try:
                            Splitter = os.path.splitext(TargFolder) #Splits text for editing, gives tuple output (<path>)
                            spl_list = list(Splitter)
                            fil_nm = spl_list[0]
                            try_name_1 = str(fil_nm) + '_' + str(logic_list[log_count]) # 'filename_<num>.ext'
                            fil_nm = try_name_1
                            fixed_name = str(spl_list[0] + spl_list[1])
                            try1 = os.path.join(TargFolder, fixed_name)
                            shutil.copy2(SourceFolder, try1)
                            print(str(SourceFolder) + '  >  ' + str(try1))
                            if log_count > 9: #Making sure log_count never gets over logic_list max index
                                lg_fix = log_count - 10
                                log_count = lg_fix
                            if count > 25:  #to make sure the count is never greater than the index of suf_letter max list
                                cnt_fix = count - 26
                                count = cnt_fix
                                
                        except shutil.SameFileError:                   #catches name errors and corrects
                            print('shutil.SameFileError' )          
                            log_count = 0
                            count = 0
                            if log_count > 9: #Making sure log_count never gets over logic_list max index
                                lg_fix = log_count - 10
                                log_count = lg_fix
                            if count > 25:  #to make sure the count is never greater than the index of suf_letter max list
                                cnt_fix = count - 26
                                count = cnt_fix
                            try:
                                #This will iterate through 'shutil.SameFileError's until file name : 'filename_<num><num><letter>.ext'
                                try_name_1 = str(fil_nm) + '_' + str(logic_list[log_count]) # 'filename_<num>.ext'
                                fil_nm = try_name_1
                                fixed_name = str(spl_list[0] + spl_list[1])
                                try1 = os.path.join(TargFolder, fixed_name)
                                shutil.copy2(SourceFolder, try1)
                                print(str(SourceFolder) + '  >  ' + str(try1))
                            
                            except shutil.SameFileError:
                                if log_count > 9: #Making sure log_count never gets over logic_list max index
                                    lg_fix = log_count - 10
                                    log_count = lg_fix
                                if count > 25:  #to make sure the count is never greater than the index of suf_letter max list
                                    cnt_fix = count - 26
                                    count = cnt_fix
                                try:
                                    try_name_2 = str(fil_nm) + '_' + str(logic_list[log_count]) + str(logic_list[log_count])
                                    fil_nm = try_name_2
                                    fixed_name = str(spl_list[0] + spl_list[1])
                                    try2 = os.path.join(TargFolder, fixed_name)
                                    shutil.copy2(SourceFolder, try2)  # 'filename_<num><num>.ext'
                                    print(str(SourceFolder) + '  >  ' + str(try2))
                                except shutil.SameFileError:
                                    if log_count > 9: #Making sure log_count never gets over logic_list max index
                                        lg_fix = log_count - 10
                                        log_count = lg_fix
                                    if count > 25:  #to make sure the count is never greater than the index of suf_letter max list
                                        cnt_fix = count - 26
                                        count = cnt_fix
                                    try:
                                          
                                        try_name_3 = str(fil_nm) + '_' + str(logic_list[log_count]) + str(logic_list[log_count] + 
                                        suf_letter[count])  # 'filename_<num><num><letter>.ext'
                                        fil_nm = try_name_3
                                        fixed_name = str(spl_list[0] + spl_list[1])
                                        try3 = os.path.join(TargFolder, fixed_name)
                                        shutil.copy(SourceFolder, try3)
                                        print(str(SourceFolder) + '  >  ' + str(try3))
                                    except shutil.SameFileError:
                                        print('FAILED: ' + str(SourceFolder) + '  >>>  ' + str(TargFolder)) #NOTE: signpost
                                        pass
                
                except shutil.SameFileError:
                    print('TotalNamingFailure->' + str(SourceFolder) + '  >>>  ' + str(TargFolder))
                    print('Make log annotation')
                                  
                    count += 1
                    log_count += 1
        choice = ('y', 'n')
        print()  # Just for readability
        print('sent to: ' + str(dest))
        again = input('again? Y/N ') #Determine if user wants to do it again
        again2 = again.lower()
        if again2 in choice:
            if again2 == choice[0]:
                continue
            elif again2 == choice[1]:
                print('The monkey leaves the coconut tree')
                sys.exit()

def test():     # NOTE: signpost
    path = '<target>'
    list_of_files = []
    while True:
        for root, dirs, files in os.walk(path):
            for file in files:
                list_of_files.append(os.path.join(root,file))
        
        os.rename
        print('exit')
        break        
                

def Main():
    #print('main')   #NOTE: signpost
    
    print('\t'*4 +"---Coconut monkey---")
    print('\n'*2)
    print('\t'*2 +"---Made by a weirdo in a garage-sized apartment---" + '\n' *3)
    start = input("<Enter> to continue / H for help / S for settings / Q to quit: ")
    choices = [ '', 'h','s','q']
    i = 0
    while True:
        if start.lower() in choices:
            if start.lower() == choices[0]:
                #If user presses enter
                #Motor()
                Mover()
            elif start.lower() == choices[1]:
                #if user chooses h
                print("--- Help section under Construction---")
            elif start.lower() == choices[3]:
                #if user chooses q
                print('You have quit')
                sys.exit()
            elif start.lower() == choices[2]:
                #if user chooses S
                print("--- Settings under construction---")    
                #could I do some wizardry with a number somewhere? maybe an list index?
        else:
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
