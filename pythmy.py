import tkinter as tk
import os
from PIL import Image, ImageTk
import csv
from pygame import mixer
mixer.init()


address = "./parolebi/users.txt"
csv_file = "./parolebi//users_info.csv"


def submit():
    
    
    mixer.music.load("./Breaking Bad Main Title Theme (Extended).mp3")
    mixer.music.play()
    email_error.config(text="", fg="red")
    password_error.config(text="", fg="red")

    is_valid = True

    if len(email.get()) == 0:
        email_error.config(text="ელ-ფოსტის ველი სავალდებულოა")
        is_valid = False
    elif not email.get().endswith("@gmail.com"):
        email_error.config(text="ელ-ფოსტა უნდა იყოს @gmail.com ფორმატში")
        is_valid = False


    if len(password.get()) == 0:
        password_error.config(text="პაროლის ველი სავალდებულოა")
        is_valid = False
    elif len(password.get()) < 8:
        password_error.config(text="პაროლი უნდა იყოს 8 სიმბოლოზე მეტი")
        is_valid = False

    if not is_valid:
        return
    
    
    
    email_get = email.get()
    password_get = password.get()
    data = [email_get, password_get]
    csv_open = open(csv_file, "a" , newline="", encoding="utf-8") 
    writer = csv.writer(csv_open)
    writer.writerow(data)
    csv_open.close()
    email.delete(0, tk.END)
    password.delete(0, tk.END)
    for widget in root.winfo_children():
        widget.destroy()
        

    root.title("Profile")
    tk.Label(root, text="მომხმარებელი დარეგისტრირდა", font=("Arial", 20)).pack(pady=20)
    logout_btn = tk.Button(root, text="Logout", bg="red", fg="white", command=logout )
    logout_btn.pack()
    tk.Label(root, text="ელ-ფოსტა: " + email_get).pack(pady=10)
    tk.Label(root, text="პაროლი: " + password_get).pack()
    tk.Label(root, text="Profile Photo").pack(pady=10)
    profile_image = Image.open("../tkinter/walter smile.webp").resize((30, 30))
    profile_photo = ImageTk.PhotoImage(profile_image)
    image_profile_label = tk.Label(root, image=profile_photo)
    image_profile_label.image = profile_photo
    image_profile_label.pack()
    
    
    
    image = Image.open("./gilocav.jpg")
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.image = photo
    happy_label = tk.Label(root, text="გილოცავთ ახლა ვოლტერმა იცის შენი პაროლი :)", font=("Arial", 20) , fg="green")
    happy_label.pack(pady=10)
    image_label.pack()
    
    
   
    

def logout():
    root1 = tk.Tk()
    root1.title("Form")
    root1['bg'] = "#ffe400"
    root1.geometry("720x220")
    root1.resizable(width=False, height=True)
    # text_label = Label(root1, text="გილოცავთ თქვენ ვეღარ გახვალთ აქედან :)", font=("Arial", 20))
    text_label = tk.Label(root1, text="გილოცავთ თქვენ ვეღარ გახვალთ აქედან :)", font=("Arial", 20))
    text_label.pack(pady=20)
    root1.mainloop()
    
        

root = tk.Tk()
root.title("Form")
root['bg'] = "#ffe400"
root.geometry("800x1000")
root.resizable(width=False, height=True)

label_frame = tk.Frame(root)
label_frame.place(relwidth=1, relheight=0.1)

pr_label = tk.Label(label_frame, text="BreakingLevan.ge" , font=("Arial", 20))
pr_label.pack(pady=20)


image = Image.open("./levan.png")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack(pady=120)

reg_title = tk.Label(root, text="სისტემაში შესვლა" , font=("Arial", 20) )
reg_title.pack(pady=2)

email_titles = tk.Label(root, text="ელ-ფოსტა")
email_titles.pack(pady=10)
email = tk.Entry(root, text="Email")
email_error = tk.Label(root)
email_error.pack()
email.pack()

password_title = tk.Label(root, text="პაროლი")
password_title.pack(pady=5)
password = tk.Entry(root, text="Password" , show="*")
password_error = tk.Label(root)
password_error.pack()
password.pack(pady=5)
submit_btn = tk.Button(root, text="Submit", bg="blue", fg="white" , command=submit )
submit_btn.pack()
root.mainloop()



