
from tkinter import *

#creating window
window=Tk()
window.title("Registration form")
window.state("zoomed")
icon=PhotoImage(file="VVIT_Logo.png")
window.iconphoto(True, icon)

#heading
Label(window,text="STUDENT REGISTRATION FORM",font =("sans serif",30,"bold"), fg="black", padx=20,pady=10,image=icon,compound=LEFT).pack(pady=20)


# name,roll number,email,phone number,address
details=["NAME","REGISTRATION NUMBER","EMAIL","PHONE NUMBER","ADDRESS"]
for i in details:
    Label(window,text=i,font=("Arial" ,10 ,"bold")).pack(pady=5)
    Entry(window,width=30,font=("Arial" ,10 )).pack(pady=10)

#course
Label(window,text="COURSE",font=("Arial" ,10 ,"bold")).pack(pady=5)   

course_Var=StringVar()
course_Var.set("SELECT COURSE")
course_menu=OptionMenu(window,course_Var,
                       "CSM", "CSE", "ECE","MECH","CIVIL","BBA","MBA","BSC")
course_menu.pack(pady=5)

#register button
def register():
    result.config(text=f"Congratulations! You have successfully registered for {course_Var.get()} course")

Button(window,text="REGISTER",font=("Arial",10,"bold"),bg="green",fg="black",activebackground="green",command=register).pack(pady=20)
result=Label(window,text="",font=("Arial",15),fg="black")
result.pack(pady=20)

window.mainloop()
