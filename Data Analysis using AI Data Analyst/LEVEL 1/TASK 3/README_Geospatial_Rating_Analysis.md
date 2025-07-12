# 🌍 Restaurant Dataset: Geospatial and Rating Analysis

## ✅ Objective
This project performs geospatial analysis and rating distribution insights using restaurant location data. It involves:
- Mapping restaurant locations using latitude and longitude
- Analyzing how restaurant ratings vary across cities and countries

---

## 📌 Project Overview

This Python script is divided into two major components:

### 1. 🗺️ **Geospatial Mapping**
- Visualizes restaurant locations using **Folium**
- Adds interactive markers grouped in a **MarkerCluster**
- Each marker includes:
  - Restaurant name
  - Rating
  - City
- Saves the output to an HTML file (`restaurant_map.html`)

### 2. 📊 **Rating Distribution Analysis**
- Computes average **Aggregate Ratings** per:
  - **Country** (`Country Code`)
  - **City**
- Plots the **Top 10 Countries** and **Top 10 Cities** based on average ratings using **Seaborn bar charts**

---

## 📂 Project Structure

```plaintext
LEVEL 1/
├── Dataset .csv                # Input dataset file
├── geospatial_rating_analysis.py  # This script
├── restaurant_map.html         # Output interactive map
└── README.md                   # This file
