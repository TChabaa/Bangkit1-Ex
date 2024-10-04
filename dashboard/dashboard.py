import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load datasets
day_df = pd.read_csv("data/day.csv", header=0)
hour_df = pd.read_csv("data/hour.csv", header=0)

datachange = [day_df, hour_df]

for column in datachange:
    column['dteday'] = pd.to_datetime(column['dteday'])

day_df.info()
print("Jumlah Duplikasi", day_df.duplicated().sum())

hour_df.info()
print("Jumlah Duplikasi", hour_df.duplicated().sum())

print(day_df.describe(include=[np.number]))
print(hour_df.describe(include=[np.number]))

# Scale the temperature
day_df['atemp_scaled'] = day_df['atemp'] * 50

# Define the temperature ranges and corresponding labels
bins = [0, 10, 20, 30, 40, 50]  # Temperature intervals in Celsius
labels = ['Very Cold', 'Cold', 'Mild', 'Warm', 'Hot']

# Create a new column 'atemp_range' by categorizing the scaled 'atemp'
day_df['atemp_range'] = pd.cut(day_df['atemp_scaled'], bins=bins, labels=labels, right=False, include_lowest=True)

# Helper functions to create grouped DataFrames
def create_by_season_casual_df(df):
    return df.groupby(by='season').casual.mean().reset_index()

def create_by_season_registered_df(df):
    return df.groupby(by='season').registered.mean().reset_index()

def create_by_season_cnt_df(df):
    return df.groupby(by='season').cnt.mean().reset_index()

def create_by_workingday_casual_df(df):
    return df.groupby(by='workingday').casual.mean().reset_index()

def create_by_workingday_registered_df(df):
    return df.groupby(by='workingday').registered.mean().reset_index()

def create_by_workingday_cnt_df(df):
    return df.groupby(by='workingday').cnt.mean().reset_index()

def create_by_hour_casual_df(df):
    return df.groupby(by='hr').casual.mean().reset_index()

def create_by_hour_registered_df(df):
    return df.groupby(by='hr').registered.mean().reset_index()

def create_by_hour_cnt_df(df):
    return df.groupby(by='hr').cnt.mean().reset_index()

def create_by_weathersit_casual_df(df):
    return df.groupby(by='weathersit').casual.mean().reset_index()

def create_by_weathersit_registered_df(df):
    return df.groupby(by='weathersit').registered.mean().reset_index()

def create_by_weathersit_cnt_df(df):
    return df.groupby(by='weathersit').cnt.mean().reset_index()

# Call the helper functions to get the necessary dataframes
q1_casual = create_by_season_casual_df(day_df)
q1_registered = create_by_season_registered_df(day_df)
q1_cnt = create_by_season_cnt_df(day_df)

q2_casual = create_by_workingday_casual_df(day_df)
q2_registered = create_by_workingday_registered_df(day_df)
q2_cnt = create_by_workingday_cnt_df(day_df)

q3_casual = create_by_hour_casual_df(hour_df)
q3_registered = create_by_hour_registered_df(hour_df)
q3_cnt = create_by_hour_cnt_df(hour_df)

q4_casual = create_by_weathersit_casual_df(hour_df)
q4_registered = create_by_weathersit_registered_df(hour_df)
q4_cnt = create_by_weathersit_cnt_df(hour_df)

# Streamlit header
st.header("Dicoding Bike Sharing Dataset")

colors = ["#90CAF9", "#D3D3D3"]  # Reduced to 2 colors to prevent palette warning

# Effect of Season on Number of Users
st.subheader('Effect of Season on Number of Users')

