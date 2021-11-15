# Brazilian Immigrant Participation in Brazil-Held Elections (TEAM 1) - Description of Data
For our project, we used three separate datasets:
* Demographic data on the Brazilian Electorate (for election years 1998, 2002, 2006, 2010, 2014, 2018)
* Voting data for the Brazilian Electorate (for Presidential Elections in the years 1998, 2002, 2006, 2010, 2014, 2018))
* Population Data (estimates of total Brazilian immigrants by country) for the years 2008, 2011, 2014, 2020

## Electorate Data
Our files containing electorate data are labeled "perfil_eleitorado_< year >.csv. The clean versions of the data are available in our [data/clean folder](./data/clean) and the original versions of the data are available in the [data/original folder](./data/original). A description of each of the features in the dataset is below:
* Election Year - The election year of the data (1998, 2002, etc.)
* Place (ZZ = Exterior) - The identification code for the source location of the data (all of our data has code ZZ, indicating these members of the electorate reside outside of Brazil)
* Municipality Code - the internal code for the location of the region where the immigrants are based.
* Municipality Name - the Portuguese name of the actual location (e.g.: Paraguai, Estados Unidos, Espanha, etc...)
* Gender Code - the internal code for the gender of the population within the municipality.
* Gender Description - the actual gender of the population.
* Marital Status Code - the internal code describing the marital status of the immigrants.
* Marital Starus Description - the name for the internal code for marital status.
* Age Group Code - the internal code for the age of the immigrants (only datasets from 2010 upwards have this feature).
* Age Group Description - the name for the internal code for the age of the immigrants.
* Educational Attainment Code - the internal code for the level of education that the immigrants have successfully reached.
* Educational Attainment Description - the name for the internal code of the level of education of the immigrants.
* Quantity of voters - the number of Brazilian immigrants that fit the specific descriptions from each of the previous data values.

## Election (Voting) Data
Our files containing voting data are labeled "< year >_Election_Data.csv. The clean versions of the data are available in our [data/clean folder](./data/clean) and the original versions of the data are available in the [data/original folder](./data/original). A description of each of the features in the dataset is below:
* Election Year - The election year of the data (1998, 2002, etc.)
* Election Round - The round of the election to which the votes correspond (Presidential Elections have 2 rounds)
* Place (ZZ = Exterior) - The identification code for the source location of the data (all of our data has code ZZ, indicating these votes come from members of the electorate reside outside of Brazil)
* Municipality Code - the internal code for the location of the region where the voters are based.
* Municipality Name - the Portuguese name of the actual location (e.g.: Paraguai, Estados Unidos, Espanha, etc...)
* Office - the position in Brazilian Government which is being voted on (since all Brazilian immigrants residing outside the country must vote in the Presidential election, the only value for this column is "presidente."
* Paty number - the internal value of the party that is being voted for.
* Party initials - the initials of the party that is being voted for.
* Party Name - the official name of the party.
* Number of votes - the number of Brazilian immigrants which voted for the given party.

## Population Data
Our files containing voting data are labeled "PopTotal_< year >.csv. The clean versions of the data are available in our [data/clean folder](./data/clean) and the original versions of the data are available in the [data/original folder](./data/original). A description of each of the features in the dataset is below:
* Pais/Country - The country to which the dataset entry refers (this feature is called "Pais" in the original data and "country" in the cleaned data)
* total  - The (estimated) total Brazilian immigrant population in the country
