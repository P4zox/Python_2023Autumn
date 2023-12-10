import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# connect python with 
cred=credentials.Certificate("C:/Users/halst/Documents/Python_2023Autumn/Python_2023Autumn/fir-test-f1500-firebase-adminsdk-cjknd-f8bb2db471.json")
firebase_admin.initialize_app(cred)

email="halstonchen1119@gmail.com"
password="123456"
user= auth.create_user(email=email, password=password)
print("User create susccessfully! {}".format(user.uid))