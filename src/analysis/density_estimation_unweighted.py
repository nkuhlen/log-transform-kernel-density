"""Programme to estimate the world income distribution based on unweighted
income for different years and different bandwidth selection procedures using#
the standard kernel density estimator from the UnivariateKernelDensity module.

"""


import pickle
import json

from bld.project_paths import project_paths_join as ppj
from src.model_code.kde import UnivariateKernelDensity

# Load cleaned and prepared data.
with open(ppj('OUT_DATA', 'data_pwt71.pickle'), 'rb') as f_results:
    data = pickle.load(f_results)

with open(ppj('OUT_DATA', 'years_pwt.pickle'), 'rb') as f_years:
    years = pickle.load(f_years)

# Specify bandwidth selection methods to be used in estimation.
bw_methods = ['lscv', 'silverman']

# Estimate the densities for the different years and bandwidth selection
# methods.
estimated_densities_unweighted = {}

for year in years:
    # Create dictionary entry for year.
    estimated_densities_unweighted[year] = {}

    # Restrict data to specified year.
    data_unweighted_yearly = data[data['year'] == year].rgdpwok

    # Initialise the kernel density estimator.
    kde = UnivariateKernelDensity(data=data_unweighted_yearly)

    for bandwidth in sorted(bw_methods):
        kde(bandwidth, stretch=2.9)

        # Save the estimated density and corresponding support in dictionary
        estimated_densities_unweighted[year][bandwidth] = {
            'support': list(kde.support),
            'density': list(kde.estimated_density)
        }

# Save the results in pickle object.
with open(
    ppj('OUT_ANALYSIS', 'estimated_densities_unweighted.json'), 'w'
) as f_results:
    json.dump(estimated_densities_unweighted, f_results, sort_keys=True)
