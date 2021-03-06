<h2>Português<h2>

<h4>Nome do Projeto:</h4>

Produção de Energia Elétrica com Fontes Renováveis. Um comparativo entre a produção brasileira e dos três países a frente do Brasil na escala de PIB nominal do FMI em 2020.

<h4>Objetivo principal</h4>

Destacar o progresso do Brasil no que se refere a produção de energia renovável na última década em comparação com as três economias a frente do Brazil no rank de PIB do Fundo Monetário Internacional em 2020.

<h4>Objetivos Secundários</h4>

Demonstrar habilidades com ferramentas como Pandas, Matplotlib, Seaborn e Power BI, incluindo:

* abertura de arquivos e criação de DataFrames com pandas;
* limpeza dos dados para análise (verificação de valores duplicados, faltantes, eliminação de colunas, etc.);
* filtragem de grandes volumes de dados de acordo com as necessidades do projeto;
* aplicação de métodos estatísticos para aquisição de insights;
* representar dados visualmente;
* melhores práticas e documentação de métodos.

<h3>Este projeto:</h3>

Considera apenas energias de fontes renováveis (solar, hidroelétrica, etc.). <br>
Considera apenas a produção entre 2010 e 2020.

<h3>Sobre os dados</h3>

Disponíveis no site da Kaggle através do seguinte link:
https://www.kaggle.com/prateekmaj21/electricity-production-by-source-world/metadata

<br>
<h2><strong>English</strong><h2>

<h4>Project name:</h4>

Production of electricity through renewable sources: A comparative between Brazil's production and the three economies ahead of Brazil on IMF's nominal GDP rank for 2020.

<h4>Main goal:</h4>
To highlight Brazil's progress regarding production of electricity through renewable sources in the last decade compared to the next three economies ahead of Brazil in the International Monetary Fund's nominal GDP rank.

<h4>Secondary goal:</h4>
To display abilities with Pandas, Matplotlib, Seaborn and Power BI, including but not limited to:

* read files and create DataFrames
* clean unnecessary data (drop columns, check duplicates, check missing data, etc.
* filter large amounts of data according to the needs of the project
* application of statistic functions to gather valuable information
* visually represent data
* best practices and documentation


<h3>Task</h3>

To highlight differences and similarities among Brazil's production of electricity through renewable sources and the next three countries on IMF's nominal GDP rank for 2020. According to the International Monetary Fund (IMF), the three countries ahead of Brazil regarding nominal GDP in 2020 were: Russia, South Korea and Canada.

<h3>This project:</h3>

* considers only renewable energy sources (wind, solar, etc.)
* considers only the production between 2010 and 2020

<h3>Data</h3>
Data from Our World in Data, compilled by the same in two sources: BP Statistical Review of World Energy & Ember. Csv file acquired on Kaggle. Link to the Dataset:
https://www.kaggle.com/prateekmaj21/electricity-production-by-source-world/metadata

<h3>How to adapt this project</h3>

The way in which this project is coded makes it highly adaptable. The functions have been documented, should you need help with them.

If you want to analyse <i>different sources</i>:
* change the columns specified in the usecol= (inside pandas' read_csv function). Also, remember to specify which source to analyse in the functions/plots.

If you want to analyse <i>different countries</i>:
* Change the name of the country in "your_dataframe.loc['country']" and in the functions/plots.

If you want to plot <i>different graphs/charts</i>:
* Check the documentation for the matplotlib and seaborn libraries. Pandas also has some visualisation options, hwever, limited.

To plot the current data:
* Uncomment lines with <i>plt.function_name</i>.

<h3>Future Updates</h3>

Test file with either pytest or unittest.
