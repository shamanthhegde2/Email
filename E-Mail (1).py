#!/usr/bin/env python
# coding: utf-8

# In[114]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox # to use messagebox command in tkinter
from PIL import Image,ImageTk #to use image as background in tkinter
import webbrowser #to open browser
from email.mime.multipart import MIMEMultipart # Main template of email in which values are given
from email.mime.text import MIMEText #used when sending a text
from email.mime.image import MIMEImage #used when sending an image
from pathlib import Path #to set the path of an image
import smtplib #to access server
from datetime import date#for date
import time #for time
today=date.today()
is_image=False
def img(): #To send an Image
    entry6.destroy()
    label6.destroy()
    path=StringVar()
    is_image=True
    label_image=tk.Label(window,text="Image Path:",font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
    label_image.place(x=200,y=450)
    entry_image=tk.Entry(window,textvar=path,width=60)
    entry_image.place(x=460,y=454)
    button3=tk.Button(window,text="Send Mail",font=("Bazooka",10),fg="#D4AF37",bg="#DC143C",relief=RIDGE,width=10,command=lambda:send(is_image,r"{0}".format(path.get())))
    button3.place(x=750,y=700)
    
def tick():#to update the clock every 200ms
    time_string=time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)
def setup(event):#to access the req browser
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")


def send(is_image,path=" "): #to set the required parameters in MIIMEMultipart and sending it using smtplib module
    
    a=account.get()
    p=password.get()
    r=receiver.get()
    s=subject.get()
    if not is_image:
        msg=entry6.get("1.0","end-1c")
    else:
        msg=path
    message=MIMEMultipart()
    message["from"] = "User"
    message["to"] = r
    message["subject"] = s
    if not is_image:
        message.attach(MIMEText(msg))
    else:
        message.attach(MIMEImage(Path(path).read_bytes()))
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        try:
            smtp.login(a,p)
            smtp.send_message(message)
            tk.messagebox.showinfo("output","Successfully Sent!!")
    
        except:
            tk.messagebox.showinfo("output","unsuccessfull sorry:(")
    
   


window = tk.Tk()
image=Image.open(r"D:/Shrunk.png")
photo=ImageTk.PhotoImage(image)
lab=tk.Label(image=photo)
lab.place(x=0,y=0)
account = tk.StringVar()
password = tk.StringVar()
receiver = tk.StringVar()
subject = tk.StringVar()
msgbody = tk.StringVar()
window.title("MaIL✉")
window.config(background="black")
window.geometry("1000x800")
label = tk.Label(window, text="QuicK MaiL", font=(
    "Arial Bold", 50), fg="#D4AF37",bg="#DC143C")#,relief='solid')
label.place(x=340,y=0)
a = tk.Label(window, text="To use this app turn this setting ON for your account",font=("Bazooka",12),fg="blue",bg="papaya whip",cursor="hand2")
a.place(x=530,y=120)
a.bind("<Button-1>", setup)
today_date=tk.Label(window,text=today,font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
today_date.place(x=400,y=160)
clock=tk.Label(window,font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
clock.place(x=550,y=160)
tick()
label1=tk.Label(window,text="Your Email Account:",font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
label1.place(x=200,y=200)
entry1=tk.Entry(window,textvar=account,width=60)
entry1.place(x=460,y=205)
label2=tk.Label(window,text="Your Password:",font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
label2.place(x=200,y=250)
entry2=tk.Entry(window,textvar=password,width=60,show="*")
entry2.place(x=460,y=255)
label3=tk.Label(window,text="Receiver's Email:",font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
label3.place(x=200,y=300)
entry3=tk.Entry(window,textvar=receiver,width=60)
entry3.place(x=460,y=305)
label4=tk.Label(window,text="Lets Prepare",font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
label4.place(x=500,y=350)
label5=tk.Label(window,text="Subject:",font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
label5.place(x=200,y=400)
entry5=tk.Entry(window,textvar=subject,width=60)
entry5.place(x=460,y=404)
label6=tk.Label(window,text="Body:",font=("Bazooka",15),fg="#D4AF37",bg="#DC143C")
label6.place(x=200,y=450)
entry6 =tk.Text(window, height=13, width=45)
entry6.place(x=460,y=454)
button1=tk.Button(window,text="Send Mail",font=("Bazooka",10),fg="#D4AF37",bg="blue",relief=RIDGE,width=10,command=lambda:send(is_image))
button1.place(x=750,y=700)
button2=tk.Button(window,text="Add image",font=("Bazooka",10),fg="#D4AF37",bg="blue",relief=RIDGE,width=10,command=img)
button2.place(x=600,y=700)
window.mainloop()


# In[107]:


from datetime import date
today=str(date.today())
print(today)


# In[ ]:


import time

