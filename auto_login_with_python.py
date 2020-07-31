from tkinter import *


def fun():
    def autologin():
        username.set("coding community")
        password.set("****************")

    login_screen = Tk()
    login_screen.title("Auto login with python")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username = StringVar()
    password = StringVar()
    username_login_entry = Entry(login_screen, textvariable=username)
    username_login_entry.pack()
    l1 = Label(login_screen, text="").pack()
    l2 = Label(login_screen, text="Password").pack()
    password_login_entry = Entry(login_screen, textvariable=password)
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Apply auto fill", command=autologin).pack()
    Button(login_screen, text="Login Now", width=10, height=1).pack(pady=10)
    login_screen.mainloop()

fun()
