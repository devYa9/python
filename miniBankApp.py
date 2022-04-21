import random
import tkinter.messagebox
import json
from tkinter import *

# class

class Account:
    def __init__(self, fname, lname, email, password: str, idAcc, solde=None):
        rib_gen = random.randint(10000000000, 99999999999)
        self.fname = fname.title()
        self.lname = lname.title()
        self._email = email
        self._password = str(password)
        self.id = idAcc
        self._solde = solde
        self._rib = rib_gen


# colors

background = "white"
grey = "#5A5A5A"
orange = "#f98f21"

# main window
window = Tk()
window.geometry("600x500")
window.title("Home")
window.config(bg=orange)

# main frame
login_frame = Frame(window)
login_frame.pack(expand=True)


def cleaning(frame):
    for widge in frame.winfo_children():
        widge.destroy()


def data_update(new_data, i):
    data = open(r"accounts.json", "r")
    accounts = json.load(data)
    accounts[i] = new_data
    with open(r"accounts.json", "w") as jfile:
        json.dump(accounts, jfile, indent=4)


def del_acc(i):
    data = open(r"accounts.json", "r")
    accounts = json.load(data)
    del accounts[i]
    with open(r"accounts.json", "w") as jfile:
        json.dump(accounts, jfile, indent=4)


def home(data, id_acc):
    cleaning(login_frame)
    welcome_label = Label(login_frame, text=f"{data['lname']} {data['fname']}", fg=grey,
                          bg=background, font="poppins 14")
    welcome_label.place(x=40, y=40)
    ribmsg_label = Label(login_frame, text=f"Account RIB:", fg=grey, bg=background,
                         font="poppins 12")
    ribmsg_label.place(x=40, y=80)
    rib_label = Label(login_frame, text=f"{data['_rib']}", fg=grey, bg=background,
                      font="poppins 13")
    rib_label.place(x=40, y=105)
    soldemsg_label = Label(login_frame, text=f"Sold:", fg=grey, bg=background, font="poppins 13")
    soldemsg_label.place(x=280, y=80)

    if data["_solde"] is None:
        solde_label = Label(login_frame, text=f"0.0 DH", fg=grey, bg=background, font="poppins 13")
        solde_label.place(x=280, y=105)

        def confirm():
            if setting_sold_entry.get().isdigit():
                solde = setting_sold_entry.get()
                data['_solde'] = solde
                setting_sold_entry.destroy()
                setting_sold_btn.destroy()
                setting_sold_label.destroy()
                dh_label.destroy()
                home(data, id_acc)
                data_update(data, id_acc)
            else:
                tkinter.messagebox.showerror("Solde inccorect", "Enter a valid number")
        setting_sold_label = Label(login_frame, text="You Haven't Set Your Solde Yet", fg=grey, bg=background,
                                   font="poppins 13")
        setting_sold_label.place(x=40, y=150)
        setting_sold_entry = Entry(login_frame, width=23, font="poppins 13", highlightbackground='grey',
                                   highlightcolor=orange, highlightthickness=0.5, borderwidth=0)
        setting_sold_entry.place(x=40, y=190, width=280, height=35)
        dh_label = Label(login_frame, text="DH", fg=grey, bg=background, font="poppins 13")
        dh_label.place(x=330, y=190)
        setting_sold_btn = Button(login_frame, text="Confirm", font="poppins 10 bold", bg=orange, fg="white",
                                  width=12, relief="flat", activebackground=background, activeforeground=orange,
                                  border=0, cursor="hand2", command=confirm)
        setting_sold_btn.place(x=219, y=230)
    else:
        def delete():
            askyesno = tkinter.messagebox.askyesno("Delete Account", "Are you sure ?")
            if askyesno:
                del_acc(id_acc)
                login_landpage()
            else:
                pass
        rib_label = Label(login_frame, text=f"{float(data['_solde'])} DH", fg=grey, bg=background, font="poppins 13")
        rib_label.place(x=280, y=105)
        debit_sold_btn = Button(login_frame, text="Debit", font="poppins 10 bold", bg=orange, fg="white",
                                width=12, relief="flat", activebackground=background, activeforeground=orange,
                                border=1, cursor="hand2")
        debit_sold_btn.place(x=40, y=230)
        credit_sold_btn = Button(login_frame, text="Credit", font="poppins 10 bold", bg=orange, fg="white",
                                 width=12, relief="flat", activebackground=background, activeforeground=orange,
                                 border=1, cursor="hand2")
        credit_sold_btn.place(x=240, y=230)
        logout_btn = Button(login_frame, text="Log out", font="poppins 10 bold", bg=grey, fg="white",
                            width=12, relief="flat", activebackground=background, activeforeground=orange,
                            border=1, cursor="hand2", command=login_landpage)
        logout_btn.place(x=240, y=350)
        delete_btn = Button(login_frame, text="Delete Account", font="poppins 10 bold", bg="red", fg="white",
                            width=12, relief="flat", activebackground=background, activeforeground=orange,
                            border=1, cursor="hand2", command=delete)
        delete_btn.place(x=40, y=350)


