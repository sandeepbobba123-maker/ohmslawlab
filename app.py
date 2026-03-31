import streamlit as st
import numpy as np

# Page setup
st.set_page_config(page_title="Ohm's Law Lab", layout="centered")

# Title
st.title("⚡ Ohm's Law Virtual Laboratory")

# Theory
st.header("📘 Theory")
st.write("Ohm’s Law states that Voltage = Current × Resistance")

# Formula
st.header("📐 Formula")
st.latex("V = I \\times R")

# Calculator
st.header("🧮 Calculator")

option = st.selectbox(
    "Choose calculation",
    ["Voltage (V)", "Current (I)", "Resistance (R)"]
)

if option == "Voltage (V)":
    I = st.number_input("Current (I)", min_value=0.0)
    R = st.number_input("Resistance (R)", min_value=0.0)
    if st.button("Calculate Voltage"):
        st.success(f"Voltage = {I * R} Volts")

elif option == "Current (I)":
    V = st.number_input("Voltage (V)", min_value=0.0)
    R = st.number_input("Resistance (R)", min_value=0.1)
    if st.button("Calculate Current"):
        st.success(f"Current = {V / R} Amps")

elif option == "Resistance (R)":
    V = st.number_input("Voltage (V)", min_value=0.0)
    I = st.number_input("Current (I)", min_value=0.1)
    if st.button("Calculate Resistance"):
        st.success(f"Resistance = {V / I} Ohms")

# Graph (NO matplotlib)
st.header("📊 V-I Graph")

R_val = st.slider("Select Resistance", 1, 100, 10)

I_values = np.linspace(0, 10, 50)
V_values = R_val * I_values

# Simple built-in chart
st.line_chart(V_values)

# Procedure
st.header("🧪 Procedure")
st.write("""
1. Select resistance  
2. Apply voltage  
3. Measure current  
4. Verify V = IR  
""")

# Conclusion
st.header("📌 Conclusion")
st.write("Voltage and Current are directly proportional.")