from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from generalFileFunctions import*
from adminFunctions import*
from publishTest import*
import time
import os
#from publishTest import*

masterKey = "letmein"
CurrUser = ""
mainCount = 0
qList = []
newqList = []
testNameGlobe = ""
count_terminate = 0

class TestGUI_Interface_loginScr:#Login Screen
    def __init__(self, master):
        self.master = masterKey                     #Master root thread
        master.title("ECI TELECOM Test Interface")  #Window title
        master.geometry("800x600")                  #Window dimensions

        widgetF = Frame(master)                     #Widget Frame

        self.Header = Label(widgetF, text ="ECI TELECOM Login Portal", fg = "#0b34ba",font=("Helvetica", 20))#Header Label
        self.Header.grid(row=0,column=2)#Label pack to frame

        self.ULabel = Label(widgetF, text="Username")   #Text Label
        self.ULabel.grid(row=1,column=1)                #Label pack to frame
        self.UsernameBox = Entry(widgetF)           #Data entry box
        self.UsernameBox.grid(row=1,column=2)       #Box pack

        self.checkMaster = ttk.Checkbutton(widgetF,text="Supervisor Login",command=self.MasterBox)#Checkbox
        self.checkMaster.grid(row=1,column=3)#Checkbox pack

        self.PLabel = Label(widgetF, text="Password")   #Text Label
        self.PLabel.grid(row=2,column=1)                #Label pack to frame
        self.PasswrdBox = Entry(widgetF, show="*")      #Data entry box for password
        self.PasswrdBox.grid(row=2,column=2)            #Data box pack to frame
        
        self.submitCredential = Button(widgetF, text="Submit", command=self.submit) #Button
        self.submitCredential.grid(row=3,column=2)#Button pack

        self.close_button = Button(widgetF, text="Close", command=root.destroy)#Close program button
        self.close_button.grid(row=4,column=2)#Button pack

        self.unlockmsg1 = Label(widgetF, text="success",fg="blue")#Success message
        self.unlockmsg2 = Label(widgetF, text="error wrong username or password",fg="red")#Error message

        self.MasterBoxE = Entry(widgetF,show="*")#Master pass box
        

        widgetF.pack()#WidgetFrame pack to window root

    def MasterBox(self):
        self.MasterBoxE.grid(row=2,column=3)#Reveals hidden entry box


    def submit(self):#pack this in the controller class
        #return to database
        usernameArgs = self.UsernameBox.get()       #gets username data
        passwordArgs = self.PasswrdBox.get()        #gets password data
        if (check_User(usernameArgs,passwordArgs)): #Authentication
            #print(usernameArgs, passwordArgs)
            self.unlockmsg1.grid(row=5,column=2)    #Unlock success for employee
            #print(self.checkMaster.state()[0])DEBUGGER
            global masterKey
            #print(masterKey)
            #print(self.MasterBoxE.get())
            if(self.checkMaster.state()[0]=='selected'):#Supervisor unlock
                if(self.MasterBoxE.get() == masterKey):
                    global CurrUser#Global current user store
                    CurrUser = usernameArgs     #Alias
                    root = Tk()                 #New root process spawn
                    GUI1 = TestGUI_Interface_SuperInterface(root)       #Object creation
                    root.mainloop()             #New window spin-off
                else:
                    messagebox.showerror("Title", "Incorrect Root Username or Password")
            else:
                CurrUser = usernameArgs
                root = Tk()         #New root process
                GUI1 = TestGUI_Interface_SubInterface_ViewTests(root)#object creation
                root.mainloop()     #New window spin-off
            
        else:
            self.unlockmsg2.grid(row=5,column=2)#Unlock error msg
            messagebox.showerror("Title", "Incorrect Username or Password")

