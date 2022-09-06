from cProfile import label
from distutils import dep_util
from email import message
from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from matplotlib.pyplot import title
from pandas import wide_to_long
from tkinter import messagebox
import mysql.connector 
import cv2
from tkhtmlview import HTMLLabel




class Developer:
    def __init__(self,root):
        #main window set up
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("About Us")
        
        # title of the system
        title_lbl = Label(self.root,text="About The Developer",font=("sans serif",30,"bold"),bg="white",fg="black")        
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        #top image of train page
        img_top=Image.open(r"college_images\dev-f.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        
        #right side frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=60,width=500,height=600)
        
        
        #dev image
        img_top1=Image.open(r"college_images\Audity.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        #developer info
        dev_label = Label(main_frame,text="Hello, I am Audity",font=("sans serif",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label = Label(main_frame,text="A Python Programmer",font=("sans serif",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)
        
        
        #3rd image top setup
        img2=Image.open(r"college_images\photo-1486312338219-ce68d2c6f44d.jpg")
        img2=img2.resize((500,390),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
    