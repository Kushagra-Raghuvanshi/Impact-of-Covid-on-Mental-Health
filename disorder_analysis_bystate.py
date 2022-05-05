"""Project: Impact of Covid 19 on Mental Health - Study on effects of the Pandemic on stress,
anxiety and depression levels and an insight on thier subsequent corellation with Impact on Drug Use
 and Suicidal Ideation

Authors : Kushagra Raghuvanshi, Madhav Garg, Jacob Grimm

"""
from typing import Any
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

###################################################################################################
# Files containing the data
###################################################################################################
# file1 = 'pulse_survey_dataset.csv'
# NOTE: This file shold be in same folder as this python file

###################################################################################################
# Code for reading file
###################################################################################################


def read_csv_file() -> Any:
    """Read csv file as a pandas Dataframe
    """
    return pd.read_csv('pulse_survey_dataset.csv', index_col=None, na_values=['NA'])


###################################################################################################
# Depression Levels Visualization
###################################################################################################


def depression_levels_plot() -> Any:
    """Represent % of respondents showing symptoms of depression over specific Time periods during
    which survey was carried out which State of residence as basis using Line graph
    """
    orig_dataframe = read_csv_file()
    for state in set(orig_dataframe.State):
        dataframe = orig_dataframe[
            (orig_dataframe.Indicator == 'Symptoms of Depressive Disorder')
            & (orig_dataframe.State == state)]
        y = dataframe.Value
        x = ['Apr 23 - May 5, 2020', 'May 7 - May 12, 2020', 'May 14 - May 19, 2020',
             'May 21 - May 26, 2020']
        plt.plot(x, y, label=state)
        plt.legend()
        plt.ylabel('% of people reporting symptoms of Depressive Disorder')
        plt.xlabel('Time period')
        plt.title('% of Candidates showings Depression symptoms')

    plt.show()


def depression_scatter_plot() -> Any:
    """Represent variation of depression levels among respondents over specific Time periods during
    which survey was carried out which State of residence as basis using Scatter plot to carry out
    further analysis
    """
    orig_dataframe = read_csv_file()
    for state in set(orig_dataframe.State):
        dataframe = orig_dataframe[
            (orig_dataframe.Indicator == 'Symptoms of Depressive Disorder')
            & (orig_dataframe.State == state)]
        y = dataframe.Value
        x = ['Apr 23 - May 5, 2020', 'May 7 - May 12, 2020', 'May 14 - May 19, 2020',
             'May 21 - May 26, 2020']
        plt.scatter(x, y, label=state)
        plt.ylabel('% of people reporting symptoms of Depressive Disorder')
        plt.xlabel('Time period')
        plt.title('Scatter plot for % of Candidates showings Depression symptoms')

    plt.legend(loc='best')
    plt.show()


def depression_linear_regression(state: str) -> Any:
    """Perform linear regression on the scatter plot obtained by depression_scatter_plot() function

    Set of States available to input = {'Maine', Rhode Island, Pennsylvania, Vermont, Connecticut,
    'New Jersey', 'New Hampshire', 'Massachusetts'}
    """
    orig_dataframe = read_csv_file()
    dataframe = orig_dataframe[
        (orig_dataframe.Indicator == 'Symptoms of Depressive Disorder')
        & (orig_dataframe.State == state)]
    y = dataframe.Value
    x = dataframe['Time Period']
    plt.scatter(x, y, label=state)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
    plt.ylabel('% of people reporting symptoms of Depressive Disorder')
    plt.xlabel('Time period')
    plt.xticks([1, 2, 3, 4])
    plt.title('Linear Regression on plot of % of Candidates showings Depression symptoms')

    plt.legend(loc='best')
    plt.show()


def allstate_depression_regression() -> Any:
    """Represent Linear regression plots for all states for comparison and deduction
    """
    orig_dataframe = read_csv_file()
    for state in set(orig_dataframe.State):
        dataframe = orig_dataframe[
            (orig_dataframe.Indicator == 'Symptoms of Depressive Disorder')
            & (orig_dataframe.State == state)]
        y = dataframe.Value
        x = dataframe['Time Period']
        plt.scatter(x, y, label=state)
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m * x + b)
        plt.ylabel('% of people reporting symptoms of Depressive Disorder')
        plt.xlabel('Time period')
        plt.xticks([1, 2, 3, 4])
        plt.title('Linear Regression on plot of % of Candidates showings Depression symptoms')

    plt.legend(loc='best')
    plt.show()

