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





class Help:
    def __init__(self,root):
        #main window set up
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("About Us")
        
        # title of the system
        title_lbl = Label(self.root,text="Help Desk",font=("sans serif",30,"bold"),bg="white",fg="black")        
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        #top image of train page
        img_top=Image.open(r"college_images\tech-support.png")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        dev_label = Label(f_lbl,text="Email:audityghosh@gmail.com",font=("times new roman",20,"bold"),fg="black")
        dev_label.place(x=550,y=100)
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
    