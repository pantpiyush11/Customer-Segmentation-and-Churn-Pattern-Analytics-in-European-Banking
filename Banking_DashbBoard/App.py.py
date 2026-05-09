import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


path=r"C:\Users\piyus\Desktop\3 months Data Science Internship\Project 02 European Bank\JL\anaconda_projects\db\Banking DataSet\European_Bank.csv"
df=pd.read_csv(path)
print("Loaded Dataset sucessfully!")

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Churn Dashboard", layout="wide")


# # ── Sidebar ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/color/96/bank.png", width=60)
    st.title("🏦 Churn Dashboard")
    st.markdown("---")

    st.subheader("🔍 Filters")
    # ── Sidebar Filters ─────────────────────────────────────────────────────────────
with st.sidebar:

    # Gender (already written by you)
    seg_filter = st.multiselect(
        "Gender",
        options=['Male', 'Female'],
        default=['Male', 'Female']
    )

    # Credit Score Bands (Low: <584, Medium: 584–718, High: >718)
    credit_filter = st.multiselect(
        "Credit Score Band",
        options=['Low', 'Medium', 'High'],
        default=['Low', 'Medium', 'High']
    )

    # Tenure Groups (New: ≤3, Mid-term: 4–8, Long-term: 9–10)
    tenure_filter = st.multiselect(
        "Tenure Group",
        options=['New', 'Mid-term', 'Long-term'],
        default=['New', 'Mid-term', 'Long-term']
    )

    # Balance Segments (Zero: ==0, Low: 0–127644, High: >127644)
    balance_filter = st.multiselect(
        "Balance Segment",
        options=['Zero-balance', 'Low-balance', 'High-balance'],
        default=['Zero-balance', 'Low-balance', 'High-balance']
    )

    # Age Segmentation (<30, 30–45, 46–60, 60+)
    age_filter = st.multiselect(
        "Age Segment",
        options=['<30', '30–45', '46–60', '60+'],
        default=['<30', '30–45', '46–60', '60+']
    )


# ── Mapping Labels → Conditions ─────────────────────────────────────────────────

# Credit Score label column
def get_credit_band(score):
    if score < 584:   return 'Low'
    elif score < 718: return 'Medium'
    else:             return 'High'

# Tenure label column
def get_tenure_group(tenure):
    if tenure <= 3:   return 'New'
    elif tenure <= 8: return 'Mid-term'
    else:             return 'Long-term'

# Balance label column
def get_balance_segment(balance):
    if balance == 0:        return 'Zero-balance'
    elif balance <= 127644: return 'Low-balance'
    else:                   return 'High-balance'

# Age label column
def get_age_segment(age):
    if age < 30:    return '<30'
    elif age <= 45: return '30–45'
    elif age <= 60: return '46–60'
    else:           return '60+'

# ── Add Label Columns ────────────────────────────────────────────────────────────
df['Credit_Band']       = df['CreditScore'].apply(get_credit_band)
df['Tenure_Group']      = df['Tenure'].apply(get_tenure_group)
df['Balance_Segment']   = df['Balance'].apply(get_balance_segment)
df['Age_Segment']       = df['Age'].apply(get_age_segment)


# ── Apply Filters ────────────────────────────────────────────────────────────────
df = df[
    (df['Gender'].isin(seg_filter)) &
    (df['Credit_Band'].isin(credit_filter)) &
    (df['Tenure_Group'].isin(tenure_filter)) &
    (df['Balance_Segment'].isin(balance_filter)) &
    (df['Age_Segment'].isin(age_filter))
]

# ── Guard: empty result warning ──────────────────────────────────────────────────
if df.empty:
    st.warning("No customers match the selected filters.")

# ── Tabs ────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Home",
    "📊 Churn Summary",
    "🌍 Geography",
    "👤 Age & Tenure",
    "💎 High-Value Customers"
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — HOME / KPIs
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
     pass
    # st.title("Customer Churn Intelligence Dashboard")
    # st.markdown("Real-time churn metrics across segments, regions, and demographics.")
    # st.markdown("---")

    # total        = len(filtered_df)
    # churned      = filtered_df['Exited'].sum()
    # overall_rate = churned / total * 100

    # premium_df        = filtered_df[filtered_df['Value_Segment'] == 'Premium']
    # hv_churn_ratio    = premium_df['Exited'].sum() / len(premium_df) * 100 if len(premium_df) > 0 else 0

    # geo_churn         = filtered_df.groupby('Geography')['Exited'].mean() * 100
    # geo_risk_index    = geo_churn.max()

    # inactive_churned  = filtered_df[(filtered_df['IsActiveMember'] == 0) & (filtered_df['Exited'] == 1)]
    # engagement_drop   = len(inactive_churned) / churned * 100 if churned > 0 else 0

    # seg_churn         = filtered_df.groupby('Value_Segment')['Exited'].mean() * 100
    # highest_seg       = seg_churn.idxmax()
    # highest_seg_rate  = seg_churn.max()

    # # KPI Row
    # k1, k2, k3, k4, k5 = st.columns(5)
    # k1.metric("📉 Overall Churn Rate",     f"{overall_rate:.1f}%",    f"{churned} customers")
    # k2.metric("📦 Highest Segment Churn",  f"{highest_seg_rate:.1f}%", highest_seg)
    # k3.metric("💎 High-Value Churn Ratio", f"{hv_churn_ratio:.1f}%",  "Premium tier")
    # k4.metric("🌍 Geographic Risk Index",  f"{geo_risk_index:.1f}%",  geo_churn.idxmax())
    # k5.metric("😴 Engagement Drop",        f"{engagement_drop:.1f}%", "Inactive & churned")

    # st.markdown("---")
    # st.subheader("📋 KPI Definitions")

    # kpi_data = {
    #     "KPI": [
    #         "Overall Churn Rate %",
    #         "Segment Churn Rate",
    #         "High-Value Churn Ratio",
    #         "Geographic Risk Index",
    #         "Engagement Drop Indicator"
    #     ],
    #     "Description": [
    #         "% of total customers who exited the bank",
    #         "Churn % broken down by value segment (Low / Medium / High / Premium)",
    #         "Churn rate specifically among Premium-tier customers",
    #         "Highest regional churn % — identifies geographic hotspots",
    #         "% of churned customers who were inactive members — inactivity as churn signal"
    #     ]
    # }
    # st.dataframe(pd.DataFrame(kpi_data), use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — OVERALL CHURN SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.title("📊 Overall Churn Summary")
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


    
# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — GEOGRAPHY
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.title("🌍 Geography-wise Churn Visualization")
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
            
    

# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — AGE & TENURE
# ══════════════════════════════════════════════════════════════════════════════
with tab4:
    st.title("👤 Age & Tenure Churn Comparison")
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
    
# ══════════════════════════════════════════════════════════════════════════════
# TAB 5 — HIGH VALUE CUSTOMER EXPLORER
# ══════════════════════════════════════════════════════════════════════════════
with tab5:
    st.title("💎 High-Value Customer Churn Explorer")
    
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