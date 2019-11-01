"""
The syntax to open a file object in Python is: 
file_object  = open(“filename”, “mode”) where file_object is the variable to add the file object. 

The second argument you see – mode – tells the interpreter and developer which way the file will be used.
Mode


Including a mode argument is optional because a default value of ‘r’ will be assumed if it is omitted. The ‘r’ value stands for read mode, which is just one of many. 

The modes are: 

    ‘r’ – Read mode which is used when the file is only being read 
    ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
    ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
    ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file 

So, let’s take a look at a quick example. 
"""

file = open("testfile.txt", "r") 
for line in file: 
	print(line)
	
file.close() 