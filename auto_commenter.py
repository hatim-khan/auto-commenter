"""
Author: Hatim Khan
Date Started: 9/27/15
"""
from function_abstraction import *

print('*********************************************')
print('*** Welcome to the Auto Commenter Program ***')
print('*********************************************')


#get the name of the file

#make sure the file has an extension
filename = input('Enter in a filename: ')

#
#read through lines and find the lines containing def (functions)
# lines = file.readlines()
# assert len(lines) >= 1, 'This file has no content'

new_file_name = filename[0:-3] + '_commented.py'
new_file = open(new_file_name, 'w+')



found_function = False
function_list =[]
temp_files = [] #used to store files
with open(filename, 'r+') as f:
    current_line = f.readline()
    print(current_line)
    while current_line:
        splitted = current_line.split()
        if len(splitted) == 0:
            print('empty line')
            #do nothing
        #if the line is a function
        elif splitted[0] == 'def' and found_function == False:
            name = splitted[1]
            #get list of args
            args = form_arg_list(splitted)
            found_function = True
        elif splitted == 'return' and found_function == True:
            #returnType = type(evalspltted[1])?
            return_value = spltted[1]
            function_list.append(make_function_outline(name, args, return_value ))
            found_function = False
            #write the function and the rest of the lines
            temp.append(current_line)
            write_function_to_file(f, function_list[-1])
            for line in temp:
                f.write(line)

        if found_function == True:
            temp.append(current_line)
        else:
            f.write(current_line)
        current_line = f.readline()
