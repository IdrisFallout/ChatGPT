from tkinter import *

from dotenv import dotenv_values
from pyChatGPT import ChatGPT

config = dotenv_values(".env")

print(config['EMAIL'], config['PASSWORD'])


api = ChatGPT(auth_type='google', email=f"{config['EMAIL']}", password=f"{config['PASSWORD']}")


def update_human_textbox_height(human_chat_frame, new_height):
    human_chat_frame.configure(height=new_height)
    enable_scroll.counter += new_height
    conversation_frame.configure(height=conversation_frame.winfo_height() + new_height)


def update_ai_textbox_height(ai_chat_frame, new_height):
    ai_chat_frame.configure(height=new_height)
    enable_scroll.counter += new_height
    conversation_frame.configure(height=conversation_frame.winfo_height() + new_height)


def execute_prompt():
    response = api.send_message(message_box_txt.get())

    human_chat_frame = Frame(conversation_frame, bg="#343541", width=1200, height=70)
    human_chat_frame.pack(side="top", fill="both", expand=True)
    Label(human_chat_frame, image=human_user_icon, bg="#343541").place(x=140, y=17)
    lb = Label(human_chat_frame, text=f"{message_box_txt.get()}", pady=20, bg="#343541", font=font, fg="white",
               wraplength=800, justify=LEFT)
    lb.place(x=190, y=0)
    root.after(100, lambda: update_human_textbox_height(human_chat_frame, lb.winfo_height()))

    ai_chat_frame = Frame(conversation_frame, bg="#444654", width=1200, height=70)
    ai_chat_frame.pack(side="top", fill="both", expand=True)
    Label(ai_chat_frame, image=ai_user_icon, bg="#444654").place(x=140, y=17)
    lb1 = Label(ai_chat_frame, text=f"{response['message']}", pady=20, bg="#444654", font=font, fg="white",
                wraplength=800, justify=LEFT)
    lb1.place(x=190, y=0)
    root.after(120, lambda: update_ai_textbox_height(ai_chat_frame, lb1.winfo_height()))
    chatgpt_description_lbl.destroy()
    message_box_txt.delete(0, END)


def on_mousewheel(event):
    if enable_scroll.allowScroll:
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def enable_scroll():
    enable_scroll.allowScroll = True


def disable_scroll():
    enable_scroll.allowScroll = False


root = Tk()
root.title("ChatGPT")
photo = PhotoImage(file='images/chatgpt/chatgpt-icon.png')
root.wm_iconphoto(True, photo)
width = 1440
height = 735

enable_scroll.allowScroll = False
enable_scroll.counter = 0

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

root.geometry(f'{width}x{height}+{int(x)}+{int(y) - 30}')
font = ("OpenSans-Regular", 11)

human_user_icon = PhotoImage(file=f"images/chatgpt/profile-user.png")
ai_user_icon = PhotoImage(file=f"images/chatgpt/chatgpt2.png")

