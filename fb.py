import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

def implicit():
    from google.cloud import storage
    storage_client = storage.Client()

    buckets = list(storage_client.list_buckets())
    print(buckets)

def setup():
    print("setting up firebase")
    path ="config/objectdetection-db905-firebase-adminsdk-psdeh-d6754e4c1f.json"
    cred = credentials.Certificate(path)
    fb = firebase_admin.initialize_app(cred,{
        'storageBucket': 'objectdetection-db905.appspot.com'
    })
    print("connected to firebase")
    return fb,cred

