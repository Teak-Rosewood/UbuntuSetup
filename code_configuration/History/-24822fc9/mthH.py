from flask import Flask,render_template,request,render_template_string,redirect,flash, session
from flask_session import Session
import flask_func.retrieve as retrieve
import flask_func.model_inference as model

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if not session.get("email"):
        return redirect("/login")
    return render_template('index.html')
 
 
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["email"] = request.form.get("email")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["email"] = None
    return redirect("/")

@app.route('/home')
def render_home_page():
    return render_template('index.html')

@app.route('/tumor_detect',methods=['POST','GET'])
def render_tumor_detect():
    if request.method == 'POST':
        name,email,image = retrieve.validate(request)
        prob,pred,segment = model.brainTumor(image)
        flash("True")
        return render_template('BrainTumor.html',email=email)
    return render_template('BrainTumor.html')

@app.route('/retinal_detect')
def render_retinal_detect():
    return render_template('Retinal.html')

@app.route('/info')
def render_info():
    return render_template('information.html')

@app.route('/feedback')
def render_feedback():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)