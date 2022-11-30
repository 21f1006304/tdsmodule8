import streamlit as st
#import pandas as pd
#from sklearn import datasets
#from sklearn.ensemble import RandomForestClassifier
#import pickle
st.write("""
# credit card default prediction
this app do something
""")
st.header('user input parameters')
def user_input_features():
  number1 = st.number_input("NUMBER1",min_value=0.,max_value=100.0)
  number2 = st.number_input("NUMBER2",min_value=0.,max_value=100.0)
  data = {'NUMBER1': number1,
      'NUMBER2': number2
  }
  return number1 + number2

df = user_input_features()
st.subheader("This is subheader")
st.write(df)
