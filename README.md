# What Makes a Society Healthy?

## A Machine Learning Analysis of Life Expectancy Across Countries

This project analyzes the determinants of life expectancy across countries using international datasets and machine learning methods.

The central research question is:

**Which economic, healthcare, lifestyle, environmental and social factors best explain differences in life expectancy across countries?**

The project compares multiple model specifications, starting from simple economic and healthcare baselines and progressively adding social, lifestyle and environmental variables.

---

## Project Overview

Life expectancy is treated as a multidimensional outcome influenced by several macro-categories:

1. **Economic Factors**
   - GDP per capita

2. **Healthcare Factors**
   - Health expenditure as a percentage of GDP
   - Health expenditure per capita

3. **Lifestyle Factors**
   - Obesity prevalence
   - Smoking prevalence

4. **Environmental Factors**
   - PM2.5 air pollution

5. **Social Factors**
   - Education

The final model selection is based on predictive performance, sample size, interpretability and data availability.

---

## Data

The project uses country-level international data from public sources, mainly World Bank indicators and World Bank Data360 health-related data.

Most variables refer to 2022. PM2.5 air pollution data were not available for 2022 in the selected indicator, so 2020 PM2.5 exposure was used as the most recent available environmental proxy with broad country coverage.

The final model dataset contains:

| Variable | Macro-category |
|---|---|
| Life expectancy | Target variable |
| GDP per capita | Economic |
| Health expenditure per capita | Healthcare |
| Obesity prevalence | Lifestyle |
| Smoking prevalence | Lifestyle |
| PM2.5 air pollution | Environmental |

The final model dataset contains **155 observations** and no missing values across the selected predictors.

---

## Methodology

The project follows an end-to-end data science workflow:

- Data collection from international public datasets
- Data cleaning and preparation
- Missing value checks
- Aggregate observation checks
- Exploratory data analysis
- Linear Regression baseline models
- Log-GDP Linear Regression
- Random Forest Regression
- Model comparison using R² and Mean Absolute Error
- Feature importance analysis
- Final model selection

The full exploratory workflow is preserved in the working notebook, while the final analysis notebook presents the cleaned and structured version of the project.

---

## Model Comparison

Nine models were tested.

| Model | Description | Observations | R² | MAE |
|---|---|---:|---:|---:|
| M1 | Baseline Linear Regression | 191 | 0.447 | 4.59 |
| M2 | Log-GDP Linear Regression | 191 | 0.789 | 2.80 |
| M3 | Baseline Random Forest | 191 | 0.757 | 2.75 |
| M4 | Social Extension Random Forest | 107 | 0.630 | 2.58 |
| M5 | Obesity Extension Random Forest | 177 | 0.732 | 2.86 |
| M6 | Lifestyle Extension Random Forest | 155 | 0.802 | 2.77 |
| M7 | Absolute Healthcare Spending Random Forest | 155 | 0.787 | 2.79 |
| M8 | Lifestyle & Environment Random Forest | 155 | 0.812 | 2.70 |
| M9 | Absolute Healthcare & Environment Random Forest | 155 | 0.822 | 2.59 |

The best-performing final model is:

**M9 — Absolute Healthcare & Environment Random Forest**

It combines:

- GDP per capita
- Health expenditure per capita
- Obesity prevalence
- Smoking prevalence
- PM2.5 air pollution

Performance:

- **R² = 0.822**
- **MAE = 2.59 years**
- **Observations = 155**

M4 has a slightly lower MAE, but it uses only 107 observations and has substantially lower R². For this reason, M9 is selected as the strongest final model because it provides the best overall balance between explanatory power, predictive accuracy, sample size and interpretability.

---

## Final Model Feature Importance

The final model, M9, produced the following feature importance ranking:

| Feature | Importance |
|---|---:|
| GDP per capita | 0.637 |
| Health expenditure per capita | 0.195 |
| Smoking prevalence | 0.078 |
| PM2.5 air pollution | 0.053 |
| Obesity prevalence | 0.037 |

GDP per capita remains the dominant predictor, confirming the central role of economic development.

Health expenditure per capita is the second most important variable, suggesting that absolute healthcare spending per person is more informative than healthcare spending as a percentage of GDP in the final model.

Smoking prevalence is the most informative lifestyle variable, while air pollution provides moderate additional predictive value.

---

## Key Findings

### Economic Factors

GDP per capita is the strongest predictor of life expectancy across all Random Forest models.

The Log-GDP Linear Regression model substantially improves over the baseline linear model, suggesting a diminishing-returns relationship between income and life expectancy.

### Healthcare Factors

Health expenditure per capita is more informative than health expenditure as a percentage of GDP.

This is because a country can spend a high share of GDP on healthcare but still spend little per person if its GDP is low. Per-capita healthcare spending better captures the absolute healthcare resources available to individuals.

### Lifestyle Factors

Lifestyle variables improve model performance.

Smoking prevalence is more informative than obesity prevalence in the final model.

Obesity remains included as a lifestyle risk factor, but its contribution is smaller and should be interpreted carefully because BMI-based obesity measures do not perfectly capture body composition.

### Environmental Factors

PM2.5 air pollution improves model performance and contributes moderate additional predictive value.

Because 2022 data were unavailable, 2020 PM2.5 exposure was used as the most recent available proxy.

### Social Factors

Education appears to be a promising social determinant.

In the social extension model, education has high feature importance. However, including education substantially reduces the sample size, so it is not included in the final model.

---

## Main Conclusion

The project shows that cross-country differences in life expectancy are best explained through a multidimensional framework.

Economic development is the strongest explanatory dimension, but life expectancy is not explained by income alone. Healthcare resources, lifestyle risks, environmental exposure and social conditions all contribute to understanding why people live longer in some countries than in others.

The final model suggests that a healthy society is not simply a richer society. Economic development matters most, but longer life expectancy also depends on how resources are translated into healthcare capacity, healthier behaviors, cleaner environments and broader social development.

---

## Repository Structure

| Path | Description |
|---|---|
| `data/` | Cleaned datasets, model audit tables and feature importance outputs |
| `notebooks/01_working_notebook.ipynb` | Full exploratory workflow and intermediate experiments |
| `notebooks/02_final_analysis.ipynb` | Clean final analysis notebook |
| `reports/figures/` | Final project visualizations |
| `README.md` | Project overview and key results |

---

## Main Files

- [Final Analysis Notebook](notebooks/02_final_analysis.ipynb)
- [Working Notebook](notebooks/01_working_notebook.ipynb)
- [Model Audit Table](data/model_audit.csv)
- [Feature Importance Audit](data/feature_importance_audit.csv)
- [Random Forest Performance Audit](data/random_forest_performance_audit.csv)

---

## Limitations

This project should be interpreted as a predictive and exploratory analysis, not as a causal study.

Main limitations include:

- The analysis is cross-sectional.
- Random Forest feature importance should not be interpreted causally.
- Education is limited by data availability.
- PM2.5 air pollution uses 2020 data as a proxy because 2022 data were unavailable.
- BMI-based obesity prevalence is an imperfect measure of unhealthy body composition.
- GDP per capita and health expenditure per capita are likely correlated.
- Other relevant factors, such as institutions, inequality, sanitation, vaccination, conflict or demographic structure, are not included.

---
