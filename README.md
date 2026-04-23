# Consumer Signal Tracker — DoorDash Case Study

Can public search behavior detect consumer stress before it shows up in earnings reports?

This project tracks Google Trends signals around DoorDash — cancellations, price sensitivity, and switching intent — and compares them against earnings call narratives.

## Key Finding
Despite DoorDash reporting record subscribers and all-time high MAUs in its Q4 2025 earnings call, Google Trends data shows sustained consumer frustration signals throughout 2025 — culminating in a sharp spike 7 weeks after the earnings call.

## Tech Stack
- Python, pytrends, pandas
- Streamlit, Plotly
- Google Trends data (US, 12 months)

## How to Run
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Methodology
See the Methodology & Limitations section in the dashboard for full details on data sources, assumptions, and limitations.
