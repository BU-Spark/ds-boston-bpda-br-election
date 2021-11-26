# Brazilian Election Analysis: Code Description (Team 1)
This document provides an overview of our code base used for our project. For ease of understanding, we have broken these descriptions into two broad categories (Data Cleaning and Analysis), describe the purpose of each of our files within each category, and provide instructions on running the files (where applicable).

## Data Cleaning
The below files are used for data cleaning and pre-processing. 

### 1. CSV_clean.ipynb
#### File Description
The primary cleaning "application" is the [CSV_clean.ipynb](./src/CSV_clean.ipynb) file which handles importing all CSV files for the dataset (from the [data/original folder](./data/original)), and applying various cleaning functions to standardize the data so that it can be used in our analysis notebooks. After each dataset is cleaned, it is written to a new CSV file in the [data/clean folder](./data/clean).

This notebook calls several helper functions and data objects which are defined in the files within the [data_cleaning folder](./src/data_cleaning) and are described in greater detail below.

#### Instructions for Use
To run this file, you must first download the datasets (see the data in the [data/original folder](./data/original)) and open it as a Jupyter Notebook. Then, simply click "run all" to apply the cleaning functions to the original data and write the new files into new CSV's.

### 2. data_cleaning/cleaning_utilities.py
#### File Description
[This file](./src/data_cleaning/cleaning_utilities.py) contains a single function (remove_accents) which removes accents from a Python string. The primary purpose of this function is to standardize string related to country and education-attainment names by removing any Portuguese-language accents (which are used in some data sets and not used in others)

#### Instructions for Use
To utilize the functions in this file, it must be imported as follows:

```
from data_cleaning import cleaning_utilities
```

See [CSV_clean.ipynb](./src/CSV_clean.ipynb) for example usage.

In addition, the remove accents function requires the **unidecode** library, which should be installed (via pip) as follows:

```
pip install unidecode
```

### 3. data_cleaning/country_match.py
#### File Description
[This file](./src/data_cleaning/country_match.py) contains a Python dictionary object (country_code_map) which maps post-2010 municipality codes to pre-2010 country codes/names. Within the dictionary, the key is code for municipality in post-2010 data and the value is a 2-tuple containing (< code for country in pre-2010 data >, < Name of Country in pre-2010 data >). This file is needed to match pre-2010 data (where municipalities were identified by country) to post-2010 data (where municipalities correspond to the city name where a Brazilian consulate is located)

#### Instructions for Use
To utilize the functions in this file, it must be imported as follows:

```
from data_cleaning.country_match import country_code_map
```

Then the country_code_map object can simply be used as a normal Python dictionary. See [CSV_clean.ipynb](./src/CSV_clean.ipynb) for example usage.

### 4. data_cleaning/education_codes.py
#### File Description
[This file](./src/data_cleaning/education_codes.py) contains the following functions to perform data-cleaning tasks specific to the education features in the Electorate Dataset
* **read_data_post2006(filename)**
    - This function is used to drop the extraneous row in post-2006 datasets (which includes the column headers in Portuguese). 
    - Note: this function was created, but was ultimately not used in the data cleaning (replaced by our extract_dataframe function)
* **read_data_pre2010(filename)**
    - This function is used to read in pre-2010 datasets, drop the extraneous Portguese column names, and convert the "Educational Attainment Code" feature to an integer type.
    - Note: this function was created, but was ultimately not used in the data cleaning
* **clean2018(df)** 
    - This function standardizes the 'educational_attainment_descriptions' for the 2018 electorate dataset by removing errors in the descriptions created by improper conversions of Portuguese accents.
* **add_education_codes(data_2002, data)**
    - This function adds educational attainment codes to the 2002 electorate dataset.

#### Instructions for Use
To utilize the functions in this file, it must be imported as follows:

```
from data_cleaning.education_codes import add_education_codes, clean2018
```

See [CSV_clean.ipynb](./src/CSV_clean.ipynb) for example usage.

