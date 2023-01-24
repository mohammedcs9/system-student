from tkinter import *
from PIL import Image,ImageTk

class Student:
    def __init__(self,window):
        self.master=window
        self.master.title("Student Management System")
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state('zoomed')
        ################# Frame Top Start Here #################
        self.frametop=Frame(self.master,bg='#1b9ea4',height=150)
        self.frametop.pack(fill=X)
        self.sms=Label(self.frametop,text='School Management System',bg='#1b9ea4',fg='white',font=('tahoma',50),pady=30)
        self.sms.pack()
        ################# Frame Top End Here #################
        
        ################# Frame Center Start Here #################
        self.centerFrame=Frame(self.master)
        self.centerFrame.pack(fill=X)
        ################# Frame Center End Here #################
        
        ################# Frame University info #################
        self.universityInfo=Frame(self.centerFrame,pady=10,padx=10)
        self.universityInfo.grid(row=0,column=0,sticky='senw')
        self.img=Image.open('img/istockphoto-1150645589-612x612.jpg')
        self.img.thumbnail((200,200))
        self.new_img=ImageTk.PhotoImage(self.img)
        self.imgUniversity=Label(self.universityInfo,image=self.new_img,padx=10,pady=10)
        self.imgUniversity.pack()
        self.buttonUniversity=Button(self.universityInfo,font=('tahoma',10,'bold'),text='About University',bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonUniversity.pack()
        ################# Frame Student info #################
        self.studentFrame=Frame(self.centerFrame,pady=10,padx=10)
        self.studentFrame.grid(row=0,column=1,sticky='senw')
        self.img2=Image.open('img/download.png')
        self.img2.thumbnail((200,200))
        self.new_img2=ImageTk.PhotoImage(self.img2)
        self.imgStudent=Label(self.studentFrame,image=self.new_img2,padx=10,pady=10)
        self.imgStudent.pack()
        self.buttonStudent=Button(self.studentFrame,font=('tahoma',10,'bold'),text='Student Management',bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonStudent.pack()
        ################# Frame Staff info #################
        self.staffFrame=Frame(self.centerFrame,pady=10,padx=10)
        self.staffFrame.grid(row=0,column=2,sticky='senw')
        self.img3=Image.open('img/SMS_Feature-800x4000.jpg')
        self.img3.thumbnail((200,200))
        self.new_img3=ImageTk.PhotoImage(self.img3)
        self.imgStaff=Label(self.staffFrame,image=self.new_img3,padx=10,pady=10)
        self.imgStaff.pack()
        self.buttonStaff=Button(self.staffFrame,font=('tahoma',10,'bold'),text='Staff Management',bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonStaff.pack()
        self.centerFrame.grid_columnconfigure(0,weight=1)
        self.centerFrame.grid_columnconfigure(1,weight=1)
        self.centerFrame.grid_columnconfigure(2,weight=1)
        ################# Bottom Frame Start Here #################
        self.bottomFrame=Frame(self.master,height=200)
        self.bottomFrame.pack(fill=X)
        ################# Bottom Frame End Here #################
        
        ################# Library Frame #################
        self.libraryFrame=Frame(self.bottomFrame,pady=10,padx=50)
        self.libraryFrame.grid(row=1,column=0,sticky='senw')
        self.img4=Image.open('img/open-book.png')
        self.img4.thumbnail((200,200))
        self.new_img4=ImageTk.PhotoImage(self.img4)
        self.imgLibrary=Label(self.libraryFrame,image=self.new_img4,padx=10,pady=10)
        self.imgLibrary.pack()
        self.buttonLibrary=Button(self.libraryFrame,font=('tahoma',10,'bold'),text='Library Management',bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonLibrary.pack()
        ################# Exam Frame #################
        self.examFrame=Frame(self.bottomFrame,pady=10,padx=50)
        self.examFrame.grid(row=1,column=1,sticky='senw')
        self.img5=Image.open('img/Exam-Logo-PNG-HD-Quality.png')
        self.img5.thumbnail((200,200))
        self.new_img5=ImageTk.PhotoImage(self.img5)
        self.imgExam=Label(self.examFrame,image=self.new_img5,padx=10,pady=10)
        self.imgExam.pack()
        self.buttonExam=Button(self.examFrame,font=('tahoma',10,'bold'),text='Exam Management',bg='#1b9ea4',fg='white',padx=10,pady=10)
        self.buttonExam.pack()
        
        self.bottomFrame.grid_columnconfigure(0,weight=1)
        self.bottomFrame.grid_columnconfigure(1,weight=1)
        
        
        

if(__name__=='__main__'):
    window = Tk()
    std = Student(window)
    mainloop()