import streamlit as st
import pickle
import pandas as pd
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Heart Disease Predictor")
# st.text("1 means you've a heart disease, 0 means you don't have a heart disease")
#Age
Age = st.number_input('Age of Person')
#Sex
Sex = st.selectbox('Sex',df['Sex'].unique())
#ChestPainType
ChestPainType = st.selectbox('Chest Pain Type',df['ChestPainType'].unique())
#RestingBP
RestingBP = st.number_input('Resting Blood Pressure')
#Cholesterol
Cholesterol = st.number_input('Serum Cholesterol')
#FastingBS
FastingBS = st.selectbox('Fasting Blood Sugar',[0,1])
#RestingECG
RestingECG = st.selectbox('Resting Electrocardiogram Results',df['RestingECG'].unique())
#MaxHR
MaxHR = st.number_input('Maximum Heart Rate Achieved')
#ExerciseAngina
ExerciseAngina = st.selectbox('Exercise Induced Angina',df['ExerciseAngina'].unique())
#Oldpeak
Oldpeak = weight = st.number_input('Old peak')
#ST_Slope
ST_Slope = st.selectbox('The slope of the peak exercise ST segment',df['ST_Slope'].unique())
if st.button('Predict Heart Health'):
    query = np.array([Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope])
    query = query.reshape(1, 11)
    result=str(pipe.predict(query)[0])
    if result == 1:
        st.header("You've a heart disease. Please, consult your doctor")
    else:
        st.header("You don't have a heart disease")
    # st.title("Your Heart Health is " + str(pipe.predict(query)[0]))
    # query = query.reshape(1, 11)
    # st.title("Your Heart Health Status is "+ str(int(pipe.predict(query)[0])))
    # st.header("Your Heart Health(1 means you've a disease) Status is:" + str(int(result[0])))



