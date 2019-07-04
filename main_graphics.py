from tkinter import *
from tkinter import Radiobutton
from tkinter import messagebox
import mysql.connector

class add_data():
    def add():
        customer_name = entryName.get()
        customer_email = entryEmail.get()
        phone = entryPhone.get()
        city = entryCity.get()
        state = entryState.get()

        print(customer_name, customer_email, phone, city, state)

        insert = "insert into customer_details values(null, '{}', '{}', '{}', '{}', '{}')".format(customer_name,customer_email, phone,city, state)

        con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")

        cursor = con.cursor()
        cursor.execute(insert)

        con.commit()
        messagebox.showinfo("Message", "Data has been Added Successfully")
        # print(customer_name," Saved in Database")

    add_window = Tk()
    add_window.title("Save Data")
    add_window.geometry("500x270")

    Lb1 = Label(add_window, text="Enter the Customer Name : ", font="Arial 14").place(x=10, y=10)
    # Lb1.pack()
    entryName = Entry(add_window, width=22, font="Arial 14")
    entryName.place(x=250, y=10)

    Lb2 = Label(add_window, text="Enter the Customer Email : ", font="Arial 14").place(x=10, y=50)
    # Lb2.pack()
    entryEmail = Entry(add_window, width=22, font="Arial 14")
    entryEmail.place(x=250, y=50)

    Lb3 = Label(add_window, text="Enter Phone Number : ", font="Arial 14").place(x=10, y=90)
    # Lb3.pack()
    entryPhone = Entry(add_window, width=22, font="Arial 14")
    entryPhone.place(x=250, y=90)

    Lb4 = Label(add_window, text="Enter City : ", font="Arial 14").place(x=10, y=130)
    # Lb4.pack()
    entryCity = Entry(add_window, width=22, font="Arial 14")
    entryCity.place(x=250, y=130)

    Lb5 = Label(add_window, text="Enter State : ", font="Arial 14").place(x=10, y=170)
    # Lb5.pack()
    entryState = Entry(add_window, width=22, font="Arial 14")
    entryState.place(x=250, y=170)

    Btn1 = Button(add_window, text="Save Data", command=add, font="Arial 14")
    Btn1.place(x=390, y=210)

    add_window.configure()

