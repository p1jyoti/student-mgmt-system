from tkinter import *
from PIL import Image, ImageTk  # for images pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1250x480+80+170")  # hXw+x-axis+y-axis
        self.root.config(bg="white")
        self.root.focus_force()  # focus

        # title
        title = Label(self.root, text="Manage Student Details", font=("Times New Roman", 20), bg="#34206B", fg="white",
                      ).place(x=5, y=5, width=1250, height=40)

        # Text Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        indian_states = ["Select", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
                         "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

        # LABELS-1st column
        lbl_roll = Label(self.root, text="Roll No", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=10, y=100)
        lbl_email = Label(self.root, text="Email", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=10, y=180)
        lbl_state = Label(self.root, text="State", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=10, y=220)
        lbl_address = Label(self.root, text="Address", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=10, y=260)

        # LABELS - 2nd column
        lbl_dob = Label(self.root, text="D.O.B", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=340, y=60)
        lbl_contact = Label(self.root, text="Contact", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=340, y=100)
        lbl_admission = Label(self.root, text="Admission", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=340, y=140)
        lbl_course = Label(self.root, text="Course", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=340, y=180)
        lbl_city = Label(self.root, text="City", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=340, y=220)
        lbl_pin = Label(self.root, text="Pin", font=(
            "goudy old style ", 15, "bold"), bg="white",).place(x=510, y=220)

        # Entry Fields : 1st column
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        self.txt_roll.place(x=110, y=60, width=200)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        txt_name.place(x=110, y=100, width=200)

        txt_email = Entry(self.root, textvariable=self.var_email, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        txt_email.place(x=110, y=140, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, font=(
            "goudy old style", 15, "bold"), state="readonly", justify="center", values=("Select", "Male", "Female", "Other"))
        self.txt_gender.place(x=110, y=180, width=200)
        self.txt_gender.current(0)

        self.txt_state = ttk.Combobox(self.root, textvariable=self.var_state, font=(
            "goudy old style", 15, "bold"), state="readonly", justify="center", values=(indian_states))
        self.txt_state.place(x=110, y=220, width=200)
        self.txt_state.current(0)

        # Entry Fields : 2st column
        # =========================

        self.course_list = []
        # function call to update the list
        self.fetch_course()
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        txt_dob.place(x=460, y=60, width=200)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        txt_contact.place(x=460, y=100, width=200)

        txt_admission = Entry(self.root, textvariable=self.var_a_date, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        txt_admission.place(x=460, y=140, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, font=(
            "goudy old style", 15, "bold"), state="readonly", justify="center", values=self.course_list)
        self.txt_course.place(x=460, y=180, width=200)
        self.txt_course.set("Select")

        txt_city = Entry(self.root, textvariable=self.var_city, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        txt_city.place(x=390, y=220, width=100)

        txt_pin = Entry(self.root, textvariable=self.var_pin, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        txt_pin.place(x=560, y=220, width=100)

        # Text address
        self.txt_address = Text(self.root, font=(
            "goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=110, y=260, width=500, height=100)

        #  buttons

        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="green", fg="white", cursor="hand2",
                              command=self.add,)
        self.btn_add.place(x=110, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=(
            "goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2",
            command=self.update)
        self.btn_update.place(x=250, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=(
            "goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2",
            command=self.delete)
        self.btn_delete.place(x=380, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="grey", fg="white", cursor="hand2",
            command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # =================
        # search panel

        lbl_search_roll = Label(self.root, text="Student RollNo.", font=("goudy old style ", 15, "bold"), bg="white",
                                ).place(x=700, y=60)

        self.var_search = StringVar()
        search_course = Entry(self.root, textvariable=self.var_search, font=(
            "goudy old style", 15, "bold"), bg="lightyellow",)
        search_course.place(x=850, y=60, width=250)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="plum", fg="white", cursor="hand2",
                            command=self.search)
        btn_search.place(x=1110, y=60, width=110, height=27)

        # content Frame ========
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=700, y=100, height=340, width=550,)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.courseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob", "contact", "admission",
                                        "course", "state", "city", "pin", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,)

        # pack the scroll
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        # working of scrollbar
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("roll", text="roll")
        self.courseTable.heading("name", text="name")
        self.courseTable.heading("email", text="email")
        self.courseTable.heading("gender", text="gender")
        self.courseTable.heading("dob", text="dob")
        self.courseTable.heading("contact", text="contact")
        self.courseTable.heading("admission", text="admission")
        self.courseTable.heading("course", text="course")
        self.courseTable.heading("state", text="state")
        self.courseTable.heading("city", text="city")
        self.courseTable.heading("pin", text="pin")
        self.courseTable.heading("address", text="address")

        self.courseTable["show"] = "headings"

        self.courseTable.column("roll", width=50)
        self.courseTable.column("name", width=100)
        self.courseTable.column("email", width=100)
        self.courseTable.column("gender", width=100)
        self.courseTable.column("dob", width=50)
        self.courseTable.column("contact", width=100)
        self.courseTable.column("admission", width=100)
        self.courseTable.column("course", width=100)
        self.courseTable.column("state", width=100)
        self.courseTable.column("city", width=100)
        self.courseTable.column("pin", width=100)
        self.courseTable.column("address", width=100)

        self.courseTable.pack(fill=BOTH, expand=1)

        self.courseTable.bind("<ButtonRelease-1>",
                              self.get_data)  # helps to bind
        self.show()
        # self.fetch_course() #course name fetch

    # =====================================================================
    # connecting with database

    # clear function
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("Select")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete('1.0', END)
        self.txt_roll.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Roll No is required", parent=self.root)
            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()  # return
                print(row)
                if row == None:
                    messagebox.showerror(
                        "Error", "Please Select Roll No/Student From the list ", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?",
                                    (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Student Details Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # console/set the data whom i select on the table view
    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        # print(row)
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Roll Number is required", parent=self.root
                )
            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()  # return
                print(row)
                if row != None:
                    messagebox.showerror(
                        "Error", "Roll Number already Exist", parent=self.root)
                else:
                    cur.execute("insert into student (roll ,name, email, gender, dob, contact, admission, course, state, city, pin, address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get(
                            "1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Added Succesfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            print(rows)
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            # fetch the course name from the course table
            cur.execute("select name from course")
            rows = cur.fetchall()
            print(rows)
            # v=[]
            if len(rows) > 0:
                for row in rows:
                    # v.append(row[0])
                    self.course_list.append(row[0])
            # print(v)
            # self.course_list=v
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll=?",
                        (self.var_search.get(),))
            row = cur.fetchone()
            print(row)
            if row != None:
                self.courseTable.delete(*self.courseTable.get_children())
                self.courseTable.insert('', END, values=row)
            else:
                messagebox.showerror(
                    "Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror(
                    "Error", "Roll No is required", parent=self.root
                )
            else:
                cur.execute("select * from student where roll=?",
                            (self.var_roll.get(),))
                row = cur.fetchone()  # return
                print(row)
                if row == None:
                    messagebox.showerror(
                        "Error", "Select Roll No/Student From List", parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=? ,city=? ,pin=? ,address=? where roll=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get(
                            "1.0", END),
                        self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Updated Succesfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