### 5. data_cleaning/standardize_age.py
#### File Description
[This file](./src/data_cleaning/standardize_age.py) contains a single function which is used to standardize  post 2010 (2014 and 2018) age descriptions to match age descriptions in the 2010 dataset (prior to 2010, age codes werenot provided)

#### Instructions for Use
To utilize the functions in this file, it must be imported as follows:

```
from data_cleaning.standardize_age import standardize_age_desc
```

See [CSV_clean.ipynb](./src/CSV_clean.ipynb) for example usage.

---

## Data Analysis
The below files are used for performing analysis on the datasets.


### 1. electorate_location.ipynb
#### File Description
[This file](./src/electorate_location.ipynb) contains the code and analysis used to examine country-level population size, growth, and gender ratios in the aggregate dataset as well as demographic trends in the "top-10 countries" (the 10 countries with the highest Brazilian immigrant populations in 2018).The first part of this notebook analyzes trends related to the location of the Brazilian electorate Population, looking into how the location of immigrant Brazilian voters has changed over time (as well as how some demographic trends have changed at a country level).The second part of the notebook contains analsysis of demographic features focusing only on the top-10 countries.

Below, we describe the funtions in this notebook:
##### Aggregate Analysis (note: some of these functions are also used in the Top 10 analysis)
* **combine_data(*dfs)** 
    - This function combined all Electorate Datasets into a single Pandas dataframe
* **plot_total_voters(df)** 
    - This function plots the Total Brazilian Immigrant Electorate size by Year
* **plot_total_countries(df)** 
    - This function plots the Number of Countries in which the Electorate Resides by Year
* **calculate_country_pop(df)** 
    - This function calculates the total population for each country (by year) over the 6 datasets and returns a pandas "groupby" object
* **calculate_country_growth(df, ignore_init=False)** 
    - This function calculates the country population growth rate over the 6 datasets and returns a pandas "groupby" object
* **calculate_country_gender_pop(df)** 
    - This function calculates the country population by gender over the 6 datasets and returns a pandas "groupby" object
* **calculate_gender_ratio(df_orig)** 
    - This function calculates the the % males and % females for each country over the 6 datasets and returns a pandas dataframe

##### Top 10 Analysis
* **get_top_N(total_data, sorted_countries, N:int)** 
    - This function extracts the top N countries from a sorted list by getting the top N country names from the a sorted list of countries by population in 2018 and then filtering the aggregate dataset to only include those countries. It returns a new Pandas dataframe with only these top 10 countries.
* **plot_top_10_populations(df_top10, df_combined)** 
    - This function plots the populations of the top 10 countries across all years (plus the average population of the dataset) by year
* **plot_top_10_populations_growth(df_top10, df_combined)** 
    - This function plots the voter population growth rates of the top 10 countries across all years (plus the average population growth in the entire dataset) by year
* **plot_gender_ratio_by_country(df, df_combined)** 
    - This function plots the gender ratios for the top 10 countries (as well as average ratios from the aggregate dataset) by year
* **plot_education_by_country(df, df_combined, education_level, gender = None)** 
    - This function plots the ratio for each educational_attainment level for the top 10 countries (as well as the overall dataset average)
* **plot_education_ratios(df)** 
    - This function plots the ratio (as % of total electorate in top 10) for educational attainment description for all top_10 countries combined across all years
* **plot_age_by_country(df, df_combined, age, gender = None)** 
    - This function plots the ratio of age groups for the top 10 countries (as well as the overall dataset average)
* **plot_age_ratios(df)** 
    - This function plots the ratios for each age group in the top 10 countries by year

#### Instructions for Use
To run this file, you must first run the cleaning functions in [CSV_clean.ipynb](./src/CSV_clean.ipynb) to produce the cleaned datasets. Then, open this file as a Jupyter Notebook and simply click "run all" to run the entire notebook (or you can run each cell sequentially).



### 2. electorate_gender.ipynb
#### File Description
[This file](./src/electorate_gender.ipynb) contains the code and analysis used to examine gender and educational features on the aggregate dataset (all countries, all years). This notebook contains the following functions:
* **combine_data(*dfs)** 
    - This function combined all Electorate Datasets into a single Pandas dataframe
