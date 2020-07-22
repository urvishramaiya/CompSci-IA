import csv;
import os;

univFilePath = "../"# A universal Filepath to the location of program's FileSystem

def questionbank_add(Q,A,B,C,D,CAns,CurrBank):#Function to add questions to a QuestionBank DataBase
    with open("%sFileSystem/SuperV/Test_sets/tBank/%s"%(univFilePath,CurrBank), "a+") as file_handle:#FileHandling
        reader = csv.reader(file_handle, delimiter=',');#Initiation of reader handle
        writer = csv.writer(file_handle, delimiter=',');#Initiation of writer handle
        
        file_handle.seek(0) #Resests the cursor to the top of the file
        sl_no = 1           #Slot Number Counter to number the levels of data
        
        for x in reader:#Iteration loop through reader handle
           sl_no+=1     #Counts the number of rows present in the database
        writer.writerow([sl_no,Q,A,B,C,D,CAns]);
        
def questionbank_preview(bank):#returns the entire contents of a QuestionBank databse
    with open("%sFileSystem/SuperV/Test_sets/tBank/%s"%(univFilePath,bank), "a+") as file_handle:
        reader = csv.reader(file_handle, delimiter=',');#Initiation of reader handle
        writer = csv.writer(file_handle, delimiter=',');#Initiation of writer handle
        preview = [] #Array that stores the entire database for live use in the program (eg: previewing database contents)
        
        file_handle.seek(0);#Resests the cursor to the top of the file
        
        for row in reader:      #Iteration loop through reader handle
            preview.append(row) #Appends 1 row of database at a time (iteratively) into elements (2D array of elements of rows)
            
        return preview          #Returns the entire database to the class that calls it
            #print(row) DEBUGGER
        

def questionbank_remove(qNums,CurrBank):#Function to remove questions from a QuestionBank DataBase
    row_mem = []#Holds entire questionbank database for live use by program
    try:
        with open("%sFileSystem/SuperV/Test_sets/tBank/%s"%(univFilePath,CurrBank), "r+") as file_handle:
            reader = csv.reader(file_handle, delimiter=',');#Initiation of reader handle
            writer = csv.writer(file_handle, delimiter=',');#Initiation of writer handle

            file_handle.seek(0) #Resests the cursor to the top of the file
            x_count = 0;        #Counter that checks for serial number of question to be removed
        
            for row in reader:          #Iteration loop through reader handle
                if(row[0]!=qNums):      #Checks for serial number match
                    row_mem.append(row) #If doesn't match, then append to live array (temp database)
                x_count += 1
                    
            if x_count == 0:
                return 'QuestionBank Empty' #Empty database handling statement
            
            #print(row_mem) debugging purposes
            file_handle.close()
        with open("%sFileSystem/SuperV/Test_sets/tBank/%s"%(univFilePath,CurrBank), "w+") as file_handle:
            reader = csv.reader(file_handle, delimiter=',');#Initiation of reader handle
            writer = csv.writer(file_handle, delimiter=',');#Initiation of writer handle

            x_count = 1

            for row_append in row_mem:      #Iteration loop through temporary database array
                row_append[0] = x_count     #Serialisation
                writer.writerow(row_append) #Filewriter
                #print(row_append[0])       #debugging purposes
                x_count += 1

    except Exception:
        print("Unable to handle file")#Error handling erratic behaviour

def setBank(setName, confirmation=None):#Polymorphised function to create/remove test sets
    #TestSet add new testBank polymorphised
    if confirmation is None:#Functional Polymorphism in python
        setName = setName + ".csv"
        flag_duplicate = False  #Duplicate error checking
        fileList = []           #holds directory content list
        fileList = os.listdir("%sFileSystem/SuperV/Test_sets/tBank"%(univFilePath)) #Searches directory contents
        for x in fileList:
            if x == setName:
                flag_duplicate = True #Flags duplicate
        if flag_duplicate == False: #Flag condition checking
            try:
                open("%sFileSystem/SuperV/Test_sets/tBank/%s" %(univFilePath,setName), "w+")
            except:
                print("unexpected error")   #Unexpected error handling
        elif confirmation is not None:
            print("duplicate exists")       #Duplicate error handling
    else:
        #TestSet remove testBank polymorphised
        setName = setName + ".csv"
        try:
            os.remove("%sFileSystem/SuperV/Test_sets/tBank/%s" %(univFilePath,setName)) #Uses os library to remove test Database
        except:
            print("file does not exit")#Unexpected error handling
            return 1;

            
#Legacy Code UPDATED
'''def setBank(setName,confirmation):#certified working + add try catch,polymorphism
    #TestSet remove polymorphised
    setName = setName + ".csv"
    try:
        os.remove("%sFileSystem/SuperV/Test_sets/tBank/%s" %(univFilePath,setName))
    except:
        print("file does not exit")#
    #needs return statement'''

#DEBUGGER
#questionbank_add('Question','A','B','C','D','ans')
'''
questionbank_remove('1')
questionbank_preview()
make_set("lol")
rm_set("lol")
'''


