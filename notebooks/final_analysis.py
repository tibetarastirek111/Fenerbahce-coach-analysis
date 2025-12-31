# =========================
# 0) Imports
# =========================
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =========================
# 1) Load data (Colab local files)
# =========================
df_coaches = pd.read_excel("fenerbahce_coaches_data.xlsx")
df_market  = pd.read_excel("market_values.xlsx")

# Basic cleaning
df_coaches["season"] = df_coaches["season"].astype(str).str.strip()
df_market["season"]  = df_market["season"].astype(str).str.strip()

# Create a common merge key: season_start_year
df_coaches["season_start_year"] = df_coaches["season"].str[:4].astype(int)
df_market["season_start_year"]  = df_market["season"].str[:4].astype(int)

# Merge on season_start_year (robust)
df = pd.merge(
    df_coaches,
    df_market[["season_start_year", "avg_market_value_mil_euro"]],
    on="season_start_year",
    how="inner"
).copy()

# Sort chronologically
df = df.sort_values("season_start_year").reset_index(drop=True)

print("Merged shape:", df.shape)
print("Year range:", df["season_start_year"].min(), "→", df["season_start_year"].max())

# =========================
# 2) Feature engineering (market value dynamics)
#    - NO dropna() that kills rows
# =========================
mv = df["avg_market_value_mil_euro"].astype(float)

df["mv_lag_1"] = mv.shift(1)
df["mv_pct_change"] = mv.pct_change()
df["mv_roll_mean_3"] = mv.rolling(3).mean()
df["mv_roll_std_3"]  = mv.rolling(3).std()

# Fill ONLY engineered NaNs (first rows)
engineered_cols = ["mv_lag_1","mv_pct_change","mv_roll_mean_3","mv_roll_std_3"]
df[engineered_cols] = df[engineered_cols].bfill()

# =========================
# 3) Select target + features
# =========================
target = "points_per_game"
assert target in df.columns, "Target column points_per_game not found!"

# Candidate feature set (we keep only those that exist)
numeric_candidates = [
    "avg_market_value_mil_euro",
    "mv_lag_1",
    "mv_pct_change",
    "mv_roll_mean_3",
    "mv_roll_std_3",
    "avg_goals_conceded",
    "avg_goals_scored",
    "win_rate",
    "total_matches"
]
categorical_candidates = ["is_foreign"]

numeric_features = [c for c in numeric_candidates if c in df.columns]
categorical_features = [c for c in categorical_candidates if c in df.columns]

# Drop rows only if target is missing
df = df.dropna(subset=[target]).reset_index(drop=True)

X = df[numeric_features + categorical_features].copy()
y = df[target].astype(float).copy()

print("Features used:", numeric_features + categorical_features)
print("Final dataset rows:", len(df))

# =========================
# 4) Time-based train/test split (last 25% = test)
# =========================
split = int(len(df) * 0.75)

X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

train_years = (df.iloc[:split]["season_start_year"].min(), df.iloc[:split]["season_start_year"].max())
test_years  = (df.iloc[split:]["season_start_year"].min(), df.iloc[split:]["season_start_year"].max())

print("Train years:", train_years[0], "→", train_years[1], "| n =", len(X_train))
print("Test years :", test_years[0],  "→", test_years[1],  "| n =", len(X_test))

# =========================
# 5) Pipeline (preprocess + Ridge regression)
# =========================
num_tf = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_tf = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocess = ColumnTransformer([
    ("num", num_tf, numeric_features),
    ("cat", cat_tf, categorical_features)
], remainder="drop")

pipe = Pipeline([
    ("prep", preprocess),
    ("model", Ridge(alpha=1.0))
])

pipe.fit(X_train, y_train)

# =========================
# 6) Evaluation (NO squared=False, compatible)
# =========================
pred = pipe.predict(X_test)

mae  = mean_absolute_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2   = r2_score(y_test, pred)

print("\n=== Ridge Test Performance ===")
print("MAE :", mae)
print("RMSE:", rmse)
print("R2  :", r2)

# Baseline: predict train mean
baseline = np.repeat(y_train.mean(), len(y_test))
mae_b  = mean_absolute_error(y_test, baseline)
rmse_b = np.sqrt(mean_squared_error(y_test, baseline))

print("\n=== Baseline (Train Mean) ===")
print("MAE :", mae_b)
print("RMSE:", rmse_b)

# Prediction table
result = pd.DataFrame({
    "year": df.iloc[split:]["season_start_year"].values,
    "actual_ppg": y_test.values,
    "pred_ppg": pred
})

print("\nPrediction table:")
result
