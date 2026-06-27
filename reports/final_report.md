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

The project is therefore both predictive and interpretative. It aims to identify a strong final model, but also to understand what the model suggests about the broader determinants of longevity.

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

A specific methodological note concerns obesity prevalence. In this project, obesity is measured using a standard BMI-based definition: the percentage of adults with a body mass index of 30 kg/m² or higher. This is a widely used population-level indicator and is appropriate for international comparison, but BMI does not directly measure body fat and does not distinguish between fat mass, muscle mass and bone mass. Therefore, obesity prevalence should be interpreted as an approximate population-level indicator rather than a perfect measure of unhealthy body composition.

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

This audit is important because the analysis compares countries, not regional or income-level aggregate groups. The initial merged dataset still contained some potential World Bank aggregate groups, but the final model dataset was checked to ensure that no detected aggregate observations remained.

The data cleaning process also checked for implausible life expectancy values. No observations below 40 years remained in the cleaned datasets used for the final analysis.

Overall, the cleaning and audit process ensures that the final model is based on a consistent country-level dataset with complete information for all selected predictors.

---

## 5. Exploratory Data Analysis

The exploratory analysis focuses on the main relationships between life expectancy and the explanatory variables used in the final model.

The most important relationship is between GDP per capita and life expectancy. The raw relationship is positive but non-linear, suggesting that economic development is strongly associated with longevity, especially at lower income levels.

The log transformation of GDP per capita makes this relationship more linear, supporting the idea of diminishing returns to income.

Environmental exposure is also explored through PM2.5 air pollution, which provides additional information beyond economic and healthcare variables.

### GDP per Capita and Life Expectancy

![GDP per Capita vs Life Expectancy](figures_report/01_gdp_vs_life_expectancy.png)

The relationship between GDP per capita and life expectancy is positive but non-linear. This suggests that economic development is strongly associated with longer life expectancy, but the marginal association appears stronger at lower income levels and weaker at higher income levels.

### Log GDP per Capita and Life Expectancy

![Log GDP per Capita vs Life Expectancy](figures_report/02_log_gdp_vs_life_expectancy.png)

The log transformation makes the relationship between GDP per capita and life expectancy more linear. This supports the interpretation of diminishing returns to income: additional income is more strongly associated with life expectancy improvements in lower-income countries than in already wealthy countries.

### Air Pollution and Life Expectancy

![PM2.5 Air Pollution vs Life Expectancy](figures_report/03_air_pollution_vs_life_expectancy.png)

PM2.5 air pollution provides an environmental perspective on life expectancy. The variable is not interpreted causally, but it adds useful predictive information in the final Random Forest models.

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

The progressive model structure allows the analysis to evaluate whether adding social, lifestyle and environmental variables improves the understanding of life expectancy beyond economic and healthcare baselines.

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

### Model Comparison by R²

![Model Comparison by R²](figures_report/04_model_comparison_r2.png)

The R² comparison shows that M9 achieves the highest explanatory performance among all tested models.

### Model Comparison by Mean Absolute Error

![Model Comparison by MAE](figures_report/05_model_comparison_mae.png)

The MAE comparison shows that M4 has the lowest error, but it uses a much smaller sample and has substantially lower R². M9 therefore remains the strongest final model candidate because it balances predictive accuracy, explanatory performance and sample size.

---

## 8. Feature Importance

The final model, M9, produced the following feature importance ranking:

| Feature | Importance |
|---|---:|
| GDP per capita | 0.637 |
| Health expenditure per capita | 0.195 |
| Smoking prevalence | 0.078 |
| PM2.5 air pollution | 0.053 |
| Obesity prevalence | 0.037 |

### M9 Feature Importance Chart

![M9 Feature Importance](figures_report/06_m9_feature_importance.png)

The chart confirms that GDP per capita is by far the most important predictor in the final model. Health expenditure per capita is the second most important variable, followed by smoking prevalence, air pollution and obesity prevalence.

Feature importance should not be interpreted causally. It shows which variables are useful for prediction within the Random Forest model, not which variables independently cause life expectancy to increase or decrease.

---

## 9. Interpretation by Macro-category

### 9.1 Economic Factors

The most important macro-category in the project is **economic development**, measured by GDP per capita.

GDP per capita is the dominant predictor in every Random Forest model. In the final model M9, it has a feature importance of approximately 63.7%, by far the highest feature importance in the final model.

This result suggests that countries with higher income levels tend to have higher life expectancy. This makes intuitive sense: richer countries generally have better infrastructure, better nutrition, better housing, stronger institutions, wider access to healthcare, better sanitation and more resources for prevention and treatment.

A key point is that GDP per capita remains the most important variable even though its feature importance decreases when additional variables are added. In the baseline Random Forest model M3, GDP per capita has feature importance of approximately 83.2%. In the final model M9, after adding healthcare spending per capita, obesity, smoking and air pollution, it decreases to 63.7%.

This decrease should not be interpreted as GDP becoming unimportant. Rather, it means that part of the predictive information previously captured by GDP is now shared with more specific variables, especially health expenditure per capita. Even after this redistribution, GDP per capita remains clearly the strongest predictor.