class TestGUI_Interface_SuperInterface:
    def __init__(self,master):
        self.master = master
        master.title("ECI TELECOM Test Interface")
        master.geometry("800x600")
        
        widgetF = Frame(master)
        self.Header = Label(widgetF, text ="Welcome to ECI TELECOM", fg = "#0b34ba",font=("Helvetica", 20),pady = 50)
        self.Header.grid(row=0, column=1)

        self.AdminFunction = Menubutton(widgetF, text="Admin Functions", fg="blue",width=40,height=2)
        self.AdminFunction.grid(row=4, column=1,pady=5)
        self.AdminFunction.menu = Menu(self.AdminFunction, tearoff = 0)
        self.AdminFunction["menu"] = self.AdminFunction.menu
        self.AdminFunction.menu.add_command(label="Add User", command=self.addRemove_Submit)
        self.AdminFunction.menu.add_command(label="Remove User",command=self.addRemove_Submit)

        self.QuestionBankOptions = Menubutton(widgetF, text="QuestionBank Options", fg="blue",width=40,height=2)
        self.QuestionBankOptions.grid(row=5, column=1,pady=5)
        self.QuestionBankOptions.menu = Menu(self.QuestionBankOptions, tearoff = 0)
        self.QuestionBankOptions["menu"] = self.QuestionBankOptions.menu
        self.QuestionBankOptions.menu.add_command(label="Add Question" , command=self.nextWindow)
        self.QuestionBankOptions.menu.add_command(label="Remove Question", command=self.nextWindow)
        self.QuestionBankOptions.menu.add_command(label="Add new Questionbank", command=self.nextWindow)
        self.QuestionBankOptions.menu.add_command(label="Remove Questionbank", command=self.nextWindow)
        
        self.PublishTest = Button(widgetF, text="Test Publish", fg="blue", width=40,height=2,command=self.Publish)
        self.PublishTest.grid(row=6, column=1,pady=5)

        self.EmployeeOverview = Button(widgetF, text="Employee Overview", width=40, height=2, command=self.Employee)
        self.EmployeeOverview.grid(row=7, column=1,pady=5)

        widgetF.pack()

    def nextWindow(self):
        root = Tk()
        GUI1 = TestGUI_Interface_SuperInterface_QuestionManager(root)
        root.mainloop()

        widgetF.pack()
    def addRemove_Submit(self):
        root = Tk()
        GUI1 = TestGUI_Interface_SuperInterface_AdF(root)
        root.mainloop()

    def Publish(self):
        root = Tk()
        GUI1 = TestGUI_Interface_SuperInterface_PublishTest(root)
        root.mainloop()

    def Employee(self):
        root = Tk()
        GUI1 = TestGUI_Interface_SuperInterface_Overview(root)
        root.mainloop()

