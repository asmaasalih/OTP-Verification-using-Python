from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

import random
import math
import smtplib
from email.message import EmailMessage

def generate_otp():
    digits = '0123456789'
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP  

otp_code = generate_otp()  

def send_otp():
    body = "Your OTP verification code: " + otp_code
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = 'OTP CODE'
    msg['to'] = email_entry.get()
    user = "aemam383@gmail.com"
    msg['from'] = user
    password = "niadjkjlpbwqprwl"
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    
def verify_otp():
    otp_send = otp_entry.get()
    print(otp_send)
    if otp_send == otp_code:
        print("Verified OTP")
    else:
        print("OTP unverified")    

    
window = Tk()
window.title("OTP")
window.geometry("400x400")
window.configure(bg="#ffffff")


frm_line = Frame(master=window, width=400,height=5,bg="#063970")
frm_line.grid(row=0,column=0)
frm_body = Frame(master=window, width=400,height=300,bg="#ffffff")
frm_body.grid(row=1,column=0)

app_name = Label(frm_body,text="OTP Verification",height=2,font=("Anton 15 bold"),bg="#ffffff",fg="#063970")
app_name.place(x=130,y=10)

email_img = Image.open('email.png')
email_img.resize((50,50))
email_img = ImageTk.PhotoImage(email_img)

lbl_email_img = Label(frm_body,height=50,image=email_img,bg="white")
lbl_email_img.place(x=10,y=60)

email_entry = Entry(frm_body,width=24,bg="#ddded9",font=(("AdobeGothicStd  16")))
email_entry.place(x=70,y=70)
email_entry.place(height=35)

send_btn = Button(frm_body,text="Send OTP",width=15,bg="#063970",fg="#ffffff",command=send_otp,font=(("AdobeGothicStd ")))
send_btn.place(x=120,y=130)

otp_img = Image.open('otp.png')
otp_img.resize((50,50))
otp_img = ImageTk.PhotoImage(otp_img)

lbl_otp_img = Label(frm_body,height=50,image=otp_img,bg="white")
lbl_otp_img.place(x=10,y=200)

otp_entry = Entry(frm_body,width=24,bg="#ddded9",font=(("AdobeGothicStd  16")))
otp_entry.place(x=70,y=200)
otp_entry.place(height=35)

verify_btn = Button(frm_body,text="Verify OTP",width=15,bg="#063970",fg="#ffffff",command=verify_otp,font=(("AdobeGothicStd")))
verify_btn.place(x=120,y=260)



window.mainloop()

