import csv
import os
import traceback
import hashlib
import os

univFilePath = "../"

def add_User(UID, passkey, passkey2,mailID):#Admin Function to add new user
    try:
        with open("%sFileSystem/SuperV/userBase.csv"%(univFilePath), "a+") as file_handle:#File handling
            reader = csv.reader(file_handle, delimiter=',');#File reader handling
            writer = csv.writer(file_handle, delimiter=',');#file writer handling
            file_handle.seek(0)                             #Reset cursor to database top
            
            for x in reader:    #Iteration of reader handle
                if x[0] == UID: #Duplicate error handling
                    return "User already exists"
            if passkey != passkey2:
                return "passwords do not match" #Password match check

            file_handle.seek(2)                 #Cursor seek to database bottom

            m = hashlib.sha256()
            m.update(passkey.encode('utf8'))
            hash = m.hexdigest()

            writer.writerow([UID,hash,mailID])                       #Write new user
            os.mkdir("%sFileSystem/SuperV/User/%s"%(univFilePath,UID))  #Make user file directory
            file_handle.close()     #Memory leak prevention
    except Exception:
        return traceback.print_exc()#Better error messages
    
def check_User(UID, passkey=None):#Functional Polymorphism
    if(passkey is not None):
        try:
            with open("%sFileSystem/SuperV/userBase.csv"%(univFilePath), "r") as file_handle:
                reader = csv.reader(file_handle, delimiter=',');#File writer handling
                file_handle.seek(0)#Reset cursor to database top
                #print(UID,passkey) DEBUGGER Code

                m = hashlib.sha256()
                m.update(passkey.encode('utf8'))
                hash = m.hexdigest()

                for x in reader:
                    #print(x[0],x[1]) DEBUGGER Code
                    if x[0] == UID and x[1] == hash: #Verifies user credentials from database
                        return True
                return False
        except:
            return "Error"
    else:
        try:
            with open("%sFileSystem/SuperV/userBase.csv"%(univFilePath), "r") as file_handle:
                reader = csv.reader(file_handle, delimiter=',');
                file_handle.seek(0)
                #print(UID,passkey)

                for x in reader:
                    #print(x[0],x[1])
                    if x[0] == UID: #Searches if user exists
                        return True
                return False
        except:
            return "Error"


            
def rm_User(UID, passkey):#Remove User credentials from database
    try:
        with open("%sFileSystem/SuperV/userBase.csv"%(univFilePath), "r+") as file_handle:#File handling
            reader = csv.reader(file_handle, delimiter=',');#File reader handling
            writer = csv.writer(file_handle, delimiter=',');#File writer handling

            row_mem = []#Array to temp store entire userBase database
            x_count = 0
            y_count = 0


            m = hashlib.sha256()
            m.update(passkey.encode('utf8'))
            hash = m.hexdigest()
                
            for row in reader:                          #Iteration loop 
                if row[0] != UID or row[1] != hash:  #User delete confirmation credential validation
                    row_mem.append(row)
                x_count += 1
                y_count += 1

            if x_count == 0:
                return "User database empty"#Error handling for empty database
            file_handle.close()             #Memory leak prevention
        with open("%sFileSystem/SuperV/userBase.csv"%(univFilePath), "w+") as file_handle:#File handling
            writer = csv.writer(file_handle, delimiter=',');#File writer handling
            write_count = 0                                 #Counter variable
            

            for row in row_mem:     #Iteration loop to overwrite existing file without removed user
                writer.writerow(row)
                write_count += 1

            file_handle.close()     #Memory leak prevention

        if write_count == y_count - 1:
            return 0#operation confirmation
        else:
            return 1  #Returns if UID password correct
    except:
        return "Unable to remove user"                      #Exception handling unexpected behaviour

#add_User("Denaliis", "lol", "lol", "lolsoop@gmail.com")
#rm_User('Denalii', 'lol')