class update():
    def __init__(self,customer_name,customer_email,phone):
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.phone = phone

    def radio1():
        newName.configure(state="normal")
        newEmail.configure(state="disabled")
        newPhone.configure(state="disabled")
        Rbtn4.configure(state="disabled")
        Rbtn5.configure(state="normal")
        Rbtn6.configure(state="normal")

    def radio2():
        newEmail.configure(state="normal")
        newPhone.configure(state="disabled")
        newName.configure(state="disabled")
        Rbtn4.configure(state="normal")
        Rbtn5.configure(state="disabled")
        Rbtn6.configure(state="normal")

    def radio3():
        newEmail.configure(state="disabled")
        newPhone.configure(state="normal")
        newName.configure(state="disabled")
        Rbtn4.configure(state="normal")
        Rbtn5.configure(state="normal")
        Rbtn6.configure(state="disabled")

    def radio4():
        Rbtn1.configure(select="normal")
        Rbtn2.configure(select="disabled")
        Rbtn3.configure(select="disabled")
        existingName.configure(state="normal")
        existingEmail.configure(state="disabled")
        existingPhone.configure(state="disabled")

    def radio5():
        existingName.configure(state="disabled")
        existingEmail.configure(state="normal")
        existingPhone.configure(state="disabled")

    def radio6():
        existingName.configure(state="disabled")
        existingEmail.configure(state="disabled")
        existingPhone.configure(state="normal")

    def confirm_update():
        radiobutton = radio.get()
        radiobutton1 = radio12.get()

        if radiobutton == 1:
            if radiobutton1 == 5:
                customer_name = newName.get()
                customer_email = existingEmail.get()
                update1 = "update customer_details set customer_name = '{}' where customer_email = '{}'".format(
                    customer_name, customer_email)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update1)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
                # print("Data Updated Successfully")
            elif radiobutton1 == 6:
                customer_name = newName.get()
                phone = existingPhone.get()
                update2 = "update customer_details set customer_name = '{}' where phone = '{}'".format(customer_name,
                                                                                                       phone)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update2)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
                # print("Data deleted Successfully")
            else:
                messagebox.showerror("Error", "Please Select All option which is required for updation ")

        elif radiobutton == 2:
            if radiobutton1 == 4:
                customer_email = newEmail.get()
                customer_name = existingName.get()
                update3 = "update customer_details set customer_email = '{}' where customer_name = '{}'".format(
                    customer_email, customer_name)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update3)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
                # print("Data deleted Successfully")
            elif radiobutton1 == 6:
                customer_email = newEmail.get()
                phone = existingPhone.get()
                update4 = "update customer_details set customer_email = '{}' where phone = '{}'".format(customer_email,
                                                                                                        phone)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update4)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
                # print("Data deleted Successfully")
            else:
                messagebox.showerror("Error", "Please Select All option which is required for updation ")

        elif radiobutton == 3:
            if radiobutton1 == 4:
                phone = newPhone.get()
                customer_name = existingName.get()
                update5 = "update customer_details set phone = '{}' where customer_name = '{}'".format(phone,
                                                                                                       customer_name)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update5)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
                # print("Data deleted Successfully")
            elif radiobutton1 == 5:
                phone = newPhone.get()
                customer_email = existingEmail.get()
                update5 = "update customer_details set phone = '{}' where customer_email = '{}'".format(phone,
                                                                                                        customer_email)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update5)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
                # print("Data deleted Successfully")
            else:
                messagebox.showerror("Error", "Please Select All option which is required for updation ")
        else:
            messagebox.showerror("Error", "Please Select Any Option For Updation")

    side_window = Tk()
    side_window.title("Updating Data")
    side_window.geometry("500x440")
    radio = IntVar()
    radio12 = IntVar()

    Lbl1 = Label(side_window, text="Sir/Madam, What thing you want To Update?", font="Arial 16")
    Lbl1.place(x=5, y=5)

    Lbl8 = Label(side_window, text="From which option would you want to update !!", font="Arial 16")
    Lbl8.place(x=5, y=70)

    Lbl2 = Label(side_window, text="Enter New Name -> ", font="Arial 16").place(x=10, y=145)
    newName = Entry(side_window, width=22, font="Arial 14", state=DISABLED)
    newName.place(x=250, y=145)

    Lbl3 = Label(side_window, text="Enter New Email -> ", font="Arial 16").place(x=10, y=185)
    newEmail = Entry(side_window, width=22, font="Arial 14", state=DISABLED)
    newEmail.place(x=250, y=180)

    Lbl4 = Label(side_window, text="Enter New Phone -> ", font="Arial 16").place(x=10, y=225)
    newPhone = Entry(side_window, width=22, font="Arial 14", state=DISABLED)
    newPhone.place(x=250, y=225)

    Lbl5 = Label(side_window, text="Enter Existing Name -> ", font="Arial 16").place(x=10, y=265)
    existingName = Entry(side_window, width=22, font="Arial 14", state=DISABLED)
    existingName.place(x=250, y=265)

    Lbl6 = Label(side_window, text="Enter Existing Email -> ", font="Arial 16").place(x=10, y=305)
    existingEmail = Entry(side_window, width=22, font="Arial 14", state=DISABLED)
    existingEmail.place(x=250, y=305)

    Lbl7 = Label(side_window, text="Enter Existing Phone -> ", font="Arial 16").place(x=10, y=345)
    existingPhone = Entry(side_window, width=22, font="Arial 14", state=DISABLED)
    existingPhone.place(x=250, y=345)

    Rbtn1 = Radiobutton(side_window, text="By Name", variable=radio, value=1, font="Arial 16", command=radio1)
    Rbtn1.place(x=0, y=35)

    Rbtn2 = Radiobutton(side_window, text="By Email", variable=radio, value=2, font="Arial 16", command=radio2)
    Rbtn2.place(x=190, y=35)

    Rbtn3 = Radiobutton(side_window, text="By Phone", variable=radio, value=3, font="Arial 16", command=radio3)
    Rbtn3.place(x=370, y=35)

    Rbtn4 = Radiobutton(side_window, text="By Name", variable=radio12, value=4, font="Arial 16", command=radio4,
                        state=DISABLED)
    Rbtn4.place(x=0, y=100)

    Rbtn5 = Radiobutton(side_window, text="By Email", variable=radio12, value=5, font="Arial 16", command=radio5,
                        state=DISABLED)
    Rbtn5.place(x=190, y=105)

    Rbtn6 = Radiobutton(side_window, text="By Phone", variable=radio12, value=6, font="Arial 16", command=radio6,
                        state=DISABLED)
    Rbtn6.place(x=370, y=105)

    Btn5 = Button(side_window, text="Update", command=confirm_update, font="Arial 16", width=9)
    Btn5.place(x=370, y=385)

    side_window.mainloop()
    breakpoint()

class delete():
    pass

class view():
    pass

c1 = add_data()

window = Tk()
window.title("Database Project")
window.geometry("500x270")

Lbl1 = Label(window, text="Hello User :) ", font="Arial 18").place(x=180, y=10)
Lbl2 = Label(window, text="What you want to do ?", font="Arial 18").place(x=130, y=50)

Btn1 = Button(window, text="Add Data", command=c1, font="Arial 14")
Btn1.place(x=10, y=210)

Btn2 = Button(window, text="Update Data", command=update, font="Arial 14")
Btn2.place(x=130, y=210)

Btn3 = Button(window, text="Delete Data", command=delete, font="Arial 14")
Btn3.place(x=265, y=210)

Btn4 = Button(window, text="View Data", command=view, font="Arial 14")
Btn4.place(x=390, y=210)

window.mainloop()