class TestGUI_Interface_SuperInterface_AdF:
    def __init__(self,master):
        self.master = master#Master root
        master.title("ECI TELECOM Test Interface")#Master window
        master.geometry("900x600")#Master window dimension
        
        widgetM = Frame(master)#Master frame 1
        self.Header = Label(widgetM, text ="Administrative Functions", fg = "#0b34ba",font=("Helvetica", 20), padx = 10, pady = 50)
        self.Header.pack()#Label pack

        widgetF = Frame(master)#Master frame 2
        self.ULabel0 = Label(widgetF, text="Username")  #Text label
        self.ULabel0.grid(row=0,column=2)               #label pack
        self.ULabel0 = Label(widgetF, text="Password")  #Text label
        self.ULabel0.grid(row=0,column=3)               #label pack
        self.ULabel0 = Label(widgetF, text="Password")  #Text label
        self.ULabel0.grid(row=0,column=4)               #label pack
        self.ULabel0 = Label(widgetF, text="E-mail")    #Text label
        self.ULabel0.grid(row=0,column=5)               #label pack
        
        self.ULabel = Label(widgetF, text="Add User: ") #Text label
        self.ULabel.grid(row=1,column=1)                #label pack
        self.UsernameBox = Entry(widgetF)               #Entry box
        self.UsernameBox.grid(row=1,column=2)           #Entry box pack
        self.PasswrdBox = Entry(widgetF, show ='*')     #Entry box
        self.PasswrdBox.grid(row=1,column=3)            #Entry box pack
        self.PasswrdBox01 = Entry(widgetF, show ='*')   #Entry box
        self.PasswrdBox01.grid(row=1,column=4)          #Entry box pack
        self.EmailBox = Entry(widgetF)                  #Entry box
        self.EmailBox.grid(row=1,column=5)              #Entry box pack
        self.submitCredential = Button(widgetF, text="Submit", command=self.submit) #Action Button
        self.submitCredential.grid(row=2,column=2)                                  #Action button pack


        self.PLabel = Label(widgetF, text="Remove User: ")  #Text label
        self.PLabel.grid(row=3,column=1)                    #label pack
        self.UsernameBox1 = Entry(widgetF)                  #Entry box
        self.UsernameBox1.grid(row=3,column=2)              #Entry box pack
        self.PasswrdBox1 = Entry(widgetF, show ='*')        #Entry box
        self.PasswrdBox1.grid(row=3,column=3)               #Entry box pack

        self.submitCredential1 = Button(widgetF, text="Submit", command=self.submit2)
        self.submitCredential1.grid(row=5,column=2)

        self.unlockmsg1 = Label(widgetF, text="success",fg="blue")                                  #Success message
        self.unlockmsg2 = Label(widgetF, text="error user exist or password too short",fg="red")    #Error message
        self.unlockmsg3 = Label(widgetF, text="User does not exist or incorrect credentials",fg="red")#Error message
        
        widgetM.pack()#WidgetFrame Pack
        widgetF.pack()#WidgetFrame Pack

    def submit(self):
        #print("lol")
        usernameArgs = self.UsernameBox.get()#checks username to prevent duplicates
        passwordArgs = self.PasswrdBox.get()
        passwordArgs1 = self.PasswrdBox01.get()
        EmailArgs = self.EmailBox.get()
        #print(usernameArgs)

        
        if (check_User(usernameArgs) != True and passwordArgs != "" and passwordArgs == passwordArgs1):
            self.unlockmsg2.grid_forget()
            self.unlockmsg1.grid(row=6,column=2)
            add_User(usernameArgs, passwordArgs, passwordArgs1, EmailArgs)
            return True
        elif(check_User(usernameArgs) == True):
            messagebox.showerror("Error", "Username Taken")

            
        else:
            self.unlockmsg2.grid(row=6,column=2)
    def submit2(self):
        usernameArgs = self.UsernameBox1.get()#checks username to prevent duplicates
        passwordArgs = self.PasswrdBox1.get()
        #print(usernameArgs, passwordArgs)
        if (check_User(usernameArgs,passwordArgs)):
            #print(check_User(usernameArgs,passwordArgs))
            self.unlockmsg3.grid_forget()
            self.unlockmsg1.grid(row=6,column=2)
            rm_User(usernameArgs, passwordArgs)

            return True
        else:
            self.unlockmsg3.grid(row=6,column=2)
            messagebox.showerror("Error", "No such User exists")

