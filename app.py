import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image
model=pickle.load(open('model.pkl','rb'))


#app=Flask(__name__)
#Swagger(app)

#@app.route('/')
def welcome():
    return "Welcome All"

def predict_note_authentication( Wind_speed_in_m_s , Wind_direction ):
    input=np.array([[Wind_speed_in_m_s, Wind_direction]]).astype(np.float64)
    
    prediction=model.predict(input)
    print((prediction))
    return(prediction)

def main():
    st.title("Wind Energy Prediction")
    html_temp = """
    <div style="background-color:#33E0FF;padding:10px">
    <h2 style="color:white;text-align:center;">Wind Energy Prediction ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Wind_speed_in_m_s=st.text_input("Wind speed | (m/s)","Type Here")
    Wind_direction=st.text_input("Wind direction | (deg)","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Wind_speed_in_m_s , Wind_direction )
        st.success('The expected wind energy output in kw is: {}'.format(result))


if __name__=='__main__':
    main()