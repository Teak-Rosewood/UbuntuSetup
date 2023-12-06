import pyrebase 
import cv2
import base64
import json
import pickle
from PIL import Image
import numpy

config = {
    "apiKey": "AIzaSyAp2BvHM-vU8VTJDPrGvSiR1zfe19sV-Ho",
    "authDomain": "medical-suite-b2e95.firebaseapp.com",
    "databaseURL": "https://medical-suite-b2e95-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "medical-suite-b2e95.appspot.com"
}

firebase = pyrebase.initialize_app(config)

def im2json(im):
    imdata = pickle.dumps(im)
    jstr = json.dumps({"image": base64.b64encode(imdata).decode('ascii')})
    return jstr

def json2im(jstr):
    load = json.loads(jstr)
    imdata = base64.b64decode(load['image'])
    im = pickle.loads(imdata)
    return im

def check_pass(email,password,firebase):
    auth = firebase.auth()
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        id = auth.get_account_info(user['idToken'])['users'][0]['localId']
        return id
    except:
        return False

def signup(name, email, phone, gender, age, password, firebase):
    auth = firebase.auth()
    try:
        auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)
        id = auth.get_account_info(user['idToken'])['users'][0]['localId']
        data = {
        "name": name,
        "email": email,
        "phone": phone,
        "gender": gender,
        "age": age
        }
        db = firebase.database()
        #db.child("users")
        db.child("users").child(id).set(data)
        return True
    except: 
        return False

def get_user_data(id, firebase):
    db = firebase.database()
    try:
        data = db.child("users").child(id).get()
        return data.val()
    except:
        return False

def feedback(id, name, email, improvement, experience, etc, firebase):
    db = firebase.database()
    try:
        data = {
        "name": name,
        "email": email,
        "improvement": improvement,
        "experience": experience,
        "etc": etc
        }
        db.child("feedback").child(id).push(data)
        return True
    except:
        return False

def send_result_data(id, origin, result, firebase):
    db = firebase.database()
    origin = im2json(origin)
    result = im2json(result)
    try:
        data = {
        "origin": origin,
        "result": result
        }
        db.child("results").child(id).push(data)
        return True
    except:
        return False

def get_result_data(id, firebase):
    db = firebase.database()
    try:
        results = db.child("results").child(id).get()
        origin_result = []
        inference_result = []
        for result in results.each():
            origin_result.append(json2im(result.val()["origin"]))
            inference_result.append(json2im(result.val()["retult"]))
        return origin_result, inference_result        
    except:
        return False
    
flag = signup("saatwik", "saatwik.vasishtha@gmail.com", 9740225444, "M", 20, "Hello123", firebase)
print("signup: ", flag)
id = check_pass("saatwik.vasishtha@gmal.com", "Hello123", firebase)
print("user local ID: ", id)
get_user_data(id, firebase)
flag = feedback(id, "Saatwik", "saatwik.vasishtha@gmal.com", "good", "good", "good", firebase)
print("feedback: ", flag)
img = cv2.imread("download.png")
flag = send_result_data(id, img, img)
print("sending img: ", flag)
a, b = get_result_data(id, firebase)
print("original images:", len(a), "infered images:", len(b))







