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
        return user
    except:
        return False

def signup(name,email,password, firebase):
    auth = firebase.auth()
    try:
        auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)
        data = {
        "phone": 9740225444,
        "gender": "M",
        "age": 20
        }
        db = firebase.database()
        #db.child("users")
        db.child("users").child(name).set(data)
        return True
    except: 
        return False

def feedback(name, email, improvement, experience, etc, firebase):
    db = firebase.database()
    try:
        data = {
        "email": email,
        "improvement": improvement,
        "experience": experience,
        "etc": etc
        }
        db.child("feedback").child(name).push(data)
        return True
    except:
        return False

def send_usr_data(name, origin, result, firebase):
    db = firebase.database()
    origin = im2json(origin)
    result = im2json(result)
    try:
        data = {
        "origin": origin,
        "result": result
        }
        db.child("results").child(name).push(data)
        return True
    except:
        return False

def get_usr_data(name, firebase):
    db = firebase.database()
    try:
        results = db.child("results").child(name).get()
        origin_result = []
        inference_result = []
        for result in results.each():
            origin_result.append(json2im(result.val()["origin"]))
            inference_result.append(json2im(result.val()["retult"]))
        return origin_result, inference_result        
    except:
        return False


# a, b = get_usr_data("saatwik")
# for img in range(2):
#     cv2.imwrite("origin"+str(img)+".png", a[img])
#     cv2.imwrite("result"+str(img)+".png", b[img])
feedback("saatwik", "saatwik.vasishtha@gmail.com", "Node Js can be used as server", "Good security of Files", "Overall good expereince", firebase)


    

