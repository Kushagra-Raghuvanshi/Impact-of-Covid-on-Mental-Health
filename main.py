"""Project: Impact of Covid 19 on Mental Health - Study on effects of the Pandemic on stress,
anxiety and depression levels and an insight on thier subsequent corellation with Impact on Drug Use
 and Suicidal Ideation

Authors : Kushagra Raghuvanshi, Madhav Garg, Jacob Grim

"""
import stress_anxiety_usa
import disorder_analysis_bystate
import disorder_visualisation_complete
import drug_suicide_visualisation
import correlation_and_computations

if __name__ == '__main__':
    # Module 1
    stress_anxiety_usa.stress_box_plot()
    stress_anxiety_usa.anxiety_box_plot()

    # Module 2
    disorder_analysis_bystate.depression_levels_plot()
    disorder_analysis_bystate.depression_scatter_plot()
    disorder_analysis_bystate.allstate_depression_regression()
    disorder_analysis_bystate.anxiety_levels_plot()
    disorder_analysis_bystate.anxiety_scatter_plot()
    disorder_analysis_bystate.allstate_anxiety_regression()

    # Module 3
    disorder_visualisation_complete.disorder_age()
    disorder_visualisation_complete.disorder_gender()
    disorder_visualisation_complete.disorder_race()
    disorder_visualisation_complete.disorder_income()
    disorder_visualisation_complete.disorder_education()

    # Module 4
    drug_suicide_visualisation.drug_suicide_age()
    drug_suicide_visualisation.drug_suicide_gender()
    drug_suicide_visualisation.drug_suicide_race()
    drug_suicide_visualisation.drug_suicide_income()
    drug_suicide_visualisation.drug_suicide_education()

    # Module 5
    correlation_and_computations.relation_axiety_substanceuse()
    correlation_and_computations.relation_depression_substanceuse()
    correlation_and_computations.relation_axiety_suicidalideation()
    correlation_and_computations.relation_depression_suicidalideation()
