# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 07:22:47 2022

@author: mvipi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Loading the saved models
diabetes_model = pickle.load(open('C:/Users/mvipi/Desktop/MS_application_DS_proj/Diabetes_prediction/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/mvipi/Desktop/MS_application_DS_proj/Heart_diease_prediction/Heart_disease.sav', 'rb'))

parkinson_disease_model = pickle.load(open('C:/Users/mvipi/Desktop/MS_application_DS_proj/Parkinsons_prediction/parkinsons_model.sav', 'rb'))

#Creating sidebars in UI
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', ['Diabetes Prediction', 
                                                                  'Heart Disease Prediction',
                                                                  'Parkinsons Disease Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
    
    
#Diabetes Prediction Page
if (selected == 'Diabetes Prediction' ):
    
    st.title('Diabetes Prediction using ML')  #Page Title
    
    #Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('No of Pregnancies')
    with col2:    
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('BP')
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    with col2:
        Insulin = st.text_input('Insulin')
    with col3:
        BMI = st.text_input('BMI Level')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Pedigree function')
    with col2:
        Age = st.text_input('Age')
    
    diab_diagnosis = ''
    
    #creating a button
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                                  Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0]==1):
            diab_diagnosis='Person IS Diabetic'
        else:
            diab_diagnosis='Person IS NOT Diabetic'
    
    st.success(diab_diagnosis)
    
    
#Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction' ):
    st.title('Heart Disease Prediction using ML') 
    
    #Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:    
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum cholestrol in mg/dL')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120mg/dL')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
         exang = st.text_input('Exercise induced angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by excercise')
    with col2:    
        slope = st.text_input('Slope of peak excercise ST segment')
    with col3:
        ca = st.text_input('ca')
    with col1:
        thal = st.text_input('thal')
    
    heart_diagnosis = ''
    
    #creating a button
    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age,
sex,
cp,
trestbps,
chol,
fbs,
restecg,
thalach,
exang,
oldpeak,
slope,
ca,
thal]])
        if (heart_prediction[0]==1):
            heart_diagnosis='Person IS Diabetic'
        else:
            heart_diagnosis='Person IS NOT Diabetic'
    
    st.success(heart_diagnosis)
    
#Parkinsons Disease Prediction Page
if (selected == 'Parkinsons Disease Prediction' ):
    st.title('Parkinsons Disease Prediction using ML')  
    
    #Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        one = st.text_input('MDVP:Fo(Hz)')
    with col2:    
        two = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        three = st.text_input('MDVP:Flo(Hz)')
    with col1:
        four = st.text_input('MDVP:Jitter(%)')
    with col2:
        five = st.text_input('MDVP:RAP')
    with col3:
        six = st.text_input('MDVP:PPQ')
    with col1:
        seven = st.text_input('Jitter:DDP')
    with col2:
        eight = st.text_input('MDVP:Shimmer')
    with col3:
         nine = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        ten = st.text_input('Shimmer:APQ3')
    with col2:    
        eleven = st.text_input('Shimmer:APQ5')
    with col3:
        twelve = st.text_input('MDVP:APQ')
    with col1:
        thirteen = st.text_input('Shimmer:DDA')
    with col2:    
        fourteen = st.text_input('NHR')
    with col3:
        fifteen = st.text_input('HNR')
    with col1:
        sixteen = st.text_input('RPDE')
    with col2:    
        seventeen = st.text_input('DFA')
    with col3:
        eighteen = st.text_input('spread1')
    with col1:
        nineteen = st.text_input('spread2')
    with col2:    
        twenty = st.text_input('D2')
    with col3:
        twentyone = st.text_input('PPE')
    
    parkinson_diagnosis = ''
    
    #creating a button
    if st.button('Parkinson Test Result'):
        parkinson_prediction = parkinson_disease_model.predict([[one,
        two,
        three, 
        four, 
        five ,
        six ,
        seven, 
        eight ,
         nine ,
        ten ,
        eleven,
        twelve,
        thirteen, 
        fourteen ,
        fifteen ,
        sixteen ,
        seventeen, 
        eighteen,
        nineteen,
        twenty ,
        twentyone]])
        if (parkinson_prediction[0]==1):
            parkinson_diagnosis='Person IS Diabetic'
        else:
            parkinson_diagnosis='Person IS NOT Diabetic'
    
    st.success(parkinson_diagnosis)