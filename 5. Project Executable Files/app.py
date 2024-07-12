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

@app.route('/contributors', methods=['GET','POST'])
def contributors():
    return render_template("contributors.html")

@app.route('/predict', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        print('in predict')

        # Get form data
        Gender = request.form.get('Gender')
        Coping_Mechanisms = request.form.get("Coping_Mechanisms")
        Current_Stressors = request.form.get("Current_Stressors")
        Demographics = request.form.get("Demographics")
        Family_History = request.form.get("Family_History")
        Personal_History = request.form.get("Personal_History")
        Impact_on_Life = request.form.get("Impact_on_Life")
        Symptoms = request.form.get("Symptoms")
        Severity = request.form.get("Severity")
        Medical_History = request.form.get("Medical_History")
        Psychiatric_History = request.form.get("Psychiatric_History")
        Substance_Use = request.form.get("Substance_Use")
        Social_Support = request.form.get("Social_Support")
        Lifestyle_Factors = request.form.get("Lifestyle_Factors")

        # Create a DataFrame from the input data
        input_data = pd.DataFrame(
            [[Gender, Family_History, Personal_History,
                     Current_Stressors, Symptoms, Severity, Impact_on_Life,
                     Demographics, Medical_History, Psychiatric_History,
                     Substance_Use, Coping_Mechanisms, Social_Support,
                     Lifestyle_Factors]],
            columns=[ 'Gender', 'Family History', 'Personal History',
                     'Current Stressors', 'Symptoms', 'Severity', 'Impact on Life',
                     'Demographics', 'Medical History', 'Psychiatric History',
                     'Substance Use', 'Coping Mechanisms', 'Social Support',
                     'Lifestyle Factors']
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
