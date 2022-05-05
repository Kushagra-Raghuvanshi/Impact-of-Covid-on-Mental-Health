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
# file1 = 'Table-1.csv'
# NOTE: This file shold be in same folder as this python file

###################################################################################################
# Code for reading file
###################################################################################################


def read_csv_file() -> Any:
    """Read csv file as a pandas Dataframe
    """
    return pd.read_csv('Table-1.csv', index_col=None, na_values=['NA'])


###################################################################################################
# Visualisation by AGE
###################################################################################################

def disorder_age() -> Any:
    """Visualise how Age group of respondents relate to prevalence of anxiety & depression
    disorders.
    """
    orig_dataframe = read_csv_file()
    dataframe = orig_dataframe.loc[6:9, :]

    column1 = 'Anxiety disorder'
    column2 = 'Depressive disorder'
    labels = [column1[0:34], column2]

    group_1 = [dataframe[column1][6], dataframe[column2][6]]
    group_2 = [dataframe[column1][7], dataframe[column2][7]]
    group_3 = [dataframe[column1][8], dataframe[column2][8]]
    group_4 = [dataframe[column1][9], dataframe[column2][9]]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, group_1, width, label='18 to 24 years')
    rects2 = ax.bar(x - width / 4, group_2, width, label='25 to 44 years')
    rects3 = ax.bar(x + width * (1 / 4), group_3, width, label='44 to 64 years')
    rects4 = ax.bar(x + width * (1 / 2), group_4, width, label='>64 years')

    ax.set_ylabel('Percentage')
    ax.set_title('% of Repondents showing symptoms By Age')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    ax.bar_label(rects4, padding=3)

    fig.tight_layout()

    plt.show()


###################################################################################################
# Visualisation by GENDER
###################################################################################################

def disorder_gender() -> Any:
    """Visualise how the Gender of respondents relate to prevalence of anxiety & depression
    disorders.
    """
    orig_dataframe = read_csv_file()
    dataframe = orig_dataframe.loc[2:4, :]

    column1 = 'Anxiety disorder'
    column2 = 'Depressive disorder'
    labels = [column1[0:34], column2]

    group_1 = [dataframe[column1][2], dataframe[column2][2]]
    group_2 = [dataframe[column1][3], dataframe[column2][3]]
    group_3 = [dataframe[column1][4], dataframe[column2][4]]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 3, group_1, width, label='Female')
    rects2 = ax.bar(x + width / 3, group_2, width, label='Male')
    rects3 = ax.bar(x + width, group_3, width, label='Other')

    ax.set_ylabel('Percentage')
    ax.set_title('% of Repondents showing symptoms By Gender')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.show()


###################################################################################################
# Visualisation by Race/Ethinicity
###################################################################################################

def disorder_race() -> Any:
    """Visualise how the Race/Ethinic background of respondents relate to prevalence of
    anxiety & depression disorders.
    """
    orig_dataframe = read_csv_file()
    dataframe = orig_dataframe.loc[11:16, :]

    column1 = 'Anxiety disorder'
    column2 = 'Depressive disorder'
    labels = [column1[0:34], column2]

    group_1 = [dataframe[column1][11], dataframe[column2][11]]
    group_2 = [dataframe[column1][12], dataframe[column2][12]]
    group_3 = [dataframe[column1][13], dataframe[column2][13]]
    group_4 = [dataframe[column1][14], dataframe[column2][14]]
    group_5 = [dataframe[column1][15], dataframe[column2][15]]
    group_6 = [dataframe[column1][16], dataframe[column2][16]]

    x = np.arange(len(labels))
    width = 0.2

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, group_1, width, label='White, non-Hispanic')
    rects2 = ax.bar(x - width * (1 / 2), group_2, width, label='Black, non-Hispanic')
    rects3 = ax.bar(x, group_3, width, label='Asian, non-Hispanic')
    rects4 = ax.bar(x + width * (1 / 2), group_4, width, label='Other race or multiple races,'
                                                               ' non-Hispanic')
    rects5 = ax.bar(x + width, group_5, width, label='Hispanic, any race(s)')
    rects6 = ax.bar(x + width * (3 / 2), group_6, width, label='Unknown')

    ax.set_ylabel('Percentage')
    ax.set_title('% of Repondents showing symptoms By Race/Ethinicity')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    ax.bar_label(rects4, padding=3)
    ax.bar_label(rects5, padding=3)
    ax.bar_label(rects6, padding=3)

    fig.tight_layout()

    plt.show()


