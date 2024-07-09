import pickle 
from flask import Flask,request, render_template
import warnings

app = Flask(__name__)
model = pickle.load(open("knn.pk1", "rb"))

@app.route("/")
def indput():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def admin():
    print('in predict')
    Coping_Mechanisms = eval(request.form["Coping_Mechanmism"])
    Current_Stressors = eval(request.form["stress"])
    Demographics = eval(request.form["Demographics"])
    Family_History = eval(request.form("Family_History"))
    Gender = eval(request.form["gender"])
    Impact_on_Life = eval(request.form['Impact_on_Life'])
    Symptoms = eval(request.form["Symptoms"])
    
    print([[Coping_Mechanisms,Current_Stressors,Demographics,Family_History,Gender,Impact_on_Life,Symptoms]])
    try:
        preds=model.predict([[Coping_Mechanisms,Current_Stressors,Demographics,Family_History,Gender,Impact_on_Life,Symptoms]])
        print(preds)
    except Exception as e:
        print(e)
    if preds[0]==1:
        return render_template("index.html", p='Patient might face panic disorder')
    return render_template("index.html", p='Patient is normal')

if __name__ == '__main__':
    app.run(debug = False, port=4000)
    