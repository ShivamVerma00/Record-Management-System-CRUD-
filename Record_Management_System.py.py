from tkinter import *
import sqlite3



ms=Tk()
ms.title('Library Management System')
ms.geometry('1280x700')
ms.resizable(width=False,height=False)


#-------Creating DB......
conn=sqlite3.connect("Shivam_LibraryDBMS.db")
cursor=conn.cursor()
cursor.execute("create table if not exists Book_Records(MemberType text,FirstName text,MiddleName text,LastName text,Address text,PostCode text,MobileNO text,BookID text,BookTitle text,Author text,DateBorrowed text,DueDate text,LateReturnFine text,SellingPrice text)")

conn.commit()
conn.close()











#-------------------------------FUNCTION USED-----------------------

def exit():
    """ Exit the  Main Window..."""
    ms.destroy()

def add():
    """ To Add new data in Database.."""
    mem=e1var.get()
    first=e2var.get()
    middle=e3var.get()
    last=e4var.get()
    address=e5var.get()
    post=e6var.get()
    mob=e7var.get()
    bid=e8var.get()
    btitle=e9var.get()
    author=e10var.get()
    dateb=e11var.get()
    ddate=e12var.get()
    lrfine=e13var.get()
    sp=e14var.get()


    conn=sqlite3.connect("Shivam_LibraryDBMS.db")
    

    with conn:
        cursor=conn.cursor()
        #--Queries.....
        cursor.execute("create table if not exists Book_Records(MemberType text,FirstName text,MiddleName text,LastName text,Address text,PostCode text,MobileNO text,BookID text,BookTitle text,Author text,DateBorrowed text,DueDate text,LateReturnFine text,SellingPrice text)")
        cursor.execute("insert into Book_Records(MemberType,FirstName,MiddleName,LastName,Address,PostCode,MobileNO,BookID,BookTitle,Author,DateBorrowed,DueDate,LateReturnFine,SellingPrice)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (mem,first,middle,last,address,post,mob,bid,btitle,author,dateb,ddate,lrfine,sp))

        
        conn.commit()

def display():
    """ Display the Records of Books"""
    conn=sqlite3.connect("Shivam_LibraryDBMS.db")
    cursor=conn.cursor()
    cursor.execute("select * from Book_Records")
    d=cursor.fetchall()
    ef2.insert(0,d)

    conn.commit()
    conn.close()
     

def clear():
    """ Reset Setting..."""
    e1var.set("")
    e2var.set("")
    e3var.set("")
    e4var.set("")
    e5var.set("")
    e6var.set("")
    e7var.set("")
    e8var.set("")
    e9var.set("")
    e10var.set("")
    e11var.set("")
    e12var.set("")
    e13var.set("")
    e14var.set("")

    ef2.delete(0,END)


def delete():
    """ Delete the Selected Data..."""
    def ddata():
        conn=sqlite3.connect("Shivam_LibraryDBMS.db")
        cursor=conn.cursor()
        cursor.execute("delete from Book_Records where Book_ID=?",evar)

        conn.commit()
        conn.close()

    fd=Frame(ms,bg='white')
    fd.place(x=25,y=100,width=1230,height=400)

    l=Label(fd,text="Enter the Book_ID whose data is to be deleted:")
    l.place(x=200,y=100)

    evar=IntVar()
    e=Entry(fd,textvariable=evar)
    e.place(x=600,y=100)

    btn=Button(fd,text="Delete Data",bg='black',fg='white',command=ddata)
    btn.place(x=10,y=10)

    
    
def update():
    pass

def search():
    pass







#--------Label Library.......
l=Label(ms,bg='darkgreen',width=140,height=5)
l.place(x=120,y=10)

l1=Label(ms,text="Library Database Management System",font="Times 30 bold",fg='black')
l1.place(x=260,y=23)

l2=Label(ms,bg='darkgreen',width=141,height=4)
l2.place(x=120,y=520)

#----------Frame...........
f=Frame(ms,bg='white')
f.place(x=25,y=100,width=1230,height=400)

f1=Frame(ms,bg='darkgreen')
f1.place(x=40,y=110,width=690,height=380)

f2=Frame(ms,bg='darkgreen')
f2.place(x=740,y=110,width=500,height=380)






#--------------------Label & Entry Box Frame f1...
#-----------Label.........

l3=Label(f1,text="Library Membership Info:",bg='darkgreen',fg='black',
         font="Arial 20 bold")
l3.place(x=4,y=4)

l4=Label(f1,text="Member Type:",bg='darkgreen',fg='black',font="Arial 13 bold")
l4.place(x=8,y=70)

l5=Label(f1,text="First Name:",bg='darkgreen',fg='black',font="Arial 13 bold")
l5.place(x=8,y=110)

l6=Label(f1,text="Middle Name:",bg='darkgreen',fg='black',font="Arial 13 bold")
l6.place(x=8,y=150)

l7=Label(f1,text="Last Name:",bg='darkgreen',fg='black',font="Arial 13 bold")
l7.place(x=8,y=190)

l8=Label(f1,text="Address:",bg='darkgreen',fg='black',font="Arial 13 bold")
l8.place(x=8,y=230)

l9=Label(f1,text="Post Code:",bg='darkgreen',fg='black',font="Arial 13 bold")
l9.place(x=8,y=270)

l10=Label(f1,text="Mobile No:",bg='darkgreen',fg='black',font="Arial 13 bold")
l10.place(x=8,y=310)

l11=Label(f1,text="Book ID:",bg='darkgreen',fg='black',font="Arial 13 bold")
l11.place(x=320,y=70)

l12=Label(f1,text="Book Title:",bg='darkgreen',fg='black',font="Arial 13 bold")
l12.place(x=320,y=110)

l13=Label(f1,text="Author:",bg='darkgreen',fg='black',font="Arial 13 bold")
l13.place(x=320,y=150)

l14=Label(f1,text="Date Borrowed:",bg='darkgreen',fg='black',font="Arial 13 bold")
l14.place(x=320,y=190)

l15=Label(f1,text="Due Date:",bg='darkgreen',fg='black',font="Arial 13 bold")
l15.place(x=320,y=230)

l16=Label(f1,text="Late Return Fine:",bg='darkgreen',fg='black',font="Arial 13 bold")
l16.place(x=320,y=270)

l17=Label(f1,text="Selling Price:",bg='darkgreen',fg='black',font="Arial 13 bold")
l17.place(x=320,y=310)


#--------------Entry Box.......
e1var=StringVar()#Stores the value in e1.
e1=Entry(f1,textvariable=e1var,width=28)
e1.place(x=125,y=72)

e2var=StringVar()
e2=Entry(f1,textvariable=e2var,width=28)
e2.place(x=125,y=112)

e3var=StringVar()
e3=Entry(f1,textvariable=e3var,width=28)
e3.place(x=125,y=152)

e4var=StringVar()
e4=Entry(f1,textvariable=e4var,width=28)
e4.place(x=125,y=192)

e5var=StringVar()
e5=Entry(f1,textvariable=e5var,width=28)
e5.place(x=125,y=232)

e6var=StringVar()
e6=Entry(f1,textvariable=e6var,width=28)
e6.place(x=125,y=272)

e7var=StringVar()
e7=Entry(f1,textvariable=e7var,width=28)
e7.place(x=125,y=312)

e8var=StringVar()
e8=Entry(f1,textvariable=e8var,width=28)
e8.place(x=470,y=72)

e9var=StringVar()
e9=Entry(f1,textvariable=e9var,width=28)
e9.place(x=470,y=112)

e10var=StringVar()
e10=Entry(f1,textvariable=e10var,width=28)
e10.place(x=470,y=152)

e11var=StringVar()
e11=Entry(f1,textvariable=e11var,width=28)
e11.place(x=470,y=192)

e12var=StringVar()
e12=Entry(f1,textvariable=e12var,width=28)
e12.place(x=470,y=232)

e13var=StringVar()
e13=Entry(f1,textvariable=e13var,width=28)
e13.place(x=470,y=272)

e14var=StringVar()
e14=Entry(f1,textvariable=e14var,width=28)
e14.place(x=470,y=312)




#--------------Label and EntryBox Frame f2....
lf2=Label(f2,text="Book Detail:",bg='darkgreen',fg='black',font="Arial 20 bold")
lf2.place(x=4,y=4)

global ef2
ef2=Entry(f2,bd=2)
ef2.place(x=25,y=50,width=450,height=300)




#--------------------------------------Buttons...................

btn_add=Button(ms,text='Add Data',width=15,height=2,font="arial 10 bold",
               command=add)
btn_add.place(x=130,y=530)

btn_display=Button(ms,text='Display Data',width=15,height=2,font="arial 10 bold",
               command=display)
btn_display.place(x=270,y=530)

btn_clear=Button(ms,text='Clear Data',width=15,height=2,font="arial 10 bold",
               command=clear)
btn_clear.place(x=410,y=530)

btn_delete=Button(ms,text='Delete Data',width=15,height=2,font="arial 10 bold",
               command=delete)
btn_delete.place(x=550,y=530)

btn_update=Button(ms,text='Update Data',width=15,height=2,font="arial 10 bold",
               command=update)
btn_update.place(x=690,y=530)

btn_search=Button(ms,text='Search Data',width=15,height=2,font="arial 10 bold",
               command=search)
btn_search.place(x=830,y=530)

btn_exit=Button(ms,text='Exit',width=15,height=2,font="arial 10 bold",
               command=exit)
btn_exit.place(x=970,y=530)

















ms.mainloop()
