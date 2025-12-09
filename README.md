# Performance analysis of Fenerbahçe Football Team based on manager selection (Domestic / Foreign)
**DSA210 - Introduction to Data Science (Fall 2025) - Tibet Aras Tirek**
---

# Project Motivation

Football clubs make strategic choices when appointing head coaches, and the nationality of these coaches is often a key discussion topic among fans, analysts, and club management. For a club like **Fenerbahçe**, which has experienced many coaching changes between 2005 and 2025, understanding whether **Turkish** or **foreign** coaches perform better is an important analytical question.

This project aims to **analyze the seasonal performance metrics** of all Fenerbahçe head coaches who managed the team between **2005–2006 and 2024–2025**, using manually compiled datasets.  
By comparing performance indicators such as:

- Points Per Game (PPG)  
- Win Rate (%)  
- Goals scored & conceded  
- Trophy achievements  

and by building basic machine learning models that incorporate coach nationality as a feature, the project investigates whether nationality systematically influences success.

The ultimate goal is to determine **whether there is a significant difference between domestic and foreign coaches**, what factors influence performance, and how accurately a model can capture seasonal success patterns.

---

# Objectives

- Collect and organize season-level coaching performance data (2005–2025)
- Perform **data cleaning** and **exploratory data analysis (EDA)**
- Engineer additional variables such as:
  - `is_foreign` (0 = Turkish, 1 = Foreign)
  - `has_trophy` (0/1)
  - `season_start_year`
- Conduct **hypothesis testing** to evaluate differences between Turkish and foreign coaches
- Build **machine learning models** to examine how nationality and other features influence performance
- Visualize key differences with bar plots, line charts, and distribution plots
- Interpret results and discuss real-world implications for football management

---

## Data Source
Data will be collected manually from publicly available football databases such as:
- Transfermarkt
- Wikipedia – Fenerbahçe SK Managers
- TFF Official Website
- Mackolik

Three raw Excel files were provided:

- `fenerbahce_coaches_data.xlsx` – Season-level detailed stats  
- `fenerbahce_coaches_data2.xlsx` – Aggregated summary for foreign coaches  
- `fenerbahce_coaches_data3.xlsx` – Aggregated summary for domestic coaches  

All data will be cleaned and merged into:

- `data/processed/fenerbahce_coaches_seasons.csv`

---
# Data Structure

The processed CSV will include (at least) the following variables:

| Variable            | Description                                   | Type        |
|---------------------|-----------------------------------------------|-------------|
| season              | Season (e.g. 2005–2006)                       | Categorical |
| coach_name          | Name of head coach                            | String      |
| nationality         | Country of coach                              | String      |
| is_foreign          | 1 if coach is foreign, 0 if Turkish           | Binary      |
| total_matches       | Total matches coached in that season          | Numerical   |
| win                 | Number of wins                                | Numerical   |
| draw                | Number of draws                               | Numerical   |
| loss                | Number of losses                              | Numerical   |
| points_per_game     | Points per game average                       | Numerical   |
| win_rate            | Win percentage                                | Numerical   |
| avg_goals_scored    | Average goals scored per match                | Numerical   |
| avg_goals_conceded  | Average goals conceded per match              | Numerical   |
| trophies_text       | Cup names (if any)                            | Categorical |
| has_trophy          | 1 if trophy won that season                   | Binary      |
| season_start_year   | First year of the season (e.g., 2005)         | Numerical   |

# Methods

## 1. Exploratory Data Analysis (EDA)

The EDA focuses on understanding seasonal performance differences between Turkish and foreign coaches.

### Planned EDA Steps

1. **Descriptive Statistics**
   - Mean, median, and distribution of PPG, win rate, goals scored/conceded and trophy rate by nationality.

2. **Points Per Game Comparison**
   - Bar plots of average PPG by nationality.
   - Boxplots of PPG distribution for Turkish vs foreign coaches.

3. **Win Rate Analysis**
   - Comparison of win percentages between groups.

4. **Goal Performance**
   - Comparison of average goals scored and conceded per match for each nationality group.

5. **Trophy Achievements**
   - Calculation of trophy rate:
     - `trophy_rate = total seasons with trophy / total seasons coached`
   - Comparison between Turkish and foreign coaches.

6. **Trend Over Time**
   - Line plots of PPG and win rate over seasons, colored by coach nationality.
   - Identification of periods dominated by domestic or foreign coaches.

