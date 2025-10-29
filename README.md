# Performance analysis of Fenerbahçe Football Team based on manager selection (Domestic / Foreign) (DSA210 Term Project)

## Motivation
Fenerbahçe, one of the most established football clubs in Turkey, has had numerous coaches from both Turkish and foreign backgrounds. A long-standing debate has been whether a Turkish or a foreign coach is more suitable for Fenerbahçe. Through this project, I aim to apply data science techniques to answer this question objectively, by analyzing Fenerbahçe’s historical performance under different managers.

---

## Project Goal
The goal of this project is to determine whether **foreign** or **Turkish** head coaches have been **more successful** in Fenerbahçe’s recent history.  
To measure “success,” I will compare key performance metrics such as:
- Win rate (%)
- Average goals scored per match
- Average goals conceded per match
- Number of trophies (league titles, cups)
- Average league position per season  

The main research question:
> *Is there a statistically significant difference in Fenerbahçe’s performance under foreign vs. Turkish head coaches?*

---

## Data Source
I will collect the data manually from publicly available football databases such as:
- Transfermarkt
- Wikipedia – Fenerbahçe SK Managers
- TFF Official Website
- Mackolik

Each row in the dataset will represent one coach’s tenure and include:
| Variable | Description |
|-----------|--------------|
| Coach Name | Name of the manager |
| Nationality | Turkish or Foreign |
| Period | Starting and ending years |
| Total Matches | Number of games managed |
| Wins | Number of wins |
| Draws | Number of draws |
| Losses | Number of losses |
| Win Rate (%) | Calculated as Wins / Total Matches |
| Avg. Goals Scored | Goals scored per match |
| Avg. Goals Conceded | Goals conceded per match |
| Trophies Won | Total number of trophies |

The dataset will be recorded in an Excel file named `fenerbahce_coaches_data.csv`.

---

## Google Colab Link
The project notebook will be developed and shared via Google Colab.  
Link: *to be added after code implementation.*

---

## Methods and Analysis
1. **Data Cleaning**
   - Convert all numeric fields to numeric format.
   - Standardize nationality into two groups: “Turkish” and “Foreign.”
   - Remove missing values or incomplete tenures.

2. **Exploratory Data Analysis (EDA)**
   - Create bar plots to compare average win rates and goals between Turkish and foreign coaches.
   - Use pie charts to show trophy distribution by coach nationality.
   - Visualize historical performance trends over time.

3. **Statistical Testing**
   - Conduct an **independent samples t-test** to check whether win rates differ significantly between Turkish and foreign coaches.
   - Hypotheses:
     - H₀: There is no significant difference in success metrics between Turkish and foreign coaches.
     - H₁: There is a significant difference in success metrics between Turkish and foreign coaches.

4. **Machine Learning (Optional if dataset size allows)**
   - Apply logistic regression to predict “success” (e.g., win rate > 60%) based on nationality and other features.

---

## Expected Findings
- Identify whether nationality has a measurable impact on performance.
- Quantify which type of manager tends to perform better statistically.
- Provide visual and data-driven insights to support or challenge fan opinions.

---

## Limitations and Future Work
**Limitations**
- Limited number of coaches may reduce statistical power.
- Trophy success can be influenced by factors beyond coaching (player quality, injuries, management).
- Data may not include cup matches or unofficial tournaments.

**Future Work**
- Extend the analysis to other Turkish football clubs (e.g., Galatasaray, Beşiktaş) for comparison.
- Incorporate player statistics or transfer spending into the model.
- Use advanced models to predict performance trends under future coaches.

---

## Files
- `fenerbahce_coaches_data.csv` — manually collected dataset  
- `DSA210_project.ipynb` — Python code for analysis  
- `README.md` — project documentation  

---

## Conclusion
This project aims to apply data science techniques to a culturally and statistically interesting question for football fans: whether Turkish or foreign coaches have brought more success to Fenerbahçe. By analyzing historical data and testing hypotheses, I hope to provide data-driven insights into a long-standing debate.
