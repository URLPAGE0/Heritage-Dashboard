# Saudi Heritage Sentiment Dashboard
# Run after the transformer notebook has generated best_model_test_predictions.csv
# Install: pip install streamlit pandas
# Start: streamlit run app.py

import csv
from collections import Counter, defaultdict
import streamlit as st

PREDICTION_FILE = "data/best_model_test_predictions.csv"

st.set_page_config(page_title="Saudi Heritage Sentiment Dashboard", layout="wide")
st.title("Saudi Heritage Review — Aspect-Level Sentiment Dashboard")
st.caption("Research prototype displaying predictions from the best-performing transformer model.")

rows = []
try:
    with open(PREDICTION_FILE, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    st.error(f"Missing {PREDICTION_FILE}. Run the transformer experiment notebook first.")
    st.stop()

places = sorted({r["place"] for r in rows})
aspects = sorted({r["aspect"] for r in rows})

col1, col2 = st.columns(2)
with col1:
    selected_place = st.selectbox("Heritage attraction", ["All sites"] + places)
with col2:
    selected_aspect = st.selectbox("Aspect", ["All aspects"] + aspects)

filtered = rows
if selected_place != "All sites":
    filtered = [r for r in filtered if r["place"] == selected_place]
if selected_aspect != "All aspects":
    filtered = [r for r in filtered if r["aspect"] == selected_aspect]

sentiment_counts = Counter(r["pred_sentiment"] for r in filtered)
total = sum(sentiment_counts.values())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Predictions", total)
c2.metric("Positive", sentiment_counts.get("Positive", 0))
c3.metric("Neutral", sentiment_counts.get("Neutral", 0))
c4.metric("Negative", sentiment_counts.get("Negative", 0))

st.subheader("Predicted sentiment distribution")
chart_data = {
    "Negative": sentiment_counts.get("Negative", 0),
    "Neutral": sentiment_counts.get("Neutral", 0),
    "Positive": sentiment_counts.get("Positive", 0),
}
st.bar_chart(chart_data)

st.subheader("Aspect summary")
summary = []
for aspect in aspects:
    subset = [r for r in filtered if r["aspect"] == aspect]
    if not subset:
        continue
    c = Counter(r["pred_sentiment"] for r in subset)
    n = len(subset)
    summary.append({
        "Aspect": aspect,
        "N": n,
        "Positive %": round(100*c.get("Positive",0)/n, 1),
        "Neutral %": round(100*c.get("Neutral",0)/n, 1),
        "Negative %": round(100*c.get("Negative",0)/n, 1),
    })
st.dataframe(summary, use_container_width=True)

st.info(
    "Prototype limitation: this dashboard visualizes model predictions for aspect instances "
    "that are already annotated as present in the research dataset. It is not yet a production "
    "system for detecting new aspects in completely unseen reviews."
)
