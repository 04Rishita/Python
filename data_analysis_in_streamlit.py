import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Data Analysis")
st.subheader("Data Analysis using python and streamlit")
upload=st.file_uploader("Upload your file here in csv format")
if upload is not None:
    data=pd.read_csv(upload)

if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

if upload is not None:
   if st.checkbox("Datatype of each column", key="Datatypes"):
        st.subheader("Datatypes")
        st.write(data.dtypes)

if upload is not None:
    if st.checkbox("Shape of Dataset(No.of Rows and Columns)",key="Shape"):
        st.subheader("Shape of Dataset")
        st.write(data.shape)

if upload is not None:
    show_nulls = st.checkbox("Show Null Values Heatmap", key="null_check")

    if show_nulls:
        if data.isnull().values.any():
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull(), ax=ax)
            st.pyplot(fig)
        else:
            st.success("No null values are there in your dataset ✅")
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset contains some duplicate values")
        dup=st.selectbox("Do you want to remove duplicates?",("select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate values are removed")
        else:
            st.text("OK! No problem")
if upload is not None:
    st.checkbox("Summary of Dataset")
    st.write(data.describe(include='all'))

with st.expander("📘 About This App"):
    st.write("""
    ### 📊 Data Analysis using Python & Streamlit

    This application allows users to perform **basic exploratory data analysis (EDA)**
    on any CSV dataset without writing code.

    #### 🚀 Features:
    - Upload CSV files easily
    - Preview dataset (Head & Tail)
    - View column datatypes
    - Check dataset shape (rows & columns)
    - Visualize missing values using a heatmap
    - Detect and remove duplicate records
    - Generate statistical summary of the dataset

    #### 🛠 Technologies Used:
    - Python
    - Pandas (Data manipulation)
    - Seaborn & Matplotlib (Visualization)
    - Streamlit (Web application)

    #### 🎯 Use Case:
    This app is useful for **students, beginners, and data analysts**
    to quickly understand and clean datasets before advanced analysis or modeling.
    """)
if st.checkbox("Byee"):
    st.success("See you soon!")