###################################################################################################
# Visualisation by Income
###################################################################################################

def disorder_income() -> Any:
    """Visualise how Income levels of respondents relate to prevalence of anxiety & depression
    disorders.
    """

    orig_dataframe = read_csv_file()
    dataframe = orig_dataframe.loc[18:23, :]

    column1 = 'Anxiety disorder'
    column2 = 'Depressive disorder'
    labels = [column1[0:34], column2]

    group_1 = [dataframe[column1][18], dataframe[column2][18]]
    group_2 = [dataframe[column1][19], dataframe[column2][19]]
    group_3 = [dataframe[column1][20], dataframe[column2][20]]
    group_4 = [dataframe[column1][21], dataframe[column2][21]]
    group_5 = [dataframe[column1][22], dataframe[column2][22]]
    group_6 = [dataframe[column1][23], dataframe[column2][23]]

    x = np.arange(len(labels))
    width = 0.2

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, group_1, width, label='<$25,000')
    rects2 = ax.bar(x - width * (1 / 2), group_2, width, label='$25,000-499999')
    rects3 = ax.bar(x, group_3, width, label='$50,000-99,999')
    rects4 = ax.bar(x + width * (1 / 2), group_4, width, label='$100,000-199,999')
    rects5 = ax.bar(x + width * 1, group_5, width, label='>$200,000')
    rects6 = ax.bar(x + width * (3 / 2), group_6, width, label='Unknown')

    ax.set_ylabel('Percentage')
    ax.set_title('% of Repondents showing symptoms By Income')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    ax.bar_label(rects4, padding=3)
    ax.bar_label(rects5, padding=3)
    ax.bar_label(rects6, padding=3)

    fig.tight_layout()

    plt.show()


###################################################################################################
# Visualisation by Education Status
###################################################################################################

def disorder_education() -> Any:
    """Visualise how Educational status of respondents relate to prevalence of anxiety & depression
    disorders.
    """
    orig_dataframe = read_csv_file()
    dataframe = orig_dataframe.loc[25:30, :]

    column1 = 'Anxiety disorder'
    column2 = 'Depressive disorder'
    labels = [column1[0:34], column2]

    group_1 = [dataframe[column1][25], dataframe[column2][25]]
    group_2 = [dataframe[column1][26], dataframe[column2][26]]
    group_3 = [dataframe[column1][27], dataframe[column2][27]]
    group_4 = [dataframe[column1][28], dataframe[column2][28]]
    group_5 = [dataframe[column1][29], dataframe[column2][29]]
    group_6 = [dataframe[column1][30], dataframe[column2][30]]

    x = np.arange(len(labels))
    width = 0.2

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, group_1, width, label='Less than high school diploma')
    rects2 = ax.bar(x - width * (1 / 2), group_2, width, label='High school diploma')
    rects3 = ax.bar(x, group_3, width, label='Some college')
    rects4 = ax.bar(x + width * (1 / 2), group_4, width, label='Bachelor’s degree')
    rects5 = ax.bar(x + width * 1, group_5, width, label='Professional degree')
    rects6 = ax.bar(x + width * (3 / 2), group_6, width, label='Unknown')

    ax.set_ylabel('Percentage')
    ax.set_title('% of Repondents showing symptoms By Education Status')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)
    ax.bar_label(rects4, padding=3)
    ax.bar_label(rects5, padding=3)
    ax.bar_label(rects6, padding=3)

    fig.tight_layout()

    plt.show()


if __name__ == '__main__':
    disorder_age()
    disorder_gender()
    disorder_race()
    disorder_income()
    disorder_education()
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
