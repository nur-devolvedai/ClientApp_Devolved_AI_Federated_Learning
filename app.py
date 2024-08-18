import tkinter as tk
from PIL import Image, ImageTk

def show_home():
    clear_right_frame()
    label = tk.Label(right_frame, text="Home Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

def show_upload():
    clear_right_frame()
    label = tk.Label(right_frame, text="Upload Data Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

def show_preprocessing():
    clear_right_frame()
    label = tk.Label(right_frame, text="Preprocessing Data Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

def clear_right_frame():
    for widget in right_frame.winfo_children():
        widget.destroy()

def show_finetuning():
    clear_right_frame()
    label = tk.Label(right_frame, text="Finetuning Data Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

def show_evaluation():
    clear_right_frame()
    label = tk.Label(right_frame, text="Evaluation Data Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

def show_profile():
    clear_right_frame()
    label = tk.Label(right_frame, text="Profile Data Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

def show_notification():
    clear_right_frame()
    label = tk.Label(right_frame, text="Notification Data Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

def show_logout():
    clear_right_frame()
    label = tk.Label(right_frame, text="Logout Data Section", font=("Arial", 20), bg="#252B36", fg="white")
    label.pack(pady=20)

# Initialize the main window
root = tk.Tk()
root.title("Athena-2 Client Application")
root.geometry("1080x720")

# Create a frame for the header at the top
header_frame = tk.Frame(root, bg="#000000", height=60)
header_frame.pack(side="top", fill="x")

# Header label or title, aligned to the left
header_label = tk.Label(header_frame, text="Athena-2 Client Application", bg="#000000", fg="white", font=("Arial", 21, "bold"))
header_label.pack(side="left", padx=20, pady=20)

# User information on the right side of the header
user_info_frame = tk.Frame(header_frame, bg="#000000")
user_info_frame.pack(side="right", padx=20)

# Add user information (username and profile icon)
username_label = tk.Label(user_info_frame, text="Nazmul Hossain", bg="#000000", fg="white", font=("Arial", 14))
username_label.pack(side="left", padx=10)

# Assuming you have a user profile icon
profile_icon = ImageTk.PhotoImage(Image.open("image/profile_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
profile_label = tk.Label(user_info_frame, image=profile_icon, bg="#000000")
profile_label.pack(side="left")

# Create a frame for the navigation bar on the left
nav_frame = tk.Frame(root, width=300, bg="#343A46")
nav_frame.pack(side="left", fill="y")
nav_frame.pack_propagate(False)

# Create a frame for the content on the right
right_frame = tk.Frame(root, bg="#252B36")
right_frame.pack(side="right", fill="both", expand=True)

# Load icons (replace with actual file paths)
icon_home = ImageTk.PhotoImage(Image.open("image/home_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
icon_upload = ImageTk.PhotoImage(Image.open("image/upload_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
icon_preprocess = ImageTk.PhotoImage(Image.open("image/preprocess_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
icon_finetune = ImageTk.PhotoImage(Image.open("image/finetune_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
icon_evaluate = ImageTk.PhotoImage(Image.open("image/evaluate_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
icon_profile = ImageTk.PhotoImage(Image.open("image/profile_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
icon_notification = ImageTk.PhotoImage(Image.open("image/notification_icon.png").resize((24, 24), Image.Resampling.LANCZOS))
icon_logout = ImageTk.PhotoImage(Image.open("image/logout_icon.png").resize((24, 24), Image.Resampling.LANCZOS))

# Add buttons to the navigation frame with icons
btn_home = tk.Button(nav_frame, image=icon_home, text="Dashboard", compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_home)
btn_home.pack(pady=15, padx=(40, 0), anchor="w")

btn_upload = tk.Button(nav_frame, text="Data", image=icon_upload, compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_upload)
btn_upload.pack(pady=15, padx=(40, 0), anchor="w")

btn_preprocessing = tk.Button(nav_frame, text="Data Preprocess", image=icon_preprocess, compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_preprocessing)
btn_preprocessing.pack(pady=15, padx=(40, 0), anchor="w")

btn_finetuning = tk.Button(nav_frame, text="Finetuning", image=icon_finetune, compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_finetuning)
btn_finetuning.pack(pady=15, padx=(40, 0), anchor="w")

btn_evaluation = tk.Button(nav_frame, text="Evaluation", image=icon_evaluate, compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_evaluation)
btn_evaluation.pack(pady=15, padx=(40, 0), anchor="w")

btn_profile = tk.Button(nav_frame, text="Profile", image=icon_profile, compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_profile)
btn_profile.pack(pady=15, padx=(40, 0), anchor="w")

btn_notification = tk.Button(nav_frame, text="Notification", image=icon_notification, compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_notification)
btn_notification.pack(pady=15, padx=(40, 0), anchor="w")

btn_logout = tk.Button(nav_frame, text="Logout", image=icon_logout, compound="left", bg='#343A46', fg='white', font=("", 13, "bold"), bd=0, highlightthickness=0, relief="flat", cursor='hand2', activebackground='#252B36', activeforeground="white", command=show_logout)
btn_logout.pack(pady=15, padx=(40, 0), anchor="w")

# Start by showing the Home section
show_home()

# Run the application
root.mainloop()
