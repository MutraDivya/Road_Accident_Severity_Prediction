import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title = "Road Accident Severity Prediction",
    page_icon = "🤕", layout = "wide"
)

model = joblib.load("model.joblib")
st.title("🤕 Road Accident Severity Prediction")
st.divider()


col1, col2 = st.columns(2)
with col1:
    st.subheader("Road & Accident Details")
    Weather_Condition = st.selectbox(
        "Weather Condition",['Clear', 'Rain', 'Fog', 'Snow', 'Storm']
    )

    Road_Surface_Condition = st.selectbox(
        "Road Surface Condition",['Dry', 'Wet', 'Snow', 'Icy']
    )

    Light_Condition = st.selectbox(
        "Light Condition",['Daylight', 'Darkness', 'Dawn', 'Dusk'] 
    )

    Road_Type = st.selectbox(
        "Road Type",['Highway', 'Urban Road', 'Rural Road', 'Residential Road']
    )

    Junction_Type = st.selectbox(
        "Junction Type",['No Junction', 'T Junction', 'Crossroad', 'Roundabout']
    )

    Area_Type = st.selectbox(
        "Area Type",['Urban', 'Rural']
    )

    Traffic_Level = st.selectbox(
        "Traffic Level",['Low', 'Medium', 'High']
    )

    Vehicle_Type = st.selectbox(
        "Vehicle Type",['Car', 'Bike', 'Bus', 'Truck', 'Other']
    )

with col2:
    st.subheader("Driver & Other Details")
    Speed_Limit = st.number_input(
        "Speed Limit",min_value=0,value=50,step=5
    )

    Number_of_Vehicles = st.number_input(
        "Number of Vehicles",min_value=1,value=2
    )

    Number_of_Casualties = st.number_input(
        "Number of Casualties",min_value=0,value=1
    )

    Driver_Age = st.number_input(
        "Driver Age",min_value=18,value=30,step=1
    )

    Driver_Experience_Years = st.number_input(
        "Driver Experience (Years)",min_value=0,value=5,step=1
    )

    Visibility_km = st.number_input(
        "Visibility (km)",min_value=0.0,value=5.0,step=2.0
    )

    Time_of_Day = st.selectbox(
        "Time of Day",['Morning','Afternoon','Evening','Night']
    )

    Day_of_Week = st.selectbox(
        "Day of week",['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    )

st.divider()
if st.button("🔍Predict Accident Severity", use_container_width=True):
    data = pd.DataFrame([{
        "Weather_Condition": Weather_Condition,
        "Road_Surface_Condition": Road_Surface_Condition,
        "Light_Condition": Light_Condition,
        "Road_Type":Road_Type,
        "Junction_Type":Junction_Type,
        "Area_Type": Area_Type,
        "Traffic_Level": Traffic_Level,
        "Vehicle_Type": Vehicle_Type,
        "Speed_Limit": Speed_Limit,
        "Number_of_Vehicles": Number_of_Vehicles,
        "Number_of_Casualties": Number_of_Casualties,
        "Driver_Age": Driver_Age,
        "Driver_Experience_Years": Driver_Experience_Years,
        "Visibility_km": Visibility_km,
        "Time_of_Day": Time_of_Day,
        "Day_of_Week": Day_of_Week
    }])

    data = pd.get_dummies(data)

    data = data.reindex(columns=model.feature_names_in_,fill_value=0)
    prediction = model.predict(data)
    severity = str(prediction[0])

    if severity.lower() in ['high','serious']:
        st.markdown(
            f"""
            <div style="
                background-color: #ffcccc;
                color: #cc0000;
                padding: 25px;
                border-radius: 12px;
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                margin-top: 20px;
                border: 2px solid #cc0000;
            ">
                ⚠️ Accident Severity: {severity}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                background-color: #ccffcc;
                color: #008000;
                padding: 25px;
                border-radius: 12px;
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                margin-top: 20px;
                border: 2px solid #008000;
            ">
                ✔️ Accident Severity: {severity}
            </div>
            """,
            unsafe_allow_html=True
        )

