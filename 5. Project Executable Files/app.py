import pickle
from flask import Flask, request, render_template

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
model = pickle.load(open("dtf.pkl","rb"))

@app.route('/')
def indput():

        return render_template("index.html")

@app.route('/predict', methods ['GET', 'POST'])
def admin():

    print('in predict')
    Coping_Mechanisms = eval(request.form["Coping_Mechanisms"])

    Current_Stressors = eval(request.form["stresss"])
    Demographics = eval(request.form["Demographics"])

    Family_History = eval(request.form["Family_History"])
    Gender = eval(request.form["gender"])

    Impact_on_Life = eval(request.form["Impact_on_Life"])
    Symptoms = eval(request.form["Symptoms"])

    print([[Coping_Mechanisms, Current_Stressors, Demographics, Family_History, Gender, Impact_on_Life, Symptoms]])
    try:

                            preds = model.predict([[Coping_Mechanisms, Current_Stressors, Demographics, Family_History, Gender, Impact_on_Life, Symptoms]])
                            print(preds)

    except Exception as e:   print(e)

    if preds[0]==1:          
        return render_template("index.html", p="Patient might face panic disorder")

    else:
        return render_template("index.html",p="Patient is normal")

if __name__ == '__main__':
         app.run(debug=False, port=4000)