###################################################################################################
# Anxiety Levels Visualization
###################################################################################################


def anxiety_levels_plot() -> Any:
    """Represent % of respondents showing symptoms of anxiety over specific Time periods during
    which survey was carried out which State of residence as basis using Line graph
    """
    orig_dataframe = read_csv_file()
    for state in set(orig_dataframe.State):
        dataframe = orig_dataframe[
            (orig_dataframe.Indicator == 'Symptoms of Anxiety Disorder')
            & (orig_dataframe.State == state)]
        y = dataframe.Value
        x = ['Apr 23 - May 5, 2020', 'May 7 - May 12, 2020', 'May 14 - May 19, 2020',
             'May 21 - May 26, 2020']
        plt.plot(x, y, label=state)
        plt.legend()
        plt.ylabel('% of people reporting symptoms of Anxiety Disorder')
        plt.xlabel('Time period')
        plt.title('% of Candidates showings Anxiety symptoms')
    plt.show()


def anxiety_scatter_plot() -> Any:
    """Represent variation of anxiety levels among respondents over specific Time periods during
    which survey was carried out which State of residence as basis using Scatter plot to carry out
    further analysis
    """
    orig_dataframe = read_csv_file()
    for state in set(orig_dataframe.State):
        dataframe = orig_dataframe[
            (orig_dataframe.Indicator == 'Symptoms of Anxiety Disorder')
            & (orig_dataframe.State == state)]
        y = dataframe.Value
        x = ['Apr 23 - May 5, 2020', 'May 7 - May 12, 2020', 'May 14 - May 19, 2020',
             'May 21 - May 26, 2020']
        plt.scatter(x, y, label=state)
        plt.ylabel('% of people reporting symptoms of Anxiety Disorder')
        plt.xlabel('Time period')
        plt.title('Scatter plot for % of Candidates showings Anxiety symptoms')

    plt.legend(loc='best')
    plt.show()


def anxiety_linear_regression(state: str) -> Any:
    """Develop Linear regression plots for all states for comparison and deduction
    """
    orig_dataframe = read_csv_file()
    dataframe = orig_dataframe[
        (orig_dataframe.Indicator == 'Symptoms of Anxiety Disorder')
        & (orig_dataframe.State == state)]
    y = dataframe.Value
    x = dataframe['Time Period']
    plt.scatter(x, y, label=state)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
    plt.ylabel('% of people reporting symptoms of Anxiety Disorder')
    plt.xlabel('Time period')
    plt.xticks([1, 2, 3, 4])
    plt.title('Linear regression on plot of % of Candidates showings Anxiety symptoms')

    plt.legend(loc='best')
    plt.show()


def allstate_anxiety_regression() -> Any:
    """Develop Linear regression plots for all states for comparison and deduction
    """
    orig_dataframe = read_csv_file()
    for state in set(orig_dataframe.State):
        dataframe = orig_dataframe[
            (orig_dataframe.Indicator == 'Symptoms of Anxiety Disorder')
            & (orig_dataframe.State == state)]
        y = dataframe.Value
        x = dataframe['Time Period']
        plt.scatter(x, y, label=state)
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m * x + b)
        plt.ylabel('% of people reporting symptoms of Anxiety Disorder')
        plt.xlabel('Time period')
        plt.xticks([1, 2, 3, 4])
        plt.title('Linear regression on plot of % of Candidates showings Anxiety symptoms')

    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    depression_levels_plot()
    depression_scatter_plot()
    allstate_depression_regression()
    anxiety_levels_plot()
    anxiety_scatter_plot()
    allstate_anxiety_regression()
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['python_ta.contracts', 'numpy', 'pandas', 'matplotlib.pyplot'],
    #     'allowed-io': [],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200']
    # })

    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # import doctest
    # doctest.testmod()
