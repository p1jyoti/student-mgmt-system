# Register Form
from tkinter import*
from PIL import Image,ImageTk

class Register:
    def __init__(self,root):
        self.root = root #initializing the root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # background Image
        self.bg = ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.bg_img = Image.open("images/register.jpg")
        self.bg_img = self.bg_img.resize((500, 500), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(
            x=80, y=100, width=400, height=500
        )

        # Frame for register
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)


        title=Label(frame1,text="REGISTRATION HERE",font=("Times new Roman",25,"bold"), bg="white",fg="#0F5658").place(x=50,y=30)

        # Labels
        self.var_fname = StringVar()


        # row 1
        f_name=Label(frame1,text="First Name: ",font=("Times new Roman",15),bg="white").place(x=50,y=100)
        self.txt_fname = Entry(frame1, textvariable=self.var_fname,font=("Times new Roman",15),bd=2,relief="solid")
        self.txt_fname.place(x=50,y=130,width=250)

        self.var_lname = StringVar()

        self.l_name=Label(frame1,text="Last Name: " , textvariable=self.var_lname,font=("Times new Roman",15),bg="white").place(x=340,y=100)
        self.txt_lname = Entry(frame1,font=("Times new Roman",15),bd=2,relief="solid")
        self.txt_lname.place(x=340,y=130,width=250)

        # Row 2
        self.contact=Label(frame1,text="Contact No.: ",font=("Times new Roman",15),bg="white").place(x=50,y=180)
        self.txt_contact = Entry(frame1,font=("Times new Roman",15),bd=2,relief="solid").place(x=50,y=210,width=250)

        self.email=Label(frame1,text="Email: ",font=("Times new Roman",15),bg="white").place(x=340,y=180)
        self.txt_email = Entry(frame1,font=("Times new Roman",15),bd=2,relief="solid").place(x=340,y=210,width=250)

        # Row 3
        self.password=Label(frame1,text="Password:",font=("Times new Roman",15),bg="white").place(x=50,y=260)
        self.txt_password = Entry(frame1,font=("Times new Roman",15),bd=2,relief="solid").place(x=50,y=290,width=250)

        self.cpassword=Label(frame1,text="Confirm Password: ",font=("Times new Roman",15),bg="white").place(x=340,y=260)
        self.txt_cpassword = Entry(frame1,font=("Times new Roman",15),bd=2,relief="solid").place(x=340,y=290,width=250)


        self.btn_register = Button(frame1 ,text="REGISTER", font=("Times new Roman",15,"bold"),bg="#0F5658",fg="white",cursor="hand2",command=self.register_data)
        self.btn_register.place(x=50,y=370,width=150,height=50)
        self.btn_sign_in = Button(self.root ,text="Sign In",font=("Times new Roman",15,"bold"),bg="#72CDD0",fg="black",cursor="hand2").place(x=190,y=540,width=150,height=50)


        # Entry Fields
    def register_data(self):
        print(self.var_fname.get())
        print(self.var_lname.get())







root =Tk()
obj = Register(root)
root.mainloop()