"""Programme to plot the weighted and unweighted GDP per worker time series
for some specified countries.

"""

import pickle
from matplotlib import rc
import matplotlib.pyplot as plt

from bld.project_paths import project_paths_join as ppj

# Load cleaned and prepared data.
with open(ppj('OUT_DATA', 'data_pwt71.pickle'), 'rb') as f_results:
    data = pickle.load(f_results)

# Specify countries.
countries = ['CH2', 'IND', 'GER', 'NGA', 'SLE', 'USA']

# Specify plot parameters.
plot_params = {
    'colour_bw': {'lscv': '#9C9C9C', 'silverman': '#484748'},
    'colour_bw_presentation': {'lscv': 'blue', 'silverman': 'black'},
    'figure_width': 10,
    'figure_height': 7.5,
    'font_size_labels': 30,
    'font_size_legend': 28,
    'font_size_ticks': 32,
    'line_width': 3.5,
    'title_size': 28
}
colour = {
    'CH2': '#b2182b',
    'IND': '#d6604d',
    'GER': '#4d4d4d',
    'NGA': '#2166ac',
    'SLE': '#4393c3',
    'USA': '#878787'
}
labels = {
    'CH2': 'China',
    'IND': 'India',
    'GER': 'Germany',
    'NGA': 'Nigeria',
    'SLE': 'Sierra Leone',
    'USA': 'USA'
}

# Loop over unweighted and weighted GDP per worker to plot the time series for
# the countries specified above.
for gdp in ['rgdpwok', 'weighted_rgdpwok']:
    # Create figure.
    fig, ax = plt.subplots(
        figsize=(plot_params['figure_width'], plot_params['figure_height'])
    )

    for country in countries:
        # Use latex font.
        rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
        rc('text', usetex=True)

        # Create plot.
        ax.plot(
            data[data['isocode'] == country]['year'],
            data[data['isocode'] == country][gdp],
            label=labels[country],
            linewidth=plot_params['line_width'],
            color=colour[country]
        )

        if gdp == 'rgdpwok':
            ax.set_ylim([-2000, 100000])
        elif gdp == 'weighted_rgdpwok':
            ax.set_ylim([-100, 5000])

        # Set axis labels.
        ax.set_xlabel(
            'Year',
            fontsize=plot_params['font_size_labels']
        )
        if gdp == 'rgdpwok':
            ax.set_ylabel(
                'GDP per Worker',
                fontsize=plot_params['font_size_labels']
            )
        elif gdp == 'weighted_rgdpwok':
            ax.set_ylabel(
                'Weighted GDP per Worker',
                fontsize=plot_params['font_size_labels']
            )

        # Adjust axis ticks.
        ax.tick_params(
            axis='x', labelsize=plot_params['font_size_ticks'], direction='out'
        )
        ax.tick_params(
            axis='y', labelsize=plot_params['font_size_ticks'], direction='out'
        )
        plt.xticks(
            [1970, 1980, 1990, 2000, 2010]
        )

        if gdp == 'rgdpwok':
            plt.yticks(
                [0, 20000, 40000, 60000, 80000, 100000],
                ['0', '20K', '40K', '60K', '80K', '100K']
            )
        elif gdp == 'weighted_rgdpwok':
            plt.yticks(
                [0, 1000, 2000, 3000, 4000, 5000],
                ['0', '1K', '2K', '3K', '4K', '5K']
            )

        # Remove frame.
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # Add a legend.
        if gdp == 'rgdpwok':
            ax.legend(
                fontsize=plot_params['font_size_legend'], frameon=False,
                loc='upper left', bbox_to_anchor=(0, 1.08), ncol=2
            )

    # Save figure to pdf file.
    fig.savefig(
        ppj('OUT_FIGURES', 'fig_comparison_gdp_{}.pdf'.format(gdp)),
        bbox_inches="tight"
    )

    # Clear figure.
    plt.close(fig)
