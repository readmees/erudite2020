'''
This file contains a helper function for polynomial_fit.ipynb.
The function is called visualize_time and is use to visualise
the timeseries of the CHClim and the Vip dataset from the
Automonous Greenhouse Challenge 1st edition.
'''
import matplotlib.pyplot as plt
import numpy as np

def visualize_time(data, datasets, feature, feature_name, ylabel, csv_file='GHClim', time='GHtime'):
    '''
    This function visualizes four graphs: one with 33133 timestamps and a feature value of 5 minutes
    for every dataset given in the datasets parameter, one with their trendlines and one with
    samples taken every week (and trendlines) the last one with the average feature value every week.
    '''
    # Plot 33133 timestamps of 5 minutes
    plt.title(f'{feature_name} with 33133 timestamps of 5 minutes for every dataset'.capitalize())
    for dataset in datasets:
        x, y = data[dataset][csv_file][time], data[dataset][csv_file][feature]
        plot = plt.plot(x, y, '.', label=dataset)
        plt.plot()
    plt.xlabel('Timestamp every 5 minutes')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

    # Plot trendlines of all the 33133 datapoints
    plt.title(f'Trendlines of {feature_name} of all the 33133 datapoints')
    for dataset in datasets:
        x, y = data[dataset][csv_file][time], data[dataset][csv_file][feature]
        a,b = np.polyfit(list(x),list(y),1)
        x_trend = np.linspace(min(x), max(x), 2)
        plt.plot(x_trend, x_trend*a+b, label=dataset)
    plt.xlabel('Timestamp every 5 minutes')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

    # Plot samples taken every week and their trendlines
    plt.title(f'{feature_name} sample every week for every dataset, with trendlines'.capitalize() )
    for dataset in datasets:
        x, y = np.arange(16), data[dataset][csv_file][feature][::2016][1:]
        a,b = np.polyfit(list(x),list(y),1)
        x_trend = np.linspace(min(x), max(x), 2)
        plot = plt.plot(x, y, '.', label=dataset)
        plt.plot(x_trend, x_trend*a+b,color=plot[0].get_color())
    plt.xlabel('Week')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

    # Plot the average taken every week and their trendlines
    plt.title(f'{feature_name} average every week for every dataset, with trendlines'.capitalize())
    for dataset in datasets:
        weekly_HumDef = []
        for i in range(len(data[dataset][csv_file][time])//2016):
            weekly_HumDef.append(data[dataset][csv_file][feature][i*2016:i*2016+2016].mean())
        x, y = np.arange(16), weekly_HumDef
        a,b = np.polyfit(list(x),list(y),1)
        x_trend = np.linspace(min(x), max(x), 2)
        plot = plt.plot(x, y, '.', label=dataset)
        plt.plot(x_trend, x_trend*a+b,color=plot[0].get_color())
        plt.plot()
    plt.xlabel('Week')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

def calculate_weekly_data(data, datasets):
    '''
    This function devides the data in weeks, which means instead of taking an average feature
    value for every team for every relevant feature. The average feature value of a week per team will
    be taken and the associated production in that week. Because the first week was not that productive
    and the data will be devided in weeks, there is chosen not to take the data of the first week
    into account.
    '''
    # Create a dictionary with weekly data to create more usuable data
    weekly_CO2, weekly_HumDef, weekly_temp = [], [], []
    weekly_prodA, weekly_prodB = [], []
    for team in datasets:
        for i in range(1,len(data[team]['GHClim']['GHtime'])//2016):
            weekly_HumDef.append(data[team]['GHClim']['HumDef'][i*2016:i*2016+2016].mean())
            weekly_CO2.append(data[team]['GHClim']['CO2air'][i*2016:i*2016+2016].mean())
            weekly_temp.append(data[team]['GHClim']['Tair'][i*2016:i*2016+2016].mean())
        # Add weekly production sum (both A and B)
        # Timestamp is per day
        for i in range(1,len(data[team]['prod']['time'])//7):
            weekly_prodA.append(np.mean(data[team]['prod']['ProdA_num'][i*7:i*7+7]))
            weekly_prodB.append(np.mean(data[team]['prod']['ProdB_num'][i*7:i*7+7]))
    weekly_data  = {'CO2air':weekly_CO2, 'HumDef':weekly_HumDef,
                            'Tair':weekly_temp, 'prodA':weekly_prodA,
                            'prodB':weekly_prodB}
    print("The code is succesfully runned and the weekly data not\
          devided by team is now in the variable 'weekly_data_total'")
    return weekly_data