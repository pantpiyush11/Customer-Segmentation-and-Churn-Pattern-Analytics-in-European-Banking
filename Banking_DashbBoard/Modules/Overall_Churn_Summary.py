import pandas as pd


path=r"C:\Users\piyus\Desktop\3 months Data Science Internship\Project 02 European Bank\JL\anaconda_projects\db\Banking DataSet\European_Bank.csv"
df=pd.read_csv(path)
print("Loaded Dataset sucessfully!")



import streamlit as st
import plotly.graph_objects as go

total = len(df)
churned = df[df["Exited"] == 1].shape[0]
retained = df[df["Exited"] == 0].shape[0]
churn_pct = (churned / total) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total:,}")
col2.metric("Total Churned", f"{churned:,}")
col3.metric("Churn %", f"{churn_pct:.1f}%")
col4.metric("Retained", f"{retained:,}")




labels = ["Churned Customers","Retained Cusomers" ]
values = [df[df["Exited"]==1].shape[0],df[df["Exited"]==0].shape[0]]
colors = ["#E24B4A","#1D9E75"]

fig = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    hole=0.6,                    # donut style
    marker=dict(colors=colors, line=dict(color="#1a1a1a", width=1.5)),
    textinfo="label+percent",
    hovertemplate="%{label}<br>%{value:,} customers<br>%{percent}<extra></extra>"
)])

fig.update_layout(
    title_text="Pie Plot of Overall Churn Summary",
    title_font_size=20,
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.2),
    margin=dict(t=60, b=60, l=20, r=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)


st.plotly_chart(fig, use_container_width=True)

