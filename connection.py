import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import uuid

# Use a service account
cred = credentials.Certificate('conf/FirebaseKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_new_id():
    return uuid.uuid1()