class TestGUI_Interface_SuperInterface_QuestionManager:
    SessionBankNameVariable = ""#Stores current session Bank being worked on
    def __init__(self, master):
        self.master = master
        master.title("ECI TELECOM Test Interface")
        master.geometry("800x600")


        widgetF = Frame(master)
        dirlist = os.listdir("%sFileSystem/SuperV/Test_sets/tBank"%(univFilePath))
        #print(dirlist)

        self.label1 = Label(widgetF, text="TestBank")
        self.label1.grid(row=1,column=1)
        self.label2 = Label(widgetF, text="Test Questions")
        self.label2.grid(row=1,column=2,padx=100)
        self.listbox1 = Listbox(widgetF)
        count = 1;
        for f in dirlist:
            self.listbox1.insert(count, f)
            count +=1
        self.listbox1.grid(row=2, column=1)
        self.listbox2 = Listbox(widgetF)
        self.listbox2.grid(row=2, column=2)
        
        self.submitTBankSelection_Button = Button(widgetF, text="submit", command=self.submitTBankSelection_Function)
        self.submitTBankSelection_Button.grid(row=3,column=1)
        self.removeQuestion_Button = Button(widgetF, text="remove question", command=self.removeQuestion_Function)
        self.removeQuestion_Button.grid(row=2, column=3)

        widgetF.pack()

        widgetG = Frame(master)

        self.label3 = Label(widgetG, text="Add question")
        self.label3.grid(row=1, column=2)
        
        self.label4 = Label(widgetG, text="Question:")
        self.label4.grid(row=2, column=1)
        self.Box4e = Entry(widgetG)
        self.Box4e.grid(row=2, column=2)
        
        self.label5 = Label(widgetG, text="Option A:")
        self.label5.grid(row=3, column=1)
        self.Box5e = Entry(widgetG)
        self.Box5e.grid(row=3, column=2)
        
        self.label6 = Label(widgetG, text="Option B:")
        self.label6.grid(row=4, column=1)
        self.Box6e = Entry(widgetG)
        self.Box6e.grid(row=4, column=2,padx=30)
        
        self.label7 = Label(widgetG, text="Option C:")
        self.label7.grid(row=5, column=1)
        self.Box7e = Entry(widgetG)
        self.Box7e.grid(row=5, column=2)
        
        self.label8 = Label(widgetG, text="Option D:")
        self.label8.grid(row=6, column=1)
        self.Box8e = Entry(widgetG)
        self.Box8e.grid(row=6, column=2)

        self.label9 = Label(widgetG, text="Answer:")
        self.label9.grid(row=7, column=1)
        self.Box9e = Entry(widgetG)
        self.Box9e.grid(row=7, column=2)

        self.addQuestion_Button = Button(widgetG,text="add question",command=self.submitAddQuestion)
        self.addQuestion_Button.grid(row=4,column=3,padx=30)
        

        widgetG.pack()

        widgetH = Frame(master)

        self.label10 = Label(widgetH, text="TestBank")
        self.label10.grid(row=1, column=1)
        self.Box10e = Entry(widgetH)
        self.Box10e.grid(row=2, column=1)

        self.label11 = Label(widgetH, text="Add or Remove TestBank?")
        self.label11.grid(row=1, column=2)
        self.Box11e = Entry(widgetH)
        self.Box11e.grid(row=2, column=2)

        self.testBankButton = Button(widgetH, text="submit", command=self.polyTestSet)
        self.testBankButton.grid(row=2,column=3,padx=30)

        self.PolySuccess = Label(widgetH, text='Success!',fg = "#0b34ba")
        self.PolySuccess2 = Label(widgetH, text='Success!',fg = "red")
        self.PolySuccess3 = Label(widgetH, text='Error',fg = "red")

        widgetH.pack()

    def submitTBankSelection_Function(self):#Modular function allows reuse of button
        TBank_choice = self.listbox1.get(ACTIVE)
        TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable = TBank_choice#Because variable is not accessisble outside 
        #print(TBank_choice)
        #print(TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable)
        count = 1;
        for f in questionbank_preview(TBank_choice):
            self.listbox2.insert(count, f)
            count +=1
        
    def removeQuestion_Function(self):#Modular function allows reuse of button
        #print(TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable)
        removeQuestion_selection = self.listbox2.get(ACTIVE)
        questionbank_remove(removeQuestion_selection[0], TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable)
        #print(removeQuestion_selection)

    def submitAddQuestion(self):#Modular function allows reuse of button
        questionbank_add(self.Box4e.get(),self.Box5e.get(),self.Box6e.get(),self.Box7e.get(),self.Box8e.get(),self.Box9e.get(),TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable)
        messagebox.showerror("Success", "Question successfully added")

    def polyTestSet(self):
        BankName = self.Box10e.get()
        BankAction = self.Box11e.get()
        #print(BankName, BankAction)DEBUGGER
        if BankAction == 'add' or BankAction == 'Add':
            setBank(BankName)
            self.PolySuccess.grid(row=3,column=3)
            messagebox.showerror("Success", "Test Bank successfully created")
        elif BankAction == 'remove' or BankAction == 'Remove':
            if(setBank(BankName, BankAction) == 1):
                messagebox.showerror("Error", "Test Bank remove failed")
            
            else:
                setBank(BankName, BankAction)
                messagebox.showerror("Success", "Test Bank successfully removed")
                self.PolySuccess2.grid(row=4,column=3)
        else:
            self.PolySuccess3.grid(row=5,column=3)
            messagebox.showerror("Error", "Test Bank remove failed")

