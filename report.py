from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")  # hXw+x-axis+y-axis
        self.root.config(bg="white")
        self.root.focus_force()  # focus

        # title
        title = Label(
            self.root,
            text="Student Report Details",
            font=("Times New Roman", 20, "bold"),
            bg="#F58B39",
            fg="white",
        ).place(x=10, y=5, width=1180, height=60)

        # text variables
        self.var_id = ""
        self.var_search = StringVar()


        # label
        lbl_select = Label(self.root, text="Search by Roll No", font=(
            "Times New Roman ", 20), bg="white",).place(x=150, y=100)

        # field
        txt_search = Entry(self.root, textvariable=self.var_search, font=(
                    "Times New Roman", 20, "bold"),bd=2,relief="solid")
        txt_search.place(x=400, y=100, width=250)

        # search button
        btn_search = Button(self.root, text="Search", font=("Times New Roman", 20), bg="lightblue", fg="black", cursor="hand2",
                            command=self.search
                        )
        btn_search.place(x=670, y=100, width=110, height=35)

        # clear btn
        btn_clear = Button(self.root, text="Clear", font=("Times New Roman", 20), bg="white", fg="black", 
                           cursor="hand2",command=self.clear)
        btn_clear.place(x=790, y=100, width=110, height=35)


        # Labels
        lbl_roll = Label(self.root, text="Roll No", font=(
            "goudy old style ", 15, "bold"), bg="white",bd=2 , relief=GROOVE , padx=10).place(x=150, y=190,width=150,height=50 )
        lbl_name = Label(self.root, text="Name", font=(
            "goudy old style ", 15, "bold"), bg="white",bd=2 , relief=GROOVE , padx=10).place(x=300, y=190,width=150,height=50 )
        lbl_course = Label(self.root, text="course", font=(
            "goudy old style ", 15, "bold"), bg="white",bd=2 , relief=GROOVE , padx=10).place(x=450, y=190,width=150,height=50 )
        lbl_marks = Label(self.root, text="Marks Obtained", font=(
            "goudy old style ", 15, "bold"), bg="white",bd=2 , relief=GROOVE , padx=10).place(x=600, y=190,width=200,height=50 )
        lbl_full = Label(self.root, text="Full Markls", font=(
            "goudy old style ", 15, "bold"), bg="white",bd=2 , relief=GROOVE , padx=10).place(x=800, y=190,width=150,height=50 )
        lbl_per = Label(self.root, text="Percentage", font=(
            "goudy old style ", 15, "bold"), bg="white",bd=2 , relief=GROOVE , padx=10).place(x=950, y=190,width=150,height=50 )


        self.roll = Label(self.root, font=(
            "goudy old style ", 15), bg="white",bd=2 , relief=GROOVE , padx=10)
        self.roll.place(x=150, y=240,width=150,height=50 )

        self.name = Label(self.root, font=(
            "goudy old style ", 15), bg="white",bd=2 , relief=GROOVE , padx=10)
        self.name.place(x=300, y=240,width=150,height=50 )

        self.course = Label(self.root, font=(
            "goudy old style ", 15), bg="white",bd=2 , relief=GROOVE , padx=10)
        self.course.place(x=450, y=240,width=150,height=50 )

        self.marks = Label(self.root, font=(
            "goudy old style ", 15), bg="white",bd=2 , relief=GROOVE , padx=10)
        self.marks.place(x=600, y=240,width=200,height=50 )

        self.full = Label(self.root,  font=(
            "goudy old style ", 15), bg="white",bd=2 , relief=GROOVE , padx=10)
        self.full.place(x=800, y=240,width=150,height=50 )

        self.per = Label(self.root,  font=(
            "goudy old style ", 15), bg="white",bd=2 , relief=GROOVE , padx=10)
        self.per.place(x=950, y=240,width=150,height=50 )

        # delete buttons

        self.btn_delete = Button(self.root, text="Delete", font=(
            "Times New Roman", 15), bg="red", fg="white", cursor="hand2",
            activebackground='pink',command=self.delete
        )
        self.btn_delete.place(x=550, y=340, width=110, height=40)       

    
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error" , "Roll No. should be required" , parent=self.root)
            else: 
                cur.execute("select * from result where roll=?",
                            (self.var_search.get(),))
                row = cur.fetchone()
                print(row)
                if row != None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror(
                        "Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror(
                    "Error", "Search Student Result first", parent=self.root)
            else:
                cur.execute("select * from result where rid=?",
                            (self.var_id,))
                row = cur.fetchone()  # return
                print(row)
                if row == None:
                    messagebox.showerror("Error" , "Invalid " , parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm" , "Do you really want to delete?" , parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,)) 
                        con.commit()
                        messagebox.showinfo("Delete" , "Result Deleted Successfully" , parent=self.root)
                        self.clear()
                        
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    
if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()