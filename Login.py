from tkinter import *


def toggle_remember_me():
    if toggle_remember_me.state:
        remember_me_lbl.configure(image=img2)
        toggle_remember_me.state = False
    else:
        remember_me_lbl.configure(image=img3)
        toggle_remember_me.state = True


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

password_entry = Entry(root, width=50, bd=0, relief='flat', fg="white", bg="#101117", insertbackground="white")
password_entry.place(x=37, y=285, width=316, height=25)

img2 = PhotoImage(file=f"images/login/img2.png")
img3 = PhotoImage(file=f"images/login/img3.png")
remember_me_lbl = Label(image=img2, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#15171E")
remember_me_lbl.place(x=30, y=330, width=151, height=21)
remember_me_lbl.bind("<Button-1>", lambda e: toggle_remember_me())

root.resizable(False, False)
root.mainloop()
