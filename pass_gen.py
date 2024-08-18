from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import math

class password_generator:
    def __init__(self,root):
        self.root = root 
        self.root.title("Password Generator")
        self.root.geometry("650x445+370+140")

        main_frame=Frame(self.root,relief=RIDGE)
        main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        title_lbl=Label(main_frame,text="PASSWORD GENERATOR",font=("times new roman",20,"bold"),fg="red",bg="white")
        title_lbl.place(relx=0,rely=0,relwidth=1,relheight=0.1)

        img=Image.open("img.jpg")
        img=img.resize((300,300))
        self.photo=ImageTk.PhotoImage(img)
        img_lbl=Label(main_frame,image=self.photo)
        img_lbl.place(relx=0.02, rely=0.15, relwidth=0.45, relheight=0.6)

        len_lbl=Label(main_frame,text="Enter password length",font=("times new roman",12,"bold"),fg="black")
        len_lbl.place(relx=0.52, rely=0.2, relwidth=0.45)

        self.input=StringVar()
        entry_fill=ttk.Entry(main_frame,textvariable=self.input,width=35,font=("times new roman",12,"bold"))
        entry_fill.place(relx=0.52, rely=0.27, relwidth=0.45)

        btn=Button(main_frame,text="GENERATE PASSWORD",font=("times new roman",15,"bold"),fg="white",bg="red",bd=4,relief=SUNKEN,cursor="hand2",command=self.pass_gen)
        btn.place(relx=0.52, rely=0.35, relwidth=0.45, relheight=0.1)

        pass_lbl=Label(main_frame,text="Password Generated:",font=("times new roman",12,"bold"),fg="black")
        pass_lbl.place(relx=0.52, rely=0.5, relwidth=0.45)
    
    def generate_pass(self,length, array, is_alpha=False):
        for i in range(length):
            index = random.randint(0, len(array) - 1)
            character = array[index]
            if is_alpha:
                case = random.randint(0, 1)
                if case == 1:
                    character = character.upper()
            self.password.append(character)

    def pass_gen(self):
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
        special = "@#$%&*"
        if self.input.get()=="":
            messagebox.showerror("Error","Please enter some input")
        else:
            pass_len=int(self.input.get())
            alpha_len = pass_len//2
            num_len = math.ceil(pass_len*30/100)
            special_len = pass_len-(alpha_len+num_len)
            self.password = []
            # alpha password
            self.generate_pass(alpha_len, alpha, True)
            # numeric password
            self.generate_pass(num_len, num)
            # special Character password
            self.generate_pass(special_len, special)
            # suffle the generated password list
            random.shuffle(self.password)
            # convert List To string
            gen_password = ""
            for i in self.password:
                gen_password = gen_password + str(i)
            
            res_lbl=Label(self.root,text=gen_password,font=("times new roman",12,"bold"),fg="black")
            res_lbl.place(relx=0.52, rely=0.57, relwidth=0.45)

if __name__=="__main__":
    root=Tk()
    app=password_generator(root)
    root.mainloop()