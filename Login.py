import os
from tkinter import *

from dotenv import dotenv_values

config = dotenv_values(".env")


def toggle_remember_me():
    if toggle_remember_me.state:
        remember_me_lbl.configure(image=img2)
        toggle_remember_me.state = False
    else:
        remember_me_lbl.configure(image=img3)
        toggle_remember_me.state = True


def login_hovered():
    login_btn.configure(image=img5)


def login_not_hovered():
    login_btn.configure(image=img4)


def switching_windows():
    root.destroy()
    os.system('python ChatGPT.py')


def login():
    if email_entry.get() == "" or password_entry.get() == "":
        return
    try:
        if not toggle_remember_me.state:
            with open('.env', 'r') as f:
                output = f.readlines()
            if output[-1] == "SAVE_PASSWORD=YES":
                output[-1] = "SAVE_PASSWORD=NO"
            with open('.env', 'w') as f:
                f.write(f"EMAIL={email_entry.get()}\nPASSWORD={password_entry.get()}\n{output[2]}")
        else:
            with open('.env', 'r') as f:
                output = f.readlines()
            if output[-1] == "SAVE_PASSWORD=NO":
                output[-1] = "SAVE_PASSWORD=YES"
            with open('.env', 'w') as f:
                f.write(f"EMAIL={email_entry.get()}\nPASSWORD={password_entry.get()}\n{output[2]}")
    except:
        pass
    switching_windows()


def check_for_password():
    with open('.env', "r") as f:
        output = f.readlines()
        if output[-1] != "SAVE_PASSWORD=NO":
            return True
        else:
            return False


def remove_email_placeholder():
    add_password_placeholder()
    if email_entry.get() == "" or email_entry.get() == "Email":
        email_entry.delete(0, END)
        email_entry.configure(fg="white")


def add_email_placeholder():
    if email_entry.get() == "" or email_entry.get() == "Email":
        email_entry.delete(0, END)
        email_entry.configure(fg="#33343A")
        email_entry.insert(0, "Email")


def remove_password_placeholder():
    add_email_placeholder()
    if password_entry.get() == "" or password_entry.get() == "Password":
        password_entry.delete(0, END)
        password_entry.configure(fg="white")

def add_password_placeholder():
    if password_entry.get() == "" or password_entry.get() == "Password":
        password_entry.delete(0, END)
        password_entry.configure(fg="#33343A")
        password_entry.insert(0, "Password")

root = Tk()
root.title("ChatGPT")
photo = PhotoImage(file='images/chatgpt/chatgpt-icon.png')
root.wm_iconphoto(True, photo)
width = 390
height = 529

toggle_remember_me.state = False

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

root.geometry(f'{width}x{height}+{int(x)}+{int(y) - 30}')
root.configure(bg="#15171e")
canvas = Canvas(root, bg="#15171e", height=529, width=390, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"images/login/background.png")
background = canvas.create_image(204.0, 274.0, image=background_img)

img0 = PhotoImage(file=f"images/login/img0.png")
b0 = Label(image=img0, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#15171E")
b0.place(x=30, y=231, width=330, height=35)

email_entry = Entry(root, width=50, bd=0, relief='flat', fg="white", bg="#101117", insertbackground="white")
email_entry.place(x=37, y=236, width=316, height=25)

img1 = PhotoImage(file=f"images/login/img1.png")
b1 = Label(image=img1, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#15171E")
b1.place(x=30, y=280, width=330, height=35)

password_entry = Entry(root, width=50, bd=0, relief='flat', fg="white", bg="#101117",
                       insertbackground="white", show="*")
password_entry.place(x=37, y=285, width=316, height=25)
password_entry.bind("<Return>", lambda e: login())

img2 = PhotoImage(file=f"images/login/img2.png")
img3 = PhotoImage(file=f"images/login/img3.png")
remember_me_lbl = Label(image=img2, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#15171E")
remember_me_lbl.place(x=30, y=330, width=151, height=21)
remember_me_lbl.bind("<Button-1>", lambda e: toggle_remember_me())

img4 = PhotoImage(file=f"images/login/login.png")
img5 = PhotoImage(file=f"images/login/login-selected.png")
login_btn = Button(image=img4, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#15171E",
                   activebackground="#15171E", command=login)
if not check_for_password():
    login_btn.place(x=30, y=380, width=335, height=40)
    email_entry.configure(fg="#33343A")
    email_entry.insert(0, "Email")
    email_entry.bind("<Button-1>", lambda e: remove_email_placeholder())
    password_entry.configure(show="", fg="#33343A")
    password_entry.insert(0, "Password")
    password_entry.bind("<Button-1>", lambda e: remove_password_placeholder())
else:
    if config['SAVE_PASSWORD'] == "YES":
        toggle_remember_me()
        email_entry.insert(0, config['EMAIL'])
        password_entry.insert(0, config['PASSWORD'])
        root.after(1000, lambda: login())

login_btn.bind("<Enter>", lambda e: login_hovered())
login_btn.bind("<Leave>", lambda e: login_not_hovered())

root.resizable(False, False)
root.mainloop()
