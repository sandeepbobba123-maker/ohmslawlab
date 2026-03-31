import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Ohm's Law Lab", layout="centered")

# Title
st.title("⚡ Ohm's Law Virtual Laboratory")

# ---------------- THEORY ----------------
st.header("📘 Theory")
st.write("""
Ohm’s Law states that current flowing through a conductor is directly proportional 
to the voltage across it, provided temperature remains constant.
""")

# ---------------- FORMULA ----------------
st.header("📐 Formula")
st.latex("V = I \\times R")

# ---------------- CALCULATOR ----------------
st.header("🧮 Calculator")

option = st.selectbox("Choose calculation",
                      ["Voltage (V)", "Current (I)", "Resistance (R)"])

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

# ---------------- GRAPH ----------------
st.header("📊 V-I Graph")

R_val = st.slider("Select Resistance", 1, 100, 10)

I_values = np.linspace(0, 10, 50)
V_values = R_val * I_values

fig, ax = plt.subplots()
ax.plot(I_values, V_values)
ax.set_xlabel("Current (I)")
ax.set_ylabel("Voltage (V)")
ax.set_title("Ohm's Law Graph")

st.pyplot(fig)

# ---------------- PROCEDURE ----------------
st.header("🧪 Procedure")
st.write("""
1. Select resistance value
2. Apply voltage
3. Measure current
4. Verify V = IR
""")

# ---------------- CONCLUSION ----------------
st.header("📌 Conclusion")
st.write("Voltage and Current are directly proportional. Graph is a straight line.")