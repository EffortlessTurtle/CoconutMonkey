#       <CoconutMonkey, Recursive file consolidator, v0.06,Github,EffortlessTurtle>


#This is a python language CLI port for a program I wrote in C# (https://github.com/EffortlessTurtle/Wanorexia)
#This is supposed to walk down to the bottom of a file tree and recursively
#Move the files to the containing pathway OR a target directory


"""
Notes:
++os.path.splitext(), gives tuple with file name in position[0] and file ext in position[1]. 
Maybe I can use dictionaries to compare the pos[1] and filter or sort the output files?

++TODO:
++ Fix false negatives on pathways (I suspect a permissions issue)
++ Build function to MOVE files, use it as default
++ make way to choose Copy or move and filtering. Use settings?
++ Make Dictionaries for filtering?
++ for filter, make 1 dir with 1 subdirectory, main directory is what you want, one subdirectory is all unrecognized file ext.
place txt document of filtered file names WITH PATH in wanted folder.


"""





# Imports

from pathlib import PurePosixPath as ppp
import pathlib
import shutil
import os
import sys
from os.path import abspath, dirname



    
# Functions
def POBox():    #Determines TARGET
    """Takes input from user for destination folder. Then tests to ensure the destination is a legitimate path. 
    Kicks an error and a 'do it again' message if destination target isn't legit. TODO: I need to make this a path plus a folder
    This will necessitate a mkdir and something else in Motor() for loop."""
    #Shows defauld path
   
    dest = os.path.join('<target>', 'Anaconda Projects/testFire')
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
                dest = dest2
                return dest
            else:
                print('path not valid')
                POBox()        
        elif choose.lower() == choices[1]:
            #If user chooses n
            print(dest)
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
        print('Program reseting')
        POBox()

def MailRoom():     #Determine SOURCE
    """File's path as default SOURCE. This checks user's source, and takes correction (if needed).
    This then validates paths given by user, the returns the Source Directory path
    """
    #src = dirname(abspath(__file__))
    src = os.path.join('<target>','<target>')
    print('current source is: ' + str(src))
    confirm = input('Pull files from here? Y/N/Q: ')
    choices = ('y', 'n', 'q', 'h', '') #Tuple used to make choices a bit smoother
    #Goes through logic to decide what the user has told the program
    if confirm.lower() in choices:
        if confirm.lower() == choices[0]:
            #If user chooses Y
            print('Source: ' + str(src))
            return src
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

