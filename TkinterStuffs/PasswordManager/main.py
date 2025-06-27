from tkinter import *
from tkinter import messagebox
import random
import json

# Search Password
def find_password():
    website = website_entry.get()
    try:
        data_file =  open("./TkinterStuffs/PasswordManager/data.json", "r")
        data = json.load(data_file)
    except:   
        messagebox.showerror("Error", "Data file not found")
    else:
        try:
            details = data[website]
            email_details = details["email"]
            password_details = details["password"]
            messagebox.showinfo(website, f"Email: {email_details}\nPassword: {password_details}")
        except KeyError:
            messagebox.showerror(website, "Website not found")

# Generate Password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = random.choices(letters, k=random.randint(4, 6))
    rand_numbers = random.choices(numbers, k=random.randint(3, 5))
    rand_symbols = random.choices(symbols, k=random.randint(2, 3))

    rand_password_list = rand_letters + rand_numbers + rand_symbols
    random.shuffle(rand_password_list)
    rand_password = ""
    for char in rand_password_list:
        rand_password += char
    
    password_entry.insert(0, rand_password)

# Save Password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror("Oops", "Don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(website, f"You have entered:\n{email}\n{password}")
        if is_ok:
            try:
                data_file = open("./TkinterStuffs/PasswordManager/data.json", "r")
                data = json.load(data_file)
            except:
                data_file = open("./TkinterStuffs/PasswordManager/data.json", "w")
                json.dump(new_data, data_file, indent=4)
            else:
                
                data.update(new_data)
                data_file = open("./TkinterStuffs/PasswordManager/data.json", "w")
                json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
    
    
    
# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

logo = Canvas(width=200, height=189)
logo_image = PhotoImage(file="./TkinterStuffs/PasswordManager/logo.png")
logo.create_image(100, 95, image=logo_image)
logo.grid(row=0, column=1)

website_label = Label(text="Website: ", font=("Arial", 15))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ", font=("Arial", 15))
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=("Arial", 15))
password_label.grid(row=3, column=0)

website_entry = Entry(width=17)    
website_entry.grid(row=1, column=1)
website_entry.focus()
# website_entry.place(x=170, y=195)

email_entry = Entry(width=35)  
email_entry.insert(0, "name@example.com")  
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=17)    
password_entry.grid(row=3, column=1)
# password_entry.place(x=170, y=258)

search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
# generate_button.place(x=470, y=255)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)
# add_button.config(pady=15)
# add_button.place(x=168, y=290)

window.mainloop()