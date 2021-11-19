from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import psycopg2


DB_HOST ='localhost'
DB_NAME='airres'
DB_USER='postgres'
DB_PASS= 'Shankar01'

conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur= conn.cursor()

root =Tk()  
root.title('Airport Reservation System')
root.geometry("500x300")




#mainframe
mainFrame =LabelFrame(root, text="", padx=20, pady=20)
mainFrame.pack(padx=10, pady=10)
mainLabel= Label(mainFrame, text="Airport Reservation System").grid(row=1, column=2)
#landingimg =ImageTk.PhotoImage(Image.open("icon.png"))
#landinglabel= Label(mainFrame, image=landingimg).grid(row=2, column=2)

fNameLabel= Label(mainFrame, text="First Name").grid(row=2, column=1)
fNameEntry= Entry(mainFrame, width=30)
fNameEntry.grid(row=2, column=2)

lNameLabel= Label(mainFrame, text="Last Name").grid(row=3, column=1)
lNameEntry= Entry(mainFrame, width=30)
lNameEntry.grid(row=3, column=2)

emailLabel= Label(mainFrame, text="Email ID").grid(row=4, column=1)
emailEntry= Entry(mainFrame, width=30)
emailEntry.grid(row=4, column=2)

phoneLabel= Label(mainFrame, text="Phone Number").grid(row=5, column=1)
phoneEntry= Entry(mainFrame, width=30)
phoneEntry.grid(row=5, column=2)

registerButton= Button(mainFrame, text="Register", command= registerClick)
registerButton.grid(row=8, column=2)
root.mainloop()

def registerClick():
    #top= Toplevel()
	#top.title("Book Your Flight")
    #flightFrame=LabelFrame(top, text="")
    #flightFrame.pack()
    fname = fNameEntry.get()
    lname = lNameEntry.get()
    email = emailEntry.get()
    phno = phoneEntry.get()

    insertquery= """insert into user1 values (%s, %s, %s, %s)"""
	record=(fname, lname, email, phno)
	cur.execute(insertquery,record)
	conn.commit()
	cur.close()
	conn.close()

	fname.delete(0, END)
	lname.delete(0, END)
	email.delete(0, END)
	phno.delete(0, END)

	messagebox.showinfo("Info added","Succesfully added user details")
