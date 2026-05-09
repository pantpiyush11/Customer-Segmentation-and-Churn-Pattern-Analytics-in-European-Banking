import pandas as pd
import streamlit as st
import plotly.graph_objects as go

path = r"C:\Users\piyus\Desktop\3 months Data Science Internship\Project 02 European Bank\JL\anaconda_projects\db\Banking DataSet\European_Bank.csv"
df = pd.read_csv(path)

# country wise churn count
country_churn = df[df["Exited"] == 1].groupby("Geography")["Exited"].count().reset_index()
country_churn.columns = ["Country", "Churned"]

fig = go.Figure(data=[go.Pie(
    labels=country_churn["Country"],
    values=country_churn["Churned"],
    hole=0.6,
    marker=dict(
        colors=["#378ADD", "#E24B4A", "#1D9E75"],
        line=dict(color="#1a1a1a", width=1.5)
    ),
    textinfo="label+percent+value",
    textfont=dict(size=15, color="white"),
    textposition="outside",
    hovertemplate="%{label}<br>%{value:,} churned<br>%{percent} of total churn<extra></extra>"
)])

fig.update_layout(
    title="Country-wise Churn vs Total Churn",
    paper_bgcolor="rgba(0,0,0,0)",                          # ← little more height for outside labels
    height=450,
    margin=dict(t=60, b=60, l=60, r=60)
)

col1,col2= st.columns(2)

with col1:
    st.plotly_chart(fig, use_container_width=True)   # donut chart

with col2:
      
    country = st.selectbox("Select Country", ["France", "Germany", "Spain"])

    filtered = df[df["Geography"] == country]

    churned  = filtered[filtered["Exited"] == 1].shape[0]
    retained = filtered[filtered["Exited"] == 0].shape[0]
    total    = len(filtered)

    labels = ["Total", "Churned", "Retained"]
    values = [total, churned, retained]
    colors = ["#F72585", "#4CC9F0", "#FFBE0B"]
    pcts   = [100.0, round(churned/total*100,1), round(retained/total*100,1)]

    fig_bar = go.Figure(data=[go.Bar(
        x=labels,
        y=values,
        marker_color=colors,
        text=[f"{v:,} ({p}%)" for v, p in zip(values, pcts)],
        textposition="outside",
        textfont=dict(size=13)
    )])

    fig_bar.update_layout(
        title=f"Population Breakdown — {country}",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Customers",
        yaxis_range=[0, max(values) * 1.2],
        height=450
    )
    st.plotly_chart(fig_bar, use_container_width=True)
        




