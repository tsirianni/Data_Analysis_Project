<h1>Overview</h1>

<h4>Project name:</h4>

Production of electricity through renewable sources: A comparative between Brazil's production and the three economies ahead of Brazil on IMF's nominal GDP rank for 2020.

<h4>Main goal:</h4>
To complete the task as described on the next section.

<h4>Secondary goal:</h4>
To display abilities with pandas, matplotlib and seaborn, including but not limited to:

* read files and create DataFrames
* clean unnecessary data (drop columns, check duplicates, check missing data, etc.
* filter large amounts of data according to the needs of the project
* application of statistic functions to gather valuable information
* visually represent data


<h3>Task</h3>

To highlight differences and similarities among Brazil's production of electricity through renewable sources and the next three countries on IMF's nominal GDP rank for 2020. According to the Intermational Monetary Fund (IMF), the three countries ahead of Brazil regarding nominal GDP in 2020 were: Russia, South Korea and Canada.

<h3>This project:</h3>

* considers only renewable energy sources (wind, solar, etc.)
* considers only the production between 2010 and 2020

<h3>Data</h3>
Data from Our World in Data, compilled by the same in two sources: BP Statistical Review of World Energy & Ember. Csv file acquired on Kaggle. Link to the Dataset:
https://www.kaggle.com/prateekmaj21/electricity-production-by-source-world/metadata

<h3>How to adapt this project</h3>

The way in which this project is coded makes it highly adaptable.

If you want to analyse <i>different sources</i>:
* change the columns specified in the usecol= (inside pandas' read_csv function). Also, remember to specify which source to analyse in the functions/plots.

If you want to analyse <i>different countries</i>:
* Change the name of the country in "your_dataframe.loc['country']" and in the functions/plots.

If you want to plot <i>different graphs/charts</i>:
* Check the documentation for the matplotlib and seaborn libraries. Pandas also has some visualisation options, hwever, limited.

To plot the current data:
* Uncomment lines with <i>plt.function_name</i>.
