import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create Panda's DataFrame.
# Columns repeated after the method to specify the desired order.
production = pd.read_csv('Electricity_Production_By_Source.csv',
usecols=['Entity', 'Year', 'Electricity from hydro (TWh)', 'Electricity from solar (TWh)', 'Electricity from wind (TWh)', 'Electricity from other renewables (TWh)'],
index_col='Entity')[['Year', 'Electricity from hydro (TWh)', 'Electricity from solar (TWh)', 'Electricity from wind (TWh)', 'Electricity from other renewables (TWh)']]

print(production.loc[['Brazil'], 'Electricity from hydro (TWh)'].tail(11).mean())

# Cleaning DataFrame:
# Checking whether the countries of our sample have missing data or not and if there are duplicated values.
production.loc['Brazil'].isnull().sum()
production.loc['Russia'].isnull().sum()
production.loc['South Korea'].isnull().sum() # Confirmed!
production.loc['Canada'].isnull().sum()

# Checking for duplicated values in each country.
production.loc['Brazil'].duplicated().any()
production.loc['Russia'].duplicated().any()
production.loc['South Korea'].duplicated().any() # No duplicated values. Great!
production.loc['Canada'].duplicated().any()


##### Filtering the countries, range for the analisys (2010-2020) and renewable sources.
# .tail() specifies the analysis range (last 10 years)

def ren_source(country, source=False):

    all_sources = production.loc[str(country)].tail(11)

    if source:
        if source == 'hydro':
            source = production.loc[[str(country)], 'Electricity from hydro (TWh)'].tail(11)
            return source
        elif source == 'solar':
            source = production.loc[[str(country)], 'Electricity from solar (TWh)'].tail(11)
            return source
        elif source == 'wind':
            source = production.loc[[str(country)], 'Electricity from wind (TWh)'].tail(11)
            return source
        else:
            source = production.loc[[str(country)], 'Electricity from other renewables (TWh)'].tail(11)
            return source
    else:
        return all_sources
    
print(ren_source('Canada'))



# Getting the mean for each using the same structure from the previous function

def mean_source(country, source=False):
    all_sources = production.loc[str(country)].tail(11).mean()

    if source:
        if source == 'hydro':
            source = production.loc[[str(country)], 'Electricity from hydro (TWh)'].tail(11).mean()
            return source
        elif source == 'solar':
            source = production.loc[[str(country)], 'Electricity from solar (TWh)'].tail(11).mean()
            return source
        elif source == 'wind':
            source = production.loc[[str(country)], 'Electricity from wind (TWh)'].tail(11).mean()
            return source
        else:
            source = production.loc[[str(country)], 'Electricity from other renewables (TWh)'].tail(11).mean()
            return source
    else:
        return all_sources


# Data Visualization 1 - Comparison of electricity production among countries (line plot)

sns.set_theme(style='whitegrid')
sns.set_context("notebook", font_scale=1, rc={"lines.linewidth": 2.0})
period = list(range(2010, 2021))
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(period, ren_source('Brazil', 'hydro'), label='Hydro', marker='.')
axs[0, 0].plot(period, ren_source('Brazil', 'solar'), label='Solar', marker='.')
axs[0, 0].plot(period, ren_source('Brazil', 'wind'), label='Wind', marker='.')
axs[0, 0].plot(period, ren_source('Brazil', 'other'), label='Other', marker='.')
axs[0, 0].set_title('Brazil')

axs[0, 1].plot(period, ren_source('Russia', 'hydro'), label='Hydro', marker='.')
axs[0, 1].plot(period, ren_source('Russia', 'solar'), label='Solar', marker='.')
axs[0, 1].plot(period, ren_source('Russia', 'wind'), label='Wind', marker='.')
axs[0, 1].plot(period, ren_source('Russia', 'other'), label='Other', marker='.')
axs[0, 1].set_title('Russia')

axs[1, 0].plot(period, ren_source('South Korea', 'hydro'), label='Hydro', marker='.')
axs[1, 0].plot(period, ren_source('South Korea', 'solar'), label='Solar', marker='.')
axs[1, 0].plot(period, ren_source('South Korea', 'wind'), label='Wind', marker='.')
axs[1, 0].plot(period, ren_source('South Korea', 'other'), label='Other', marker='.')
axs[1, 0].set_title('South Korea')

axs[1, 1].plot(period, ren_source('Canada', 'hydro'), label='Hydro', marker='.')
axs[1, 1].plot(period, ren_source('Canada', 'solar'), label='Solar', marker='.')
axs[1, 1].plot(period, ren_source('Canada', 'wind'), label='Wind', marker='.')
axs[1, 1].plot(period, ren_source('Canada', 'other'), label='Other', marker='.')
axs[1, 1].set_title('Canada')

# Setting labels for each plot
for ax in axs.flat:
    ax.set(xlabel='Years', ylabel='Production in Terawatt-hour (TWh)')

# plt.suptitle('Electricity production from renewable sources (2010 - 2020)')
# plt.subplots_adjust(wspace=0.3, hspace=0.45)
# plt.legend()
# plt.show()


#### Mean of production by source/country (horizontal bar)
# Countries = y axis | source_means = x axis

hydro_countries = ['Brazil', 'Russia', 'South Korea', 'Canada']
hydro_means = [mean_source('Brazil', 'hydro'), mean_source('Russia', 'hydro'), mean_source('South Korea', 'hydro'), mean_source('Canada', 'hydro')]

solar_countries = ['Brazil', 'Russia', 'South Korea', 'Canada']
solar_means = [mean_source('Brazil', 'solar'), mean_source('Russia', 'solar'), mean_source('South Korea', 'solar'), mean_source('Canada', 'solar')]

wind_countries = ['Brazil', 'Russia', 'South Korea', 'Canada']
wind_means = [mean_source('Brazil', 'wind'), mean_source('Russia', 'wind'), mean_source('South Korea', 'wind'), mean_source('Canada', 'wind')]

other_countries = ['Brazil', 'Russia', 'South Korea', 'Canada']
other_sources_means = [mean_source('Brazil', 'other'), mean_source('Russia', 'other'), mean_source('South Korea', 'other'), mean_source('Canada', 'other')]


# Setting the plot speficications (number of subplots, background, etc.)
sns.set_theme(style='whitegrid')
sns.set_context("notebook", font_scale=1, rc={"lines.linewidth": 2.0})
fig, axs = plt.subplots(2, 2)

axs[0, 0].barh(hydro_countries, hydro_means)
axs[0, 0].set_title('Hydro')

axs[0, 1].barh(solar_countries, solar_means)
axs[0, 1].set_title('Solar')

axs[1, 0].barh(wind_countries, wind_means)
axs[1, 0].set_title('Wind')

axs[1, 1].barh(other_countries, other_sources_means)
axs[1, 1].set_title('Other')

# for ax in axs.flat: # So that the two subplots show the xlabel
#     ax.set(xlabel='Production in TWh')

# # plt.suptitle('Average production by source and country in the last decade (2010-2020)')
# # plt.subplots_adjust(wspace=0.35, hspace=0.5) # Space between subplots
# # plt.show()
