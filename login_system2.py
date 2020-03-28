import tkinter 
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk
from csv import DictReader,DictWriter


window=tkinter.Tk()

class login_page:
    def __init__(self,window):
        self.window=window
        self.window.title("Login Page")
        self.window.geometry("900x600+0+0")

        self.bg_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\icons\background_image.png")        
        self.user_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\icons\user image.png")        
        self.username_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\icons\username.png")        
        self.password_image=ImageTk.PhotoImage(file=r"E:\mayankvscode\icons\password.png")      

        ttk.Label(self.window,image=self.bg_image).pack(expand=True,fill="both")  
        ttk.Label(self.window,text="\t User Login",font=("algerian",40,"bold"),foreground="black",background="green",border=30,relief="raised").place(x=0,y=0,relwidth=True)

        self.login_frame=tkinter.Frame(self.window,background="#B9BAAC")
        self.login_frame.place(x=220,y=150)

        # user image introducing
        ttk.Label(self.login_frame,image=self.user_image,background="#B9BAAC").grid(row=0,columnspan=4,pady=30)

        # username image & labelling
        ttk.Label(self.login_frame,image=self.username_image,text="Username  =",font=("times new roman",15,"bold"),background="#B9BAAC",compound=tkinter.LEFT).grid(row=1,column=0,sticky=tkinter.W,padx=5,pady=10)

        # password image & labelling
        ttk.Label(self.login_frame,image=self.password_image,text="Password   =",font=("times new roman",15,"bold"),background="#B9BAAC",compound=tkinter.LEFT).grid(row=2,column=0,sticky=tkinter.W,padx=5,pady=10)


        # username entry box
        self.username=tkinter.StringVar()
        self.username_entry=ttk.Entry(self.login_frame,width=50,textvariable=self.username)
        self.username_entry.grid(row=1,column=1,padx=10,pady=10)

        # password entry box
        self.password=tkinter.StringVar()
        self.password_entry=ttk.Entry(self.login_frame,width=50,textvariable=self.password)
        self.password_entry.grid(row=2,column=1,padx=10,pady=10)

        for i in self.login_frame.winfo_children():
            i.grid_configure(padx=15,pady=15)


    
        def function_call():
            self.usernames=self.username.get()
            self.passwords=self.password.get()
            if (self.usernames):
                with open("Login_page_database.csv") as new_file:
                    c=DictReader(new_file)
                    for i in c:
                        if (self.usernames==i["Username"]):
                            if (self.passwords):
                                if (self.passwords==i["Password"]):
                                    mb.showinfo("Congrats","Login Successfully")
                                    self.username_entry.delete(0,tkinter.END)
                                    self.password_entry.delete(0,tkinter.END)
                                    break
        
                                else:
                                    mb.showerror("Error","Incorrect Password")
                                    self.password_entry.delete(0,tkinter.END)
                                    
                            else:
                                mb.showwarning("Warning","Password Not Entered")
                                
                        continue

            elif (self.usernames=="" and self.passwords!=""):
                mb.showwarning("Warning","Username Not Entered")
            elif (self.usernames=="" and self.passwords==""):
                mb.showerror("Error","Input not given")


            
        # login button
        ttk.Button(self.login_frame,text="Login",command=function_call).grid(row=3,column=1,padx=15,pady=15)



login_page_object=login_page(window)
window.mainloop()