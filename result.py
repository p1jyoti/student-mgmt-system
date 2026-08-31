from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")  # hXw+x-axis+y-axis
        self.root.config(bg="white")
        self.root.focus_force()  # focus

        # title
        title = Label(
            self.root,
            text="Add Student Result",
            font=("Times New Roman", 20, "bold"),
            bg="#34206B",
            fg="white",
        ).place(x=10, y=5, width=1180, height=60)

        # text variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        lbl_select = Label(self.root, text="Select Student", font=(
            "Times New Roman ", 15), bg="white",).place(x=50, y=100)
        lbl_name = Label(self.root, text="Name", font=(
            "Times New Roman ", 15), bg="white").place(x=50, y=150)
        lbl_cours = Label(self.root, text="Course", font=(
            "Times New Roman ", 15), bg="white",).place(x=50, y=200)
        lbl_marks_ob = Label(self.root, text="Marks Obtained", font=(
            "Times New Roman ", 15), bg="white",).place(x=50, y=250)
        lbl_full_marks = Label(self.root, text="Full Marks", font=(
            "Times New Roman ", 15), bg="white",).place(x=50, y=300)

        # combox for llno
        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, font=(
            "goudy old style", 15, "bold"), state="readonly", justify="center", values=self.roll_list)
        self.txt_student.place(x=250, y=100, width=150)
        self.txt_student.set("Select")

        # search button
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="lightblue", fg="black", cursor="hand2",
                            command=self.search)
        btn_search.place(x=420, y=100, width=110, height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", state="readonly", bd=1, relief="solid")
        txt_name.place(x=250, y=150, width=200)

        txt_course = Entry(self.root, textvariable=self.var_course, font=(
            "goudy old style", 15, "bold"), bg="lightyellow", state="readonly", bd=1, relief="solid")
        txt_course.place(x=250, y=200, width=200)

        txt_marks = Entry(self.root, textvariable=self.var_marks, font=(
            "goudy old style", 15, "bold"), bd=1, relief="solid")
        txt_marks.place(x=250, y=250, width=200)

        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=(
            "goudy old style", 15, "bold"), bd=1, relief="solid")
        txt_full_marks.place(x=250, y=300, width=200)

        # adding buttons

        self.btn_add = Button(self.root, text="Submit", font=("goudy old style", 15, "bold"), bg="green", fg="white", cursor="hand2",
                              activebackground='lightgreen',command=self.add)
        self.btn_add.place(x=250, y=350, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="grey", fg="white", cursor="hand2",
            activebackground='lightblue',command=self.clear
        )
        self.btn_clear.place(x=380, y=350, width=110, height=40)

        # image
        self.bg_img = Image.open("images/result.png")
        self.bg_img = self.bg_img.resize((650, 400), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(
            x=550, y=70, width=650, height=400
        )

    # =====================================================================
    # connecting with database

    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            # fetch the course name from the course table
            cur.execute("select roll from student")
            rows = cur.fetchall()
            print(rows)
            # v=[]
            if len(rows) > 0:
                for row in rows:
                    # v.append(row[0])
                    self.roll_list.append(row[0])
            # print(v)
            # self.course_list=v
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",
                        (self.var_roll.get(),))
            row = cur.fetchone()
            print(row)
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror(
                    "Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please search the student Record", parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",
                            (self.var_roll.get(),self.var_course.get(),))
                row = cur.fetchone()  # return
                print(row)
                if row != None:
                    messagebox.showerror("Error", "Result already Exist", parent=self.root)
                else:
                    # calculating marks
                    per = (float(self.var_marks.get()) * 100) / float(self.var_full_marks.get())
                    cur.execute("insert into result (roll, name, course, marks_ob, full_marks,per) values(?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Succesfully", parent=self.root)
                    

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_full_marks.set(""),
        self.var_marks.set("")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
