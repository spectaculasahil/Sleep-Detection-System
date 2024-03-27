from tkinter import *
import tkinter as Tk
def loginaccount():
    a=()
    e1=entry1.get()
    p1=entry0.get()
    import mysql.connector as sqltor
    connect=sqltor.connect(host='localhost',user='root',passwd='1234')
    cursor=connect.cursor()
    cursor.execute('use customer_database;')
    cursor.execute('select * from login_info;')
    rows=cursor.fetchall()
    for x in rows:
        a=a+x
    if e1 not in a and p1 in a:
        messagebox.showinfo('Login','Account not present Sign up first !')
    elif e1 and p1 in a:
        messagebox.showinfo('Login','Account found redirecting you to different window')
        boardpage()
        s=a.index(e1)
        global v
        v=a[s-1]
        u=a[s+4]


from Signuppage import *
from window import *




loginpage = Tk.Toplevel()

loginpage.geometry("1920x1080")
loginpage.configure(bg = "#ffffff")
canvas = Canvas(
    loginpage,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundlog.png")
background = canvas.create_image(
    845.0, 520.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0log.png")
entry0_bg = canvas.create_image(
    255.5, 535.0,
    image = entry0_img)

entry0 = Entry(loginpage,
    bd = 0,
    bg = "#f1f3f6",
    highlightthickness = 0)

entry0.place(
    x = 49.077810287475586, y = 510,
    width = 412.8443794250488,
    height = 48)

entry1_img = PhotoImage(file = f"img_textBox1log.png")
entry1_bg = canvas.create_image(
    255.5, 422.0,
    image = entry1_img)

entry1 = Entry(loginpage,
    bd = 0,
    bg = "#f1f3f6",
    highlightthickness = 0)

entry1.place(
    x = 49.077810287475586, y = 397,
    width = 412.8443794250488,
    height = 48)

img0 = PhotoImage(file = f"img0log.png")
b0 = Button(loginpage,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = loginaccount,
    relief = "flat")

b0.place(
    x = 41, y = 620,
    width = 429,
    height = 50)

img1 = PhotoImage(file = f"img1log.png")
b1 = Button(loginpage,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = signup,
    relief = "flat")

b1.place(
    x = 41, y = 771,
    width = 429,
    height = 50)

loginpage.resizable(False, False)
loginpage.mainloop()
