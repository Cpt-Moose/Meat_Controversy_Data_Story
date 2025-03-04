#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 19:30:30 2025

@author: pnl17v28
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ensure necessary dependencies are installed
try:
    import openpyxl
except ModuleNotFoundError:
    st.error("Missing dependency: openpyxl. Install it using `pip install openpyxl`.")

# Load Data with Error Handling
@st.cache_data
def load_data(file_path, sheet_name=0):
    try:
        return pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    except Exception as e:
        st.error(f"Error loading {file_path}: {e}")
        return None

# File paths (Update paths if running locally)
meat_consumption = load_data("statistic_id679528_per-capita-meat-consumption-in-european-countries-2018-2024.xlsx")
global_meat_production = load_data("global-meat-production.xlsx")
health_impact = load_data("A summary of meat intakes and health burdens..xlsx")
ghg_emissions = load_data("greenhouse-gas-emissions-per-kilogram-of-food-product.xlsx")

# Streamlit UI
st.title("📊 The Impact of Meat Consumption: A Data Story")
st.write("This interactive dashboard explores trends, health effects, and the environmental impact of meat consumption.")

# Section 1: Meat Consumption Trends
st.header("🥩 Meat Consumption Trends in Europe")

if meat_consumption is not None:
    st.write("How has meat consumption evolved in different European countries?")
    fig, ax = plt.subplots(figsize=(10, 5))
    for country in meat_consumption.columns[1:]:  # Assuming first column is Year
        ax.plot(meat_consumption.iloc[:, 0], meat_consumption[country], label=country)
    ax.set_xlabel("Year")
    ax.set_ylabel("Kg per capita")
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("Meat consumption data could not be loaded.")

# Section 2: Global Meat Production
st.header("🌍 Global Meat Production Over Time")

if global_meat_production is not None:
    st.write("A look at the rise in global meat production.")
    fig2, ax2 = plt.subplots()
    ax2.plot(global_meat_production["Year"], global_meat_production["Production (Million Tons)"], marker='o')
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Million Tons")
    st.pyplot(fig2)
else:
    st.warning("Global meat production data could not be loaded.")

# Section 3: Health Impact
st.header("🩺 Health Risks of High Meat Consumption")

if health_impact is not None:
    st.write("How does meat consumption correlate with health risks?")
    st.dataframe(health_impact.head())
else:
    st.warning("Health impact data could not be loaded.")

# Section 4: Environmental Impact
st.header("🌱 Environmental Impact of Meat Production")

if ghg_emissions is not None:
    st.write("Greenhouse gas emissions per kilogram of different food products.")
    st.bar_chart(ghg_emissions.set_index(ghg_emissions.columns[0]))  # Assuming first column is food product names
else:
    st.warning("Greenhouse gas emissions data could not be 
