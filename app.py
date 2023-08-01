import pyshorteners
import customtkinter as ctk
import pyperclip


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("500x300")
app.title("Url Shortener")


def submit():
    long_url = entry.get()

    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)

    pyperclip.copy(short_url)

    url_gen.configure(text=f"Your New Link is was copied to clipboard")


frame = ctk.CTkFrame(master=app)
frame.pack(padx=5, pady=5, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Url to be shorten: ")
label.pack(padx=5, pady=5)

entry = ctk.CTkEntry(master=frame)
entry.pack(padx=5, pady=5)

btn = ctk.CTkButton(master=frame, text="Generate", command=submit)
btn.pack(padx=5, pady=5)

url_gen = ctk.CTkLabel(
    master=frame, text="Url will be copied to clipboard when generated"
)
url_gen.pack(padx=5, pady=5)

app.mainloop()
