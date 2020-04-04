# Data analysis project

Our project is titled **Armed conflicts dataproject** and is about armed conflict around the world. 

The **results** of the project can be seen from running [Armed_conflicts_dataproject.ipynb](Armed_conflicts_dataproject.ipynb)

This **loades following datasets**:

1. [Armed conflicts dataproject.ipynb](Armed conflicts dataproject.ipynb)
2. [export_dataframe.csv](export_dataframe.csv) 
is a smaller version of "ged191.csv" with dropped variables from 
https://ucdp.uu.se/?fbclid=IwAR0586RVfBKd1n4Q7DlMVIRV4pDtJV8szoAGG7w62-Fm8QbVKPyTSqlJdM4#/
3. [Countries](Countries)

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:
``geopandas`` and ``seaborn``
This can be installed in Anaconda

**Data generation**
Because of the very large dataset, we have chosen to drop some of the variables. This wasn’t enough, therefore we have decided only to use “2018” as our year of analysis, which is in our csv file [export_dataframe.csv](export_dataframe.csv) .
Because of a lot of armed conflicts in Afghanistan, Afghanistan was split into 5 different coordinates, that we have summed up to 1.

Furthermore we had a lot of armed conflicts in Afghanistan, and we have therefore choosen to remove “Afghanistan” from the bar chart. This gives us a better insight of the armed conflicts in the rest of the world.

**Data analysis**
In this workbook we have analyzed the data generated in [Armed conflicts dataproject.ipynb](Armed conflicts dataproject.ipynb) by:
- Makeing a barplot to analyze with continent where most armed conflicts occur 
- Makeing a barplot to analyze whick countries have the most armed conflicts
- Makeing a map to analyze the degree of armed conflicts




