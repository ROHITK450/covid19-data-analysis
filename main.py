import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Direct URL se data load karna
url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(url)

# 2. Basic cleaning (Date ko datetime format mein convert karna)
df['Date'] = pd.to_datetime(df['Date'])

# 3. Global total nikalna (date wise)
global_trend = df.groupby('Date')[['Confirmed', 'Recovered', 'Deaths']].sum()

# 4. Folder banana agar nahi hai toh
if not os.path.exists('outputs/plots'):
    os.makedirs('outputs/plots')

# 5. Visualization: Global Cases Trend
plt.figure(figsize=(10,6))
plt.plot(global_trend.index, global_trend['Confirmed'], label='Confirmed', color='blue')
plt.title('Global COVID-19 Confirmed Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)

# 6. Image save karna (README ke liye)
plt.savefig('outputs/plots/cases_trend.png')
print("Graph saved successfully in outputs/plots/cases_trend.png")
