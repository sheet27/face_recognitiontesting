from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")
        self.root.wm_iconbitmap("logo.jpg")

        
        #============variable====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        # bg image
        img3=Image.open(r"D:\face_recognizer_project\college_photos\gZ7BM8C.jpg")
        img3=img3.resize((1600,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1600,height=900)
        
        #==============left image ====================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\Pictures\college_photos\l3.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)
        
        #==============label and entry=================
        
        #================row1===========
        fname=Label(frame,text="Frist Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",20,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=295,y=100,width=250)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",20,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)
        
        #================row2===========
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",20,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",20,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        #================row3===========
        security_Q=Label(frame,text="Select Security questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)
                
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",20,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        #=====row4==========
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",20,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        cofirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cofirm_pswd.place(x=370,y=310)
        
        self.txt_cofirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",20,"bold"))
        self.txt_cofirm_pswd.place(x=370,y=340,width=250)
        
        #====================checkbox=============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Term And Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)
        
        #============button==============
        img=Image.open(r"C:\Users\HP\Pictures\college_photos\reg.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white")
        b1.place(x=50,y=420,width=200)
        
        
        #============button==============
        img1=Image.open(r"C:\Users\HP\Pictures\college_photos\login.jfif")
        img1=img1.resize((200,60),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=380,y=420,width=200)
        
        
        #===============function declaration============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Requried")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='face_recognizer')
            my_cursor=conn.cursor()
            query=("select * from face where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into face values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(), 
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get(),
                                                                                    
                                                                                     
                                                                                     ))       
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Register Sucessfully")
        
            
        
        
        
        
               
        
        
                                                       
        
        
        
if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
                               
