.. _analysis:

************************************
Main model estimations / simulations
************************************

The *src/analysis* directory contains the main modules for the density estimation and the approximation of the optimal bandwidths for distributions other than the standard normal distribution. 

Density Estimation
==================

The modules beginning with ``density_estimation_`` contain the density estimations for the world income distributions for unweighted and weighted income. ``density_estimation_log`` uses the log-transform kernel density estimator to estimate the world income distribution. The module reads the data and the specified years from the data management process and calculates the density for every year. The results are stored in a JSON file for the visualisation step.

Mean Integrated Absolute Error
==============================

The modules beginning with ``miae_`` estimate the Mean Integrated Squared Error for the standard kernel density estimator and the log-transform kernel density estimator. Note that the calculation of the Integrated Absolute Error integrals is restricted to positive values since both the Dagum distribution and the log-transform estimator are only defined for positive values. The results are stored in pickle objects for the visualisation step.


Testing
=======

The module ``test_kde.py`` contains a limited test suite for the kernel density estimator in ``kde.py``.
