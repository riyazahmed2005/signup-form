# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:53:00 2024
  **** signup ****
@author: Riyaz
"""
#required module
import tkinter as tk
from PIL import ImageTk
import random as rd
from tkinter import messagebox
import mysql.connector
# database connectivity
connect=mysql.connector.connect(host="localhost",user="root",password="",port='3306',database="signup")
if connect.is_connected():
    pass
else:
    messagebox.showwarning('not connected','dbs not connected')
c=connect.cursor()
w=tk.Tk()
# window function
def window():
    global e1,e2,e3,b1,b2,connection,c
    w.title('signup')
    w.geometry('1000x670+200+0')
    w.resizable(False,False)
    w.configure(bg='white')
    #w.mainloop()
    w.configure(bg='white')
def dataentry():
    email=s1.get()
    name=s2.get()
    password=s3.get()
    if email.endswith('@gmail.com'):
        pass 
    else:
        messagebox.showerror('invalid format','invalid email format')
    if email=="" or password=="" or name=="":
        messagebox.showerror('invalid','enter all details')
    else:
        messagebox.showinfo('submited','submitted successfully')
        insert_values="INSERT INTO `formdetails`(`Email`, `username`, `password`) VALUES (%s,%s,%s)"
        vals=(email,name,password)
        c.execute(insert_values,vals)
        connect.commit()
def clear():
    global e1,e2,e3
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')
    passl.configure(text="")
def show():
    global img_button,image,e3
    e3.configure(show='')
    image=ImageTk.PhotoImage(file='D:\\python programs\\nohideicon.png')
    img_button.configure(image=image,command=hide)
def hide():
    global img_button,image2,e2
    e3.configure(show='*')
    image2=ImageTk.PhotoImage(file='D:\\python programs\\hideicon.png')
    img_button.configure(image=image2,command=show)
def suggest():
    global e3
    A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    B=A.lower()
    digit="1234567890"
    special="!@#$%^&*()_+{}:?><.,\/"
    defined_pass=A+B+digit+special 
    current_password=""
    for i in range(8):
        current_password+=rd.choice(defined_pass)
    passl.configure(text=current_password)
def design():
    global e1,e2,e3,l5,passl
    photo=tk.PhotoImage(file='loginimage2.png')
    l1=tk.Label(w,image=photo,bg='white',width=400,height=300)
    l1.place(x=40,y=120)
    frame=tk.Frame(w,width=460,height=540,bg='white',bd=0)
    frame.place(x=450,y=60)
    # heading lable
    head_lable=tk.Label(frame,text='Sign up',fg='black',bg='white',font=('microsoft yahi ui light',40,'bold'))
    head_lable.place(x=120,y=2)
    l3=tk.Label(frame,text='Email',fg='black',bg='white',font=('microsoft yahi ui light',14))
    l3.place(x=75,y=100)
    e1=tk.Entry(frame,width=22,bg='white',fg='black',font=('microsoft yahi ui light',14),bd=0,textvariable=s1)
    e1.place(x=80,y=130)
    lframe=tk.Frame(frame,width=265,height=2,bg='black')
    lframe.place(x=80,y=152)
    l4=tk.Label(frame,text='Username',fg='black',bg='white',font=('microsoft yahi ui light',14))
    l4.place(x=74,y=190)
    e2=tk.Entry(frame,bg='white',fg='black',font=('microsoft yahi ui light',14),bd=0,textvariable=s2)
    e2.place(x=80,y=220)
    l2frame=tk.Frame(frame,width=265,height=2,bg='black')
    l2frame.place(x=80,y=250)
    #passsword
    l5=tk.Label(frame,text='password',fg='black',bg='white',font=('microsoft yahi ui light',14))
    l5.place(x=74,y=280)
    e3=tk.Entry(frame,bg='white',show='*',fg='black',font=('microsoft yahi ui light',14),bd=0,textvariable=s3)
    e3.place(x=80,y=310)
    l2frame=tk.Frame(frame,width=265,height=2,bg='black')
    l2frame.place(x=80,y=340)
    #suggest me a password
    password_suggest=tk.Button(frame,text='Suggest password',bg='white',fg='blue',bd=0,font=('microsoft yahi ui light',11,'bold'),command=suggest)
    password_suggest.place(x=70,y=370)
    #pass lable 
    passl=tk.Label(frame,bg="white",fg="black",font=('microsoft yahi ui light',14,'bold')) 
    passl.place(x=260,y=370)
    #button
    b1=tk.Button(frame,width=10,text='signup',bg='green',fg='white',font=('microsoft yahi ui light',14),bd=0,command=dataentry)
    b1.place(x=80,y=440)
    b2=tk.Button(frame,width=10,text='Reset',bg='blue',fg='white',font=('microsoft yahi ui light',14),bd=0,command=clear)
    b2.place(x=220,y=440)
    global img_button,image2
    image2=ImageTk.PhotoImage(file='D:\\python programs\\hideicon.png')
    img_button=tk.Button(w,image=image2,bg='white',bd=0,command=show)
    img_button.place(x=810,y=370)
    w.mainloop()
s1=tk.StringVar()
s2=tk.StringVar()
s3=tk.StringVar()
window()
design()

