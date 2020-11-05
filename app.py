from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("titanic.pkl")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        PC = request.form["Passanger Class"]
        pc = int(PC)
        print(pc)
        SEX = request.form["Sex"]
        SEX = int(SEX)
        print(SEX)
        AGE = request.form["Age"]
        AGE = int(AGE)
        print(AGE)
        PCH = request.form["Child accompanied"]
        PCH = float(PCH)
        print(PCH)      
        list1=[[pc,SEX,AGE,PCH]]  
        print(list1)
        price = np.abs(model.predict(list1))
        return render_template('index.html',prediction_text="Survivied={}".format(price))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
