import pickle
import pandas as pd
from flask import Flask, request, render_template

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load the model
with open("dtf.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def input():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        print('in predict')

        # Get form data
        Coping_Mechanisms = request.form.get("Coping Mechanisms")
        Current_Stressors = request.form.get("stress")
        Demographics = request.form.get("Demographics")
        Family_History = request.form.get("Family History")
        Gender = request.form.get("Gender")
        Impact_on_Life = request.form.get("Impact on Life")
        Symptoms = request.form.get("Symptoms")

        # Create a DataFrame from the input data
        input_data = pd.DataFrame(
            [[Coping_Mechanisms, Current_Stressors, Demographics, Family_History, Gender, Impact_on_Life, Symptoms]],
            columns=['Coping Mechanisms', 'Current Stressors', 'Demographics', 'Family History', 'Gender', 'Impact on Life', 'Symptoms']
        )

        print(input_data)

        try:
            # Directly use the model to predict
            preds = model.predict(input_data)
            print(preds)
        except Exception as e:
            print(f"Error during prediction: {e}")
            return render_template("index.html", p="An error occurred during prediction.")

        if preds[0] == 1:
            return render_template("index.html", p="Patient might face panic disorder")
        else:
            return render_template("index.html", p="Patient is normal")

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, port=4000)
