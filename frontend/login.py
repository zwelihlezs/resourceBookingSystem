from tkinter import *
# from styles import *
import tkinter
import sys

sys.path.append('\\backend')
import login


primaryColor = "#D5E8FB"
secondaryColor = '#0055af'
window = Tk()
frame = tkinter.Frame()
frame.configure(bg=secondaryColor)

window.geometry('1245x680')
window.title('SCR Bokking System')
icon = PhotoImage(file='./assets/scrbs.png')
window.iconphoto(True,icon)
window.configure(bg=secondaryColor)

#create widgets
label = Label(frame,
            text="Resources Center",
            font=('ubuntu',28,'bold'), 
            fg=primaryColor,
            bg=secondaryColor,
            padx=20,
            image=icon,
            compound='left')
loginLabel = Label(frame, text="Login",font=('ubuntu', 19,'bold'), fg=primaryColor,bg=secondaryColor)
usernameLabel =Label(frame,text="username", font=('ubuntu', 14), fg=primaryColor,bg=secondaryColor)
usernameEntry = Entry(frame)
passwordLabel = Label(frame,text="pasword", font=('ubuntu', 14,), fg=primaryColor,bg=secondaryColor)
passwordEntry = Entry(frame, show="*") 
loginButton = Button(frame, text="login", font=('ubuntu', 14), fg=secondaryColor,bg=primaryColor, command=login)
warningLababel = Label(frame, text='warn',font=('ubuntu', 12,), fg='red',bg=secondaryColor)


#placing widget on the window
label.grid(row=1, column=0)
loginLabel.grid(row=2, column=0, columnspan=2, pady=4)
usernameLabel.grid(row=3, column=0)
usernameEntry.grid(row=4, column=0)
passwordLabel.grid(row=5, column=0)
passwordEntry.grid(row=6, column=0)
loginButton.grid(row=7, column=0,pady=5)
warningLababel.grid(row=8, column=0, )

frame.pack()

window.mainloop()