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
    for every dataset given in the datasets parameter, one with their trendlines and the last one with
    the average feature value every week.
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

    # Plot the average taken every week and their trendlines
    plt.title(f'{feature_name} average every week for every dataset, with trendlines'.capitalize())
    for dataset in datasets:
        weekly_feature_value = []
        for i in range(len(data[dataset][csv_file][time])//2016):
            weekly_feature_value.append(data[dataset][csv_file][feature][i*2016:i*2016+2016].mean())
        x, y = np.arange(16), weekly_feature_value
        a,b = np.polyfit(list(x),list(y),1)
        x_trend = np.linspace(min(x), max(x), 2)
        plot = plt.plot(x, y, '.', label=dataset)
        plt.plot(x_trend, x_trend*a+b,color=plot[0].get_color())
        plt.plot()
    plt.xlabel('Week')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

def calculate_weekly_data(features, data, datasets):
    '''
    This function divides the data in weeks, which means instead of taking an average feature
    value for every team for every relevant feature. The average feature value of a week per team will
    be taken and the associated production in that week. Because the first week was not that productive
    it was decided not to take the data of the first week into account.
    '''
    features = list(features)
    features.extend(['ProdA_num', 'ProdB_num'])
    weekly_data = dict()
    for feature in features:
        feature_weekly_data = []
        for dataset in datasets:
            if 'Prod' not in feature:
                # Take the mean per week of all the 5 minute incremental datapoints.
                for i in range(1,len(data[dataset]['GHClim']['GHtime'])//2016):
                    feature_weekly_data.append(data[dataset]['GHClim'][feature][i*2016:i*2016+2016].mean())
            else:
                # Take the mean of the total production per day in a week.
                for i in range(1,len(data[dataset]['prod']['time'])//7):
                    feature_weekly_data.append(data[dataset]['prod'][feature][i*7:i*7+7].mean())
        weekly_data[feature] = feature_weekly_data
    print("The code has succesfully ran and the data is divided into weekly data (see the 'weekly_data' variable)")
    return weekly_data