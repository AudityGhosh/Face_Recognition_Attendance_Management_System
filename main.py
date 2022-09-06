from cProfile import label
from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter 
from PIL import Image,ImageTk
from matplotlib.pyplot import title
import os
from student import Student #student.py 's Student Class
from train import Train #train.py 's Train Class
from face_recognition import Face_Recognition #face_recognition.py 's Face_Recognition Class
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        #main window set up
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance Management System") #main window tab title
        
        #1st image top setup
        img=Image.open(r"college_images\photo-1606761568499-6d2451b23c66.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        
        #2nd image top setup
        img1=Image.open(r"college_images\photo-1590402494682-cd3fb53b1f70.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        
        #3rd image top setup
        img2=Image.open(r"college_images\photo-1486312338219-ce68d2c6f44d.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        
        #background image
        img3=Image.open(r"college_images\future-of-AI.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        
        # title of the system
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("sans serif",35,"bold"),bg="white",fg="black")        
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #==========time=============
        '''
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(title_lbl,font=("times new roman",14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=20,width=110,height=20)
        time()'''
        
        
        
        
        #buttons
        
        #def GotoStudent():        
            #os.system('student.py') #audity's own search function
        #student details button 
        img4=Image.open(r"college_images\student.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("sans serif",15,"bold"),bg="blue",fg="white",command=self.student_details)
        b1_1.place(x=200,y=300,width=220,height=40)
        
        
        #detect face button 
        img5=Image.open(r"college_images\detect-face.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Recognizer",cursor="hand2",command=self.face_data,font=("sans serif",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        #attendance face button 
        img6=Image.open(r"college_images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("sans serif",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        #Contact face button 
        img7=Image.open(r"college_images\contact.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Contact Us",cursor="hand2",command=self.help_desk,font=("sans serif",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        #Train Model button 
        img8=Image.open(r"college_images\train-model.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)        
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train the model",command=self.train_data,cursor="hand2",font=("sans serif",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        #Photos button 
        img9=Image.open(r"college_images\photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("sans serif",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        #About us button 
        img10=Image.open(r"college_images\developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.dev_data)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="About Us",cursor="hand2",command=self.dev_data,font=("sans serif",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        #Exit button 
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("sans serif",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile("data") # open your local directory of images.  
    
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return 
        
    #===============================================Functions buttons===============================================================
        
    def student_details(self):
        self.new_window = Toplevel(self.root) # go to student.py function
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root) # go to train.py function
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root) # go to face_recognition.py function
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root) # go to attendance.py function
        self.app = Attendance(self.new_window)
        
        
    def dev_data(self):
        self.new_window = Toplevel(self.root) # go to attendance.py function
        self.app = Developer(self.new_window)
    
    def help_desk(self):
        self.new_window = Toplevel(self.root) # go to attendance.py function
        self.app = Help(self.new_window)
        
    
    
    
        
        
      
       
        
        

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
        
        