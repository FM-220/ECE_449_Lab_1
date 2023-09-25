import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

file0 = pd.read_csv('C:/Users/86185/Desktop/wdbc.data'
                    , names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af'])

# read the file using pandas
#  To check if there is any missing value in the file, we are going to use both find_it and exchange_it function.

co = []  # co means coordinate

def find_it(file, co_lst):
    """ Read the name of the columns and then check if there is a missing value in each column. If so, store the coordinate
    of the missing value in the list co (the row is counted itself).
    :param file: The file to be checked (if there is any missing value).
    :param co_lst: The list to store the coordinate of missing value.
    :return: Nah
    """
    column_name = list(file.loc[0].index)
    for i in column_name:
        row = 0
        for j in file[i]:
            if pd.isna(j):
                co_lst.append([i, row])
            row += 1


def exchange_it(file, co_lst):
    """ Exchange the missing value with the mean of the column.
    :param file: The file to be checked (if there is any missing value).
    :param co: The list to store the coordinate of missing value.
    :return: Nah
    """
    list0 = []  # the list for the column coordinates of missing data
    List1 = []  # the mean value of the column with missing data
    for co0 in co_lst:
        if co0 not in list0:  # this is to make sure that when there are multiple missing data in one column, the mean
            # value of the column is only calculated once.
            list0.append(co0[0])
    for col0 in list0:  # find the mean value of the column with missing data and add them to List1
        List1.append(file[col0].mean())
    flag = 0  # the flag to count the number of missing data. Since the list of mean value is corresponding to the list
    # of missing data, we can use the flag to restore the mean value to the coordinates of the mean value.
    for co0 in co_lst:
        file.loc[co0[1], co0[0]] = List1[flag]
        flag += 1



def plotting_box_whisker_box(file):
    """ Plot the box and whisker plot of the data.
    :param file: The file to be plotted.
    :return: Nah
    """

    # del file['a']  # delete ID column
    columns_to_be_scared = file[['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af']]
    fit_data = MinMaxScaler().fit(columns_to_be_scared)
    scaled_data = fit_data.transform(columns_to_be_scared)
    plt.figure(figsize=(12, 6))  # Set the size of the plot
    sns.boxplot(data=scaled_data)  # Vertical box and whisker plots
    plt.title("Box and Whisker Plots")
    plt.ylabel("Value")  # Label for the y-axis
    plt.show()


def adc(file):
    """ Change the diagnosis column to 0 and 1.
    :param file: The file to be changed.
    :return: Nah
    """
    for mark in file['b']:
        if mark == 'M':
            file['b'] = file['b'].replace('M', 1)
        else:
            file['b'] = file['b'].replace('B', 0)

train_test_split(file0, test_size=0.2, random_state=0)
