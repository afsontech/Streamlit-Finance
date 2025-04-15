import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded"
)

st.title("📁 Upload and Preview Your Data")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.dataframe(df, use_container_width=True)

    st.subheader("💼 Salary by Department")
    fig1 = px.bar(df, x="Department", y="Salary", color="Department", text="Salary")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("👔 Salary by Job Title")
    fig2 = px.bar(df, x="Job", y="Salary", color="Job", text="Salary")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📊 Department Distribution")
    dept_counts = df["Department"].value_counts().reset_index()
    dept_counts.columns = ["Department", "Count"]
    fig3 = px.pie(dept_counts, values="Count", names="Department", hole=0.14)
    st.plotly_chart(fig3, use_container_width=True)


st.sidebar.title("📊 Personal Finance App")
section= st.sidebar.radio(
    "navigate to:",
    ["Overview"]
)
if section == "Overview":
    st.subheader("📈 Dashboard Summary")
    st.write("Show income/expenses, recent activity, key metrics here.")

if section == "Goals":
    st.subheader("🎯 Savings & Debt Goals")
    st.write("Track progress toward financial goals.")

elif section == "Insights":
    st.subheader("🔍 Smart Spending Insights")
    st.write("Categorized analysis, recommendations, AI tips, etc.")

