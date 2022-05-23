EditService.py
Written by Avery Moore

Requires python libraries time and fileinput

Run a command by writing UPDATE ENTRY [Entry Name], [New Name], [File to change] or
UPDATE ATTRIBUTE [Entry Name], [Attribute], [File to change] to UpdateEntry.txt.

Assumes entry/attribute are separated by a comma e.g. entry,attribute.

Works by overwriting each line in a file with either its original contents or the new
contents specified by the command.

Make sure to back up your files, content may be erased if process is interupted 
(though automatic backups are made by fileinput).