img0 = PhotoImage(file=f"images/chatgpt/img0.png")
b0 = Label(image=img0, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
b0.place(x=240, y=0, width=1200, height=height)
img1 = PhotoImage(file=f"images/chatgpt/img1.png")
b1 = Label(image=img1, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
b1.place(x=0, y=0, width=240, height=height)

chat_viewport_frame = Frame(root, bg="#343541", height=613, width=1200, bd=0, highlightthickness=0, relief="flat")
chat_viewport_frame.place(x=240, y=0)

canvas = Canvas(chat_viewport_frame, bg="#343541", height=613, width=1200, bd=0, highlightthickness=0, relief="flat")
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", on_mousewheel)
canvas.bind("<Enter>", lambda e: enable_scroll())
canvas.bind("<Leave>", lambda e: disable_scroll())
canvas.pack(side="top", fill="both", expand=True)

conversation_frame = Frame(canvas, width=1200, height=613, bg="#343541", bd=0, relief='flat')
conversation_frame.pack(side="top", fill="both", expand=True)
conversation_frame.pack()

img2 = PhotoImage(file=f"images/chatgpt/chatgpt.png")
chatgpt_description_lbl = Label(conversation_frame, image=img2, borderwidth=0, highlightthickness=0, relief="flat", bd=0
                                , bg="#343541")

chatgpt_description_lbl.place(x=256.11, y=105, width=688, height=403)

canvas.create_window((0, 0), window=conversation_frame, anchor='nw')

img3 = PhotoImage(file=f"images/chatgpt/messagebox.png")
b3 = Label(image=img3, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
b3.place(x=456, y=644, width=768, height=50)

send_message_img = PhotoImage(file=f"images/chatgpt/send-message.png")
send_message_lbl = Label(image=send_message_img, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#40414F")

send_message_lbl.bind("<Button-1>", lambda e: execute_prompt())
send_message_lbl.place(x=1195, y=661)

message_box_txt = Entry(bg="#40414F", bd=0, relief="flat", fg="#FFFFFF", font=font)
message_box_txt.configure(insertbackground="white")
message_box_txt.bind("<Return>", lambda e: execute_prompt())
message_box_txt.place(x=456 + 10, y=644 + 10, width=768 - 50, height=50 - 20)

new_thread_img = PhotoImage(file=f"images/chatgpt/new thread.png")
new_thread_hovered_img = PhotoImage(file=f"images/chatgpt/new thread hovered.png")
new_thread_btn = Label(image=new_thread_img, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
new_thread_btn.bind("<Enter>", lambda e: new_thread_btn.configure(image=new_thread_hovered_img))
new_thread_btn.bind("<Leave>", lambda e: new_thread_btn.configure(image=new_thread_img))

new_thread_btn.place(x=15, y=17, width=209, height=47)

dark_mode_img = PhotoImage(file=f"images/chatgpt/dark mode.png")
dark_mode_hovered_img = PhotoImage(file=f"images/chatgpt/dark mode hovered.png")
dark_mode_btn = Label(image=dark_mode_img, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
dark_mode_btn.bind("<Enter>", lambda e: dark_mode_btn.configure(image=dark_mode_hovered_img))
dark_mode_btn.bind("<Leave>", lambda e: dark_mode_btn.configure(image=dark_mode_img))

dark_mode_btn.place(x=15, y=504, width=209, height=47)

discord_img = PhotoImage(file=f"images/chatgpt/discord.png")
discord_hovered_img = PhotoImage(file=f"images/chatgpt/discord hovered.png")
discord_btn = Label(image=discord_img, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
discord_btn.bind("<Enter>", lambda e: discord_btn.configure(image=discord_hovered_img))
discord_btn.bind("<Leave>", lambda e: discord_btn.configure(image=discord_img))

discord_btn.place(x=15, y=561, width=209, height=47)

updates_img = PhotoImage(file=f"images/chatgpt/updates.png")
updates_hovered_img = PhotoImage(file=f"images/chatgpt/updates hovered.png")
updates_btn = Label(image=updates_img, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
updates_btn.bind("<Enter>", lambda e: updates_btn.configure(image=updates_hovered_img))
updates_btn.bind("<Leave>", lambda e: updates_btn.configure(image=updates_img))

updates_btn.place(x=15, y=618, width=209, height=47)

logout_img = PhotoImage(file=f"images/chatgpt/logout.png")
logout_hovered_img = PhotoImage(file=f"images/chatgpt/logout hovered.png")
logout_btn = Label(image=logout_img, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")
logout_btn.bind("<Enter>", lambda e: logout_btn.configure(image=logout_hovered_img))
logout_btn.bind("<Leave>", lambda e: logout_btn.configure(image=logout_img))

logout_btn.place(x=15, y=675, width=209, height=47)

img9 = PhotoImage(file=f"images/chatgpt/line.png")
b9 = Label(image=img9, borderwidth=0, highlightthickness=0, relief="flat", bd=0, bg="#343541")

b9.place(x=0, y=496, width=240, height=0)

root.resizable(False, False)
root.mainloop()
