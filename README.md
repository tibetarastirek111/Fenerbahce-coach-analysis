# Performance Analysis of Fenerbahçe Football Team Based on Manager Selection (Domestic vs Foreign)

**DSA210 – Introduction to Data Science (Fall 2025)**  
**Author:** Tibet Aras Tirek  

---

## Project Motivation

Football clubs make strategic decisions when appointing head coaches, and the nationality of these coaches is often a subject of debate among fans, analysts, and club management. For a club like **Fenerbahçe**, which has experienced frequent managerial changes between **2005–2006 and 2024–2025**, understanding whether **Turkish or foreign coaches perform differently** is an important analytical question.

This project analyzes **season-level performance data** of all Fenerbahçe head coaches during this period. Using manually compiled datasets, the study examines whether coach nationality is associated with differences in team performance.

The analysis is conducted in three complementary stages:

1. **Exploratory Data Analysis (EDA)** to understand historical performance patterns  
2. **Hypothesis Testing** to statistically evaluate performance differences  
3. **Machine Learning (Regression)** to model and predict seasonal performance  

The primary focus is **interpretation and analytical rigor**, rather than maximizing predictive accuracy.

---

## Project Objectives

- Compile a clean, season-level dataset of Fenerbahçe head coaches (2005–2025)
- Perform structured **exploratory data analysis (EDA)** on key performance metrics
- Engineer meaningful features such as:
  - Coach nationality (`is_foreign`)
  - Trophy indicator (`has_trophy`)
  - Season start year
- Conduct **formal hypothesis testing** to compare Turkish and foreign coaches
- Build an interpretable **regression-based machine learning model**
- Evaluate whether coach nationality has a measurable effect on performance
- Present results through clear tables, plots, and statistical interpretation

---

## Data Sources

All data were **manually collected** from publicly available football resources:

- Transfermarkt  
- Wikipedia – Fenerbahçe Managers  
- Turkish Football Federation (TFF)  
- Mackolik Archive  

### Raw Data Files

The following Excel files were used:

- `fenerbahce_coaches_data.xlsx` – Season-level coaching performance data  
- `fenerbahce_coaches_data2.xlsx` – Supplementary aggregated data (foreign coaches)  
- `fenerbahce_coaches_data3.xlsx` – Supplementary aggregated data (Turkish coaches)  
- `market_values.xlsx` – Squad market values by season (used only in ML stage)

All datasets were cleaned, merged, and processed within the analysis notebooks.

---

## Data Structure

The core dataset used for EDA and hypothesis testing is season-based and includes the following variables:

| Variable | Description |
|--------|------------|
| `season` | Season (e.g., 2005–2006) |
| `season_start_year` | First year of the season |
| `coach_name` | Head coach name |
| `nationality` | Coach nationality |
| `is_foreign` | 1 = Foreign, 0 = Turkish |
| `total_matches` | Matches coached that season |
| `win`, `draw`, `loss` | Match outcomes |
| `points_per_game` | Average points per game |
| `win_rate` | Win percentage |
| `avg_goals_scored` | Goals scored per match |
| `avg_goals_conceded` | Goals conceded per match |
| `trophies_text` | Trophy description (if any) |
| `has_trophy` | 1 if at least one trophy won |

---

## 1. Exploratory Data Analysis (EDA)

EDA was conducted to understand **historical performance patterns** and differences between Turkish and foreign coaches.

### EDA Components

- **Descriptive Statistics**
  - Mean, median, standard deviation of:
    - Points per game (PPG)
    - Win rate
    - Goals scored and conceded
    - Trophy rate
- **Nationality-Based Comparisons**
  - Bar plots comparing average PPG
  - Boxplots showing PPG distributions
- **Win Rate Analysis**
  - Group-wise summary statistics
  - Distribution comparison
- **Goal Performance Analysis**
  - Offensive (goals scored)
  - Defensive (goals conceded)
- **Trophy Analysis**
  - Trophy rate by nationality:
    - `trophy_rate = seasons_with_trophy / total_seasons`
- **Time Trends**
  - Line plots of PPG and win rate over time
  - Colored by coach nationality
- **Coach-Level Summaries**
  - Aggregated performance profiles for individual coaches

EDA results provided descriptive insights but did not establish statistical significance.

---

## 2. Hypothesis Testing

### Main Hypothesis

- **H₀ (Null Hypothesis):**  
  There is **no statistically significant difference** in overall performance between Turkish and foreign coaches.

- **H₁ (Alternative Hypothesis):**  
  There **is a statistically significant difference** in overall performance between Turkish and foreign coaches.

### Performance Metric Used

- **Points Per Game (PPG)** was selected as the primary indicator of overall performance.

### Statistical Procedure

1. **Normality Testing**
   - Shapiro–Wilk test applied separately to Turkish and foreign coach PPG distributions
   - Result:
     - Turkish group: approximately normal
     - Foreign group: non-normal

2. **Variance Homogeneity**
   - Levene’s test indicated equal variances

3. **Test Selection**
   - Due to non-normality in one group:
     - **Mann–Whitney U test** was used

### Results

- Mann–Whitney U statistic = 100.0  
- p-value = 0.2419  

### Conclusion

Since **p > 0.05**, the null hypothesis **could not be rejected**.

➡️ There is **no statistically significant difference** in points per game between Turkish and foreign coaches.

---

## 3. Machine Learning: Regression Analysis

### Objective

To model and predict **season-level Points Per Game (PPG)** using historical performance metrics and squad market value information.

### Dataset Used

- Season-level coaching performance data  
- Market value data merged by season  
- Time-ordered dataset (chronological split)

### Feature Engineering

Additional features created:

- Lagged market value (`mv_lag_1`)
- Market value percentage change
- Rolling mean and standard deviation of market value
- Season start year

Initial rows with missing lag/rolling values were dropped.

---

### Model: Ridge Regression

**Target Variable**
- `points_per_game`

**Features**
- Market value features (current, lag, trend, rolling)
- Goals scored and conceded
- Win rate
- Match volume indicators

**Training Strategy**
- Chronological train-test split (75% / 25%)
- No data leakage across seasons
- Pipeline-based preprocessing:
  - Median imputation
  - Standard scaling

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² score
- Comparison against a baseline (mean PPG predictor)

### Outcome

- The regression model significantly outperformed the baseline
- Market value dynamics and performance metrics explained a meaningful portion of PPG variance
- Results were interpreted **analytically**, not as a production-grade prediction system

---

## Key Takeaways

- Turkish coaches show **slightly higher average performance**, but
- **No statistically significant difference** was found between Turkish and foreign coaches
- Market value trends help explain seasonal success but do not fully determine outcomes
- Results highlight the **complexity of football performance** beyond nationality

---

## Limitations & Future Work

- Single-club analysis
- Small sample size (season-level data)
- No player-level or tactical variables
- Future extensions:
  - Multi-club comparison
  - Panel data methods
  - Time-series models

---

## Project Timeline

| Phase | Description | Date |
|-----|------------|------|
| Phase 1 | Proposal | Oct 31, 2025 |
| Phase 2 | Data Collection & EDA | Nov 28, 2025 |
| Phase 3 | Hypothesis Testing & ML | Jan 2, 2026 |
| Phase 4 | Final Submission | Jan 9, 2026 |

