# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 01:53:30 2023

@author: ashra
"""
'''
Importing the modules
matplotlib,pandas,seaborn
stats module is imported to calculate the Skew and Kurtosis values of a data set
'''  

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import seaborn as sns
import scipy.stats as stats

"""The function read_file is defined to read the excel file and will
return 2 data frames, one with countries as columns and one with years as
columns"""
#Read the data set and delete the first 4 rows of the csv file containing irrelevent data

def reading_f(fname, Countries, Years):
    f0 = pd.read_csv(fname, skiprows=4)
    #index the country name column
    f0.drop(columns=["Country Code"], axis=1, inplace=True)
    f0.set_index(["Country Name"], inplace=True)
    #Call the data set containing only the relevant Countries and Years
    f1 = f0.iloc[Countries, Years]
    #Retrieve the transpose of the data set
    f2 = f1.T
    #Return the data set and the transposed data set
    return f1, f2


"""The function heat_map is used to plot a heat map taking in the csv file containing
the initial data set, the particular country, indicators, years and the heat map
colour scheme as it's arguments
"""
def heat_map(fname, Countries, Indicators):
    f0 = pd.read_csv(fname, skiprows=4)
    #Drop the irrelevant columns from the data set
    f0.drop(columns=["Country Code", "Indicator Code"], axis=1, inplace=True)
    #index the country name and Indicator name column
    f0.set_index(["Country Name", "Indicator Name"], inplace=True)
    f1 = f0.loc[Countries].fillna(0).T
    #Select the columns containing the specified years
    f = f1.loc[['1990', '1995', '2000', '2005',
                '2010', '2015', '2019'], Indicators]
    #Plot the heat map
    plt.figure(figsize=(10, 8))
    sns.heatmap(f.corr(), vmax=1, vmin=-1, annot=True, cmap='BrBG')
    return

#Array containing the index of the required countries
Countries = [40, 251, 109, 202, 119, 55, 35, 112, 126, 106]
#Array containing the index of required years 1995 -2010
Years = [37, 42, 47, 52, 57, 61]

'''Retrieve the data sets into the first set and the transpose of the same in the second set
   Pass the file name and the array containing indexes of Countries and Years as the arguments
   to the function
'''
co2_af1, co2_af2 = reading_f(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/co2_emission.csv", Countries, Years)
totalpop_af1, totalpop_af2 = reading_f(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/pop_total.csv", Countries, Years)
methane_af1, methane_af2 = reading_f(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/methane_emssion.csv", Countries, Years)
reneweergy_af1, reneweergy_af2 = reading_f(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/renewable_energy.csv", Countries, Years)
urbanpop_af1, urbanpop_af2 = reading_f(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/urbanpop_total.csv", Countries, Years)
ruralpop_af1, ruralpop_af2 = reading_f(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/rural_pop.csv", Countries, Years)

'''Plot the graphs with the data sets retrieved and set the title and and labels
   Rotate the x ticks so that the country names do not intertwine in the graph
'''
co2_af1.plot(kind="bar")
plt.title("CO2 emission by different Countries", fontweight='bold')
plt.xlabel('Countries', fontweight='bold')
plt.ylabel('Co2 emissions (kt)', fontweight='bold')

reneweergy_af1.plot(kind="bar")
plt.title(" Renewable energy Consumption of different countries ",
          fontweight='bold')
plt.xlabel('Countries', fontweight='bold')
plt.ylabel('Energy Consumption(%)', fontweight='bold')

methane_af2.plot(kind="line")
plt.title("Methane emission by different countries  ", fontweight='bold')
plt.xlabel('Years', fontweight='bold')
plt.ylabel('Methane Emission (kt)', fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1))

urbanpop_af2.plot(kind="line")
plt.title("Urban population ", fontweight='bold')
plt.xlabel('Years', fontweight='bold')
plt.ylabel('urban population', fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1))

#Print the Skewness and Kurtosis of a used data set
print("Skewness:", stats.skew(co2_af1["2019"]))
print("Kurtosis", stats.kurtosis(co2_af1["2019"]))

#Array containing the indicator names specifying the indicators needed to plot on the heat maps
Indicators = ["Urban population (% of total population)", "CO2 emissions from liquid fuel consumption (kt)",
              "Renewable energy consumption (% of total final energy consumption)", "Methane emissions (kt of CO2 equivalent)", ]
#Plot two heat maps with different country names  and the indicators and map collor scheme as arguments
heatmap = heat_map(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/indicators.csv", "United States", Indicators)
plt.title("United States", fontweight='bold')
heatmap = heat_map(
    "C:/Users/ashra/OneDrive/Desktop/Assignment2/indicators.csv", "Indonesia", Indicators)
#set title for heat map
plt.title("INDONESIA", fontweight='bold')
