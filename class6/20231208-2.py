import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# import secret key
cred= credentials.Certificate('../fir-test-f1500-firebase-adminsdk-cjknd-f8bb2db471.json')
# Initiate firebase
firebase_admin.initialize_app(cred)
# Initiate.client()
db = firestore.client()