import pyrebase
from tkinter import *

# creating a sign up and login window
config = {
"apiKey": "AIzaSyCVm_Bg27Zi19fNLWN0RWsP1Ck4HxqA8QI",
"authDomain": "fir-test-f1500.firebaseapp.com",
"projectId": "fir-test-f1500",
"storageBucket": "fir-test-f1500.appspot.com",
"messagingSenderId": "721958247771",
"appId": "1:721958247771:web:c543aecd1676dd53be4e7e",
"databaseURL":""
}

# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()

# setup tkinter
root=Tk()

# Create Labels(texts)
login_label=Label(root, text="login page")
account_label=Label(root, text="Account")
password_label=Label(root, text="Password")
result_label=Label(root, text="")

# Create Entrys and Buttons
account_entry=Entry(root)
password_entry=Entry(root, show="*") #To make the password into *
signup_button=Button(root, text="signup", width=10, command=lambda: addUser(root, account_entry, password_entry))

# Put those elements inside the window
login_label.pack(pady=5)
account_label.pack(pady=5)
account_entry.pack(pady=5)
password_label.pack(pady=5)
password_entry.pack(pady=5)
signup_button.pack(pady=5)
result_label.pack(pady=5)

# login firebase
def addUser(view, account_entry, password_entry):
    print(account_entry.get(), password_entry.get()) #get the password and account in terminal
    print("Sign Up...")
    # store the password and account in a variable
    account = account_entry.get()
    password = password_entry.get()
    try:
        user = auth.create_user_with_email_and_password(account, password)
        print("Successfully sign up!")
        result_label.config(text="Successfully sign up!")
    except Exception as e:
        print(f"Create User failed: {e}")
        result_label["text"]="Create User failled!"
    
root.mainloop()