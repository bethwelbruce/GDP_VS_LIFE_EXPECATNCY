import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Get the data from Our World in Data
df_gdp = pd.read_csv('https://ourworldindata.org/data/exports/gdp-per-capita-ppp-current-international-dollars-maddison.csv')
df_gdp = df_gdp.loc[(df_gdp['country'] == 'India') | (df_gdp['country'] == 'United States')]

# Select the data from 1918 to 2018
df_gdp = df_gdp.loc[df_gdp['year'] >= 1918]
df_gdp = df_gdp.loc[df_gdp['year'] <= 2018]

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(df_gdp[df_gdp['country'] == 'India']['year'], df_gdp[df_gdp['country'] == 'India']['gdp_per_capita_ppp'], label='India')
plt.plot(df_gdp[df_gdp['country'] == 'United States']['year'], df_gdp[df_gdp['country'] == 'United States']['gdp_per_capita_ppp'], label='United States')
plt.xlabel('Year')
plt.ylabel('GDP per capita (PPP, current international dollars)')
plt.title('GDP per capita (PPP) in India and the United States, 1918-2018')
plt.legend()
plt.grid(True)
plt.show()

# Get the data from Our World in Data
df_life_expectancy = pd.read_csv('https://ourworldindata.org/data/exports/life-expectancy-at-birth-years.csv')
df_life_expectancy = df_life_expectancy.loc[(df_life_expectancy['country'] == 'India') | (df_life_expectancy['country'] == 'United States')]

# Select the data from 1921 to 2021
df_life_expectancy = df_life_expectancy.loc[df_life_expectancy['year'] >= 1921]
df_life_expectancy = df_life_expectancy.loc[df_life_expectancy['year'] <= 2021]

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(df_life_expectancy[df_life_expectancy['country'] == 'India']['year'], df_life_expectancy[df_life_expectancy['country'] == 'India']['life_expectancy'], label='India')
plt.plot(df_life_expectancy[df_life_expectancy['country'] == 'United States']['year'], df_life_expectancy[df_life_expectancy['country'] == 'United States']['life_expectancy'], label='United States')
plt.xlabel('Year')
plt.ylabel('Life expectancy (years)')
plt.title('Life expectancy in India and the United States, 1921-2021')
plt.legend()
plt.grid(True)
plt.show()
