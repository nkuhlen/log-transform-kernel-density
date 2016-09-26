"""Programme to estimate the world income distribution based on weighted income
for different years and different bandwidth selection procedures using the
standard kernel density estimator from the UnivariateKernelDensity module.

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
bw_methods = ['lscv']

# Estimate the densities for the different years and bandwidth selection
# methods.
estimated_densities_weighted = {}

for year in years:
    # Create dictionary entry for year.
    estimated_densities_weighted[year] = {}

    # Restrict data to specified year.
    data_weighted_yearly = data[data['year'] == year].weighted_rgdpwok

    # Initialise the kernel density estimator.
    kde = UnivariateKernelDensity(data=data_weighted_yearly)

    for bandwidth in sorted(bw_methods):
        kde(bandwidth, stretch=2.9)

        # Save the estimated density and corresponding support in dictionary
        estimated_densities_weighted[year][bandwidth] = {
            'support': list(kde.support),
            'density': list(kde.estimated_density)
        }

# Save the results in pickle object.
with open(
    ppj('OUT_ANALYSIS', 'estimated_densities_weighted.json'), 'w'
) as f_results:
    json.dump(estimated_densities_weighted, f_results, sort_keys=True)