7. **Coach-Level Profiles**
   - Summary tables and visual comparisons of key coaches (e.g., Christoph Daum, Arthur Zico, Luis Aragones, Vitor Pereira, Aykut Kocaman, Ersun Yanal, İsmail Kartal, Jorge Jesus, Jose Mourinho).

---

## 2. Hypothesis Testing

### Main Hypothesis

- **H₀ (Null Hypothesis):**  
  There is **no significant difference** in overall performance between Turkish and foreign coaches.

- **H₁ (Alternative Hypothesis):**  
  There **is a significant difference** in overall performance between Turkish and foreign coaches.
## Research Sub-Questions (Supporting the Main Hypothesis)

In addition to the main hypothesis comparing overall performance between Turkish and foreign coaches, the project also investigates several **research sub-questions**.  
These are not formal hypotheses but **supporting analytical questions** that help interpret performance differences more precisely.

### **Sub-Analysis 1 — Points Per Game (PPG)**
**Research Question:**  
Do Turkish and foreign coaches differ significantly in their average **Points Per Game**?

### **Sub-Analysis 2 — Win Rate (%)**
**Research Question:**  
Is there a meaningful difference in the **win rate** of Turkish vs foreign coaches?

### **Sub-Analysis 3 — Goal Performance**
This analysis examines offensive and defensive strength:

- **Average Goals Scored per Match**  
  *Do foreign or Turkish coaches score more goals on average?*

- **Average Goals Conceded per Match**  
  *Do the two groups differ in defensive performance?*


### Metrics to be Tested

- Points Per Game (PPG)  
- Win Rate (%)  
- Goals scored per match  
- Goals conceded per match  
- Trophy rate (proportion of seasons with trophies)

### Statistical Tests

Depending on the distributional assumptions:

- **Two-sample t-test**
  - To compare mean PPG and win rates between Turkish and foreign coaches.

- **Chi-Square Test of Independence**  
  - To compare trophy-winning rates (has_trophy) between the two nationality groups.

These tests follow the hypothesis testing framework introduced in the DSA210 course and will be used to determine whether nationality is associated with significant performance differences.

---

## 3. ML Model

### Model 1 – Logistic Regression: Trophy Prediction

**Goal:**  
Predict whether a season ends with at least one trophy (`has_trophy` = 1) based on season-level performance metrics.

**Features (candidate set):**

- `points_per_game`  
- `win_rate`  
- `avg_goals_scored`  
- `avg_goals_conceded`  
- `is_foreign`  
- Possibly `total_matches` or `season_start_year`

**Target:**

- `has_trophy` (Binary)

**Evaluation:**

- Accuracy  
- Precision, Recall, F1-score (interpreted cautiously due to small sample size)  

The focus is on **interpretation of coefficients**, especially the effect of `is_foreign` on the probability of winning a trophy.

---

### Model 2 – Linear Regression: Predicting Points Per Game

**Goal:**  
Estimate a season’s PPG using coach nationality and other features.

**Features (candidate set):**

- `is_foreign`  
- `season_start_year`  
- `avg_goals_scored`  
- `avg_goals_conceded`  
- Possibly trophy-related or match-related variables

**Target:**

- `points_per_game` (Numerical)

**Evaluation:**

- R², RMSE  
- Inspection of regression coefficients  

Again, the main goal is **understanding** rather than high predictive power. The coefficient for `is_foreign` will be interpreted as the estimated impact of being a foreign coach on PPG, controlling for other variables.

---

# Expected Results

- A cleaned and well-documented dataset:  
  - `data/processed/fenerbahce_coaches_seasons.csv`
- EDA and visualization outputs (plots comparing Turkish vs foreign coaches)
- Statistical test results for performance metrics and trophy rates
- Interpretable machine learning models:
  - Logistic regression for trophy prediction
  - Linear regression for PPG estimation
- Discussion of whether foreign or Turkish coaches have systematically better performance
- Identification of limitations (small dataset, single club, season-level aggregation) and ideas for future work

---

## Project Timeline  
| Phase | Description | Deadline |
|-------|--------------|-----------|
| **Phase 1** | Project proposal | **Oct 31, 2025** |
| **Phase 2** | Data collection & EDA | **Nov 28, 2025** |
| **Phase 3** | ML implementation | **Jan 2, 2026** |
| **Phase 4** | Final report & submission | **Jan 9, 2026** |
