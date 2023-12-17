import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# import secret key
cred= credentials.Certificate('C:/Users/halst/Documents/Python_2023Autumn/fir-test-f1500-firebase-adminsdk-cjknd-f8bb2db471.json')
# Initiate firebase
firebase_admin.initialize_app(cred)
# Initiate.client()
db = firestore.client()

# doc={"name":"Halston","email":"halstonchen1119@gmail.com"}
# doc2={"name":"Jaclyn","email":"jaclyn@gmail.com"}
# doc_ref = doc_red=db.collection("Autumn_student").document("student01")
# doc_ref.set(doc)
# collection_ref = db.collection("Autumn2023_Student")
# collection_ref.add(doc)
# doc_ref = doc_red=db.collection("Autumn_student").document("student02")
# doc_ref.set(doc2)
# path = "Autumn_student/student02"
# doc_ref=db.document(path)
# try:
#     doc =doc_ref.get()
#     doc_dict = doc.to_dict()
#     print("The content of the document us: {}".format(doc_dict))
# except:
#     print("The reference of document is not exist, please check the path is correct or not {}".format(path))

# docs=collection_ref.where("name","==","Jaclyn").get()
# for doc in docs:
#     print("The content of the document is :{}".format(doc.to_dict()))

# path="Autumn_student/student01"
# doc_ref= db.document(path)
# doc={"birthday":"1119"}
# doc_ref.update(doc)
# doc={"email":"J11330@kcis.com.tw"}
# doc_ref.update(doc)

# contacts={
#     'email':'halstonchen1119@gmail.com',
#     'phone':"0917739664"
# }
# doc={
#     'contacts':contacts
# }
# doc_ref.update(doc)
# doc={
#     'contacts.email':'abc@gmail.com'
# }
# doc_ref.update(doc)

# path="Autumn_student/student02"
# doc_ref= db.document(path)
# doc={"email":"niceday@gmail.com"}
# doc_ref.update(doc)
# doc_ref.delete()
students_ref=db.collection('Autumn_student')
docs=students_ref.get()
for doc in docs:
    doc.reference.delete()
