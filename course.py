from tkinter import *
from PIL import Image, ImageTk  # for images pip install pillow
from tkinter import ttk, messagebox
import sqlite3


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result managemnt System")
        self.root.geometry("1200x480+80+170")  # hXw+x-axis+y-axis
        self.root.config(bg="white")
        self.root.focus_force()  # focus

        # title
        title = Label(
            self.root,
            text="Manage course details",
            font=("Segoe UI", 20, "bold"),
            bg="#34206B",
            fg="white",
        ).place(x=10, y=15, width=1180, height=40)

        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style ", 15, "bold"), bg="white",
                               ).place(x=10, y=60)

        lbl_duration = Label(self.root, text="Duration", font=("goudy old style ", 15, "bold"), bg="white",
                             ).place(x=10, y=100)

        lbl_charges = Label(self.root, text="Charges", font=("goudy old style ", 15, "bold"), bg="white",
                            ).place(x=10, y=140)

        lbl_description = Label(self.root, text="Description", font=("goudy old style ", 15, "bold"), bg="white",
                                ).place(x=10, y=180)

        # Text Variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # Course Name
        self.txt_courseName = Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        )
        self.txt_courseName.place(x=150, y=60, width=200)

        # Duration
        self.txt_duration = Entry(
            self.root,
            textvariable=self.var_duration,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        )
        self.txt_duration.place(x=150, y=100, width=200)

        # Charges
        self.txt_charges = Entry(
            self.root,
            textvariable=self.var_charges,
            font=("goudy old style", 15, "bold"),
            bg="lightyellow",
        )
        self.txt_charges.place(x=150, y=140, width=200)

        # Description
        self.txt_description = Text(
            self.root, font=("goudy old style", 15, "bold"), bg="lightyellow"
        )
        self.txt_description.place(x=150, y=180, width=450, height=130)

        # adding buttons

        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="green", fg="white", cursor="hand2",
                              command=self.add,)
        self.btn_add.place(x=150, y=350, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=(
            "goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2",
            command=self.update)
        self.btn_update.place(x=270, y=350, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=(
            "goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2",
            command=self.delete)
        self.btn_delete.place(x=390, y=350, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="grey", fg="white", cursor="hand2",
            command=self.clear)
        self.btn_clear.place(x=510, y=350, width=110, height=40)

        # serarch panel
        lbl_search_courseName = Label(self.root, text="Course Name ", font=("goudy old style ", 15, "bold"), bg="white",
                                      ).place(x=650, y=60)

        self.var_search = StringVar()
        search_course = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, "bold"), bg="lightyellow",
                              )
        search_course.place(x=800, y=60, width=250)

        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="plum", fg="white", cursor="hand2",
                            command=self.search
                            )
        btn_search.place(x=1070, y=60, width=110, height=27)

        # content Frame ========
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=650, y=100, height=340,)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.courseTable = ttk.Treeview(self.C_Frame, columns=("courseID", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,
                                        )

        # pack the scroll
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        # working of scrollbar
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("courseID", text="courseID")
        self.courseTable.heading("name", text="name")
        self.courseTable.heading("duration", text="duration")
        self.courseTable.heading("charges", text="charges")
        self.courseTable.heading("description", text="description")

        self.courseTable["show"] = "headings"
        self.courseTable.column("courseID", width=100)
        self.courseTable.column("name", width=100)
        self.courseTable.column("duration", width=100)
        self.courseTable.column("charges", width=100)
        self.courseTable.column("description", width=130)
        self.courseTable.pack(fill=BOTH, expand=1)

        self.courseTable.bind("<ButtonRelease-1>",
                              self.get_data)  # helps to bind
        self.show()

    # =====================================================================
    # connecting with database

    # clear function
    def clear(self):
        self.var_course.set(""),
        self.var_duration.set(""),
        self.var_charges.set(""),
        self.var_charges.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("select * from course where name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()  # return
                print(row)
                if row == None:
                    messagebox.showerror("Error" , "Please Select Course From the list " , parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm" , "Do you really want to delete?" , parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),)) 
                        con.commit()
                        messagebox.showinfo("Delete" , "Course Deleted Successfully" , parent=self.root)
                        self.clear()
                        
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # console/set the data whom i select on the table view
    def get_data(self, ev):
        self.txt_courseName.config(state="readonly")
        r = self.courseTable.focus()
        content = self.courseTable.item(r)
        row = content["values"]
        print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course Name is required", parent=self.root
                )
            else:
                cur.execute("select * from course where name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()  # return
                print(row)
                if row != None:
                    messagebox.showerror(
                        "Error", "Course name already Exist", parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get(
                            "1.0", END)  # fetch all the descr
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course Added Succesfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            print(rows)
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            print(rows)
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course Name is required", parent=self.root
                )
            else:
                cur.execute("select * from course where name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()  # return
                print(row)
                if row == None:
                    messagebox.showerror(
                        "Error", "Select Course From List", parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get(
                            "1.0", END),  # fetch all the descr
                        self.var_course.get(),
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course Updated Succesfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