def Mover():    #moves files
    """ This is an almost copy of Motor(). It just has the move function instead of the copy function """
    print('Mover')  #NOTE: signpost
    while True: #Loop for multiple targets
        src = MailRoom()
        dest = POBox()
        print(str(dest)+' <-dest, Mover()\n') #NOTE: signpost
        print(str(src) + ' <- src, Mover()\n') #NOTE: signpost
        print(src)
        for files in os.walk((os.path.normpath(src)), topdown=False):

            i = 0
            print()

            for names in files:
                for name in names:
       
                    print(str(i) + ' <- mover i')
                  
                    i = i + 1

                    
                    SourceFolder = os.path.join(src, str(name))      # NOTE: SOURCE PATH
                    TargFolder = os.path.join(dest, str(name))      # NOTE: TARGET PATH
                    print(str(SourceFolder) + ' <- Source Folder PATH')
                    print(str(TargFolder) + ' <- Targ Folder PATH')
                    try:
                        #SourceFolder = os.path.join(src, name)      # NOTE: SOURCE PATH
                        #TargFolder = os.path.join(dest, name)    # NOTE: TARGET PATH
                        #print(SourceFolder + ' <- SourceFolder') #NOTE:Signpost, Mark for delete
                        #print(TargFolder + ' <- TargFolder') #NOTE:Signpost, Mark for delete
                        NameCheck = os.path.isdir(TargFolder)
                        # print(str(NameCheck) + ' <-NameCheck variable')        #Throws true if filename is already in target #NOTE:Signpost, Mark for delete
                        if NameCheck == True:
                            Splitter = os.path.splitext(TargFolder) #Splits text for editing, gives tuple output (<path>)
                            spl_list = list(Splitter)  #OUTPUT: ['/home/nate/Desktop/Targ/systeminformation', '.xml']
                            fil_nm = spl_list[0]
                            shutil.move(SourceFolder, TargFolder) #edit: TargFolder
                            print(str(SourceFolder) + '  >  ' + TargFolder)    
                            
                    # except FileNotFoundError as er1:
                        # print('file not found -> ' + str(er1))
                    except shutil.SameFileError:   #Exception handling
                        
                        print('shutil.SameFileError')          
                        log_count = 0
                        count = 0
                        logic_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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
                            shutil.move(SourceFolder, try1)
                            print(str(SourceFolder) + '  >  ' + str(try1))
                        except shutil.SameFileError:
                            try:
                                try_name_2 = str(fil_nm) + '_' + str(logic_list[log_count]) + str(logic_list[log_count])
                                fil_nm = try_name_2
                                fixed_name = str(spl_list[0] + spl_list[1])
                                try2 = os.path.join(TargFolder, fixed_name)
                                shutil.move(SourceFolder, try2)  # 'filename_<num><num>.ext'
                                print(str(SourceFolder) + '  >  ' + str(try2))
                            except shutil.SameFileError:
                                try:
                                    suf_letter = [
                                    'a', 'b', 'c', 'd', 'e',
                                    'f', 'g', 'h', 'i', 'j',
                                    'k', 'l', 'm', 'n', 'o',
                                    'p', 'q', 'r', 's', 't',
                                    'u', 'v', 'w', 'x', 'y','z'
                                    ]   
                                    try_name_3 = str(fil_nm) + '_' + str(logic_list[log_count]) + str(logic_list[log_count] + 
                                    suf_letter[count])  # 'filename_<num><num><letter>.ext'
                                    fil_nm = try_name_3
                                    fixed_name = str(spl_list[0] + spl_list[1])
                                    try3 = os.path.join(TargFolder, fixed_name)
                                    shutil.move(SourceFolder, try3)
                                    print(str(SourceFolder) + '  >  ' + str(try3))
                                except shutil.SameFileError:
                                    print('FAILED: ' + str(SourceFolder) + '  >>>  ' + str(TargFolder)) #NOTE: signpost
                                    pass                
                                    count += 1
                                    log_count += 1
                        else: 
                            try:       
                                log_count = 0
                                count = 0
                                logic_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

                                if log_count > 9: #Making sure log_count never gets over logic_list max index
                                    lg_fix = log_count - 10
                                    log_count = lg_fix
                                    if count > 25:  #to make sure the count is never greater than the index of suf_letter max list
                                        cnt_fix = count - 26
                                        count = cnt_fix
                                    #This will iterate through 'shutil.SameFileError's until file name : 'filename_<num><num><letter>.ext'
                                try_name_1 = str(fil_nm) + '_' + str(logic_list[log_count]) # 'filename_<num>.ext'
                                fil_nm = try_name_1
                                fixed_name = str(spl_list[0] + spl_list[1])
                                try1 = os.path.join(TargFolder, fixed_name)
                                shutil.move(SourceFolder, try1)
                                print(str(SourceFolder) + '  >  ' + str(try1))
                            except shutil.SameFileError:
                                try:
                                    try_name_2 = str(fil_nm) + '_' + str(logic_list[log_count]) + str(logic_list[log_count])
                                    fil_nm = try_name_2
                                    fixed_name = str(spl_list[0] + spl_list[1])
                                    try2 = os.path.join(TargFolder, fixed_name)
                                    shutil.move(SourceFolder, try2)  # 'filename_<num><num>.ext'
                                    print(str(SourceFolder) + '  >  ' + str(try2))
                                except shutil.SameFileError:
                                    try:
                                        suf_letter = [
                                        'a', 'b', 'c', 'd', 'e',
                                        'f', 'g', 'h', 'i', 'j',
                                        'k', 'l', 'm', 'n', 'o',
                                        'p', 'q', 'r', 's', 't',
                                        'u', 'v', 'w', 'x', 'y','z'
                                        ]   
                                        try_name_3 = str(fil_nm) + '_' + str(logic_list[log_count]) + str(logic_list[log_count] + 
                                        suf_letter[count])  # 'filename_<num><num><letter>.ext'
                                        fil_nm = try_name_3
                                        fixed_name = str(spl_list[0] + spl_list[1])
                                        try3 = os.path.join(TargFolder, fixed_name)
                                        shutil.move(SourceFolder, try3)
                                        print(str(SourceFolder) + '  >  ' + str(try3))
                                    except shutil.SameFileError:
                                        print('FAILED: ' + str(SourceFolder) + '  >>>  ' + str(TargFolder)) #NOTE: signpost
                                        pass
                                    
                                    
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
                        spl_list = list(Splitter)  #OUTPUT: ['/home/nate/Desktop/Targ/systeminformation', '.xml']
                        fil_nm = spl_list[0]    
                        shutil.copy2(SourceFolder, TargFolder)
                        print(str(SourceFolder) + '  >  ' + str(TargFolder))
                    else:
                        try:
                            Splitter = os.path.splitext(TargFolder) #Splits text for editing, gives tuple output (<path>)
                            spl_list = list(Splitter)  #OUTPUT: ['/home/nate/Desktop/Targ/systeminformation', '.xml']
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

def Main():
    print('main')   #NOTE: signpost
    
    print("Coconut monkey")
    print("Made by a weirdo in a garage-sized apartment")
    start = input("<Enter> to continue / H for help / S for settings / Q to quit: ")
    choices = [
        '', 'h','s','q']
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
                break
            else:
                continue
    i += 1
#
#  Currently:
#      For some reason the functions aren't returning the correct addresses, I'm figuring out whether 
#      to make a class for the move and copy functions or to consolidate a lot 
#      or if I need to do something else. 22MAR2022-1622
#  


"""---Running parts---"""
#Motor()
Main()





# TODO:
# Make move the default and copy an option
# Fix false negatives on pathways
    

# Throws: "OSError: [Errno 16] Device or resource busy: '/' -> '/'", if folder doesn't exist
