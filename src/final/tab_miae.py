"""Create a LaTeX table of the simulation results obtained from miae_dagum.py
and miae_dagum_mixture.py.

"""

import pickle
from bld.project_paths import project_paths_join as ppj

# Load values of MIAE from simulation.
with open(ppj('OUT_ANALYSIS', 'miae_dagum.pickle'), 'rb') as f_results:
    miae_dagum = pickle.load(f_results)

with open(ppj('OUT_ANALYSIS', 'miae_dagum_mixture.pickle'), 'rb') as f_results:
    miae_dagum_mixture = pickle.load(f_results)

# Create list for loop.
bw_methods = ['lscv', 'silverman']

# Define a table row with placeholders.
table_row = '{method} {str} \\tabularnewline\n'
table_entry = ' & {val:.4f}'

# Write the results to a LaTeX table.
with open(ppj('OUT_TABLES', 'miae.tex'), 'w') as tex_file:

    # Specify the number of columns.
    num_of_columns = 5

    # Top of table.
    tex_file.write(
        '\\renewcommand{\\arraystretch}{1.2} \\begin{tabular}{l' + 'c' *
        (num_of_columns) + '}\n\\toprule\n'
    )

    # Header row.
    tex_file.write(
        '& \\multicolumn{' + str(2) + '}{c}{Dagum} & \\multicolumn{' + str(2) +
        '}{c}{Dagum Mixture}'
    )
    tex_file.write('\\tabularnewline\n')

    tex_file.write(
        '\\cline{2-' + str(num_of_columns) +
        '} & Standard & Log-Transform & Standard & Log-Transform'
    )
    tex_file.write('\\tabularnewline\\midrule\n')

    # Add rows to table.
    for method in bw_methods:
        table_insert = ''
        table_insert += table_entry.format(val=miae_dagum['gaussian'][method])
        table_insert += table_entry.format(
            val=miae_dagum['log_gaussian'][method]
        )
        table_insert += table_entry.format(
            val=miae_dagum_mixture['gaussian'][method]
        )
        table_insert += table_entry.format(
            val=miae_dagum_mixture['log_gaussian'][method]
        )

        # Define row names for table.
        if method == 'lscv':
            bw_table = 'LSCV'
        elif method == 'silverman':
            bw_table = 'Silverman'

        tex_file.write(table_row.format(method=bw_table, str=table_insert))
        tex_file.write('\n')

    # Bottom of table.
    tex_file.write('\\bottomrule\n\\end{tabular}\n')
