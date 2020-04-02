# Data analysis project

Our project is titled **PROJECT TITLE** and is about EXPLAIN.

The **results** of the project can be seen from running [dataproject.ipynb](dataproject.ipynb).

This **loades two datasets**:

1. INDKP101.xlsx downloaded from statistikbanekn.dk/INDKP101
1. RAS200.xlsx downloaded from statistikbanekn.dk/RAS200

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:

``pip install matplotlib-venn`` and 
``geopandas``
This can be installed in Anaconda

**Data generation**
Because of the very large dataset, we have chosen to drop some of the variables. This wasn’t enough, therefore we have decided only to use “2018” as our year of analysis. Because of a lot of armed conflicts in Afghanistan, Afghanistan was split into 5 different coordinates, that we have summed up to 1.

Furthermore we had a lot of armed conflicts in Afghanistan, and we have therefore choosen to remove “Afghanistan” from the bar chart. This gives us a better insight of the armed conflicts in the rest of the world.

**Data analysis**
In this workbook we have analyzed the data generated in **link til projekt** by:
- Makeing a barplot to analyze with continent where most armed conflicts occur 
- Makeing a barplot to analyze whick countries have the most armed conflicts
- Makeing a map to analyze the degree of armed conflicts




