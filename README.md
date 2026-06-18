# Life Expectancy Machine Learning Project

## Overview

This project investigates the economic, healthcare and lifestyle determinants of life expectancy across countries using international datasets and machine learning techniques.

The goal is to understand which factors best explain cross-country differences in life expectancy and to evaluate how different machine learning models perform in predicting health outcomes.

## Research Question

Which economic, healthcare and lifestyle factors best explain differences in life expectancy across countries?

## Data

The project uses international country-level data for 2022.

The main variables included are:

- Life expectancy at birth
- GDP per capita
- Health expenditure (% of GDP)
- Health expenditure per capita
- Obesity prevalence
- Smoking prevalence
- Education indicator

The final model focuses on:

- GDP per capita
- Health expenditure (% of GDP)
- Obesity prevalence
- Smoking prevalence

## Methods

The analysis includes:

- Data collection from international public datasets
- Data cleaning and missing value handling
- Exploratory data analysis
- Correlation analysis
- Linear Regression
- Random Forest Regression
- Feature importance analysis
- Model comparison using R-squared and Mean Absolute Error

## Model Comparison

Several models were tested.

| Model | R² | MAE |
|---|---:|---:|
| Baseline Linear Regression | 0.447 | 4.59 |
| Log GDP Linear Regression | 0.789 | 2.80 |
| Baseline Random Forest | 0.752 | 2.79 |
| Random Forest + Education | 0.631 | 2.62 |
| Random Forest + Obesity | 0.751 | 2.73 |
| Lifestyle Random Forest | 0.802 | 2.74 |
| Per-Capita Health Expenditure Random Forest | 0.787 | 2.78 |

## Best Model

The strongest candidate model is the Lifestyle Random Forest.

Features:

- GDP per capita
- Health expenditure (% of GDP)
- Obesity prevalence
- Smoking prevalence

Performance:

- R² ≈ 0.802
- MAE ≈ 2.74 years

## Key Findings

GDP per capita is the dominant predictor of life expectancy in the current dataset.

However, lifestyle variables improve predictive performance. In particular, smoking prevalence adds meaningful predictive information beyond economic and healthcare variables.

A logarithmic transformation of GDP per capita also substantially improves the performance of a linear regression model, suggesting diminishing returns of income on life expectancy.

## Repository Structure

```text
life-expectancy-machine-learning/
│
├── data/
│   ├── final_lifestyle_model_dataset.csv
│   ├── final_lifestyle_feature_importance.csv
│   ├── model_comparison.csv
│   └── intermediate datasets
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── reports/
│   └── future final report
│
├── README.md
└── .gitignore
```


## Project Status

Current status: work in progress.

Completed:

- Data collection
- Data cleaning
- Exploratory analysis
- Baseline models
- Random Forest models
- Lifestyle model
- Model comparison table
- GitHub repository setup

Next steps:

- Improve notebook organization
- Add final visualizations
- Write final report
- Prepare a concise project description for CV and motivation letter
