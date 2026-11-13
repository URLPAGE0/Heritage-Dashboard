# Arabic Heritage Review Sentiment Analysis

This repository contains the code, processed heritage subset, experiment notebooks,
verified result files, figures, and dashboard prototype used in the study:

**Aspect-Based Sentiment Analysis of Arabic Reviews for Saudi Heritage Sites Using Transformer Models**

## Dataset

The original tourism dataset is publicly available on Zenodo:

https://doi.org/10.5281/zenodo.17011574

The dataset was accessed from Zenodo in **October 2026**.

The heritage subset used in this study contains:

- 1,083 usable reviews
- 2,542 labeled aspect-sentiment pairs
- 866 training reviews
- 217 held-out test reviews
- 520 labeled test aspect instances

No new Google Maps reviews were scraped by the research team and no new manual sentiment
annotations were created.

## Models

- AraBERT
- MARBERT
- QARiB

## Main verified results

- AraBERT overall Macro-F1: 0.6436
- MARBERT overall Macro-F1: 0.6068
- QARiB overall Macro-F1: 0.6541
- Paired review-level randomization test: 10,000 permutations

The observed pairwise model differences were not statistically significant at alpha = 0.05.

## Repository structure

- `index.html` — standalone interactive dashboard used by GitHub Pages
- `app.py` — Streamlit dashboard source
- `requirements.txt` — Python dependencies
- `data/heritage_modeling_data.csv` — prepared heritage modeling dataset
- `data/best_model_test_predictions.csv` — QARiB held-out predictions used by the dashboard
- `notebooks/transformer_experiment.ipynb` — model-training and evaluation notebook
- `notebooks/significance_test.ipynb` — final experiment with paired randomization test
- `results/` — verified result CSV files
- `figures/` — result figures, confusion matrix, and dashboard snapshot
- `environment_versions.txt` — recorded software environment

## Run the Streamlit dashboard

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run from the repository root:

```bash
streamlit run app.py
```

The Streamlit app reads:

`data/best_model_test_predictions.csv`

## Public dashboard

https://urlpage0.github.io/Heritage-Dashboard/

## Prototype limitation

The dashboard visualizes predictions for aspect instances already annotated as present in the held-out
research dataset. It is a research prototype, not a production system for automatically detecting new
aspects in completely unseen reviews.
