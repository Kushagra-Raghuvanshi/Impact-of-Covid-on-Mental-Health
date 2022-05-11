"""Project: Impact of Covid 19 on Mental Health - Study on effects of the Pandemic on stress,
anxiety and depression levels and an insight on thier subsequent corellation with Impact on Drug Use
 and Suicidal Ideation

Authors : Kushagra Raghuvanshi, Madhav Garg, Jacob Grimm

"""
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt

###################################################################################################
# Files containing the data
###################################################################################################
# file1 = 'Table-1.csv'
# file2 = 'pulse_survey_dataset.csv'
# NOTE: This file shold be in same folder as this python file


###################################################################################################
# Code for reading file
###################################################################################################

def read_csv_file() -> Any:
    """Read csv file as a pandas Dataframe
    """
    return pd.read_csv('Table-1.csv', index_col=None, na_values=['NA'])


###################################################################################################
# Relation between Anxiety levels and Substance Use
###################################################################################################

def relation_axiety_substanceuse() -> Any:
    """Analyze if we can find out any functional relation/ trends between anxiety symptoms and
    substance use reports by plotting thier ratio based on different characteristics including
    Age group, Gender, Race/Ethinicity, Income and Educational status
    """

    column1, _, column3, _ = column_row_title()[0]
    plot_relation(column1, column3, 'Ratio Substance use / Anxiety disorder symptoms', 0)


###################################################################################################
# Relation between Depression levels and Substance Use
###################################################################################################

def relation_depression_substanceuse() -> Any:
    """Analyze if we can find out any functional relation/ trends between depression symptoms and
    substance use reports by plotting thier ratio based on different characteristics including
    Age group, Gender, Race/Ethinicity, Income and Educational status
    """

    _, column2, column3, _ = column_row_title()[0]
    plot_relation(column2, column3, 'Ratio Substance use / Depressive disorder symptoms', 1)


###################################################################################################
# Relation between Anxiety levels and Suicidal Ideation reports
###################################################################################################

def relation_axiety_suicidalideation() -> Any:
    """Analyze if we can find out any functional relation/ trends between anxiety symptoms and
    suicidal ideation reports by plotting thier ratio based on different characteristics including
    Age group, Gender, Race/Ethinicity, Income and Educational status
    """

    column1, _, _, column4 = column_row_title()[0]
    plot_relation(column1, column4, 'Ratio Suicidal Ideation / Anxiety disorder symptoms', 2)


###################################################################################################
# Relation between Depression levels and Suicidal Ideation reports
###################################################################################################

def relation_depression_suicidalideation() -> Any:
    """Analyze if we can find out any functional relation/ trends between depression symptoms and
    suicidal ideation reports by plotting thier ratio based on different characteristics including
    Age group, Gender, Race/Ethinicity, Income and Educational status
    """

    _, column2, _, column4 = column_row_title()[0]
    plot_relation(column2, column4, 'Ratio Suicidal Ideation / Depressive disorder symptoms', 3)


# Helper Functions ################################################################################

def column_row_title() -> list[list]:
    """Return list of variables for Column keys, Row keys and Titles to eliminate redundancy
    """

    # Column labels ##########################
    column1 = 'Anxiety disorder'
    column2 = 'Depressive disorder'
    column3 = 'Started or increased substance use to cope with pandemic-related stress or emotions'
    column4 = 'Seriously considered suicide in past 30 days'

    # Row labels #############################
    a_row1 = '18 to 24 years'
    a_row2 = '25 to 44 years'
    a_row3 = '44 to 64 years'
    a_row4 = '>64 years'

    g_row1 = 'Female'
    g_row2 = 'Male'
    g_row3 = 'Other'

    r_row1 = 'White, non-Hispanic'
    r_row2 = 'Black, non-Hispanic'
    r_row3 = 'Asian, non-Hispanic'
    r_row4 = 'Other race or multiple races, non-Hispanic'
    r_row5 = 'Hispanic, any race(s)'
    r_row6 = 'Unknown'

    i_row1 = '<$25,000'
    i_row2 = '$25,000-499999'
    i_row3 = '$50,000-99,999'
    i_row4 = '$100,000-199,999'
    i_row5 = '>$200,000'
    i_row6 = 'Unknown'

    e_row1 = 'Less than high school diploma'
    e_row2 = 'High school diploma'
    e_row3 = 'Some college'
    e_row4 = 'Bachelor’s degree'
    e_row5 = 'Professional degree'
    e_row6 = 'Unknown'

    title1 = 'Relation b/w Anxiety-level & Substance Use'
    title2 = 'Relation b/w Depression-level & Substance Use'
    title3 = 'Relation b/w Anxiety-level & Suicidal Ideation'
    title4 = 'Relation b/w Depression-level & Suicidal Ideation'

    return [[column1, column2, column3, column4], [a_row1, a_row2, a_row3, a_row4],
            [g_row1, g_row2, g_row3], [r_row1, r_row2, r_row3, r_row4, r_row5, r_row6],
            [i_row1, i_row2, i_row3, i_row4, i_row5, i_row6],
            [e_row1, e_row2, e_row3, e_row4, e_row5, e_row6], [title1, title2, title3, title4]]


def plot_relation(x: str, y: str, label_y: str, title_no: int) -> Any:
    """Develop line graphs to represent the relation
    """

    dataframe = read_csv_file()

    x_age = dataframe[x][6:10]
    y_age = dataframe[y][6:10]
    ratio_age = y_age.div(x_age)

    x_gender = dataframe[x][2:5]
    y_gender = dataframe[y][2:5]
    ratio_gender = y_gender.div(x_gender)

    x_race = dataframe[x][11:17]
    y_race = dataframe[y][11:17]
    ratio_race = y_race.div(x_race)

    x_income = dataframe[x][18:24]
    y_income = dataframe[y][18:24]
    ratio_income = y_income.div(x_income)

    x_education = dataframe[x][25:31]
    y_education = dataframe[y][25:31]
    ratio_education = y_education.div(x_education)

    plt.figure(column_row_title()[6][title_no] + '(By Age Group)')
    y = ratio_age
    x = column_row_title()[1]
    plt.plot(x, y)
    plt.ylabel(label_y)
    plt.xlabel('Age group')

    plt.figure(column_row_title()[6][title_no] + '(By Gender)')
    y = ratio_gender
    x = column_row_title()[2]
    plt.plot(x, y)
    plt.ylabel(label_y)
    plt.xlabel('Gender')

    plt.figure(column_row_title()[6][title_no] + '(By Race/Ethinicity)')
    y = ratio_race
    x = column_row_title()[3]
    plt.plot(x, y)
    plt.ylabel(label_y)
    plt.xlabel('Race/Ethinicity')

    plt.figure(column_row_title()[6][title_no] + '(By Income)')
    y = ratio_income
    x = column_row_title()[4]
    plt.plot(x, y)
    plt.ylabel(label_y)
    plt.xlabel('Household Income')

    plt.figure(column_row_title()[6][title_no] + '(By Education Status)')
    y = ratio_education
    x = column_row_title()[5]
    plt.plot(x, y)
    plt.ylabel(label_y)
    plt.xlabel('Education Status')

    plt.show()


##################################################################################################


if __name__ == '__main__':
    relation_axiety_substanceuse()
    relation_depression_substanceuse()
    relation_axiety_suicidalideation()
    relation_depression_suicidalideation()
