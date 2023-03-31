import tkinter
import customtkinter

window = tkinter.Tk()
window.geometry("500x350")
window.title("Log in")
window.iconbitmap("icon.ico")
customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("default")

def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


appearance_mode_optionemenu = customtkinter.CTkOptionMenu(window, values=["Dark", "Light", "System"], command=change_appearance_mode_event)
appearance_mode_optionemenu.pack(padx=0, pady=0)

def login():
    print("Welcome")


def dark():
    customtkinter.set_appearance_mode("dark")
    modeswitch.destroy()


def light():
    customtkinter.set_appearance_mode("light")
    modeswitch.destroy()
    modeswitch2 = customtkinter.CTkButton(master=window, text="Dark", font=("Roboto", 12), command=dark)
    modeswitch2.pack(pady=15, padx=10, side="left")


frame = customtkinter.CTkFrame(master=window)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Log in", font=("Roboto", 20))
label.pack(padx=12, pady=10)

username = customtkinter.CTkEntry(master=frame, placeholder_text="username")
username.pack(pady=12, padx=10)

password = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
password.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="login", command=login)
button.pack(pady=12, padx=10)

chkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
chkbox.pack(pady=12, padx=10)

modeswitch = customtkinter.CTkButton(master=window, text="Light", font=("Roboto", 12), command=light)
modeswitch.pack(pady=15, padx=10, side="left")


window.mainloop()
