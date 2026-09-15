from tkinter import *

window = Tk()

window.geometry("1239x670")
window.title("Resourse Booking System")

icon = PhotoImage(file='./assets/scrbs.png')
window.iconphoto(True,icon)

label = Label(window,
            text="Resources Center",
            font=('ubuntu',28,'bold'), 
            fg="#D5E8FB",
            bg='#0055af',
            padx=20,
            image=icon,
            compound='left')


label.pack()
# label.place(x=0,y=0)

window.mainloop()