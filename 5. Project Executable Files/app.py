import pickle
from flask import Flask, request, render_template

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
model = pickle.load(open("dtf.pkl", "rb"))

@app.route('/')
def indput():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        print('in predict')

        Coping_Mechanisms = request.form.get("Coping_Mechanisms")
        Current_Stressors = request.form.get("stress")
        Demographics = request.form.get("Demographics")
        Family_History = request.form.get("Family_History")
        Gender = request.form.get("gender")
        Impact_on_Life = request.form.get("Impact_on_Life")
        Symptoms = request.form.get("Symptoms")

        print([[Coping_Mechanisms, Current_Stressors, Demographics, Family_History, Gender, Impact_on_Life, Symptoms]])
        try:
            preds = model.predict([[Coping_Mechanisms, Current_Stressors, Demographics, Family_History, Gender, Impact_on_Life, Symptoms]])
            print(preds)
        except Exception as e:
            print(e)
            return render_template("index.html", p="An error occurred during prediction.")

        if preds[0] == 1:
            return render_template("index.html", p="Patient might face panic disorder")
        else:
            return render_template("index.html", p="Patient is normal")

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, port=4000)
