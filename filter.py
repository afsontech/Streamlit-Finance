import streamlit as st
import pandas as pd
import plotly.express as px

# Set up
st.set_page_config(page_title="🧮 Employee Filter Dashboard", layout="wide")
st.title("🧮 Dynamic Filtering of Employee Data")

# File upload
uploaded_file = st.file_uploader("Upload your employee CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Clean column names

    st.subheader("📋 Data Preview")
    st.dataframe(df, use_container_width=True)

    # 🎯 Filters
    st.sidebar.header("🔎 Filter Options")

    # Filter by Department
    departments = st.sidebar.multiselect("Select Departments", options=df["Department"].unique(), default=df["Department"].unique())

    # Filter by Job Role
    jobs = st.sidebar.multiselect("Select Job Titles", options=df["Job"].unique(), default=df["Job"].unique())

    # Filter by Salary Range
    min_salary = int(df["Salary"].min())
    max_salary = int(df["Salary"].max())
    salary_range = st.sidebar.slider("Select Salary Range", min_value=min_salary, max_value=max_salary, value=(min_salary, max_salary))

    # 🧮 Apply filters
    filtered_df = df[
        (df["Department"].isin(departments)) &
        (df["Job"].isin(jobs)) &
        (df["Salary"] >= salary_range[0]) &
        (df["Salary"] <= salary_range[1])
    ]

    # Show filtered data
    st.subheader(f"🔍 Filtered Results: {len(filtered_df)} records")
    st.dataframe(filtered_df, use_container_width=True)

    # 📊 Salary Visualization
    st.subheader("📊 Salary by Job Role (Filtered)")
    fig = px.bar(filtered_df, x="Job", y="Salary", color="Job", text="Salary")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("⬅️ Please upload a file to get started.")
