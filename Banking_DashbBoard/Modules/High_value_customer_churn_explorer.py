import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots



# --- Load Data ---
path = r"C:\Users\piyus\Desktop\3 months Data Science Internship\Project 02 European Bank\JL\anaconda_projects\db\Banking DataSet\European_Bank.csv"
df = pd.read_csv(path)

# --- Feature Engineering ---
features = ['CreditScore', 'Tenure', 'Balance', 'NumOfProducts',
            'HasCrCard', 'IsActiveMember', 'EstimatedSalary']

for col in features:
    df[f'{col}_z'] = (df[col] - df[col].mean()) / df[col].std()

weights = {
    'CreditScore_z':     0.20,
    'Tenure_z':          0.10,
    'Balance_z':         0.30,
    'NumOfProducts_z':   0.20,
    'HasCrCard_z':       0.05,
    'IsActiveMember_z':  0.10,
    'EstimatedSalary_z': 0.05
}

df['Customer_Value_Score'] = sum(df[col] * w for col, w in weights.items())

df['CVS_0_100'] = (
    (df['Customer_Value_Score'] - df['Customer_Value_Score'].min()) /
    (df['Customer_Value_Score'].max() - df['Customer_Value_Score'].min())
) * 100

df['Value_Tier'] = pd.cut(df['CVS_0_100'],
    bins=[0, 25, 50, 75, 100],
    labels=['Low', 'Medium', 'High', 'Premium'])

# --- Summary Table ---
tiers = ['Low', 'Medium', 'High', 'Premium']

summary = (df.groupby(['Value_Tier', 'Exited'])
             .size()
             .unstack(fill_value=0)
             .rename(columns={0: 'Retained', 1: 'Churned'})
             .reindex(tiers))

summary['Total']            = summary.sum(axis=1)
summary['Churn Rate %']     = (summary['Churned'] / summary['Total'] * 100).round(1)
summary['Retention Rate %'] = (summary['Retained'] / summary['Total'] * 100).round(1)

# --- Streamlit UI ---


# --- Donut Chart: Churn proportion tier-wise vs Total Churn ---
total_churned = summary['Churned'].sum()

fig_donut = go.Figure(go.Pie(
    labels=tiers,
    values=summary['Churned'],
    hole=0.55,
    marker_colors=['#639922', '#BA7517', '#E24B4A', '#A32D2D'],
    textinfo='label+percent',
    hovertemplate='<b>%{label}</b><br>Churned: %{value}<br>Share: %{percent}<extra></extra>'
))

fig_donut.update_layout(
    title_text=f"Churn Distribution by Value Tier  (Total Churned: {total_churned})",
    height=450,
    annotations=[dict(
        text=f'<b>{total_churned}</b><br>Churned',
        x=0.5, y=0.5,
        font_size=16,
        showarrow=False
    )]
)


st.plotly_chart(fig_donut, use_container_width=True)


# --- Plotly Charts ---
import plotly.graph_objects as go

labels    = ['Low', 'Medium', 'High', 'Premium']
total     = [2748, 5755, 3590, 175]
churned   = [151, 1067, 723, 95]
retained  = [t - c for t, c in zip(total, churned)]

fig = go.Figure()

fig.add_trace(go.Bar(
    name='Retained',
    x=labels,
    y=retained,
    marker_color='#378ADD',
    text=[f"{r}<br>({r/t*100:.1f}%)" for r, t in zip(retained, total)],
    textposition='auto'
))

fig.add_trace(go.Bar(
    name='Churned',
    x=labels,
    y=churned,
    marker_color='#E24B4A',
    text=[f"{c}<br>({c/t*100:.1f}%)" for c, t in zip(churned, total)],
    textposition='auto'
))

fig.update_layout(
    barmode='group',
    title='Customer Value Tier — Churn Analysis',
    yaxis_title='Customer Count',
    height=500
)

st.plotly_chart(fig, use_container_width=True)