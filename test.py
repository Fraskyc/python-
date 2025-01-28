from tkinter import *

 

class User:

    Username = ""

    Password = ""

 

def verify_login():

    User.Username = username_input.get()

    User.Password = password_input.get()

    if User.Username == "test" and User.Password == "test":

        login_successful()

    else:

        login_failed()

 

def login_successful():

    login_window.destroy()

    main_window = Tk()

    main_window.title("Hlavní okno")

    main_window.geometry("300x200")

    label = Label(main_window, text="Ahoj" + " " + User.Username + " "+ "Jo")

    label.pack(pady=20)

    main_window.mainloop()

 

def login_failed():

    error_label.config(text="Chybné přihlašovací údaje")

 

login_window = Tk()

login_window.title("Přihlášení")

login_window.geometry("300x200")

 

username_label = Label(login_window, text="Uživatelské jméno:")

username_label.pack(pady=10)

username_input = Entry(login_window)

username_input.pack()

 

password_label = Label(login_window, text="Heslo:")

password_label.pack(pady=10)

password_input = Entry(login_window, show="*")

password_input.pack()

 

login_button = Button(login_window, text="Přihlásit se", command=verify_login)

login_button.pack(pady=20)

 

error_label = Label(login_window, fg="red")

error_label.pack()

 

login_window.mainloop()
