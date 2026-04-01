import os #built in  module which provides functions to interact with the operating system

def list_files_recursive(path):
    ''' prints all files and directories inside the given path.
      if directory found, calls itself again (recursion) to explore the contents of that directory'''
    
    #print(os.listdir(path)) #list of file names and directory names. these are items
    #os.listdir(path) returns a list containing the names of files and directories inside the specific path
    for item in os.listdir(path):
        #os.path,join(path,item) safely combines the directory path and the file/folder names into a full path
        full_path=os.path.join(path,item) #item-rets of file name, path - holds rest of the path
        '''print(full_path)
        print(item)'''

        if os.path.isfile(full_path): #checks if given path is a file, returns boolean 
            print("File:",full_path) #prints file name
        if os.path.isdir(full_path): #checks if given path is a directory (folder), returns boolean
            print("Directory:",full_path) #prints directory path
            #recursive call the function calls itself to explore the contents of this directory
            list_files_recursive(full_path)
        #iterate through all of files and folders 
        #if its directory then or modhye dhukche sekhane file pele recursion stop so thats the base case


#path=r"C:\Users\MSCLAB-135\Desktop\bindiiiii" - rawstring
path="C:/Users/MSCLAB-135/Desktop/bindiiiii" # or change backslash to front slash
list_files_recursive(path)
#one need of recursion is to access files and directories

