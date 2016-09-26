.. _final:

************************************
Visualisation and results formatting
************************************

Documentation of the code in **final**. 

Simulation
==========

:file:`fig_simulation_true_densities.py`:

	This file creates plots of the underlying densities used in the simulation studies. 

:file:`tab_miae.py`:

	This file creates a LaTeX table of the simulation results obtained from ``miae_dagum.py`` and ``miae_dagum_mixture.py``.


Application
===========

:file:`fig_comparison_gdp.py`:

	This file plots the weighted and unweighted GDP per worker time series for some specified countries.

:file:`fig_map_included_countries.r`:

	This R file creates a map of the countries included in the estimation of the world income distributions. The list is obtained from ``data_preparation_pwt_71.py``.

:file:`fig_world_incom_distribution_log.py`:

	This file plots the estimated world income distributions from ``density_estimation_log.py`` for different years and bandwidths obtained from the specified bandwidth selection procedures.

:file:`fig_world_incom_distribution_unweighted.py`:

	This file plots the estimated world income distributions from ``density_estimation_unweighted.py`` for different years and bandwidths obtained from the specified bandwidth selection procedures.

:file:`fig_world_incom_distribution_weighted.py`:

	This file plots the estimated world income distributions from ``density_estimation_weighted.py`` for different years and bandwidths obtained from the specified bandwidth selection procedures.
