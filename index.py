from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST": 
        if request.form["height"] and request.form["weight"] is not None: 
            height =  request.form["height"]
            weight = request.form["weight"]
            result = predict(int(height), int(weight))
    return render_template("index.html", result=result)



# @app.route("predict")
def predict(a, b): 
    clf = load('gender_model.joblib') 

    prediction = clf.predict([(a, b)])

    if prediction[0]:
        result = "Male"
    else:
        result = "Female"
        
        
    return result
