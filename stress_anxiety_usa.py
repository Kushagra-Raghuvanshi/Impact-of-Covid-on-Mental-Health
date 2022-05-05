"""Project: Impact of Covid 19 on Mental Health - Study on effects of the Pandemic on stress,
anxiety and depression levels and an insight on their subsequent corellation with Impact on Drug Use
 and Suicidal Ideation

Authors : Kushagra Raghuvanshi, Madhav Garg, Jacob Grimm
"""
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt


def read_march_file() -> Any:
    """Return march.csv as a dataframe.
    """
    return pd.read_csv('march.csv', index_col=None, na_values=['NA'])


def read_may_file() -> Any:
    """Return may.csv as a dataframe.
    """
    return pd.read_csv('may.csv', index_col=None, na_values=['NA'])


def stress_box_plot() -> Any:
    """ Return a boxplot displaying preceived stress during March and May 2020
    """
    march_dataframe = read_march_file()
    may_dataframe = read_may_file()
    stress_march = march_dataframe["Scale_PSS10_UCLA_3"]
    stress_may = may_dataframe["Scale_PSS10_UCLA_3"]
    columns = [stress_march, stress_may]
    fig, ax = plt.subplots()
    ax.set_title('Perceived Stress in March')
    ax.boxplot(columns)
    ax.set_ylabel('Level of Stress')
    plt.xticks([1, 2], ["March", "May"], rotation=0)
    plt.show()


def anxiety_box_plot() -> Any:
    """ Return a boxplot displaying preceived anxiety during March and May 2020
    """
    march_dataframe = read_march_file()
    may_dataframe = read_may_file()
    anxiety_march = march_dataframe["BFF_15_1"]
    anxiety_may = may_dataframe["BFF_15_1"]
    columns = [anxiety_march, anxiety_may]
    fig, ax = plt.subplots()
    ax.set_title('Perceived Anxiety in March and May 2020')
    ax.boxplot(columns)
    ax.set_ylabel('Level of Anxiety')
    plt.xticks([1, 2], ["March", "May"], rotation=0)
    plt.show()


if __name__ == '__main__':
    stress_box_plot()
    anxiety_box_plot()
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['python_ta.contracts', 'pandas', 'matplotlib.pyplot'],
    #     'allowed-io': [],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200']
    # })

    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # import doctest
    # doctest.testmod()