def login_landpage():
    cleaning(login_frame)
    login_frame.config(width=400, height=450, bg=background, highlightcolor="orange",
                       highlightbackground="orange", highlightthickness=1)

    # connect
    def connect():
        try:
            data = open(r"accounts.json", "r")
            accounts = json.load(data)
            del accounts["id"]
            email = email_entry.get()
            password = pass_entry.get()
            for i in accounts:
                if email == accounts[i]["_email"]:

                    email_no_label.config(text="")
                    if password == accounts[i]["_password"]:
                        acces = accounts[i]
                        home(acces, i)
                        break
                    else:
                        pass_no_label.config(text="Password inccorect")
                    break
                else:
                    email_no_label.config(text="Account not found")
        except FileNotFoundError:
            cleaning(login_frame)
            data_error_label = Label(login_frame, text="No Data Found ! Create \nOne", fg=grey, bg=background,
                                     font="poppins 20")
            data_error_label.place(x=40, y=100)
            sign_in_btn = Button(login_frame, text="Create", font="poppins 12 bold", bg=orange, fg="white", width=25,
                                 relief="flat", command=signin_landpage,
                                 activebackground=background, activeforeground=orange, border=0, cursor="hand2")
            sign_in_btn.place(relx=0.5, y=280, anchor="center", height=40)

    # widgets
    login_label = Label(login_frame, text="Login", fg=grey, bg=background, font="poppins 20")
    login_label.place(x=40, y=40)
    email_label = Label(login_frame, text="Email ID/Mobile number", fg=grey, bg=background, font="poppins 10")
    email_label.place(x=40, y=100)
    email_entry = Entry(login_frame, width=23, font="poppins 12", highlightbackground='grey',
                        highlightcolor=orange, highlightthickness=0.5, borderwidth=0)
    email_entry.place(height=35, x=40, y=130, width=320)
    email_no_label = Label(login_frame, fg="red", bg=background,
                           font="poppins 10")
    email_no_label.place(x=230, y=165)
    pass_no_label = Label(login_frame, fg="red", bg=background,
                          font="poppins 10")
    pass_no_label.place(x=230, y=240)
    pass_label = Label(login_frame, text="Password", fg=grey, bg=background, font="poppins 10")
    pass_label.place(x=40, y=180)
    pass_entry = Entry(login_frame, width=23, font="poppins 13", highlightbackground='grey', highlightcolor=orange,
                       highlightthickness=0.5, borderwidth=0, show="*")
    pass_entry.place(height=35, x=40, y=210, width=320)
    checkVar = BooleanVar()
    checkVar.set(False)
    remember_check = Checkbutton(login_frame, bg=background, variable=checkVar, cursor="hand2")
    remember_check.place(x=35, y=250)
    remember_label = Label(login_frame, text="Remember me", fg="#3E3E3E", bg=background, font="poppins 10")
    remember_label.place(x=60, y=249)
    login_btn = Button(login_frame, text="Login", font="poppins 12 bold", bg=orange, fg="white", width=25,
                       relief="flat", command=connect,
                       activebackground=background, activeforeground=orange, border=0, cursor="hand2")
    login_btn.place(relx=0.5, y=320, anchor="center", height=40)

    new_label = Label(login_frame, text="New User?", font="poppins 10", bg=background, fg="#3E3E3E")
    new_label.place(x=110, y=349)
    new_label = Button(login_frame, text="Create Account", font="poppins 10", bg=background, fg="blue", border=0,
                       relief="flat", activebackground=background, cursor="hand2", command=signin_landpage)
    new_label.place(x=180, y=346)


