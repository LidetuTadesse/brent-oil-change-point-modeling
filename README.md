# Brent Oil Price Change Point Analysis

## Overview
This project explores structural changes in Brent crude oil prices over time, focusing on how global economic shifts and geopolitical events have influenced pricing trends. By applying Bayesian change point detection methods, we aim to identify significant moments when the statistical properties of oil prices changed—highlighting correlations with real-world incidents like wars, pandemics, and market crashes.

## Objectives
    Detect change points in historical Brent oil prices
    Link detected changes to real-world geopolitical or economic events
    Provide visualizations and insights to support decision-making and research

## Tech Stack
    Python (Pandas, Numpy, Matplotlib, PyMC, Ruptures)
    Jupyter Notebooks for EDA and modeling
    Flask API backend
    React.js frontend dashboard

## Project Structure
brent-oil-change-point-analysis/
│
├── data/           # Raw and processed oil price datasets
├── notebooks/      # EDA and modeling notebooks
├── src/            # Core scripts and Bayesian models
├── dashboard/      # Flask + React interactive dashboard
├── tests/          # Unit tests
└── requirements.txt

## Getting Started
Install dependencies:

```bash
pip install -r requirements.txt