class TestGUI_Interface_SuperInterface_PublishTest:
    SessionBankNameVariable = ""#Stores current session Bank being worked on
    countGlobal = 1
    listGlobal = []
    def __init__(self, master):
        self.master = master#Master root
        master.title("ECI TELECOM Test Interface")#Window Title
        master.geometry("800x600")#Window dimensions

        dirlist = os.listdir("%sFileSystem/SuperV/Test_sets/tBank"%(univFilePath))#Gets directory contents
        widgetF = Frame(master)#Master frame

        self.label1 = Label(widgetF,text="QuestionBank")#Text label
        self.label1.grid(row=1,column=1)                #label pack

        self.label2 = Label(widgetF,text="Questions")   #Text label
        self.label2.grid(row=1,column=2)                #label pack

        self.label3 = Label(widgetF,text="Questions to Publish")#Text label
        self.label3.grid(row=1,column=3)                        #label pack

        self.listbox1 = Listbox(widgetF)#Listbox scrollable view
        self.listbox1.grid(row=2,column=1)#listbox pack

        self.listbox2 = Listbox(widgetF)#Listbox scrollable view
        self.listbox2.grid(row=2,column=2)#listbox pack

        self.listbox3 = Listbox(widgetF)#Listbox scrollable view
        self.listbox3.grid(row=2,column=3)#listbox pack

        self.listbox1Button = Button(widgetF, text="submit", command=self.TBankSelect)#Button
        self.listbox1Button.grid(row=3,column=1)#Button pack

        self.listbox2Button = Button(widgetF, text=">>", command=self.TBankQuestionSelect)#Button
        self.listbox2Button.grid(row=3,column=2)#Button pack

        self.DoneButton = Button(widgetF, text="Done", command=self.Done)#Button
        self.DoneButton.grid(row=3,column=3)#Button pack


        count=1
        for f in dirlist:
            self.listbox1.insert(count, f)
            count+=1

        widgetF.pack()
    def TBankSelect(self):#Select questionbank
        count2 =1
        TBank_choice = self.listbox1.get(ACTIVE)#Get active listbox selection
        TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable = TBank_choice#Because variable is not accessisble outside
        for f in questionbank_preview(TBank_choice):#Iteration loop through live preview array
            self.listbox2.insert(count2, f)#insert new listbox entries
            count2+=1
    def TBankQuestionSelect(self):#Select questions
        TBank_choice = self.listbox2.get(ACTIVE)#Get active listbox selection
        self.listbox3.insert(TestGUI_Interface_SuperInterface_PublishTest.countGlobal, TBank_choice)#insert new listbox entry
        TestGUI_Interface_SuperInterface_PublishTest.countGlobal+=1#Global count variable increment
        TestGUI_Interface_SuperInterface_PublishTest.listGlobal.append(TBank_choice)#Global list append new entry
        #print(TestGUI_Interface_SuperInterface_PublishTest.listGlobal) DEBUGGER

    def Done(self):#Publish Exevute
        if(setBankPublish(TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable)==1):
            messagebox.showerror("Error", "Test Bank duplicate exists")
        else:
            setBankPublish(TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable)
            for f in TestGUI_Interface_SuperInterface_PublishTest.listGlobal:
                #print(f) DEBUGGER
                questionbank_add_Publish(f[1],f[2],f[3],f[4],f[5],TestGUI_Interface_SuperInterface_QuestionManager.SessionBankNameVariable,f[0])
                messagebox.showerror("Success", "Test Bank successfully Published")

