import smtplib
import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Данные авторизации
EMAIL_ADDRESS = "СЮДА НУЖНО ВСТАВИТЬ ПОЧТУ"
EMAIL_PASSWORD = "СЮДА НУЖНО ВСТАВИТЬ ПАРОЛЬ"
SMTP_SERVER = "SMTP СЕРВЕР"
SMTP_PORT = 587

# База данных
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sent_emails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipient TEXT,
    subject TEXT,
    body TEXT,
    attachments TEXT
)
""")
conn.commit()

def send_email():
    recipient = entry_recipient.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END) + text_signature.get("1.0", tk.END)
    files = file_list.get(0, tk.END)

    if not recipient or not subject:
        messagebox.showerror("Ошибка", "Получатель и тема обязательны")
        return

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    
    for file in files:
        attach_file(msg, file)
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        cursor.execute("INSERT INTO sent_emails (recipient, subject, body, attachments) VALUES (?, ?, ?, ?)",
                       (recipient, subject, body, ",".join(files)))
        conn.commit()
        
        messagebox.showinfo("Успех", "Письмо отправлено")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка отправки: {str(e)}")

def attach_file(msg, file_path):
    part = MIMEBase('application', 'octet-stream')
    with open(file_path, 'rb') as f:
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
    msg.attach(part)

def add_attachment():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_list.insert(tk.END, file_path)

def clear_form():
    entry_recipient.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    text_body.delete("1.0", tk.END)
    file_list.delete(0, tk.END)

def preview_email():
    preview = tk.Toplevel(root)
    preview.title("Предпросмотр")
    ttk.Label(preview, text="Тема: " + entry_subject.get()).pack()
    ttk.Label(preview, text="Получатель: " + entry_recipient.get()).pack()
    ttk.Label(preview, text="Текст:").pack()
    ttk.Label(preview, text=text_body.get("1.0", tk.END) + text_signature.get("1.0", tk.END)).pack()

def toggle_theme():
    global theme
    theme = "dark" if theme == "light" else "light"
    root.tk.call("set_theme", theme)

# UI
root = tk.Tk()
root.title("Почтовый клиент")
theme = "light"

ttk.Label(root, text="Получатель:").pack()
entry_recipient = ttk.Entry(root, width=50)
entry_recipient.pack()

ttk.Label(root, text="Тема:").pack()
entry_subject = ttk.Entry(root, width=50)
entry_subject.pack()

ttk.Label(root, text="Текст:").pack()
text_body = tk.Text(root, width=60, height=10)
text_body.pack()

ttk.Button(root, text="Прикрепить файл", command=add_attachment).pack()
file_list = tk.Listbox(root, width=50)
file_list.pack()

ttk.Label(root, text="Подпись:").pack()
text_signature = tk.Text(root, width=60, height=3)
text_signature.pack()

ttk.Button(root, text="Отправить", command=send_email).pack()
ttk.Button(root, text="Очистить", command=clear_form).pack()
ttk.Button(root, text="Предпросмотр", command=preview_email).pack()
ttk.Button(root, text="Тема", command=toggle_theme).pack()

root.mainloop()
conn.close()