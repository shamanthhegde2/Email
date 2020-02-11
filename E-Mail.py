#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")


def send():
    a=entry1.get()
    p=entry2.get()
    r=entry3.get()
    s=entry5.get()
    msg=entry6.get("1.0","end-1c")
    message=MIMEMultipart()
    message["from"] = "User"
    message["to"] = r
    message["subject"] = s
    message.attach(MIMEText(msg))
    try:
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(a,p)
            smtp.send_message(message)
    except:
        error=tk.Label(window,text="Not sent...",font=("Times",15),fg="red",bg="black",relief="solid")
        error.place(x=315,y=119)
    label2 = tk.Label(window, text="Mail sent...",font=("Times",15),fg="red",bg="black",relief="solid")
    label2.place(x=315,y=119)
    
   


window = tk.Tk()
account = tk.StringVar()
password = tk.StringVar()
receiver = tk.StringVar()
subject = tk.StringVar()
msgbody = tk.StringVar()
window.title("MaIL✉")
window.config(background="black")
window.geometry("800x750")
label = tk.Label(window, text="QuicK MaiL", font=(
    "Arial Bold", 50), fg="#D4AF37", bg="black")#,relief='solid')
label.place(x=230,y=0)
a = tk.Label(window, text="To use this app turn this setting ON for your account",font=("Bazooka",12),fg="blue", cursor="hand2",bg="black")
a.place(x=390,y=100)
a.bind("<Button-1>", setup)
label1=tk.Label(window,text="Your Email Account:",font=("Bazooka",15),fg="#D4AF37",bg="black")
label1.place(x=100,y=150)
entry1=tk.Entry(window,textvar=account,width=60)
entry1.place(x=360,y=155)
label2=tk.Label(window,text="Your Password:",font=("Bazooka",15),fg="#D4AF37",bg="black")
label2.place(x=100,y=200)
entry2=tk.Entry(window,textvar=password,width=60,show="*")
entry2.place(x=360,y=205)
label3=tk.Label(window,text="Receiver's Email:",font=("Bazooka",15),fg="#D4AF37",bg="black")
label3.place(x=100,y=250)
entry3=tk.Entry(window,textvar=receiver,width=60)
entry3.place(x=360,y=255)
label4=tk.Label(window,text="Lets Prepare",font=("Bazooka",15),fg="#D4AF37",bg="black")
label4.place(x=400,y=300)
label5=tk.Label(window,text="Subject:",font=("Bazooka",15),fg="#D4AF37",bg="black")
label5.place(x=100,y=350)
entry5=tk.Entry(window,textvar=subject,width=60)
entry5.place(x=360,y=354)
label6=tk.Label(window,text="Body:",font=("Bazooka",15),fg="#D4AF37",bg="black")
label6.place(x=100,y=400)
entry6 =tk.Text(window, height=13, width=45)
entry6.place(x=360,y=404)
button1=tk.Button(window,text="Send Mail",font=("Bazooka",10),fg="#D4AF37",bg="blue",relief=RIDGE,width=10,command=send)
button1.place(x=650,y=650)
window.mainloop()


# In[ ]:




