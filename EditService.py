#Avery Moore
#Entry Updating Microservice

import time
import fileinput


def update_entry(original, new, file):
    """
    Updates the given entry 'original' to 'new' in the given file
    """

    entry_found = False
    err = False
    try:
        #Open the given file with redirected output
        with fileinput.input(files=file, inplace=True) as f:
            for line in f:
                new_line = line.strip()             #Remove newline character
                args = new_line.split(",")

                #Check if there is ',' separating attributes
                if len(args) == 1:
                    entry = line.strip()
                else:
                    entry = args[0]

                #If original entry was found, replace the original line with the updated entry
                #Otherwise, print the original line to the file
                if entry == original:
                    print(new_line.replace(original, new))
                    entry_found = True
                else:
                    print(new_line)
    except:
        err = True

    #Write status message to UpdateEntry.txt
    with open("UpdateEntry.txt", "w") as f:
        if entry_found:
            f.write("Found and replaced " + original + " successfully!")
        elif err:
            f.write("Error opening file " + file)
        else:
            f.write("Error: Entry " + original + " not found")

def update_attribute(entry, new, file):
    """
    Updates a given entry's attribute in the given file
    """
    entry_found = False
    err = False
    try:
        #Open the given file with output redirected
        with fileinput.input(files=file, inplace = True) as f:
            for line in f:

                new_line = line.strip()                 #Remove newline character
                arg = new_line.split(",")

                #If entry was found and it contains a valid attribute, update line with new attribute
                #Otherwise, write original line to file
                if arg[0] == entry and len(arg[0]) != len(new_line):
                    print(new_line.replace(arg[1], new))
                    entry_found = True
                else:
                    print(new_line)
    except:
        err = True

    #Print status message to UpdateEntry.txt
    with open("UpdateEntry.txt", "w") as f:
        if entry_found:
            f.write("Updated attribute for " + entry + " successfully!")
        elif err:
            f.write("Error opening file " + file)
        else:
            f.write("Error: Entry " + entry + " not found")


def start():
    """
    Recieves commands from UpdateEntry.txt, given as:
    UPDATE ENTRY [Original Name], [New Name], [Filename]
    UPDATE ATTRIBUTE [Entry name], [New value], [Filename]
    """

    while True:
        time.sleep(1)
        with open("UpdateEntry.txt", "r+") as f:
            #Split contents between command and arguments
            line = f.readline()
            args = line.split(", ")
            command = args[0].split(" ")

            if len(command) > 3:
                i = 3
                while i < len(command):
                    #Re-combine first argument if it contains spaces
                    command[2] += " "
                    command[2] += command[i]
                    i += 1
            if command[0] == "UPDATE":
                #Check for and run the proper command
                args = line.split(", ")
                try:
                    if command[1] == "ENTRY":
                        update_entry(command[2], args[1], args[2])
                    elif command[1] == "ATTRIBUTE":
                        update_attribute(command[2], args[1], args[2])
                except:
                    with open("UpdateEntry.txt", "w") as f:
                        f.write("Error: too few arguments given")


start()