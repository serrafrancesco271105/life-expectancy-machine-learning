# What Makes a Society Healthy?

## A Machine Learning Analysis of Life Expectancy Across Countries

**Author:** Francesco Serra  
**Project Type:** Data Science / Machine Learning Project  
**Tools:** Python, pandas, scikit-learn, matplotlib, World Bank Data  

---

## Executive Summary

This report investigates the determinants of life expectancy across countries using international public datasets and machine learning models.

The analysis compares economic, healthcare, lifestyle, environmental and social variables to evaluate which factors best explain cross-country differences in life expectancy.

The final selected model is **M9 — Absolute Healthcare & Environment Random Forest**, which combines GDP per capita, health expenditure per capita, obesity prevalence, smoking prevalence and PM2.5 air pollution.

The model achieves:

- **R² = 0.822**
- **Mean Absolute Error = 2.59 years**
- **Observations = 155**

The results show that GDP per capita remains the strongest predictor of life expectancy, but the model improves when healthcare spending, lifestyle risks and environmental exposure are added.

Health expenditure per capita is more informative than healthcare spending as a percentage of GDP, while smoking prevalence is the most informative lifestyle variable. Education appears to be a promising social determinant, but it is not included in the final model because of limited data coverage.

Overall, the project suggests that life expectancy is best understood as a multidimensional outcome. Economic development matters most, but healthcare capacity, behavioral risks, environmental exposure and social development also contribute to explaining why people live longer in some countries than in others.

---

## 1. Introduction

Life expectancy is one of the most important indicators of a society’s overall well-being. It reflects not only the quality of healthcare systems, but also broader economic, social, behavioral and environmental conditions.

Countries with higher life expectancy often benefit from stronger economies, better healthcare access, healthier living conditions, safer environments and higher levels of social development. However, these factors do not operate independently. Economic development may support better healthcare systems, while education may influence health behaviors, and environmental exposure may affect long-term health outcomes.

For this reason, life expectancy should not be analyzed as the result of a single factor. A multidimensional approach is needed to understand how different categories of variables contribute to cross-country differences in longevity.

This project uses machine learning methods to analyze the relationship between life expectancy and several explanatory variables across countries. The goal is not only to build a predictive model, but also to understand which macro-categories of variables are most informative.

---

## 2. Research Question and Project Objective

The central research question is:

> **Which economic, healthcare, lifestyle, environmental and social factors best explain differences in life expectancy across countries?**

The objective of the project is to compare different groups of explanatory variables and evaluate how they contribute to the prediction of life expectancy.

The analysis focuses on five macro-categories:

1. **Economic factors**
2. **Healthcare factors**
3. **Lifestyle factors**
4. **Environmental factors**
5. **Social factors**

The project starts from simple baseline models and progressively adds new categories of variables. This allows the analysis to evaluate whether each additional dimension improves the understanding of life expectancy across countries.

---

## 3. Data Sources and Variable Framework

The project uses country-level international data from public sources, mainly World Bank indicators and World Bank Data360 health-related data.

The target variable is **life expectancy at birth**.

The explanatory variables are organized as follows:

| Macro-category | Variable |
|---|---|
| Target | Life expectancy |
| Economic | GDP per capita |
| Healthcare | Health expenditure as % of GDP |
| Healthcare | Health expenditure per capita |
| Lifestyle | Obesity prevalence |
| Lifestyle | Smoking prevalence |
| Environmental | PM2.5 air pollution |
| Social | Education |

Most variables refer to 2022. However, PM2.5 air pollution data were not available for 2022 in the selected indicator. Therefore, 2020 PM2.5 exposure was used as the most recent available environmental proxy with broad country coverage.

The final model dataset includes 155 observations and contains no missing values across the selected predictors.

---

## 4. Data Cleaning and Preparation

The data preparation process involved merging multiple country-level datasets by country code and selecting the most recent available values for each variable.

The cleaning process included:

- selecting relevant variables;
- harmonizing country identifiers;
- filtering observations by year;
- checking missing values;
- removing incomplete observations model by model;
- checking for potential World Bank aggregate groups;
- validating the final model dataset.

The final model dataset used for M9 contains:

| Check | Result |
|---|---:|
| Observations | 155 |
| Missing values | 0 |
| Potential aggregate observations | 0 |
| Final model | M9 |

This audit is important because the analysis compares countries, not regional or income-level aggregate groups. The final model dataset was checked to ensure that no detected aggregate observations remained.

---

## 5. Exploratory Data Analysis

The exploratory analysis focuses on the main relationships between life expectancy and the explanatory variables used in the final model.

The most important relationship is between GDP per capita and life expectancy. The raw relationship is positive but non-linear, suggesting that economic development is strongly associated with longevity, especially at lower income levels.

The log transformation of GDP per capita makes this relationship more linear, supporting the idea of diminishing returns to income.

Environmental exposure is also explored through PM2.5 air pollution, which provides additional information beyond economic and healthcare variables.

The final report includes the following visualizations:

