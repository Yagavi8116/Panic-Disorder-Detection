# Panic-Disorder-Detection

The aim of this project is to create and provide an easier way of self-diagnosing Panic Disorders using Machine Learning. The application is deployed in Flask and interaction with the project is made easy through web pages.

## Sci-kit Version 
We have used Sci-Kit version 1.2.2 for both training the data and deploying the websites. This was done because varying versions in the training phase and the deploying environment might cause errors during the latter

```bash
pip install sci-kit==1.2.2
```

## Using the Project

[Project Folder](https://github.com/Yagavi8116/Panic-Disorder-Detection/tree/main/5.%20Project%20Executable%20Files)

### Dataset
-The dataset consists of 20,000 entries with 17 columns, which includes demographic details, medical and psychiatric history, current stressors, symptoms, and coping mechanisms. these features are mainly aimed at identifying factors related to panic disorder diagnosis. 

-The link to access the dataset is the following:- [muhammadshahidazeem/panic-disorder-detection-dataset](https://www.kaggle.com/datasets/muhammadshahidazeem/panic-disorder-detection-dataset)

### Training the model
1. Launch the file *[Panic_Disorder_Detection_Notebook.ipynb](https://github.com/Yagavi8116/Panic-Disorder-Detection/blob/main/5.%20Project%20Executable%20Files/Panic_Disorder_Detection_Notebook.ipynb)* in Jupyter Notebook.
2. Ensure that the datasets, i.e *panic_disorder_dataset_testing.csv* and *panic_disorder_dataset_training.csv* are in same folder and loaded properly.
3. Run all the cells in a serial manner. This will lead to proper building and training of the model.
4. Running the cells upto:
```
pkl.dump(dtf, open('dtf.pkl','wb'))
```
   saves a file named 'dtf.pkl' on your device.

### Website
-The wesbite uses Flask for its deployment


-The website enables the user to choose the options from the choices provided in the dropdown or radio/check boxes and, on the basis of the user's input, provides the output stating that either the user is normal or the user might have panic disorder.

### Website Deployment
-Make sure that the file 'dtf.pkl' is present in the chosen directory, same folder as in *app.py*.


-Run the following in terminal:
```
python app.py
```
to run the application.

### Screenshots

<img width="1280" alt="image" src="https://github.com/user-attachments/assets/053778eb-dd43-4ca3-91b1-86b49061e963">
<img width="1280" alt="image" src="https://github.com/user-attachments/assets/4fdfc4a9-fc69-4d47-9838-5101d97577d4">
<img width="1280" alt="image" src="https://github.com/user-attachments/assets/52198131-a450-4598-8c26-9551ffe29d91">


TeamID: SWTID1720075414

---

Team Members:

1. Yagavi K

2. Shakthi Shamruth Dhamotharan

3. Komanduru Adithya Vyas

4. Kavuru Sai Abhijit Prasant

---

[Panic Disorder Detection Demo Video Link](https://drive.google.com/file/d/1C1nRRoOADrPTnIk-iY1yYQAUr19wXo1t/view)
