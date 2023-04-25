#importing modules from tkinter
from tkinter import *
from datetime import date

# downoad any image to make it fancy 
#from PIL import Image, ImageTk
#from tkinter import messagebox

#Creating the tkinter window
window = Tk()
window.geometry('700x550')
window.title('Age Calculator')

#getting the current date
today=str(date.today())
list_today=today.split('-')

#importing image to add into the app
''' Note :- If you download an image and the PIL check to add image file path into the code'''

'''image = Image.open("D:\\Study\\Python\\v2.png")
resize = image.resize((300, 120), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resize)
ImageLabel = Label(image=photo)
ImageLabel.place(x=90,y=300)
ImageLabel.pack(pady=20) '''

#creating function to calculate the age
def calculateAge():
    global today
    #global new
    name=str(nameEntry.get())
    b_date=int(dateEntry.get())
    b_month=int(monthEntry.get())
    b_year=int(yearEntry.get())
    result_date=int(list_today[2])
    result_month=int(list_today[1])
    result_year=int(list_today[0])
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(b_date>result_date):
        result_month=result_month-1
        result_date=result_date+month[b_month-1]

    if(b_month>result_month):
        result_year=result_year-1
        result_month=result_month+12
    resultD=str(result_date-b_date)
    resultM=str(result_month-b_month)
    resultY=str(result_year-b_year)
    Final_rslt=Label(text='Hi '+name+ '! Your age is\n '+ resultY + ' years, ' + resultM + ' Months, ' + resultD + ' Days.')
    Final_rslt.config(font=('Sans Serif',15,'bold'))
    Final_rslt.place(x=195, y=415)



#Function to clear the previous entries
def CleanEntries():
    nameEntry.delete(0,END)
    dateEntry.delete(0, END)
    monthEntry.delete(0, END)
    yearEntry.delete(0, END)

#creating labels
Label(text='Name',font=('Sans Serif',23,'bold')).place(x=200,y=150)
Label(text='Date',font=('Sans Serif',23,'bold')).place(x=200,y=200)
Label(text='Month',font=('Sans Serif',23,'bold')).place(x=200,y=250)
Label(text='Year',font=('Sans Serif',23,'bold')).place(x=200,y=300)

#assigning as string values
nameValue= StringVar()
dateValue= StringVar()
monthValue= StringVar()
yearValue= StringVar()

#Enabling Entries
#nameEntry
nameEntry=Entry(window,textvariable=nameValue,width=20,bd=5,font=27)
nameEntry.place(x=300,y=150,)
#dateEntry
dateEntry=Entry(window,textvariable=dateValue,width=7,bd=5,font=27)
dateEntry.place(x=300,y=200,)
#monthEntry
#make sure to enter month in number
monthEntry=Entry(window,textvariable=monthValue,width=7,bd=5,font=27)
monthEntry.place(x=300,y=250)
#yearEntry
yearEntry=Entry(window,textvariable=yearValue,width=7,bd=5,font=27)
yearEntry.place(x=300,y=300)

#Creating Button for calculating age
Calculate=Button(text='Calculate Age',font=27,bg='black',fg='white',width=15,height=1,command=calculateAge).place(x=170,y=360)

#Creating a Button to clear previous entries
Clear=Button(text="CLEAR",font=3,bg='black',fg='white',width=10,height=1,command=CleanEntries).place(x=380 ,y=360)

#Creating Close Applicaton Button
Close=Button(text="Close Application",font=('Sans Serif',20,'bold'),bg="black",fg="white",width=15,height=1,command=exit).place(x=200,y=480)

window.mainloop()
