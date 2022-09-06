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
import os
import numpy as np
from datetime import date
from time import strftime
from datetime import datetime
import re



class Face_Recognition:
    def __init__(self,root):
        #window set up
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Tab")
    
        # title of the system
        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("sans serif",30,"bold"),bg="white",fg="black")        
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        #left image of face recognizer page
        img_top=Image.open(r"college_images\face.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
        
        #right image of face recognizer page
        img_bottom=Image.open(r"college_images\scan.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        #button of face recognizer page on right image
        b1_1=Button(f_lbl,text="Recognize The Face",command = self.face_recog,cursor="hand2",font=("sans serif",18,"bold"),bg="lightblue",fg="black")
        b1_1.place(x=280,y=580,width=400,height=60)
    
    
    #================Attendance====================
    
    def mark_attendance(self,r,n,d):
        
        with open("6.9.2022___3200_Attendance.csv","r+",newline="\n", errors="ignore") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            str_r = [x for x in r if x!='\(' and x!='\)' and x!='\'']
            str_d = [x for x in d if x!='\(' and x!='\)' and x!='\'']
            str_n = [x for x in n if x!='\(' and x!='\)' and x!='\'']
            if((r not in name_list)and(n not in name_list)and((d not in name_list))):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{now},{d1},Present")
                
                
                
                
                
                
            
            
        
    #==========Face Recognizer Function =============
    
    def face_recog(self):
        #draw a boundary around the face of the image
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert image to grayscale
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            #extract feature 
            
            coord = [] #empty coordinate
            
            for (x,y,w,h) in features: #loop feature
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) #draw rectangle
                id,predict = clf.predict(gray_image[y:y+h,x:x+w]) #predict label 
                confidence = int((100*(1-predict/300))) #formula of model's confidence
                
                #connect database
                conn = mysql.connector.connect(host="localhost",username="root",password="A11n12K13u14",database="face_recognizer")
                my_cursor = conn.cursor()
                
                #perform sql query to get Student's name from database
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                
                #perform sql query to get Student's id from database
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                #perform sql query to get Student's dept from database
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                
                             
                
                #if model's confidence is 77%                
                if confidence>77:
                    # write student's roll name dept
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r,n,d)
                    
                else:
                    #otherwise draw red rectangle and say I don't know
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord = [x,y,w,h]
            #return boundary coordinates    
            return coord
        
        #function to recognize face
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        #Using haarcascade classifier to detect
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        #Using Linear Binary Pattern Histogram Algorithm to recognize
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") #classifier reads trained data
        
        #open webcam
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read() #read webcam data
            img = recognize(img,clf,faceCascade) #recognize
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                   
            



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
    