* **plot_genders(df)**
    - This function plots the Total Brazilian Immigrant Gender Distribution by Year (for all years in the dataset)
* **df_education(df)**
    - This function extracts the total number of members of the electorate corresponding to each educational attainment description (level of education achieved) for the years 2002-2018 and returns a new dataframe with these values (used by the plotting functions below)
* **plot_education(df)**
    - Plots the total number of individuals corresponding to each educational attainment description for the years 2002-2018
* **plot_education_women(df)**
    - Plots the total number of women corresponding to each educational attainment description for the years 2002-2018
* **plot_education_men(df)**
    - Plots the total number of men corresponding to each educational attainment description for the years 2002-2018
* **plot_education_by_country(df)**
    - Plots the proportion of the electorate corresponding to each educational attainment description across the 2002-2018 electorate datasets

#### Instructions for Use
To run this file, you must first run the cleaning functions in [CSV_clean.ipynb](./src/CSV_clean.ipynb) to produce the cleaned datasets. Then, open this file as a Jupyter Notebook and simply click "run all" to run the entire notebook (or you can run each cell sequentially).



### 3. votingdata.ipynb
#### File Description
[This file](./src/votingdata.ipynb) contains the code and analysis used to examine voting patterns among the electorate as a whole as well as within the top 10 countries. The functions within this file are described below:

##### Aggregate Analysis (note: some of these functions are also used in the Top 10 analysis)
* **combine_data(*dfs)** 
    - This function combined all Election (voting) Datasets into a single Pandas dataframe
* **plot_total_voters(df)** 
    - This function plots the total number of votes cast by Brazilian immigrants by year
* **plot_total_countries(df)** 
    - This function plots the total number of countries from which votes were cast by year
* **calculate_country_pop(df)** 
    - This function calculates the number of voters within each country (by year) over the 6 datasets and returns a pandas "groupby" object"
* **votes_by_party(df)** 
    - This function calculates the total number of votes for each party by year and returns a pandas "groupby" object

##### Top 10 Analysis
* **get_electorate_data()** 
    - This function retrieves and combines electorate dataset (to get data on top 10 countries)
* **get_top_N(total_data, N:int)** 
    - This function extracts the top N countries (in terms of overall population) by  countries and returns a new Pandas Dataframe with the voting data for only these top N countries
* **plot_top_10_voting_patterns(df_combined, top_10, years)** 
    - This function plots the voting patterns (by party) of the top 10 countries for the given years as a single plot
* **plot_top_10_voting_proportions_consulates(top_10, years, elect_round)** 
    - This function plots the estimated proportion of voters for the top 10 countries for a given election round using estimations based on population estimates provided by Brazilian consulates
* **plot_top_10_voting_proportions_electorate(df_combined, top_10, elect_round)** 
    - This function plots the estimated proportion of voters for the top 10 countries for a given election round using estimations based on electorate size (from the electorate dataset)

#### Instructions for Use
To run this file, you must first run the cleaning functions in [CSV_clean.ipynb](./src/CSV_clean.ipynb) to produce the cleaned datasets. Then, open this file as a Jupyter Notebook and simply click "run all" to run the entire notebook (or you can run each cell sequentially).



### 4. top_10_analysis.ipynb
#### File Description
[This file](./src/top_10_analysis.ipynb) combines all code and analysis related to the top 10 countries from the [electorate_location](./src/electorate_location.ipynb) and [votingdata](./src/votingdata.ipynb) notebooks. This file is provided as simple way to analyze only the top 10 countries (versus the additional analysis provided on the aggregate electorate provided in the other files). All functions in this file are described in the sections on the electorate_location and votingdata notebooks above.

#### Instructions for Use
To run this file, you must first run the cleaning functions in [CSV_clean.ipynb](./src/CSV_clean.ipynb) to produce the cleaned datasets. Then, open this file as a Jupyter Notebook and simply click "run all" to run the entire notebook (or you can run each cell sequentially).
