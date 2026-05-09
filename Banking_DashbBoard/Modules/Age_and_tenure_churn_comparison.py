import pandas as pd
import streamlit as st
import plotly.graph_objects as go


path = r"C:\Users\piyus\Desktop\3 months Data Science Internship\Project 02 European Bank\JL\anaconda_projects\db\Banking DataSet\European_Bank.csv"
df = pd.read_csv(path)

col1,col2=st.columns([2,3])
with col1:
    below_30        = df[(df["Age"] < 30)&(df["Exited"]==1)]
    above_30_to_45  = df[(df["Age"] >= 30) & (df["Age"] <= 45)&(df["Exited"]==1)]
    above_46_to_60  = df[(df["Age"] >= 46) & (df["Age"] <= 60)&(df["Exited"]==1)]
    above_60        = df[(df["Age"] > 60)&(df["Exited"]==1)]

    labels     = ["< 30 Yrs", "30–45 Yrs", "46–60 Yrs", "60+ Yrs"]
    population = [below_30.shape[0], above_30_to_45.shape[0],
                above_46_to_60.shape[0], above_60.shape[0]]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=population,
        hole=0.55,
        marker=dict(
            colors=["#F72585", "#4CC9F0", "#FFBE0B", "#9B5DE5"],
            line=dict(color="#111111", width=2)
        ),
        textinfo="label+percent+value",
        textfont=dict(size=14, color="white"),
        textposition="outside",
        hovertemplate="%{label}<br>%{value:,} customers<br>%{percent}<extra></extra>"
    )])

    fig.update_layout(
        title="Customer Age-wise population Distribution",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=60, b=60, l=60, r=60),
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    age_segment = st.selectbox("Select Age Segment", 
    ["< 30 Yrs", "30–45 Yrs", "46–60 Yrs", "60+ Yrs"], 
    key="age_seg")

    # filter by segment
    if age_segment == "< 30 Yrs":
        seg_df = df[df["Age"] < 30]
    elif age_segment == "30–45 Yrs":
        seg_df = df[(df["Age"] >= 30) & (df["Age"] <= 45)]
    elif age_segment == "46–60 Yrs":
        seg_df = df[(df["Age"] >= 46) & (df["Age"] <= 60)]
    else:
        seg_df = df[df["Age"] > 60]

    total    = len(seg_df)
    churned  = seg_df[seg_df["Exited"] == 1].shape[0]
    retained = seg_df[seg_df["Exited"] == 0].shape[0]

    values = [total, churned, retained]
    labels = ["Total", "Churned", "Retained"]
    colors = ["#4CC9F0", "#F72585", "#9B5DE5"]
    pcts   = [100.0, round(churned/total*100,1), round(retained/total*100,1)]

    fig_bar = go.Figure(data=[go.Bar(
        x=labels,
        y=values,
        marker_color=colors,
        text=[f"{v:,} ({p}%)" for v, p in zip(values, pcts)],
        textposition="outside",
        textfont=dict(size=14, color="white")
    )])

    fig_bar.update_layout(
        title=f"Churn Breakdown — {age_segment}",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Customers",
        yaxis_range=[0, max(values) * 1.2],
        height=420
    )

    st.plotly_chart(fig_bar, use_container_width=True)

#*******************************************************************************************



# ── Display side by side ──────────────────────────────────────────────────────


    
with col2:
        # ── Segments ──────────────────────────────────────────────────────────────────
    New_T      = df[df["Tenure"] <= 3]
    Mid_Term_T = df[(df["Tenure"] > 3) & (df["Tenure"] <= 8)]
    Long_Term_T= df[(df["Tenure"] > 8) & (df["Tenure"] <= 10)]

    labels     = ["New (0–3 Yrs)", "Mid-Term (4–8 Yrs)", "Long-Term (9–10 Yrs)"]
    population = [New_T.shape[0], Mid_Term_T.shape[0], Long_Term_T.shape[0]]
    colors     = ["#F72585", "#4CC9F0", "#FFBE0B"]

    # ── Donut Chart ───────────────────────────────────────────────────────────────
    fig_pie = go.Figure(data=[go.Pie(
        labels=labels,
        values=population,
        hole=0.55,
        marker=dict(colors=colors, line=dict(color="#111111", width=2)),
        textinfo="label+percent+value",
        textfont=dict(size=14, color="white"),
        textposition="outside",
        hovertemplate="%{label}<br>%{value:,} customers<br>%{percent}<extra></extra>"
    )])
    fig_pie.update_layout(
        title="Tenure-wise Population Distribution",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=60, b=60, l=60, r=60),
        height=450
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    # ── Bar Chart ─────────────────────────────────────────────────────────────────
    tenure_seg = st.selectbox("Select Tenure Segment",
        ["New (0–3 Yrs)", "Mid-Term (4–8 Yrs)", "Long-Term (9–10 Yrs)"],
        key="tenure_seg")

    seg_df = New_T if tenure_seg == "New (0–3 Yrs)" else \
            Mid_Term_T if tenure_seg == "Mid-Term (4–8 Yrs)" else Long_Term_T

    total    = len(seg_df)
    churned  = seg_df[seg_df["Exited"] == 1].shape[0]
    retained = seg_df[seg_df["Exited"] == 0].shape[0]
    values   = [total, churned, retained]
    pcts     = [100.0, round(churned/total*100,1), round(retained/total*100,1)]

    fig_bar = go.Figure(data=[go.Bar(
        x=["Total", "Churned", "Retained"],
        y=values,
        marker_color=["#4CC9F0", "#F72585", "#FFBE0B"],
        text=[f"{v:,} ({p}%)" for v, p in zip(values, pcts)],
        textposition="outside",
        textfont=dict(size=14, color="white")
    )])
    fig_bar.update_layout(
        title=f"Churn Breakdown — {tenure_seg}",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Customers",
        yaxis_range=[0, max(values) * 1.2],
        height=420
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)

import plotly.graph_objects as go
import pandas as pd

# ── Bin Age & Tenure ──────────────────────────────────────────────────────────
df["Age Group"] = pd.cut(df["Age"],
    bins=[0, 30, 45, 60, 100],
    labels=["<30", "30–45", "46–60", "60+"])

df["Tenure Group"] = pd.cut(df["Tenure"],
    bins=[-1, 3, 8, 10],
    labels=["New (0–3)", "Mid (4–8)", "Long (9–10)"])

# ── Pivot: churn % per cell ───────────────────────────────────────────────────
heatmap_df = df.groupby(["Age Group", "Tenure Group"], observed=True)["Exited"] \
               .mean().reset_index()
heatmap_df["Churn %"] = (heatmap_df["Exited"] * 100).round(1)

pivot = heatmap_df.pivot(index="Age Group", columns="Tenure Group", values="Churn %")

# ── Plot ──────────────────────────────────────────────────────────────────────
fig = go.Figure(data=go.Heatmap(
    z=pivot.values,
    x=pivot.columns.tolist(),
    y=pivot.index.tolist(),
    colorscale="RdYlGn_r",          # green=low churn, red=high churn
    text=[[f"{v:.1f}%" for v in row] for row in pivot.values],
    texttemplate="%{text}",
    textfont=dict(size=15, color="white"),
    hovertemplate="Age: %{y}<br>Tenure: %{x}<br>Churn: %{text}<extra></extra>",
    colorbar=dict(title="Churn %")
))

fig.update_layout(
    title="Churn % Heatmap — Age Group vs Tenure",
    xaxis_title="Tenure Group",
    yaxis_title="Age Group",
    paper_bgcolor="rgba(0,0,0,0)",
    height=420
)

st.plotly_chart(fig, use_container_width=True)