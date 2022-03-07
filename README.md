# Mathematical Modeling Finds Disparate Interferon Production Rates Drive Strain-Specific Immunodynamics during Deadly Influenza Infection 
Authors: Emily E. Ackerman[^1],[^†], Jordan J.A. Weaver[^1],[^†] and Jason E. Shoemaker[^1],[^2],[^3],[^*]

[^1]:	Department of Chemical & Petroleum Engineering, University of Pittsburgh, Pittsburgh, PA 15260, USA
[^2]:	McGowan Institute for Regenerative Medicine, University of Pittsburgh, Pittsburgh, PA 15260, USA
[^3]:     Department of Computational and Systems Biology, University of Pittsburgh, Pittsburgh, PA 15260, USA
[^†]:     These authors contributed equally to this work
[^*]:	Correspondence: jason.shoemaker@pitt.edu

## Abstract
The timing and magnitude of the immune response (i.e., the immunodynamics) associated with the early innate immune response to viral infection display distinct trends across influenza A virus subtypes in vivo. Evidence shows that the timing of the type-I interferon response and overall magnitude of immune cell infiltration are correlated to more severe outcomes. However, the mechanisms driving distinct immunodynamics in infections with different virus strains (strain-specific immunodynamics) remain unclear. Here, computational modeling and strain-specific immunologic data are used to identify the immune interactions that differ in mice infected with low pathogenic H1N1 or high pathogenic H5N1 influenza viruses. Using Markov chain Monte Carlo parameterization and large-scale, iterative parameter explorations, ordinary differential equation models of the early interferon and inflammatory response are trained to low pathogenic H1N1 and high pathogenic H5N1 influenza virus infection data to determine which of the systems’ kinetic rates (parameters) may differ between the infection cohorts. Computational exploration of free parameters between strains suggests that the production rate of interferon is the major driver of strain-specific immune responses observed in vivo, and points toward the positive feedback relationship between the viral load and interferon production as the main source of variance between infection outcomes. A greater understanding of the contributors to strain-specific immunodynamics can be utilized in future efforts aimed at treatment development to enhance clinical outcomes of high pathogenic viral strains. 

## Code Availability
This repository consists of example code to recreate the figures present in the original manuscript

## Plot Replication
Figure 1 (model schematic) and Figures 3 and 6 (parameter distribution and eFAST sensitivity) are straightforward plotting of results from existing packages and are thus excluded.

### Figure 2
![Figure 2](/Plotting/Figure_2/Figure_2.png)
Model 4 output for minimum energy parameter set (lines) and corresponding training data (markers) for H1N1 (top row) and H5N1 (bottom row). All Independent results (all parameters allowed to independently estimate across strains) are shown in black and All Shared results (all parameters shared between strains) are shown in blue. Intervals represent the standard deviation of the 1,000 lowest energy parameter sets. Data from Shoemaker et al [^6] are shown with the standard deviation associated with triplicate data points per timepoint.

### Figure 4
![Figure 4](/Plotting/Figure_4/Figure_4.png)
Model 4 output for the minimum energy parameter set (line) for solo independent parameteri-zations and corresponding training data (markers) for H1N1 (top row) and H5N1 (bottom row). Data from Shoemaker et al [^6] are shown with the standard deviation associated with triplicate data points per timepoint.

### Figure 5
![Figure 5](/Plotting/Figure_5/Figure_5.png)
Model 4 output for minimum energy parameter set (line) for virus related parameter independent (V) and corresponding training data (markers) for H1N1 (top row) and H5N1 (bottom row). V is representative of four viral parameters: k, K, rIFN,V and dV. Data from Shoemaker et al [^6] are shown with the standard error associated with triplicate data points per timepoint.

[^6]: [doi:10.1371/journal.ppat.1004856](https://doi:10.1371/journal.ppat.1004856)