# Explanation of seasons
st.write("""
### Explanation of Seasons
- **Season Values**:
  - `1`: Winter
  - `2`: Spring
  - `3`: Summer
  - `4`: Fall
""")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="casual",
        x="season", 
        data=q1_casual,
        hue='season',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Casual Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="registered",
        x="season", 
        data=q1_registered,
        hue='season',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Registered Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Bike Counts by season
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    y="cnt",
    x="season", 
    data=q1_cnt,
    hue='season',
    palette=colors,
    legend=False,
    ax=ax
)
ax.set_title("Average Number of Bike Counts", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

# Analysis for Season Effects
st.write(""" 
### Analysis of Season Effects
- **Casual Customers**: There is a notable increase in casual customers during spring (2) and summer (3) seasons, indicating that good weather attracts more casual users.
- **Registered Customers**: The number of registered customers shows a steadier pattern across seasons, suggesting that registered users are less affected by seasonal changes.
- **Bike Counts**: The Bike Count trend follows a similar pattern to casual customers, reflecting their higher numbers in favorable seasons.
""")

# Effect of Working Day on Number of Users
st.subheader('Effect of Working Day on Number of Users')

# Explanation of working day values
st.write("""
### Explanation of Working Days
- **Working Day Values**:
  - `0`: Not a working day (weekend)
  - `1`: Working day (Monday to Friday)
""")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="casual",
        x="workingday", 
        data=q2_casual,
        hue='workingday',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Casual Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="registered",
        x="workingday", 
        data=q2_registered,
        hue='workingday',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Registered Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Bike Counts by working day
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    y="cnt",
    x="workingday", 
    data=q2_cnt,
    hue='workingday',
    palette=colors,
    legend=False,
    ax=ax
)
ax.set_title("Average Number of Bike Counts", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

# Analysis for Working Day Effects
st.write("""
### Analysis of Working Day Effects
- **Casual Customers**: Casual users tend to be more active on non-working days, suggesting that leisure activities drive usage on weekends.
- **Registered Customers**: The registered users show a more balanced distribution, implying that they utilize the service consistently regardless of working days.
- **Bike Counts**: Bike Counts peak on non-working days, aligning with the casual usage pattern.
""")

# Effect of Time of Day on Number of Users
st.subheader('Effect of Time of Day on Number of Users')

# Explanation of hour values
st.write("""
### Explanation of Hour Values
- **Hour Values**:
  - `0` to `23`: Represents the hour of the day in a 24-hour format.
""")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="casual",
        x="hr", 
        data=q3_casual,
        hue='hr',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Casual Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="registered",
        x="hr", 
        data=q3_registered,
        hue='hr',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Registered Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Bike Counts by hour
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    y="cnt",
    x="hr", 
    data=q3_cnt,
    hue='hr',
    palette=colors,
    legend=False,
    ax=ax
)
ax.set_title("Average Number of Bike Counts", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

# Analysis for Hour Effects
st.write("""
### Analysis of Hour Effects
- **Casual Customers**: There is a significant rise in casual users during the late morning and evening hours, indicating that people tend to bike for leisure before and after work.
- **Registered Customers**: Registered users display a more consistent usage throughout the day, with peaks during commute hours, indicating their reliance on bikes for transportation.
- **Bike Counts**: The overall bike counts align closely with the registered users' pattern, highlighting the importance of commuter traffic.
""")

# Effect of Weather Situation on Number of Users
st.subheader('Effect of Weather Situation on Number of Users')

# Explanation of weather situation values
st.write("""
### Explanation of Weather Situations
- **Weather Situation Values**:
  - `1`: Clear, Few Clouds
  - `2`: Mist + Cloudy, Few Clouds
  - `3`: Light Snow, Rain, Thunderstorm, etc.
  - `4`: Heavy Rain + Ice Pellets + Snow, etc.
""")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="casual",
        x="weathersit", 
        data=q4_casual,
        hue='weathersit',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Casual Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="registered",
        x="weathersit", 
        data=q4_registered,
        hue='weathersit',
        palette=colors,
        legend=False,
        ax=ax
    )
    ax.set_title("Average Number of Registered Customers", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

# Bike Counts by weather situation
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    y="cnt",
    x="weathersit", 
    data=q4_cnt,
    hue='weathersit',
    palette=colors,
    legend=False,
    ax=ax
)
ax.set_title("Average Number of Bike Counts", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

# Analysis for Weather Situation Effects
st.write("""
### Analysis of Weather Situation Effects
- **Casual Customers**: Casual usage declines significantly during adverse weather conditions, especially during heavy rain or snow (3 and 4), indicating that weather plays a crucial role in leisure biking.
- **Registered Customers**: Registered users show some resilience to weather changes, but there is still a noticeable drop in usage during harsh conditions.
- **Bike Counts**: The overall bike count trends follow similar patterns to casual users, reflecting the impact of weather on bike-sharing demand.
""")

# Effect of daily temperature to number of user
st.subheader('Effect of daily temperature to number of user')
fig, ax = plt.subplots(figsize=(20, 10))
sns.scatterplot(
    x="atemp_scaled",
    y="casual",
    data=day_df,
    palette=colors
)
ax.set_title("Casual customers Amount Based On Temperature", fontsize=50)
ax.set_xlabel("Temperature", fontsize=35)
ax.set_ylabel("Casual Customers", fontsize=30)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20, 10))
sns.scatterplot(
    x="atemp_scaled",
    y="registered",
    data=day_df,
    palette=colors
)
ax.set_title("Registered customers Amount Based On Temperature", fontsize=50)
ax.set_xlabel("Temperature", fontsize=35)
ax.set_ylabel("Registered Customers", fontsize=30)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20, 10))
sns.scatterplot(
    x="atemp_scaled",
    y="cnt",
    data=day_df,
    palette=colors
)
ax.set_title("Count of Bike Amount Based On Temperature", fontsize=50)
ax.set_xlabel("Temperature", fontsize=35)
ax.set_ylabel("Bike Counts", fontsize=30)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

st.write("""
### Analysis of Temperature Effects
- **Casual Customers**: The scatter plot shows a positive correlation between temperature and casual customers, indicating that higher temperatures lead to more leisure biking.
- **Registered Customers**: Similar trends can be observed with registered customers, although the relationship is less pronounced.
- **Total Bike Counts**: Total bike counts follow the temperature trend, suggesting that both casual and registered users are influenced by temperature.
""")
