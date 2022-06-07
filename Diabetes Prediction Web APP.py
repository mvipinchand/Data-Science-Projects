# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:57:31 2022

@author: mvipi
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/mvipi/Desktop/Machine Learning/Deploy ML Model/trained_model.sav', 'rb'))

#Creating a function for Prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
def main():
    
    st.title('Diabetes Prediction Web APP')
    
    Pregnancies = st.text_input('No of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BP')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI Level')
    DiabetesPedigreeFunction = st.text_input('Pedigree function')
    Age = st.text_input('Age')
    
    diagnosis = ''
    
    if st.button('Predicted Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    