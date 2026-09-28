import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="NICU Clinical Monitoring Dashboard",
    page_icon="👶",
    layout="wide"
)

st.title("👶 NICU Clinical Monitoring Dashboard")
st.caption("Educational prototype using synthetic neonatal monitoring data.")

# Load sample data
data = pd.read_csv("sample_data.csv")

# Patient selection
patient = st.selectbox(
    "Select Patient",
    data["Patient_ID"].unique()
)

patient_data = data[data["Patient_ID"] == patient].copy()

# Latest observations
latest = patient_data.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

col1.metric("❤️ Heart Rate", f"{latest['Heart_Rate']} bpm")
col2.metric("🫁 Respiratory Rate", f"{latest['Respiratory_Rate']} /min")
col3.metric("🩸 SpO₂", f"{latest['SpO2']} %")
col4.metric("🌡️ Temperature", f"{latest['Temperature']} °C")

st.divider()

# Vital-sign trends
st.subheader("📈 Vital Sign Trends")

tab1, tab2, tab3 = st.tabs([
    "Heart Rate",
    "SpO₂",
    "Temperature"
])

with tab1:
    fig = px.line(
        patient_data,
        x="Time",
        y="Heart_Rate",
        markers=True,
        title="Heart Rate Trend"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.line(
        patient_data,
        x="Time",
        y="SpO2",
        markers=True,
        title="SpO₂ Trend"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    fig = px.line(
        patient_data,
        x="Time",
        y="Temperature",
        markers=True,
        title="Temperature Trend"
    )
    st.plotly_chart(fig, use_container_width=True)

# Intake and output
st.subheader("💧 Intake & Output")

io_col1, io_col2 = st.columns(2)

io_col1.metric(
    "Total Intake",
    f"{patient_data['Intake_ml'].sum()} mL"
)

io_col2.metric(
    "Total Output",
    f"{patient_data['Output_ml'].sum()} mL"
)

st.subheader("📋 Monitoring Data")

st.dataframe(
    patient_data,
    use_container_width=True,
    hide_index=True
)

st.info(
    "⚠️ This is an educational software prototype using synthetic data. "
    "It is not intended for diagnosis, treatment, or clinical decision-making."
)
