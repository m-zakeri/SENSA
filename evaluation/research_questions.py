"""
SENSA: Software Entity Name Suggestion Apparatus

This module contains method to visualize the results of SENSA-1


"""
__author__ = 'Morteza Zakeri'
__version__ = '1.0'

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)


def plot_sensa_pefromance_changes():
    dir = r'D:/Users/Morteza/OneDrive/Online2/_04_2o/o2_university/PhD/Project21/a170_refactoring_for_readability/evaluations/'
    file = 'evaluation_sensa1.xlsx'
    df = pd.read_excel(dir+file)
    df1 = df.melt(id_vars=['Model', 'Method filter'], value_name='value',)

    g = sns.barplot(data=df1,
                    x=df1['Model'], y=df1['value'],
                    hue=df1['Method filter'],
                    )
    change_width(g, .30)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_sensa_pefromance_changes()