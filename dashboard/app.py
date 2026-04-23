import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Consumer Signal Tracker", layout="wide")

st.title("📉 Consumer Signal Tracker")
st.subheader("DoorDash Case Study — Early Demand Shift Detection")

# Load data
df = pd.read_csv('data/trends_raw.csv')
df['week'] = pd.to_datetime(df['week'])

# Earnings dates
earnings_dates = [
    {"date": "2025-05-06", "label": "Q1 2025 Earnings"},
    {"date": "2025-08-05", "label": "Q2 2025 Earnings"},
    {"date": "2025-11-04", "label": "Q3 2025 Earnings"},
    {"date": "2026-02-18", "label": "Q4 2025 Earnings"},
]

# Sidebar
st.sidebar.header("Filters")
keywords = df['keyword'].unique().tolist()
selected = st.sidebar.multiselect("Select signals:", keywords, default=keywords)
show_earnings = st.sidebar.checkbox("Show earnings dates", value=True)

filtered = df[df['keyword'].isin(selected)]

# Chart
fig = go.Figure()

for keyword in selected:
    kdf = filtered[filtered['keyword'] == keyword]
    fig.add_trace(go.Scatter(
        x=kdf['week'],
        y=kdf['interest'],
        name=keyword,
        mode='lines',
        hovertemplate='%{x}<br>Interest: %{y}<extra>' + keyword + '</extra>'
    ))

if show_earnings:
    for e in earnings_dates:
        fig.add_vline(
            x=pd.Timestamp(e["date"]).timestamp() * 1000,
            line_dash="dash",
            line_color="red",
            opacity=0.5,
            annotation_text=e["label"],
            annotation_position="top right",
            annotation_font_size=10
        )

fig.update_layout(
    title='Google Trends: Consumer Stress Signals vs DoorDash Earnings',
    xaxis_title='Week',
    yaxis_title='Search Interest (0-100)',
    hovermode='x unified',
    legend=dict(orientation='h', yanchor='bottom', y=1.02),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# Key insight
st.markdown("---")
st.markdown("### 🔍 Key Insight")
st.info(
    "Consumer stress signals around DoorDash — cancellations, price sensitivity, "
    "switching intent — show measurable spikes **weeks before** earnings calls reflect "
    "demand pressure. This dashboard tracks that leading indicator in real time."
)

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    peak = df[df['keyword'] == 'doordash not worth it']['interest'].max()
    st.metric("Peak: 'not worth it'", f"{int(peak)}/100", "Apr 2026")
with col2:
    peak2 = df[df['keyword'] == 'switch to uber eats']['interest'].max()
    st.metric("Peak: 'switch to uber eats'", f"{int(peak2)}/100", "Mar 2026")
with col3:
    peak3 = df[df['keyword'] == 'cancel doordash']['interest'].max()
    st.metric("Peak: 'cancel doordash'", f"{int(peak3)}/100", "Last 12mo")

# Earnings vs Search
st.markdown("---")
st.markdown("### 📋 What the Earnings Call Said vs What Search Showed")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Q4 2025 Earnings Call — Feb 18, 2026**")
    st.success("""
✅ "Two of the fastest growing quarters in the last four years"

✅ "DashPass hit record number of subscribers"

✅ "MAUs at all-time high"

✅ "Grocery growing very, very fast"
    """)

with col2:
    st.markdown("**Google Trends — Same Period**")
    st.error("""
⚠️ "cancel doordash" — elevated at 60-80 all of 2025

⚠️ "doordash not worth it" — spiked to 100 in April 2026

⚠️ "switch to uber eats" — peaked at 100 in March 2026

⚠️ All signals rising while earnings narrative was positive
    """)

st.info("""
**The Gap:** Despite reporting record growth in Q4 earnings, consumer search behavior
shows sustained frustration signals throughout 2025 — culminating in a sharp spike
7 weeks after the earnings call. Search behavior may capture early consumer stress
before it appears in company-reported metrics.
""")

# Methodology
st.markdown("---")
st.markdown("### 📌 Methodology & Limitations")

with st.expander("Click to read full methodology"):
    st.markdown("""
**Data Source**
- Google Trends via `pytrends` (Python library)
- 12 months of weekly search interest data, US only
- 6 keywords selected to capture cancellation, price sensitivity, and switching intent

**What Google Trends Measures**
- Relative search interest (0–100 scale), not absolute volume
- 100 = peak popularity for that term in the selected period
- Good for detecting directional shifts and spikes over time

**What This Analysis Does**
- Tracks consumer stress signals around DoorDash across 6 behavioral keywords
- Overlays DoorDash earnings call dates as reference points
- Compares search signal trends against earnings call language

**Limitations (important)**
- Google Trends data is noisy — a single spike could reflect a viral tweet, not organic behavior
- Correlation is not causation — rising search interest does not prove demand decline
- Earnings calls report lagging metrics — this comparison is directional, not definitive
- This is exploratory analysis, not a financial or investment claim

**Why This Still Has Value**
- Search behavior is a real-time, unfiltered signal — unlike curated earnings narratives
- Academic research (e.g. Google Flu Trends, Fed nowcasting papers) has validated search data as a leading indicator in other domains
- The divergence between search signals and reported metrics is worth investigating further
    """)

st.markdown("---")
st.caption("Data: Google Trends via pytrends | Built by Kavya Murugan")