class TestGUI_Interface_SubInterface_ViewTests:
    def __init__(self, master):
        #print('lol') DEBUGGER
        self.master = master#Root thread
        master.title("ECI TELECOM Test Interface")#Window title
        master.geometry("800x600")      #Window sizing

        dirlist = os.listdir("%sFileSystem/SuperV/Test_sets/tPublish"%(univFilePath))          #Get directory contents

        widgetF = Frame(master)         #Master Frame

        self.label = Label(widgetF, text="Available Tests", fg="#0b34ba", font=('Helvetica',20))#Text Label
        self.label.pack()               #Label pack

        self.listbox1 = Listbox(widgetF)#Scrollable list view
        self.listbox1.pack()            #Listbox pack

        self.taketest = Button(widgetF, text="Take Test", command=self.TestForward)#Submit choice button
        self.taketest.pack()            #Button pack
        
        count = 1
        for f in dirlist:#Directory content iteration
            self.listbox1.insert(count, f)#Add item to list
            count+=1

        widgetF.pack()#WidgetFrame pack

    def TestForward(self):
        SessionBankNameVariable = self.listbox1.get(ACTIVE)#Which bank
        #print(SessionBankNameVariable)
        global qList
        qList = questionbank_preview_publish(SessionBankNameVariable)#stores session preview
        #print(qList)
        global count_terminate
        for f in qList:
            count_terminate+=1
            
        root = Tk()     #New root
        GUI1 = TestGUI_Interface_SubInterface_TestTake(root, SessionBankNameVariable)#Object creation
        root.mainloop() #New window

class TestGUI_Interface_SubInterface_TestTake:
    def __init__(self, master, TestName):
        #print(TestName) DEBUGGER
        global testNameGlobe#Global variable reference
        testNameGlobe = TestName#Global update
        self.master = master#Master root
        master.title("ECI TELECOM Test Interface")#Window title
        master.geometry("800x600")#Window sizing

        widgetF =  Frame(master)#Master Frame
        #print(qList) DEBUGGER
        varQues = qList[mainCount][1]#Question variable
        varA = qList[mainCount][2]#Option1 variable
        varB = qList[mainCount][3]#Option2 variable
        varC = qList[mainCount][4]#Option3 variable
        varD = qList[mainCount][5]#Option4 variable

        #print("lol")DEBUGGER
        self.labelQuestion = Label(widgetF, text="Q. "+varQues, font=('Helvetics',16),fg="#0b34ba")#Question Label
        self.labelQuestion.pack()#Label pack
        

        self.checkA = Label(widgetF, text="A."+varA)#Option1 label
        self.checkA.pack(anchor = W)
        self.checkB = Label(widgetF, text="B."+varB)#Option2 label
        self.checkB.pack(anchor = W)
        self.checkC = Label(widgetF, text="C."+varC)#Option3 label
        self.checkC.pack(anchor = W)
        self.checkD = Label(widgetF, text="D."+varD)#Option4 label
        self.checkD.pack(anchor = W)

        self.Ans = Entry(widgetF)
        self.Ans.pack()
        
        
        self.submitButton = Button(widgetF, text="submit", command=self.Submit)#Button
        self.submitButton.pack()#Button pack

        widgetF.pack()#WidgetFrame pack

    def Submit(self):
        answerSub = self.Ans.get()
        answer = ""
        global qList,mainCount#Global reference
        print(qList)
        if answerSub == 'A' or answerSub == 'a':
            answer = qList[mainCount][2]
        if answerSub == 'B' or answerSub == 'b':
            answer = qList[mainCount][3]
        if answerSub == 'C' or answerSub == 'c':
            answer = qList[mainCount][4]
        if answerSub == 'D' or answerSub == 'd':
            answer = qList[mainCount][5]
        
        questionbank_add_Answer(qList[mainCount][6],qList[mainCount][1],qList[mainCount][2],qList[mainCount][3],qList[mainCount][4],qList[mainCount][5],answer,CurrUser,testNameGlobe)
        mainCount+=1
        print(mainCount,count_terminate)
        if mainCount < count_terminate:
            root = Tk()#New root
            GUI1 = TestGUI_Interface_SubInterface_TestTake(root,testNameGlobe)#Object creation
            root.mainloop()#New window
        else:
            root = Tk()#New root
            GUI1 = TestGUI_Interface_SubInterface_TestComplete(root)#Object creation
            root.mainloop()#New window
