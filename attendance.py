from cProfile import label
from dataclasses import field
from distutils import dep_util
from email import message
from tkinter import *
from tkinter import ttk
#from tkinter import _XYScrollCommand
from turtle import left, update
from PIL import Image,ImageTk
from matplotlib.pyplot import title
from pandas import wide_to_long
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        #main window set up
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")
        
        #======================variables========
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_department = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        #1st image top setup
        img=Image.open(r"college_images\photo-1606761568499-6d2451b23c66.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        
        
        #2nd image top setup
        img1=Image.open(r"college_images\photo-1590402494682-cd3fb53b1f70.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        #background image
        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        # title of the system
        title_lbl = Label(bg_img,text="Attendance Management System",font=("sans serif",30,"bold"),bg="white",fg="black")        
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        
        #frame for the entire options
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1530,height=600)
        
        
        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student's Attendance",font=("sans serif",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open(r"college_images\student-details-left-2.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        #attendance ID
        attendanceId_label = Label(left_inside_frame,text="Attendance ID",font=("sans serif",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry = ttk.Entry(left_inside_frame,width=20,textvariable =self.var_atten_id,font=("sans serif",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #attendance Name
      
        attendanceName_label = Label(left_inside_frame,text="Student's Name",font=("sans serif",12,"bold"),bg="white")
        attendanceName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        attendanceName_entry = ttk.Entry(left_inside_frame,width=20,textvariable =self.var_atten_name,font=("sans serif",12,"bold"))
        attendanceName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #dept name
        deptName_label = Label(left_inside_frame,text="Department",font=("sans serif",12,"bold"),bg="white")
        deptName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        deptName_entry = ttk.Entry(left_inside_frame,width=20,textvariable =self.var_atten_department,font=("sans serif",12,"bold"))
        deptName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
         #time
        timeName_label = Label(left_inside_frame,text="Time",font=("sans serif",12,"bold"),bg="white")
        timeName_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        timeName_entry = ttk.Entry(left_inside_frame,width=20,textvariable =self.var_atten_time,font=("sans serif",12,"bold"))
        timeName_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #date
        dateName_label = Label(left_inside_frame,text="Date",font=("sans serif",12,"bold"),bg="white")
        dateName_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        dateName_entry = ttk.Entry(left_inside_frame,width=20,textvariable =self.var_atten_date,font=("sans serif",12,"bold"))
        dateName_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #attendance
        attendanceLabel = Label(left_inside_frame,text="Attendance Status",bg="white",font=("sans serif",12,"bold"))
        attendanceLabel.grid(row=2,column=2,padx=5)
        
        self.atten_status = ttk.Combobox(left_inside_frame,width=20,textvariable =self.var_atten_attendance,font=("sans serif",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=2,column=3,pady=8)
        self.atten_status.current(0)
        
        
        #buttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        #import
        import_btn = Button(btn_frame,text="Import CSV",command=self.importCsv,width=17,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        import_btn.grid(row=0,column=0)
        
        #export
        export_btn = Button(btn_frame,text="Export CSV",command = self.exportCsv,width=17,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        export_btn.grid(row=0,column=1)
        
        
        
        
         #reset
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=2)
        
        
        
        
        
        #right label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Attendance Table",font=("sans serif",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        
        #=====================scroll bar table=========
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable= ttk.Treeview(table_frame,column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"] = "headings"
        
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        

        
        self.AttendanceReportTable.pack(fill=BOTH,expand = 1)
        
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        

    #=============fecth data==========
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        
        fln = filedialog.askopenfilename(initialdir = os.getcwd(),title="Open CSV",filetypes=[("CSV File","*.csv"),("ALL File","*.*")],parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i) 
            self.fetchData(mydata)
            
            
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(),title="Open CSV",filetypes=[("CSV File","*.csv"),("ALL File","*.*")],parent=self.root)
            
            with open(fln,mode="w",newline="\n") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i) 
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" success")
        except Exception as es:
            messagebox.showerror("Error",f"Dur to : {str(es)}",parent=self.root)
            

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_department.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])
        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_department.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
        
            
            
            
    
    
            
    
                    
                
            
            
        
        
        
                                           
                                           
                                           
        
































if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
            