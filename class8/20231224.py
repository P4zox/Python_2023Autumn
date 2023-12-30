import firebase_admin
from firebase_admin import credentials, storage
cred = credentials.Certificate("C:/Users/halst/Documents/Python_2023Autumn/fir-test-f1500-firebase-adminsdk-cjknd-f8bb2db471.json")
firebase_admin.initialize_app(cred,{"storageBucket":"fir-test-f1500.appspot.com"})
file_path="Firebase_project/image/bed1.jpg"
bucket = storage.bucket()
blob=bucket.blob(file_path)
blob.upload_from_filename(file_path)