class TestGUI_Interface_SubInterface_TestComplete:
    def __init__(self, master):
        self.master = master
        master.title("ECI TELECOM Test Interface")
        master.geometry("800x600")

        widgetF = Frame(master)

        self.label = Label(widgetF, text="COMPLETE", font=('Helvetica',50), fg="blue")
        self.label.pack()

        widgetF.pack()

class TestGUI_Interface_SuperInterface_Overview:
    person = ""
    bank = ""
    def __init__(self, master):
        self.master = master
        master.title("ECI TELECOM Test Interface")
        master.geometry("800x600")

        widgetF = Frame(master)

        self.label = Label(widgetF, text="Employee Overview", font=('Helvetics',20))
        self.label.grid(row=1,column=1)

        self.EmployeeList = Listbox(widgetF)
        self.EmployeeList.grid(row=2,column=1)

        self.TestList = Listbox(widgetF)
        self.TestList.grid(row=2,column=2)


        dirlist = open("%sFileSystem/SuperV/userBase.csv"%(univFilePath))
        

        #print(dirlist)

        count = 1

        for f in dirlist:
            thing = [word.replace("\n", "") for word in f.split(",")]
            self.EmployeeList.insert(count, thing[0])
            #print(thing[0])
            count+=1
        self.button1 = Button(widgetF,text="select",command=self.select)
        self.button1.grid(row=3,column=1)

        self.button2 = Button(widgetF,text="select",command=self.submit)
        self.button2.grid(row=3,column=2)

    
        widgetF.pack()

        widgetG = Frame(master)
        

    def select(self):
        TestGUI_Interface_SuperInterface_Overview.person = self.EmployeeList.get(ACTIVE)
        dirlist = os.listdir("%sFileSystem/SuperV/User/%s"%(univFilePath,TestGUI_Interface_SuperInterface_Overview.person))
        count = 1
        for f in dirlist:
            self.TestList.insert(count,f)
            count+=1

    def submit(self):
        #widgetG = Frame(master)
        choice = self.TestList.get(ACTIVE)
        TestGUI_Interface_SuperInterface_Overview.bank = choice
        data = open("%sFileSystem/SuperV/User/%s/%s"%(univFilePath,TestGUI_Interface_SuperInterface_Overview.person,choice))
        #print(data)
        testOut = []
        
        count = 1
        for i in data:
            newOut = []
            thing = [word.replace("\n", "") for word in i.split(",")]
            for j in range(1,8):
                newOut.append(thing[j])
            testOut.append(newOut)
        print(testOut)
        count+=1
        
        root = Tk()
        GUI1 = Out(root,testOut,TestGUI_Interface_SuperInterface_Overview.bank)
        root.mainloop()
            

class Out:
    def __init__(self, master,testOut,bank):
        self.master = master
        master.title("ECI TELECOM Test Interface")
        master.geometry("800x600")

        widgetF = Frame(master)
        self.label = Label(widgetF,text="Ref No., Question, Options(A,B,C,D), Response, Correct Ans")
        self.label.pack()
        self.listbox = Listbox(widgetF)
        self.listbox.pack()
        count = 1
        for f in testOut:
            self.listbox.insert(count,f)
            count+=1

        self.listans = Listbox(widgetF)
        self.listans.pack()
        count= 1
        data = open('%sFileSystem/SuperV/Test_sets/tBank/%s'%(univFilePath,bank))
        for f in data:
            self.listans.insert(count,f)
            count+=1
        widgetF.pack()
        
        
                    
        
root = Tk()
GUI1 = TestGUI_Interface_loginScr(root)
root.mainloop()
