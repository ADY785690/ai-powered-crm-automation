import streamlit as st
import pandas as pd

st.title("AI-Powered CRM Automation System")

df = pd.read_csv("data/customers.csv")

st.subheader("Customer Database")
st.dataframe(df)

st.subheader("Add New Customer")

name = st.text_input("Customer Name")
email = st.text_input("Email")

if st.button("Add Customer"):
    st.success(f"{name} added successfully!")

st.subheader("Lead Analytics")

hot = len(df[df["Status"]=="Hot"])
warm = len(df[df["Status"]=="Warm"])
cold = len(df[df["Status"]=="Cold"])

st.write(f"Hot Leads: {hot}")
st.write(f"Warm Leads: {warm}")
st.write(f"Cold Leads: {cold}")

st.bar_chart(df["LeadScore"])
