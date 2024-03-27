from tkinter import *
from tkinter import messagebox
import tkinter as Tk
def connectioncheck():
    import mysql.connector as sqltor
    connect=sqltor.connect(host='localhost',user='root',passwd='1234')
    if connect.is_connected:
        messagebox.showinfo('Database Check','Connection to database established')
        cursor=connect.cursor()
        cursor.execute('show databases;')
        if ('customer_database',) in cursor:
            messagebox.showinfo('Database Check','Master Database present')
            register()
          
        else:
            cursor.execute('create database customer_database;')
            messagebox.showinfo('Database Check','Master Database was not present but now it is Created')
            tablecheck()
            register()

def register():
    global x1
    global x2
    global x3
    global x4
    global x5
    
    x1=Name.get()
    x2=Email.get()
    x3=Password.get()
    x4=Age.get()
    x5=Phno.get()
    import mysql.connector as sqltor
    connect=sqltor.connect(host='localhost',user='root',passwd='1234')
    cursor=connect.cursor()
    cursor.execute('use customer_database;')
    sql="insert into login_info(cust_name,cust_email,cust_password,cust_age,cust_phno) values(%s,%s,%s,%s,%s)"
    data=(x1,x2,x3,x4,x5)
    cursor.execute(sql,data)
    connect.commit()
    messagebox.showinfo('Success','Thanks for creating the account')
            
            

def tablecheck():
    import mysql.connector as sqltor
    connect=sqltor.connect(host='localhost',user='root',passwd='1234')
    cursor=connect.cursor()
    cursor.execute('use customer_database;')
    cursor.execute('show tables;')
    if ('login_info',) in cursor:
        messagebox.showinfo('Table Integrity','Table found no need to be created')
    else:
        cursor.execute(' create table login_info(cust_id int(9) auto_increment primary key,cust_name char(40),cust_email varchar(60),cust_password varchar(100),cust_age varchar(4),cust_phno varchar(13));')
        messagebox.showinfo('Table Integrity','Table was not found but now is created')


def signup():
    global Name
    global Email
    global Password
    global Age
    global Phno
    

  
        
    


    
    signuppage= Tk.Toplevel()

    signuppage.geometry("1920x1080")
    signuppage.configure(bg = "#ffffff")
    canvas = Canvas(
    signuppage,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgroundsign.png")
    background = canvas.create_image(
    910.0, 540.0,
    image=background_img)

    img0 = PhotoImage(file = f"img0sign.png")
    b0 = Button(signuppage,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = connectioncheck,
    relief = "flat")

    b0.place(
    x = 51, y = 824,
    width = 429,
    height = 50)

    img1 = PhotoImage(file = f"img1sign.png")
    b1 = Button(signuppage,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = print('hello'),
    relief = "flat")

    b1.place(
    x = 47, y = 937,
    width = 429,
    height = 50)

    Phno_img = PhotoImage(file = f"img_textBox0sign.png")
    Phno_bg = canvas.create_image(
    261.5, 679.0,
    image = Phno_img)

    Phno = Entry(signuppage,
    bd = 0,
    bg = "#f1f3f6",
    highlightthickness = 0)

    Phno.place(
    x = 55.077810287475586, y = 654,
    width = 412.8443794250488,
    height = 48)

    Age_img = PhotoImage(file = f"img_textBox1sign.png")
    Age_bg = canvas.create_image(
    260.5, 582.0,
    image = Age_img)

    Age = Entry(signuppage,
    bd = 0,
    bg = "#f1f3f6",
    highlightthickness = 0)

    Age.place(
    x = 54.077810287475586, y = 557,
    width = 412.8443794250488,
    height = 48)

    Name_img = PhotoImage(file = f"img_textBox2sign.png")
    Name_bg = canvas.create_image(
    261.5, 262.0,
    image = Name_img)

    Name = Entry(signuppage,
    bd = 0,
    bg = "#f1f3f6",
    highlightthickness = 0)

    Name.place(
    x = 55.077810287475586, y = 237,
    width = 412.8443794250488,
    height = 48)

    Email_img = PhotoImage(file = f"img_textBox3sign.png")
    Email_bg = canvas.create_image(
    261.5, 371.0,
    image = Email_img)

    Email = Entry(signuppage,
    bd = 0,
    bg = "#f1f3f6",
    highlightthickness = 0)

    Email.place(
    x = 55.077810287475586, y = 346,
    width = 412.8443794250488,
    height = 48)

    Password_img = PhotoImage(file = f"img_textBox4sign.png")
    Password_bg = canvas.create_image(
    260.5, 478.0,
    image = Password_img)

    Password = Entry(signuppage,
    bd = 0,
    bg = "#f1f3f6",
    highlightthickness = 0)

    Password.place(
    x = 54.077810287475586, y = 453,
    width = 412.8443794250488,
    height = 48)

    signuppage.resizable(False, False)
    signuppage.mainloop()


