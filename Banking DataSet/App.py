# Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go

path=r"C:\Users\piyus\Desktop\Desk Top\02-04-2026 Mess to sort out\Project 02 European Bank\European_Bank.csv"
df=pd.read_csv(path)
print("Loaded Dataset sucessfully!")

Exited_map= {1:"Yes", 0:"No"}
df["Exited"]=df["Exited"].map(Exited_map)
df["Exited"].str.upper()

Exited_map= {1:"Yes", 0:"No"}
df["Has Credit C"]=df["Has Credit C"].map(Exited_map)
df["Exited"].str.upper()

# Setting Page info
st.set_page_config(
    page_title="Churn Dashboard",
    page_icon="📊",
    layout="wide",              # "centered" or "wide"
    initial_sidebar_state="expanded"
)
col1,col2=st.columns(
    spec=[1, 8],      # column width ratio
    gap="small",     # spacing between columns
    vertical_alignment="center"  # vertical alignment
)

with col1:
    path_1=r"C:\Users\piyus\Desktop\White Logo-dfhj5sER.png"
    st.image(path_1, width=100)
    path_2=r"C:\Users\piyus\Desktop\Logo_European_Central_Bank.svg.png"
    st.image(path_2, width=100)

with col2:
    st.title("📊 Customer Churn Analysis DashBoard")
    st.markdown(">Customer Segmentation & Churn Pattern Analytics in European Banking in association with Unified Mentor Pvt Ltd and European Central Bank")
    
st.sidebar.write("lorem ipsum")
Geography=st.sidebar.multiselect(
    "Select your Geographical Region",
    options=df["Geography"].unique(),
)

Exited=st.sidebar.multiselect(
    "Customers who Exited: Yes or No",
    options=df["Exited"].unique(),
)

Gender=st.sidebar.multiselect(
    "Select your Gender Region",
    options=df["Gender"].unique(),
)
Has_Credit_Card=st.sidebar.multiselect(
    "Select your Has Credit Card Region",
    options=df["Has Credit Card"].unique(),
)
Is_Active_Member=st.sidebar.multiselect(
    "Active members or pa",
    options=df["Is Active Member"].unique(),
)
tab1, tab2, tab3,  = st.tabs(["Overview", "Churn Analysis", "Customer Segments"])

with tab1:
    st.write("Overview content")

with tab2:
    st.write("Churn charts")

with tab3:
    st.write("Segmentation data")




