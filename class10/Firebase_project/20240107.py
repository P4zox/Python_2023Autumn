import firebase_admin
import os
from firebase_admin import credentials, storage
cred = credentials.Certificate("C:/Users/halst/Documents/Python_2023Autumn/fir-test-f1500-firebase-adminsdk-cjknd-f8bb2db471.json")
firebase_admin.initialize_app(cred,{"storageBucket":"fir-test-f1500.appspot.com"})

bucket = storage.bucket()

dir_path="./image"
filelist=[f for f in os.listdir(dir_path) if f.endswith(".jpg") or f.endswith(".png")]
print(filelist)
for file in filelist:
    file_path = dir_path+"/"+file
    blob_path="project_images/"+file
    print("Now is uploading file {}.".format(file_path))
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)

