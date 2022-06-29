import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot
    plt.scatter(x,y)

    # Create first line of best fit
    lgResult = linregress(x,y)
    xL1 = pd.Series([i for i in range(1880,2051)])
    yL1 = lgResult.slope * xL1 + lgResult.intercept
    plt.plot(xL1,yL1)

    # Create second line of best fit
    newData = df[df['Year']>=2000]
    newX = newData['Year']
    newY = newData['CSIRO Adjusted Sea Level']
    lgResult2 = linregress(newX,newY)
    xL2 = pd.Series([i for i in range(2000,2051)])
    yL2 = xL2 * lgResult2.slope + lgResult2.intercept
    plt.plot(xL2,yL2)

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()