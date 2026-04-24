# 📉 Consumer Signal Tracker — DoorDash Case Study

🚀 **[View Live Dashboard](https://consumer-signal-tracker-uvqbw7akqlostyrnamt2bm.streamlit.app/)**

## **Consumers showed signs of frustration before the numbers did.**

This project explores whether **real-time search behavior can surface early signs of consumer demand pressure before it appears in company-reported metrics.**

Using Google Trends data, I tracked behavioral signals around DoorDash — cancellations, price sensitivity, and switching intent — and compared them against earnings call narratives to identify potential gaps between **what consumers are experiencing** and **what companies report**.

---

## 🔍 What This Project Does

- Tracks 6 behavioral keywords capturing:
  - cancellation intent
  - price sensitivity
  - switching behavior
- Overlays DoorDash earnings call dates as reference points
- Compares search signal trends against earnings call language
- Identifies divergence between real-time consumer behavior and reported metrics

---

## 📊 Key Findings

- **"Cancel DoorDash"** — remained elevated at **60–80 throughout 2025**
- **"DoorDash not worth it"** — spiked to **100 in April 2026**
- **"Switch to Uber Eats"** — peaked at **100 in March 2026**
- **Q4 2025 Earnings (Feb 18, 2026)** reported:
  - record subscribers
  - all-time high MAUs

👉 Despite strong reported performance, search signals related to dissatisfaction, cancellations, and switching were **rising across the same period**.

**Interpretation:**
Despite reporting record growth, DoorDash shows a visible divergence between reported performance and consumer search behavior — suggesting that **aggregated metrics and real-time sentiment may move on different timelines.**

---

## 🧠 Key Insight

Consumer sentiment does not always decline when performance metrics do — it often shifts earlier, in subtle ways.

Search behavior may provide one such **early-stage signal of changing consumer intent**.

---

## 🛠️ Tech Stack

- **Python** — pytrends, pandas
- **Streamlit** — interactive dashboard with sidebar filters
- **Plotly** — time series visualization with earnings overlays
- **Data Source** — Google Trends (US, 12 months, weekly)

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

---

## ⚠️ Methodology & Limitations

- Google Trends measures relative search interest (0–100), not absolute volume
- A single spike may reflect external events (e.g., viral content), not sustained behavior
- Search data is used as a proxy for consumer intent, not a direct measure of actions
- Correlation is not causation — rising search interest does not prove demand decline
- Earnings calls reflect aggregated, lagging metrics, while search behavior is real-time

---

## 💡 Why This Still Has Value

Search behavior is a real-time, unfiltered signal — unlike curated earnings narratives. While not a direct measure of demand, it can capture early-stage shifts in consumer intent that may not yet be reflected in aggregated metrics.

The observed divergence highlights an opportunity:
Combining behavioral signals with traditional reporting could improve how companies detect and respond to demand changes earlier.

---

## 📌 Future Improvements

- Incorporate additional data sources (e.g., Reddit, app reviews) for stronger signal validation
- Apply NLP-based classification to refine behavioral intent detection
- Quantify lead-lag relationships between search signals and earnings narratives
- Expand analysis to other consumer platforms (e.g., streaming, BNPL)