def signin_landpage():
    cleaning(login_frame)

    login_frame.config(width=400, height=450, bg=background, highlightcolor="orange",
                       highlightbackground="orange", highlightthickness=1)

    # command
    def confirm():
        try:
            fname = str(fname_entry.get())
            lname = str(lname_entry.get())
            email = str(email_entry.get())
            password = str(pass_entry.get())
            if fname == "" or lname == "" or email == "" or password == "":
                if fname == "":
                    fname_label.config(text="First Name*", fg="red")
                else:
                    fname_label.config(text="First Name", fg=grey)
                if lname == "":
                    lname_label.config(text="Last Name*", fg="red")
                else:
                    lname_label.config(text="Last Name", fg=grey)
                if password == "":
                    pass_label.config(text="New Password*", fg="red")
                else:
                    pass_label.config(text="New Password", fg=grey)
                if email == "":
                    email_label.config(text="Email ID/Mobile number*", fg="red")
                else:
                    email_label.config(text="Email ID/Mobile number", fg=grey)
            else:
                file = open(r"accounts.json", "r")
                data = json.load(file)
                data["id"] += 1
                compte = Account(fname, lname, email, password, data["id"])
                dic = {data["id"]: compte.__dict__}
                data.update(dic)
                with open(r"accounts.json", "w") as jfile:
                    json.dump(data, jfile, indent=4)
                cleaning(login_frame)
                confirm_msg = Label(login_frame, text="You signed up successfuly !", font="poppins 15", bg=background)
                confirm_msg.place(rely=0.5, relx=0.5, anchor="center")
                next_btn = Button(login_frame, text="Next", font="poppins 12 bold", bg=orange, fg="white", width=20,
                                  relief="flat", command=login_landpage,
                                  activebackground=background, activeforeground=orange, border=0, cursor="hand2")
                next_btn.place(relx=0.5, y=360, anchor="center", height=40)
        except FileNotFoundError:
            with open(r"accounts.json", "w") as file:
                new = {"id": 0}
                json.dump(new, file, indent=4)

    # widgets
    login_label = Label(login_frame, text="Sign In", fg=grey, bg=background, font="poppins 20")
    login_label.place(x=40, y=40)

    fname_label = Label(login_frame, text="First Name", fg=grey, bg=background, font="poppins 10")
    fname_label.place(x=40, y=100)
    fname_entry = Entry(login_frame, font="poppins 12", highlightbackground='grey',
                        highlightcolor=orange, highlightthickness=0.5, borderwidth=0)
    fname_entry.place(height=35, x=40, y=130, width=150)

    lname_label = Label(login_frame, text="Last Name", fg=grey, bg=background, font="poppins 10")
    lname_label.place(x=210, y=100)
    lname_entry = Entry(login_frame, font="poppins 12", highlightbackground='grey',
                        highlightcolor=orange, highlightthickness=0.5, borderwidth=0)
    lname_entry.place(height=35, x=210, y=130, width=150)

    email_label = Label(login_frame, text="Email ID/Mobile number", fg=grey, bg=background, font="poppins 10")
    email_label.place(x=40, y=180)
    email_entry = Entry(login_frame, width=23, font="poppins 13", highlightbackground='grey', highlightcolor=orange,
                        highlightthickness=0.5, borderwidth=0)
    email_entry.place(height=35, x=40, y=210, width=320)

    pass_label = Label(login_frame, text="New Password", fg=grey, bg=background, font="poppins 10")
    pass_label.place(x=40, y=250)
    pass_entry = Entry(login_frame, width=23, font="poppins 13", highlightbackground='grey', highlightcolor=orange,
                       highlightthickness=0.5, borderwidth=0, show="*")
    pass_entry.place(height=35, x=40, y=280, width=320)

    login_btn = Button(login_frame, text="Sign In", font="poppins 12 bold", bg=orange, fg="white", width=25,
                       relief="flat",
                       activebackground=background, activeforeground=orange, border=0, cursor="hand2", command=confirm)
    login_btn.place(relx=0.5, y=360, anchor="center", height=40)

    new_label = Label(login_frame, text="Already have an account ?", font="poppins 10", bg=background, fg="#3E3E3E")
    new_label.place(x=80, y=403)
    create_label = Button(login_frame, text="Log In", font="poppins 10", bg=background, fg="blue", border=0,
                          relief="flat", activebackground=background, cursor="hand2", command=login_landpage)
    create_label.place(x=260, y=400)


login_landpage()
window.mainloop()
