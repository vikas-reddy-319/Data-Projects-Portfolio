import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import time
import joblib

model_file = 'rf_model.joblib'
model = joblib.load(model_file)

st.set_page_config(page_title="Used_Car", page_icon=":tada:", layout="wide")

# Assuming you have the mappings stored in a dictionary
mappings = {
    'manufacturer': {'ford': 0, 'honda': 1, 'dodge': 2, 'chrysler': 3, 'toyota': 4, 'chevrolet': 5, 'jeep': 6, 'lexus': 7, 'bmw': 8, 'gmc': 9, 'mercedes-benz': 10, 'mazda': 11, 'rover': 12, 'ram': 13, 'nissan': 14, 'ferrari': 15, 'audi': 16, 'mitsubishi': 17, 'infiniti': 18, 'volkswagen': 19, 'kia': 20, 'hyundai': 21, 'fiat': 22, 'acura': 23, 'cadillac': 24, 'lincoln': 25, 'jaguar': 26, 'saturn': 27, 'volvo': 28, 'alfa-romeo': 29, 'buick': 30, 'subaru': 31, 'mini': 32, 'pontiac': 33, 'porsche': 34, 'harley-davidson': 35, 'tesla': 36, 'mercury': 37, 'datsun': 38, 'land rover': 39, 'aston-martin': 40},
    'condition': {'excellent': 0, 'good': 1, 'like new': 2, 'new': 3, 'fair': 4, 'salvage': 5},
    'cylinders': {'6 cylinders': 0, '8 cylinders': 1, '4 cylinders': 2, '5 cylinders': 3, '10 cylinders': 4, '3 cylinders': 5, 'other': 6, '12 cylinders': 7},
    'fuel': {'gas': 0, 'diesel': 1, 'hybrid': 2, 'electric': 3, 'other': 4},
    'transmission': {'automatic': 0, 'manual': 1, 'other': 2},
    'drive': {'rwd': 0, '4wd': 1, 'fwd': 2},
    'size': {'full-size': 0, 'mid-size': 1, 'compact': 2, 'sub-compact': 3},
    'type': {'truck': 0, 'pickup': 1, 'mini-van': 2, 'sedan': 3, 'offroad': 4, 'van': 5, 'SUV': 6, 'convertible': 7, 'coupe': 8, 'hatchback': 9, 'wagon': 10, 'other': 11, 'bus': 12},
    'paint_color': {'black': 0, 'blue': 1, 'silver': 2, 'white': 3, 'grey': 4, 'yellow': 5, 'red': 6, 'green': 7, 'brown': 8, 'custom': 9, 'purple': 10, 'orange': 11},
    'state': {'al': 0, 'ak': 1, 'az': 2, 'ar': 3, 'ca': 4, 'co': 5, 'ct': 6, 'dc': 7, 'de': 8, 'fl': 9, 'ga': 10, 'hi': 11, 'id': 12, 'il': 13, 'in': 14, 'ia': 15, 'ks': 16, 'ky': 17, 'la': 18, 'me': 19, 'md': 20, 'ma': 21, 'mi': 22, 'mn': 23, 'ms': 24, 'mo': 25, 'mt': 26, 'nc': 27, 'ne': 28, 'nv': 29, 'nj': 30, 'nm': 31, 'ny': 32, 'nh': 33, 'nd': 34, 'oh': 35, 'ok': 36, 'or': 37, 'pa': 38, 'ri': 39, 'sc': 40, 'sd': 41, 'tn': 42, 'tx': 43, 'ut': 44, 'vt': 45, 'va': 46, 'wa': 47, 'wv': 48, 'wi': 49, 'wy': 50}
}

def main(): 
    # Add a colorful background
    st.markdown(
        """
        <style>
        body {
            background-image: url("background_image.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Used Car Price Prediction")
    st.markdown("**Welcome to our Used Car Price Prediction App!**")

    # Add an interactive plot
    if st.checkbox("Show Scatter Plot"):
        sns.scatterplot(x="Odometer", y="Price", data=df)
        plt.title("Odometer vs Price")
        plt.xlabel("Odometer Reading")
        plt.ylabel("Price")
        st.pyplot(plt)

    # Add an interactive widget
    if st.button("Click me!"):
        st.success("Button Clicked!")

    # Add an animation
    st.text("Loading...")
    with st.spinner("Wait for it..."):
        time.sleep(5)
    st.success("Done!")
   
    st.markdown("##### Are you planning to buy a used car !?\n##### So let's try evaluating the price..")
    
    st.write('')
    st.write('')
    s1 = st.selectbox('What is the manufacturer of the car ?', list(mappings['manufacturer'].keys()))
    p1 = mappings['manufacturer'][s1]
    
    s2 = st.selectbox('What is the condition of the car ?', list(mappings['condition'].keys()))
    p2 = mappings['condition'][s2]
    
    s3 = st.selectbox('What is the number of cylinders in the car ?', list(mappings['cylinders'].keys()))
    p3 = mappings['cylinders'][s3]
    
    s4 = st.selectbox('What is the fuel type of the car ?', list(mappings['fuel'].keys()))
    p4 = mappings['fuel'][s4]

    # New input element for odometer reading
    p5 = st.slider('What is the odometer reading of the car?(Multiple of 5k)', 1, 50, step=2)   
    
    s5 = st.selectbox('What is the Transmission Type ?', list(mappings['transmission'].keys()))
    p6 = mappings['transmission'][s5]
    
    s6 = st.selectbox('What is the drive type of the car ?', list(mappings['drive'].keys()))
    p7 = mappings['drive'][s6]
    
    s7 = st.selectbox('What is the size of the car ?', list(mappings['size'].keys()))
    p8 = mappings['size'][s7]
    
    s8 = st.selectbox('What is the type of the car ?', list(mappings['type'].keys()))
    p9 = mappings['type'][s8]
    
    s9 = st.selectbox('What is the paint color of the car ?', list(mappings['paint_color'].keys()))
    p10 = mappings['paint_color'][s9]
    
    s10 = st.selectbox('What is the state of the car ?', list(mappings['state'].keys()))
    p11 = mappings['state'][s10]

    # Use the existing column for the age of the car
    p12 = st.number_input('What is the age of the car?', min_value=1, max_value=30, value=5, step=1)
    
    data_new = pd.DataFrame({
    'Manufacturer':p1,
    'Condition':p2,
    'Cylinders':p3,
    'Fuel_Type':p4,
    'Odometer':p5,
    'Transmission':p6,
    'Drive':p7,
    'Size':p8,
    'Type':p9,
    'Paint_Color':p10,
    'State':p11,
    'Age_of_Car':p12
},index=[0])
    try: 
        if st.button('Predict'):
            prediction = model.predict(data_new)
            if prediction>0:
                st.balloons()
                st.success('You can buy the car for {:.2f} Dollars'.format(prediction[0]))
            else:
                st.warning("You will be not able to sell this car !!")
    except:
        st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    main()
