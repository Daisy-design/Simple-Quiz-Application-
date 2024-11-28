from tkinter import *
import tkinter.messagebox as box

def open_register():
    register=Toplevel(home)
    register.title('Registration')

    unFrame=Frame(register)
    unLabel = Label(unFrame, text="User Name")
    unEntry = Entry(unFrame)

    unLabel.pack(side=LEFT)
    unEntry.pack(side=RIGHT)
    unFrame.pack(padx=20, pady=10)

    fnFrame=Frame(register)
    fnLabel = Label(fnFrame, text="First Name")
    fnEntry = Entry(fnFrame)

    fnLabel.pack(side=LEFT)
    fnEntry.pack(side=RIGHT)
    fnFrame.pack(padx=20, pady=10)

    lnFrame=Frame(register)
    lnLabel = Label(lnFrame, text="Last Name")
    lnEntry = Entry(lnFrame)

    lnLabel.pack(side=LEFT)
    lnEntry.pack(side=RIGHT)
    lnFrame.pack(padx=20, pady=10)

    clFrame=Frame(register)
    clLabel = Label(clFrame, text="User Name")
    clEntry = Entry(clFrame)

    clLabel.pack(side=LEFT)
    clEntry.pack(side=RIGHT)
    clFrame.pack(padx=20, pady=10)

    psFrame=Frame(register)
    psLabel = Label(psFrame, text="User Password")
    psEntry = Entry(psFrame)

    psLabel.pack(side=LEFT)
    psEntry.pack(side=RIGHT)
    psFrame.pack(padx=20, pady=10)

    actionsFrame = Frame(register)
    saveBtn = Button(actionsFrame, text="Register")
    saveBtn.pack(side=RIGHT, padx=20, pady=10)
    actionsFrame.pack(padx=20, pady=10)

def open_log_in():
    log_in=Toplevel(home)
    log_in.title('Log In')

    unFrame=Frame(log_in)
    unLabel = Label(unFrame, text="User Name")
    unEntry = Entry(unFrame)

    unLabel.pack(side=LEFT)
    unEntry.pack(side=RIGHT)
    unFrame.pack(padx=20, pady=10)

    psFrame=Frame(log_in)
    psLabel = Label(psFrame, text="User Password")
    psEntry = Entry(psFrame)

    psLabel.pack(side=LEFT)
    psEntry.pack(side=RIGHT)
    psFrame.pack(padx=20, pady=10)

    actionsFrame = Frame(log_in)
    saveBtn = Button(actionsFrame, text="Log In")
    saveBtn.pack(side=RIGHT, padx=20, pady=10)
    actionsFrame.pack(padx=20, pady=10)

home=Tk()
home.title('Simple Quiz Application')

label=Label(home,text='Welcome would you like to Register or Log in')
label.pack(padx=100,pady=100)

log_in_btn= Button(home,text='Log in',command=open_log_in)
log_in_btn.pack(padx=80,pady=50)

register_btn=Button(home,text='Register',command=open_register)
register_btn.pack(padx=80,pady=50)
home.mainloop()
