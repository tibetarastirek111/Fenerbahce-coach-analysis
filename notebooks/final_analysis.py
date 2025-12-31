import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score
import os


try:

    df_coaches = pd.read_excel("../data/raw/fenerbahce_coaches_data.xlsx")
    df_market = pd.read_excel("../data/raw/market_values.xlsx")
    print("Dosyalar başarıyla yüklendi (Yol: ../data/raw/)")
except:

    df_coaches = pd.read_excel("data/raw/fenerbahce_coaches_data.xlsx")
    df_market = pd.read_excel("data/raw/market_values.xlsx")
    print("Dosyalar başarıyla yüklendi (Yol: data/raw/)")



df_coaches['season'] = df_coaches['season'].astype(str).str.strip()
df_market['season'] = df_market['season'].astype(str).str.strip()


df_merged = pd.merge(df_coaches, df_market, on='season', how='inner')

print(f"\nVeri Birleştirildi! Toplam Satır: {len(df_merged)}")

display(df_merged[['season', 'coach_name', 'points_per_game', 'avg_market_value_mil_euro']].head(3))


print("\n--- MODEL 1 SONUÇLARI (Linear Reg - PPG) ---")
X = df_merged[['is_foreign', 'avg_market_value_mil_euro', 'avg_goals_conceded']]
y = df_merged['points_per_game']

lin_reg = LinearRegression()
lin_reg.fit(X, y)

print(f"Model Başarısı (R2 Skoru): {lin_reg.score(X, y):.3f}")
print("Katsayılar (Etki Değerleri):")
for feat, coef in zip(X.columns, lin_reg.coef_):
    print(f"  {feat}: {coef:.4f}")


print("\n--- MODEL 2 SONUÇLARI (Logistic Reg - Trophy) ---")
X_log = df_merged[['points_per_game', 'is_foreign']]
y_log = df_merged['has_trophy']

log_reg = LogisticRegression()
log_reg.fit(X_log, y_log)
acc = accuracy_score(y_log, log_reg.predict(X_log))

print(f"Doğruluk (Accuracy): {acc:.2f}")
