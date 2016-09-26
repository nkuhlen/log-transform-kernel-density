"""Programme to approximate the optimal bandwidth for the Dagum mixture used in
the simulation. The approximation is based on estimating the mean integrated
squared error when using the kernel density estimator with a Gaussian kernel.

"""

import numpy as np
import json
import pickle
from scipy.stats import burr
from scipy.integrate import quad

from bld.project_paths import project_paths_join as ppj
from src.model_code.kde import UnivariateKernelDensity

# Load data from simulation.
with open(ppj('OUT_DATA', 'simulation_data.pickle'), 'rb') as f_results:
    simulation_data = pickle.load(f_results)

# Load sample sizes for samples in simulation.
with open(ppj('IN_MODEL_SPECS', 'samples.json')) as f_samples:
    samples = json.load(f_samples)

# Load the number of samples to be drawn.
with open(ppj('IN_MODEL_SPECS', 'draws.json')) as f_draws:
    draws = json.load(f_draws)

# Load density parameters.
with open(ppj('IN_MODEL_SPECS', 'densities.json')) as f_densities:
    densities = json.load(f_densities)

# Create empty list for ISE, and dictionaries for MISE and the optimal
# bandwidth.
ise = []
miae = {}

# Create list of bandwidth methods and kernels.
bandwidths = ['lscv', 'silverman']
kernels = ['gaussian', 'log_gaussian']

for kernel in kernels:
    miae[kernel] = {}

    for bandwidth in bandwidths:
        miae[kernel][bandwidth] = {}

        for d in range(draws['configuration_0']):
            sample = 'sample_{}'.format(d)

            # Initialise the kernel density estimator with the current sample.
            kde = UnivariateKernelDensity(
                simulation_data['sample_size_1']['density_0'][sample],
                kernel=kernel
            )

            # Define a the integrated squared error as a function that can be
            # integrated with respect to x.
            def integrand(x):
                return (np.absolute(kde._density_value(x, bandwidth) - (
                    densities['density_1']['alpha'] *
                    burr.pdf(x,
                        densities['density_1']['c_1'],
                        densities['density_1']['d_1']) +
                    densities['density_1']['beta'] *
                    burr.pdf(x,
                        densities['density_1']['c_2'],
                        densities['density_1']['d_2'])
                )))

            # Integrate the function from minus infinity to plus infinity.
            ise_calc, err = quad(integrand, 0, np.inf)
            ise.append(ise_calc)

        miae[kernel][bandwidth] = sum(ise) / len(ise)


print(miae)

# Save the results in pickle object.
with open(ppj('OUT_ANALYSIS', 'miae_dagum_mixture.pickle'), 'wb') as f_results:
    pickle.dump(miae, f_results)
