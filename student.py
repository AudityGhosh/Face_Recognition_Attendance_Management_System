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


class Student:
    def __init__(self,root):
        #main window set up
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")
        
        
        #===variables===
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_teacher = StringVar()
        
        
        
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
        title_lbl = Label(bg_img,text="Students' Information Management",font=("sans serif",30,"bold"),bg="white",fg="black")        
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        
        #frame for the entire options
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1530,height=600)
        
        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student's Details",font=("sans serif",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open(r"college_images\student-details-left-2.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #current course information with name
        current_course_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="white",text="Current Course Information",font=("sans serif",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)
        
        #Department 
        dep_label = Label(current_course_frame,text="Department",font=("sans serif",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("sans serif",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","CSE","EEE","ECE","ETE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course 
        course_label = Label(current_course_frame,text="Course",font=("sans serif",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("sans serif",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","CSE 3200","CSE 3201","CSE 3203","CSE 3205","CSE 3207","CSE 3209")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year 
        year_label = Label(current_course_frame,text="Year",font=("sans serif",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("sans serif",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester 
        semester_label = Label(current_course_frame,text="Semester",font=("sans serif",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("sans serif",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Odd","Even")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student information
        class_student_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="white",text="Class Student Information",font=("sans serif",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)
        
        #student ID
        studentId_label = Label(class_student_frame,text="Student's ID",font=("sans serif",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("sans serif",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        studentName_label = Label(class_student_frame,text="Student's Name",font=("sans serif",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("sans serif",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #Email
        email_label = Label(class_student_frame,text="Email",font=("sans serif",12,"bold"),bg="white")
        email_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("sans serif",12,"bold"))
        email_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #phone no
        phone_label = Label(class_student_frame,text="Phone No",font=("sans serif",12,"bold"),bg="white")
        phone_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("sans serif",12,"bold"))
        phone_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #teacher name
        teacher_label = Label(class_student_frame,text="Teacher's Name",font=("sans serif",12,"bold"),bg="white")
        teacher_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("sans serif",12,"bold"))
        teacher_entry.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)
        
        
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)
        
        #buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=720,height=200)
        
        #save
        save_btn = Button(btn_frame,text="Save",command = self.add_data,width=17,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0)
        
         #update
        update_btn = Button(btn_frame,text="Update",command = self.update_data,width=17,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=1)
        
         #delete
        delete_btn = Button(btn_frame,text="Delete",command =self.delete_data,width=17,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        delete_btn.grid(row=0,column=2)
        
         #reset
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=3)
        
        
        
        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=220,width=720,height=100)
        
         #take photo sample
        take_photo_btn = Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        take_photo_btn.grid(row=1,column=0)
        
        '''
        #update photo sample
        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=35,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        update_photo_btn.grid(row=1,column=1)
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #right label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Student's Information Table",font=("sans serif",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        img_right=Image.open(r"college_images\student-details-left-2.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        #================Search System==============
        Search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white",text="Search System",font=("sans serif",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)
        
        
        search_label = Label(Search_frame,text="Search By",font=("sans serif",13,"bold"),bg="lightblue",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo = ttk.Combobox(Search_frame,font=("sans serif",12,"bold"),width=14,state="readonly")
        search_combo["values"]=("Select","ID","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        search_entry = ttk.Entry(Search_frame,width=14,font=("sans serif",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        
        search_btn = Button(Search_frame,text="Search",width=14,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        search_btn.grid(row=0,column=3,padx=4)
        
         
        showAll_btn = Button(Search_frame,text="Show All",width=14,font=("sans serif",12,"bold"),bg="lightblue",fg="black")
        showAll_btn.grid(row=0,column=4)
        
        
        
        
        #=============table frame============
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=210,width=710,height=350)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","email","phone","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone_No")
        self.student_table.heading("teacher",text="Teacher's_Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #=============Functions============= After giving entry manually, save data in mysql database
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="A11n12K13u14",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_email.get(),
                self.var_phone.get(),self.var_teacher.get(),self.var_radio1.get()            
                 ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    
    #====fetch data==== show database entries in the right table view of student details page
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="A11n12K13u14",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #==========get cursor============= 
    # If you click any of the row of right side table of student details page, 
    # left panel will automatically show all the data of that specific row.
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_email.set(data[6])
        self.var_phone.set(data[7])
        self.var_teacher.set(data[8])
        self.var_radio1.set(data[9])
    
    #=========Update student details function===========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
        else:
            try:
                Upadate = messagebox.askyesno("Update","Do you want to update this student's details?",parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="A11n12K13u14",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update Student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Email=%s,Phone=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                                      (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_email.get(),
                self.var_phone.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()
                ))
                
                else:
                    if not Upadate:
                        return
                
                messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)
                
                conn.commit()
                self.fetch_data()
                conn.close()
                
            
            except Exception as es:
                messagebox.showerror("Error",f"Due TO: {str(es)}",parent=self.root)
    
    #=========function for delete student details entries======
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student is must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student's data",parent=self.root)
                
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="A11n12K13u14",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted this student details",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due TO: {str(es)}",parent=self.root)
    
    #reset function back to default
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
    #===========Generate Dataset or Take photo samples============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
            
        else:
            try:                
                conn = mysql.connector.connect(host="localhost",username="root",password="A11n12K13u14",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = self.var_std_id.get()
                
                my_cursor.execute("Update Student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Email=%s,Phone=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                                      (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_email.get(),
                self.var_phone.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()==id
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #=========load predefined data on face frontals from opencv
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #cascade classifier to detect face
                
                
                #function to crop face from the image rightly captured by webcam
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # minimum neighbour = 5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0) #open webcam
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croppped Face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Datasets completed!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due TO: {str(es)}",parent=self.root)
            
      



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    