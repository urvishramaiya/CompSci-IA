import csv
import smtplib, ssl
import os
from datetime import date

today = str(date.today())

univFilePath = '../'

def setBankPublish(setName):#TestBank Subset publish to ready to use
    flag_duplicate = False  #Boolean flag variable
    fileList = []           #List of directory contents
    fileList = os.listdir("%sFileSystem/SuperV/Test_sets/tPublish"%(univFilePath))#Searched directory for content
    for x in fileList:              #Iteration through directory content list
        if x == setName:            #Duplicate error handling
            flag_duplicate = True   #Flag handling
    if flag_duplicate == False:
        try:
            open("%sFileSystem/SuperV/Test_sets/tPublish/%s" %(univFilePath,setName), "w+")#Exception Handling file open
        except:
            print("unexpected error")   #Unexpected behaviour handling
    else:
        print("duplicate exists")       #Duplicate error handling
        return 1

def questionbank_add_Publish(Q,A,B,C,D,CurrBank,Reference_No):#Add questions to final publishable subset TestBank
    with open("%sFileSystem/SuperV/Test_sets/tPublish/%s"%(univFilePath,CurrBank), "a+") as file_handle:#File handling
        reader = csv.reader(file_handle, delimiter=',');#File reader handle
        writer = csv.writer(file_handle, delimiter=',');#File writer handle
        
        file_handle.seek(0) #Returns cursor to file top
        sl_no = 1           #Slot number counter
        
        for x in reader:    #Iteration through reader handle
           sl_no+=1
        writer.writerow([sl_no,Q,A,B,C,D,Reference_No]);#Csv writerow File I/O

def questionbank_preview_publish(bank):#Flexible bank preview that holds question for test taking
    with open("%sFileSystem/SuperV/Test_sets/tPublish/%s"%(univFilePath,bank), "a+") as file_handle:
        reader = csv.reader(file_handle, delimiter=',');#File reader handle
        writer = csv.writer(file_handle, delimiter=',');#File writer handle
        preview = []        #Array that temporarily holds final publishing test live
        file_handle.seek(0);#Returns cursor to file top
        
        for row in reader:      #Iteration through reader handle
            preview.append(row) #Adding data to temp live array database
            
        return preview#Returns value to calling function

def questionbank_add_Answer(RealRef,Q,A,B,C,D,Response,CurrUser,CurrBank):#Records student response to publish qbase subset
    with open("%sFileSystem/SuperV/User/%s/%s"%(univFilePath,CurrUser,CurrBank), "a+") as file_handle:#File handling
        reader = csv.reader(file_handle, delimiter=',');#File reader handle
        writer = csv.writer(file_handle, delimiter=',');#File writer handle
        
        file_handle.seek(0) #Returns cursor to file top
        sl_no = 1           #Slot number counter
        
        for x in reader:#Iteration through reader handle
           sl_no+=1     #Counts slot number
        writer.writerow([sl_no,RealRef,Q,A,B,C,D,Response]);#Writes row that records student response + actual question
        #print([sl_no,RealRef,Q,A,B,C,D,Response]) DEBUGGER prompt

'''def publishTest(tBankName, randomised):
    try:
        with open("FileSystem/SuperV/%sProcess/%s" %(univFilePath, recipientStudentFile), "r+") as file_handle:
            reader = csv.reader(file_handle, delimiter=',');

            recipients = []
            person_count = 0

            for name in reader:
                recipients.append(name);
                person_count += 1
            #print(person_count) release 1
            
            file_handle.close()

        with open("%sFileSystem/SuperV/userBase.csv"%(univFilePath), "r+") as file_handle:
            reader = csv.reader(file_handle, delimiter=',');

            info_gather = []
            #person_count_checksum = 0 ??
            mismatch_list = []
            x = 0

            for x in range(person_count):#confirms exixtance of specified persons
                for name in reader:
                    #print(recipients[x][0],name[0]) release 2
                    if(recipients[x][0] == name[0]):#case sensitive
                        #print('lol')
                        info_gather.append([name[0],name[2]])
                        #print(recipients[x][0])
                        file_handle.seek(0)
                        break
                    #else:
                        #print('miss',recipients[x])

                #print(x)
                file_handle.seek(0)
            print(info_gather)
            if(person_count_checksum != person_count):
                return "%s could not be located" %(mismatch_list) #future proj
            #print (recipients) debug now legacy
    except Exception:
        return "Error no such file"
'''
