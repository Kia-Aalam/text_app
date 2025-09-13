import tkinter as tk
from tkinter import messagebox

def first_window() :
    f_window = tk.Tk()
    f_window.title("Login")
    f_window.geometry("300x200")
    f_window.resizable(0 , 0)

    # f_window.iconbitmap("text.ico")

    f_frame = tk.Frame(f_window , padx = 20 , pady = 20)
    f_frame.pack(expand = True)

    lbl_name = tk.Label(f_frame , text = "User name : ")
    lbl_name.grid(row = 0 , column = 0 , columnspan = 1 , pady = 10)

    string_name = tk.StringVar()
    entry_name = tk.Entry(f_frame , textvariable = string_name)
    entry_name.grid(row = 0 , column = 1 , columnspan = 2 , pady = 10)

    lbl_password = tk.Label(f_frame , text = "Password : ")
    lbl_password.grid(row = 1 , column = 0 , columnspan = 1 , pady = 10)

    string_password = tk.StringVar()
    entry_password = tk.Entry(f_frame , show = "\u25CF" , textvariable = string_password)
    entry_password.grid(row = 1 , column = 1 , columnspan = 2 , pady = 10)
    
    def show() : # Check for Show Password
        if show_var.get() :
            entry_password.config(show = "")
        else :
            entry_password.config(show = "\u25CF")

    show_var = tk.BooleanVar(value = False)
    btn_show = tk.Checkbutton(f_frame , text = "Show" , variable = show_var , command = show) # Show Password Button
    btn_show.grid(row = 2 , column = 0 , columnspan = 1 , pady = 10)

    def check() : # Check user name and password
        user_name = "abc"
        user_password = "1234"
        if entry_name.get() == user_name and entry_password.get() == user_password :
            print(messagebox.showinfo(title = "Successful" , message = "your Login is successful"))
            f_window.destroy() # close first window
            second_window() # open second window
        else :
            print(messagebox.showwarning(title = "Not Successful" , message = "your Login is not successful"))

    btn_login = tk.Button(f_frame , text = "Login" , width = 15 , command = check) #Login Button
    btn_login.grid(row = 2 , column = 1 , columnspan = 1 , pady = 10 , sticky = "ew")

    f_window.mainloop()

def second_window() :
    s_window = tk.Tk()
    s_window.title("App")
    s_window.geometry("300x200")
    
    # s_window.iconbitmap("text.ico")

    s_frame = tk.Frame(s_window , padx = 20 , pady = 20)
    s_frame.pack(expand = True)

    text_box = tk.Text(s_frame , width = 30 , height = 5)
    text_box.grid(row = 0 , column = 0 , columnspan = 1 , pady = 5)

    def save() :
        text = text_box.get("1.0" , tk.END)
        file = open("text.txt" , "a")
        file.write(f"{text} \n")

    btn_save = tk.Button(s_frame , text = "Save" , command = save)
    btn_save.grid(row = 1 , column = 0 , columnspan = 1 , pady = 5)

    def close() : # Close second window
        s_window.destroy()
    
    btn_close = tk.Button(s_frame , text = "Close" , command = close) # Close Button in second window
    btn_close.grid(row = 2 , column = 0 , columnspan = 1 , pady = 5)

def main() :
    first_window()
main()