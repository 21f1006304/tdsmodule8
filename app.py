import streamlit as st
st.write("""
# App to do subtraction
This will display the absolute value of subtraction of two numbers
""")
st.header('user input parameters')
def user_input_features():
  number1 = st.number_input("NUMBER1",min_value=0.)
  number2 = st.number_input("NUMBER2",min_value=0.)
  data = {'NUMBER1': number1,
      'NUMBER2': number2
  }
  if (number1 > number2) :
    return number1 - number2
  elif (number2 > number1) :
    number2 - number1
  else :
    return 0

df = user_input_features()
st.subheader("Result:")
st.write(df)
