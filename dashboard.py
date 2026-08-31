from tkinter import *
from PIL import Image, ImageTk  # for images pip install pillow
from course import CourseClass #importing the courseClass from course.py
from student import studentClass 
from result import resultClass 
from report import reportClass 
from tkinter import messagebox

import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # icons
        img = Image.open("images/logo.png")
        img = img.resize((50, 50))
        self.logo_dash = ImageTk.PhotoImage(img)

        # title
        title = Label(self.root,text="Student Result Management System",compound=LEFT,image=self.logo_dash,padx=20,font=("Segoe UI", 20, "bold"),bg="#34206B",fg="white",
        ).place(x=0, y=0, relwidth=1, height=50)

        # menu
        # M_Frame = LabelFrame(self.root, text="Menu", font=("Segoe UI", 15), bg="white")
        # M_Frame.place(x=10, y=70, width=1340, height=80)

        M_Frame = Frame(self.root, bg="#34206B")
        M_Frame.place(x=0, y=50, width=240, relheight=1)
        
        Label(
            M_Frame,
            text="MAIN MENU",
            font=("Segoe UI", 9, "bold"),
            bg="#34206B",
            fg="#AFA0DD",
        ).place(x=25, y=25)



         
        # SIDEBAR BUTTON FUNCTION

        def sidebar_button(text, y,command):
            btn = Button(
                M_Frame,
                text=text,
                font=("Segoe UI", 11),
                bg="#34206B",
                fg="white",
                activebackground="#5B35C5",
                activeforeground="white",
                bd=0,
                relief=FLAT,
                anchor="w",
                padx=25,
                cursor="hand2",
                command=command
            )

            btn.place(x=10, y=y, width=220, height=50)

            return btn

        # MENU BUTTONS : height = 50: y axis always +50 for the next button

        self.btn_dashboard = sidebar_button("⌂    Dashboard", 50,self.root)
        self.btn_course = sidebar_button("▣    Course", 100,self.add_course)
        self.btn_student = sidebar_button("♙    Students", 150 ,self.add_student)
        self.btn_result = sidebar_button("✓    Results", 200 , self.view_result)
        self.btn_view = sidebar_button("▤    View Student Results", 250,self.view_report)

        Label(
            M_Frame,
            text="ACCOUNT",
            font=("Segoe UI", 9, "bold"),
            bg="#34206B",
            fg="#AFA0DD",
        ).place(x=25, y=350)

        # self.btn_logout = sidebar_button("↪    Log Out", 400 ,command=exit )
        self.btn_exit = sidebar_button("×    Exit",450,command=exit)

        # content-window
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((1000, 500), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=240, y=50,height=500,width=1200)

        # update details
        self.lbl_course = Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            font=("goudy old style ", 20),
            bd=10,
            relief="flat",
            bg="#5B35C5",
            fg="white",
        )
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(
            self.root,
            text="Total Student\n[ 0 ]",
            font=("goudy old style ", 20),
            bd=10,
            relief="flat",
            bg="#5B35C5",
            fg="white",
        )
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(
            self.root,
            text="Total Result\n[ 0 ]",
            font=("goudy old style ", 20),
            bd=10,
            relief="flat",
            bg="#5B35C5",
            fg="white",
        )
        self.lbl_result.place(x=1020, y=530, width=300, height=100)


        # footer
        footer = Label(
            self.root,
            text="SRMS- Student Result Magmt System\nContact for any technical issue: +9123xxx90",
            # compound=LEFT,
            # image=self.logo_dash,
            padx=20,
            font=("Segoe UI", 12),
            bg="#262626",
            fg="white",
        ).pack(side=BOTTOM, fill=X)
        self.update_details()

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def view_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)


    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            cur.execute("select * from student")
            student = cur.fetchall()
            cur.execute("select * from result")
            result = cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n {str(len(cr))}")
            self.lbl_student.config(text=f"Total Student\n {str(len(student))}")
            self.lbl_result.config(text=f"Total Student\n {str(len(result))}")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()  # stay the window
 