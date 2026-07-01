import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("/content/traffic_accidents.csv")

# Basic Information
print(df.head())
print(df.info())
print(df.isnull().sum())

# Remove missing values in important columns
df = df.dropna()

# -----------------------------
# Weather Conditions
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(y='weather_condition',
              data=df,
              order=df['weather_condition'].value_counts().index[:10])
plt.title("Accidents by Weather Condition")
plt.xlabel("Number of Accidents")
plt.show()

# -----------------------------
# Road Surface Conditions
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(y='roadway_surface_cond',
              data=df,
              order=df['roadway_surface_cond'].value_counts().index)
plt.title("Accidents by Road Surface")
plt.xlabel("Number of Accidents")
plt.show()

# -----------------------------
# Time of Day Analysis
# -----------------------------
df['crash_date'] = pd.to_datetime(df['crash_date'], format='%m/%d/%Y %I:%M:%S %p')

df['Hour'] = df['crash_date'].dt.hour

plt.figure(figsize=(10,5))
sns.histplot(df['Hour'], bins=24)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Accidents")
plt.show()

# -----------------------------
# Crash Severity
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(y='most_severe_injury',
              data=df,
              order=df['most_severe_injury'].value_counts().index)
plt.title("Accident Severity")
plt.show()

# -----------------------------
# Top Crash Types
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(y='crash_type',
              data=df,
              order=df['crash_type'].value_counts().index[:10])
plt.title("Top 10 Crash Types")
plt.show()

# -----------------------------
# Accident Hotspots
# -----------------------------
# Note: 'Longitude' and 'Latitude' columns are not present in this dataset.
# This section is commented out or needs appropriate column names if available.
# plt.figure(figsize=(8,6))
# plt.scatter(df['Longitude'],
#             df['Latitude'],
#             s=5,
#             alpha=0.5)

# plt.title("Accident Hotspots")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.show()
