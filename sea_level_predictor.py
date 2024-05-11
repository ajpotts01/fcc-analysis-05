import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df_sea_level: pd.DataFrame = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15,5))
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df_sea_level)    

    f = lambda x, y: (y.slope * x) + y.intercept

    # Create first line of best fit
    lr_result_first = linregress(
        x=df_sea_level["Year"],
        y=df_sea_level["CSIRO Adjusted Sea Level"]
    )
    
    pred_first = {
        "Year": [x for x in range(1880, 2051)],
        "CSIRO Adjusted Sea Level": [f(x, lr_result_first) for x in range(1880, 2051)]
    }
    df_pred_first = pd.DataFrame.from_dict(pred_first, orient="columns")

    ax.plot(df_pred_first["Year"], df_pred_first["CSIRO Adjusted Sea Level"], c="red")

    # Create second line of best fit
    df_sea_level_2000 = df_sea_level[df_sea_level["Year"] >= 2000]
    lr_result_second = linregress(
        x=df_sea_level_2000["Year"],
        y=df_sea_level_2000["CSIRO Adjusted Sea Level"]
    )
    pred_second = {
        "Year": [x for x in range(2000, 2051)],
        "CSIRO Adjusted Sea Level": [f(x, lr_result_second) for x in range(2000, 2051)]
    }
    df_pred_second = pd.DataFrame.from_dict(pred_second, orient="columns")

    ax.plot(df_pred_second["Year"], df_pred_second["CSIRO Adjusted Sea Level"], c="orange")

    # Add labels and title
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()