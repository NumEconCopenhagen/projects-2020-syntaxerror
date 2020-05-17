# Data analysis project

Our project is titled **Armed conflicts dataproject** and is about armed conflict around the world. 

The **results** of the project can be seen from running [Armed_conflicts_dataproject.ipynb](Armed_conflicts_dataproject.ipynb)

This **loades following datasets**:

1. [Armed_conflicts_dataproject.ipynb](Armed_conflicts_dataproject.ipynb)
2. [export_dataframe.csv](export_dataframe.csv) 
is a smaller version of "ged191.csv" with dropped variables from 
https://ucdp.uu.se/?fbclid=IwAR0586RVfBKd1n4Q7DlMVIRV4pDtJV8szoAGG7w62-Fm8QbVKPyTSqlJdM4#/
3. [Countries](Countries) Which we got from the website https://www.naturalearthdata.com/downloads/110m-cultural-vectors/

**Dependencies:** Apart from a standard Anaconda Python 3 installation, the project requires the following installations:
``geopandas`` and ``Bokeh``
This can be installed in Anaconda

**Data generation**
Because of the very large dataset, we have chosen to drop some of the variables. This wasn’t enough, therefore we have decided only to use “2018” as our year of analysis, which is in our csv file [export_dataframe.csv](export_dataframe.csv) .
We chose to first group the armed conflicts in regions and then group the armed conflict according to in which country it occured.

Furthermore we had a lot of armed conflicts in Afghanistan, and we have therefore choosen to remove “Afghanistan” from the bar chart. This gives us a better insight of the armed conflicts in the rest of the world.





