from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("400x400")
window.title("Login")

name = Label(window, text="Enter Username:")
name.place(x=20, y=20)
name_ent = Entry(window)
name_ent.place(x=150, y=20)

password = Label(window, text="Enter Password:")
password.place(x=20, y=60)
password_ent = Entry(window, show="*")
password_ent.place(x=150, y=60)


def check_table():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='Hospital', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Login')
    for i in mycursor:
        print(i)


def login():
    check_table()


def register():
    name = name_ent.get()
    password = password_ent.get()
    if name_ent == "" or password_ent == "":
        messagebox.showerror("ERROR", "Please fill in username and password")
    elif name.isdigit():
        messagebox.showerror("Error", "Name does not contain letters")
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='Hospital', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO Login  VALUES (%s, %s)"
        val = (name_ent.get(), password_ent.get())
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        mycursor.execute('Select * from Login')
        messagebox.showinfo("SUCCESS", "New user and password added")

        # text file
        with open("Login.txt", "a+") as file:
            file.write("Username: " + name_ent.get() + "\n")
            file.write("Password: " + password_ent.get() + "\n")
            file.write("\n")
            file.close()


def clear():
    name_ent.delete(0, END)
    password_ent.delete(0, END)


def exit_btn():
    msg_box = messagebox.askquestion("Exit?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


login = Button(window, text="Login", command=login)
login.place(x=20, y=150)

register = Button(window, text="Register", command=register)
register.place(x=150, y=150)

exit_btn = Button(window, text="Exit", command=exit_btn)
exit_btn.place(x=20, y=200)

clear = Button(window, text="Clear", command=clear)
clear.place(x=150, y=200)

window.mainloop()
