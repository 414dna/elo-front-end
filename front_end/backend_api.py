
import pyrebase
token=0
config = {
  "apiKey": "AIzaSyCJRE8-9fsXIlj6O5yjmH6xjl62I3wgrD0",
  "authDomain": "first-baby-4aabf.firebaseapp.com",
  "databaseURL": "https://first-baby-4aabf-default-rtdb.firebaseio.com", 
  "storageBucket": "first-baby-4aabf.appspot.com",
  "messagingSenderId": "488420073997",
  "appId": "1:488420073997:web:f18907e3a1bd72559bab44",
  "measurementId": "G-MB5Y9K2R7L"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
def auth1(email=None,password=None):
  user = auth.sign_in_with_email_and_password(email,password)
  print(user)
  return user
def user1(node=None,id=None):
  data = {f"optim{id}": 0,f'valve{id}': 0}
  node=node+id
  db.child(node).update(data)
  Keys = db.child(node).shallow().get().val()
  for key in Keys:
    if key.isnumeric():
      value=db.child(node).child(key).get()
      print(value.val()) 
      return 'success'
