import pyrebase
import os

config = {
"apiKey": "AIzaSyCVm_Bg27Zi19fNLWN0RWsP1Ck4HxqA8QI",
"authDomain": "fir-test-f1500.firebaseapp.com",
"projectId": "fir-test-f1500",
"storageBucket": "fir-test-f1500.appspot.com",
"messagingSenderId": "721958247771",
"appId": "1:721958247771:web:c543aecd1676dd53be4e7e",
"databaseURL":"", 
"serviceAccount":"../fir-test-f1500-firebase-adminsdk-cjknd-f8bb2db471.json"
}

dir_name="nature"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

firebase=pyrebase.initialize_app(config)
storage=firebase.storage()
all_files = storage.list_files()
for file in all_files:
    if file.name.startswith(dir_name):
        file.download_to_filename(file.name)
