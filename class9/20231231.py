import firebase_admin
import os
from firebase_admin import credentials, storage
cred = credentials.Certificate("C:/Users/halst/Documents/Python_2023Autumn/fir-test-f1500-firebase-adminsdk-cjknd-f8bb2db471.json")
firebase_admin.initialize_app(cred,{"storageBucket":"fir-test-f1500.appspot.com"})

# file_path="sea.png"
bucket = storage.bucket()
# blob=bucket.blob(file_path)
# blob.upload_from_filename(file_path)

# def upload_blob(bucket, source_file_name, destination_blob_name):
#     blob=bucket.blob(destination_blob_name)
#     blob.upload_from_filename(source_file_name)
#     print(f"File{source_file_name} uploaded to {destination_blob_name}.")

# upload_blob(bucket, 'sea.png','nature/beautiful_sea.png')

# dir_path="./taipei"
# filelist=[f for f in os.listdir(dir_path) if f.endswith(".jpg")]
# print(filelist)
# for file in filelist:
#     file_path = dir_path+"/"+file
#     blob_path="photo/"+file
#     print("Now is uploading file {}.".format(file_path))
#     blob = bucket.blob(blob_path)
#     blob.upload_from_filename(file_path)
blob=bucket.blob("nature/beautiful_sea.png")
blob.download_to_filename("human_photo.png")