- GDP per capita vs life expectancy
- Log GDP per capita vs life expectancy
- Air pollution vs life expectancy
- Model comparison by R²
- Model comparison by MAE
- M9 feature importance

---

## 6. Modeling Strategy

The modeling strategy follows a progressive structure.

The analysis starts with simple economic and healthcare baselines and then adds additional macro-categories step by step.

The models tested are:

| Model | Description |
|---|---|
| M1 | Baseline Linear Regression |
| M2 | Log-GDP Linear Regression |
| M3 | Baseline Random Forest |
| M4 | Social Extension Random Forest |
| M5 | Obesity Extension Random Forest |
| M6 | Lifestyle Extension Random Forest |
| M7 | Absolute Healthcare Spending Random Forest |
| M8 | Lifestyle & Environment Random Forest |
| M9 | Absolute Healthcare & Environment Random Forest |

Two types of models are used.

First, Linear Regression models are used as interpretable baselines. The Log-GDP Linear Regression model is included to test whether the relationship between income and life expectancy is non-linear.

Second, Random Forest Regression models are used to capture non-linear relationships and compare feature importance across predictors.

---

## 7. Model Results

Nine models were tested and compared using R², Mean Absolute Error and number of observations.

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

The results show a clear progression.

The baseline linear model performs relatively weakly, with an R² of 0.447. When GDP per capita is log-transformed, performance improves substantially, with R² increasing to 0.789. This supports the idea that the relationship between GDP and life expectancy is non-linear.

The Random Forest models generally perform well, especially when lifestyle and environmental variables are included.

M9 achieves the highest R² among all tested models, with an R² of 0.822 and a mean absolute error of 2.59 years.

M4 achieves a slightly lower MAE of 2.58 years, but it uses only 107 observations and has a much lower R² of 0.630. Therefore, it is not selected as the final model.

---

## 8. Feature Importance and Interpretation

The final model, M9, produced the following feature importance ranking:

| Feature | Importance |
|---|---:|
| GDP per capita | 0.637 |
| Health expenditure per capita | 0.195 |
| Smoking prevalence | 0.078 |
| PM2.5 air pollution | 0.053 |
| Obesity prevalence | 0.037 |

GDP per capita remains the dominant predictor, confirming the central role of economic development in explaining cross-country differences in life expectancy.

Health expenditure per capita is the second most important variable. This suggests that absolute healthcare spending per person is more informative than healthcare spending as a percentage of GDP.

Smoking prevalence is the most informative lifestyle variable, while PM2.5 air pollution provides moderate additional predictive value.

Obesity prevalence has the lowest feature importance in the final model. This does not mean that obesity is irrelevant for health. Rather, in this cross-country predictive setting, obesity provides less additional information than the other selected variables.

---

## 9. Final Model Selection

The final selected model is **M9 — Absolute Healthcare & Environment Random Forest**.

It is selected because it provides the strongest overall balance between:

- explanatory performance;
- predictive accuracy;
- sample size;
- interpretability;
- conceptual completeness.

M9 includes economic, healthcare, lifestyle and environmental dimensions. It achieves the highest R² among all tested models while maintaining a reasonably large sample of 155 observations.

Although M4 has a slightly lower MAE, it is not selected because it uses a much smaller sample and has substantially lower explanatory power. The M4 result is still important because it suggests that education may be a relevant social determinant, but the available education data are too limited to include it in the final model.

---

## 10. Limitations

This project should be interpreted as a predictive and exploratory analysis, not as a causal study.

The main limitations are:

- The analysis is cross-sectional.
- Random Forest feature importance is predictive, not causal.
- Education is limited by data availability.
- PM2.5 air pollution uses 2020 data as a proxy because 2022 data were unavailable.
- BMI-based obesity prevalence is an imperfect measure of unhealthy body composition.
- GDP per capita and health expenditure per capita are likely correlated.
- Other relevant factors, such as institutions, inequality, sanitation, vaccination, conflict or demographic structure, are not included.

These limitations do not invalidate the analysis, but they define the scope of the conclusions. The results should be understood as evidence of predictive associations rather than causal relationships.

---

## 11. Conclusion

The project shows that cross-country differences in life expectancy are best explained through a multidimensional framework.

GDP per capita is the strongest predictor of life expectancy, confirming the central role of economic development. However, the model improves when healthcare spending, lifestyle risks and environmental exposure are added.

The final model suggests that absolute healthcare spending per person is more informative than healthcare spending as a percentage of GDP. Smoking prevalence is the most relevant lifestyle variable, while PM2.5 air pollution contributes moderate additional information.

Education appears to be an important social determinant, but limited data coverage prevents it from being included in the final model without reducing the sample size substantially.

Overall, life expectancy is not explained by income alone. Economic development provides the strongest foundation, but healthcare resources, lifestyle risks, environmental exposure and social conditions all contribute to understanding why people live longer in some countries than in others.

**A healthy society is not simply a richer society. Economic development matters most, but longer life expectancy also depends on how resources are translated into healthcare capacity, healthier behaviors, cleaner environments and broader social development.**