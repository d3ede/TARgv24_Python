from tkinter import *

import smtplib,ssl
from email.message import EmailMessage

def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    l_lisatud.configure(text=file)
    return file

def saada_kiri():
   kellele=email_box.get()
   kiri=kiri_box.get("1.0",END)
   smtp_server="smtp.gmail.com"
   port=587
   senrder_email="theskonel@gmail.com"
   password=""
   context=ssl._create_default_context()
   msg=EmailMessage()
   msg.set_content(kiri)
   msg['Subject']="E-kiri saatmine"
   msg['From']="Matviei Orlov"
   msg['To']=kellele
   with open(file,'rb') as fpilt:
       pilt=fpilt.read()
   msg.add_attachment(pilt,maintype='image',subtype=imghdr.what(None,pilt))
   try:
       server=smtplib.SMTP(smtp_server,port)
       server.starttls(context=context)
       server.login(sender_email,password)
       server.send_message(msg)
       messagebox.showinfo("Informatsioon","Kiri oli saadetud")
   except Exception as e:
       messagebox.showerror("Error",e)
   finally:
       server.quit()

root=Tk()
root.geometry("700x600")
root.resizable(False,False)
root.title("E-Kirja saatmine")

root.mainloop