This is important because GDP per capita is not only a narrow income measure. It can also act as a proxy for broader social and institutional conditions that support longevity, such as better healthcare infrastructure, better nutrition, higher living standards, better sanitation, stronger institutions, higher education levels, better housing and greater access to prevention and treatment.

However, the relationship between GDP and life expectancy is not simply linear. The strong improvement from M1 to M2 suggests the presence of diminishing returns to income. In practical terms, an increase in GDP per capita is likely to be more strongly associated with life expectancy improvements in lower-income countries than in already wealthy countries.

A careful conclusion is that **economic development is the strongest predictor of life expectancy in the dataset, but its relationship with life expectancy appears to follow a diminishing-returns pattern**.

### 9.2 Healthcare Factors

Healthcare spending is another important dimension, but the project shows that **how healthcare spending is measured matters**.

Two healthcare variables were tested:

1. **Health expenditure as a percentage of GDP**
2. **Health expenditure per capita**

Health expenditure as a percentage of GDP measures the share of a country’s economy devoted to healthcare. It is a relative measure.

Health expenditure per capita measures the average amount of healthcare spending per person. It is an absolute measure.

The results suggest that health expenditure per capita is more informative than health expenditure as a percentage of GDP in the final model structure.

In M8, which uses health expenditure as a percentage of GDP, the healthcare variable has feature importance of approximately 6.0%. In M9, which replaces it with health expenditure per capita, the healthcare variable has feature importance of approximately 19.5%.

Moreover, replacing relative healthcare spending with absolute healthcare spending improves model performance:

- **M8:** R² = 0.812, MAE = 2.70
- **M9:** R² = 0.822, MAE = 2.59

This suggests that the amount spent per person may be more closely related to life expectancy than the share of GDP allocated to healthcare.

This makes sense. A country with a low GDP may spend a high percentage of GDP on healthcare but still spend little per person in absolute terms. Another country may spend a lower percentage of GDP on healthcare but, because its economy is much larger, still spend far more per person.

For this reason, health expenditure per capita may better capture the actual healthcare resources available to individuals and healthcare systems.

However, healthcare spending per capita is also likely to be correlated with GDP per capita. This means it should not be interpreted as a purely independent causal effect. The model shows predictive importance, not causality.

A balanced interpretation is that **health expenditure per capita better captures the absolute healthcare resources available to a population, but because it is closely related to national income, this should be interpreted as predictive evidence rather than causal proof**.

### 9.3 Lifestyle Factors

The project tested two lifestyle variables:

- **Smoking prevalence**
- **Obesity prevalence**

The results suggest that lifestyle variables add useful information beyond economic and healthcare factors, especially smoking.

In the lifestyle model M6, adding obesity and smoking improved performance compared with the baseline Random Forest:

- **M3:** R² = 0.757, MAE = 2.75
- **M6:** R² = 0.802, MAE = 2.77

The MAE does not improve much in this comparison, but the R² increases substantially. This indicates that lifestyle variables help explain more variation in life expectancy.

Among the two lifestyle variables, smoking is consistently more important than obesity. In M9, smoking has feature importance of approximately 7.8%, while obesity has feature importance of approximately 3.7%.

This does not mean obesity is irrelevant. It means that, in this cross-country dataset and within the selected model structure, smoking prevalence provides more predictive information than obesity prevalence.

Smoking has a direct relationship with many causes of mortality, including cardiovascular disease, respiratory disease and cancer. Obesity is also important for health, but its cross-country relationship with life expectancy may be more complex. In some countries, higher obesity prevalence may coexist with higher income, better healthcare access and longer life expectancy, which can make its independent predictive role harder to isolate in a cross-country model.

A methodological note is needed for the obesity variable. Obesity prevalence is measured using a BMI-based definition: the percentage of adults with a body mass index of 30 kg/m² or higher. BMI is useful at the population level, but it does not directly measure body fat and does not distinguish between fat mass, muscle mass and bone mass. As a result, some highly muscular individuals may fall into overweight or obesity BMI categories without having the typical excess-fat profile associated with obesity-related risk.

This limitation does not invalidate the use of obesity prevalence in the project, because the analysis is conducted at the country level and the share of highly muscular individuals misclassified as obese is likely to be small relative to the full adult population. However, it should be acknowledged when interpreting obesity’s relatively low feature importance.

Overall, lifestyle factors improve the explanatory power of the model, with smoking prevalence emerging as the most informative lifestyle variable.

### 9.4 Environmental Factors

The environmental variable tested in the project is **PM2.5 air pollution**.

This variable required an important data decision. The selected PM2.5 indicator had no available data for 2022, while 2020 had broad country coverage. Therefore, the project used 2020 PM2.5 exposure as the most recent available environmental proxy.

This is a limitation, but it is also a reasonable modeling choice because air pollution tends to be relatively persistent over time compared with short-term variables. Still, the year mismatch must be clearly acknowledged.

Adding air pollution improved model performance:

- **M6:** R² = 0.802, MAE = 2.77
- **M8:** R² = 0.812, MAE = 2.70

This suggests that air pollution provides additional predictive information beyond economic, healthcare and lifestyle variables.

In the final model M9, air pollution has feature importance of approximately 5.3%. This is not dominant, but it is not negligible either. Air pollution contributes more than obesity in the final model and slightly less than smoking.

The correct interpretation is not that air pollution alone explains life expectancy. Rather, it adds a moderate environmental signal to a broader model.

A careful conclusion is that **environmental exposure, measured through PM2.5 air pollution, provides moderate additional predictive value. It improves the model, although its contribution is smaller than GDP per capita, healthcare spending per capita and smoking**.

### 9.5 Social Factors

The project also tested education as a social determinant of life expectancy.

Education is theoretically very important. It can affect life expectancy through many channels: health literacy, income opportunities, employment, fertility decisions, prevention, access to information and ability to navigate healthcare systems.

In the project, education was included in M4:

**M4 — Social Extension Random Forest**

- GDP per capita
- Health expenditure as % of GDP
- Education

The feature importance results for M4 were very interesting:

- **GDP per capita:** 66.2%
- **Education:** 29.5%
- **Health expenditure as % of GDP:** 4.4%

This suggests that education may provide substantial explanatory information when available.

However, M4 had only 107 observations, much lower than the 155 observations used in M6, M7, M8 and M9. M4 also had a much lower R² of 0.630.

Although M4 achieved a low MAE, this result is less directly comparable because it is based on a smaller sample.

Therefore, education should not be interpreted as unimportant. The better conclusion is that education is **promising but coverage-limited** in this dataset.

The reason education is not included in the final model is not that it has no relationship with life expectancy. On the contrary, the model where education is included suggests that it may be highly informative. The issue is that the available comparable education data reduce the usable sample too much.

This is an important data science lesson: final model selection depends not only on theoretical relevance, but also on data availability and comparability.

---

## 10. Final Model Selection

The final selected model is **M9 — Absolute Healthcare & Environment Random Forest**.

It is selected because it provides the strongest overall balance between:

- explanatory performance;
- predictive accuracy;
- sample size;
- interpretability;
- conceptual completeness.

M9 includes economic, healthcare, lifestyle and environmental dimensions. It achieves the highest R² among all tested models while maintaining a reasonably large sample of 155 observations.

Although M4 has a slightly lower MAE, it is not selected because it uses a much smaller sample and has substantially lower explanatory power. The M4 result is still important because it suggests that education may be a relevant social determinant, but the available education data are too limited to include it in the final model.

M9 is not perfect, but it is the strongest and most balanced model in the project.

---

## 11. Limitations

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

## 12. Conclusion

The project shows that cross-country differences in life expectancy are best explained through a multidimensional framework.

The best-performing model is **M9 — Absolute Healthcare & Environment Random Forest**, which combines GDP per capita, health expenditure per capita, obesity prevalence, smoking prevalence and PM2.5 air pollution. The model achieves an R² of 0.822 and a mean absolute error of 2.59 years across 155 observations.

The most important finding is that GDP per capita remains the dominant predictor of life expectancy, even after adding healthcare, lifestyle and environmental variables. Its feature importance decreases when additional variables are included, but it remains by far the most influential feature in the final model. This suggests that economic development is the strongest explanatory dimension in the dataset.

The second major finding concerns healthcare spending. The project shows that health expenditure per capita is more informative than health expenditure as a percentage of GDP. This is because percentage-based healthcare spending can be misleading: a country with a low GDP may spend a high share of GDP on healthcare but still spend little per person in absolute terms. By contrast, health expenditure per capita better captures the actual healthcare resources available to individuals.

Lifestyle factors also contribute to the model. Smoking prevalence is more informative than obesity prevalence, suggesting that smoking provides stronger predictive information in this cross-country setting. Obesity remains included as a lifestyle risk factor, but its contribution is smaller and should be interpreted with caution because it is measured using BMI-based prevalence.

Environmental factors also matter. PM2.5 air pollution improves model performance and contributes moderate additional predictive value. Its importance is smaller than GDP per capita, healthcare spending per capita and smoking, but it is still higher than obesity in M9.

Education appears to be a promising social determinant. In the social extension model, education has high feature importance, suggesting that it may be strongly related to life expectancy. However, including education reduces the sample size substantially. For this reason, education is not included in the final model, not because it is unimportant, but because the available data are too restrictive for the final cross-country comparison.

Overall, the results suggest that life expectancy is not explained by income alone. Economic development provides the strongest foundation, but healthcare resources, lifestyle risks, environmental exposure and social conditions all contribute to understanding why people live longer in some countries than in others.

At the same time, the project highlights an important lesson in applied data science: the best model is not necessarily the one that includes every theoretically relevant variable. Final model selection must balance predictive performance, sample size, data quality, interpretability and comparability.

**A healthy society is not simply a richer society. Economic development matters most, but longer life expectancy also depends on how resources are translated into healthcare capacity, healthier behaviors, cleaner environments and broader social development.**