# Brazilian Immigrant Election Analysis

## Team Members
- Wiley Hunt (whunt1965)
- Chen Feng (cefeng9988)
- John Bestavros (Johannes2755)
- Jerry Zhang (jzhang12)
- Marco Raigoza (marco-raigoza)
- Jenna Peters (jennapeters917)

## Project Description
Project seeks to understand voting patterns of Brazilian immigrants in Brazil elections and the composition of the Brazilian immigrant electorate. We hope to understand changing patterns among Brazilian immigrants that vote in Brazilian elections and what communal or environmental factors may influence voting patterns.

Pending the success of Brazilian data analysis, look at similar patterns and trends for Haitan Immigrants and Haiti-held elections as well as Dominican Republic Immigrants and Dominican Republic-held elections.
 
Contextual Note: Immigrants living in the US (or outside their home country) can still vote in national elections.

## Data Sets
For our project, we have been given 2 main datasets, each with 6 separate files (excel worksheets). The first dataset contains demographic data on Brazilian immigrant voters for the years 1998, 2002, 2006, 2010, 2014, and 2018. The second dataset contains voting records for Brazilian immigrant voters for the same years.

## Plan for Data Set Cleaning
At this stage, the main cleaning task will be reconciling pre-2010 datasets with post-2010 datasets, specifically with regard to the municipality code (location of voter) feature. Prior to 2010, these codes only identified the country of the voter. However, after 2010, the codes were updated to identify the region within a country of the voter. In order to compare data from all years, we will need to develop a mapping function to reconcile the codes for the pre-2010 and post-2010 datasets. 

## Plan for Answering Strategic Questions
To begin, we will clean the datasets and examine each separately. For the voting records dataset, we will look at how voting patterns have changed over time as well as differences in voting patterns between countries. For the electorate dataset, we will look at how electorate populations have changed over time as well as differences in electorate populations between countries. After analyzing the datasets separately, we will combine the datasets in order to answer additional questions relating electorate (demographic) information with voting patterns. 

## Key Questions to be Answered
- How are voting patterns different among Brazilian immigrants residing in different countries (eg, US vs Japan)?
- How are electorate populations different among Brazilian immigrants residing in different countries (eg, US vs Japan)?
- How have voting patterns changed over time?
- How have electorate populations changed over time?
- How have voting trends changed as the demographics of the electorate (voters) have changed?
- What are some communal or environmental factors that influence voting patterns? Which factors appear to be the most impactful? 
- Which demographic groups have experienced the most significant change in voting pattern over the scope of our dataset?

## Limitations
- Looking at the data set, it appears that new features (e.g. age, marital status, etc) have been added over time. Thus, the features present in each of the datasets may vary by year, which may make it difficult to analyze how these features have changed over time.
- There appears to be some variance in how "location" (or municipality) of voters is defined in the different datasets (for example, the 1998 dataset appears to only identify the countries in which voters live, but later datasets break down this data into major cities/regions within a country). Likely, we should be able to resolve these differences through some data cleaning, but it is worth noting.
- This is very minor, but some of the earlier datasets contain entries from countries which have since been renamed or split into multiple countries (eg, Yugoslavia). We will need to figure out how to deal with these entries as we analyze trends over time.
- We have been advised by the client to avoid making causal inferences, i.e. inferences that aren’t ground in statistical analysis. 
- We have been advised by the client that there is limited interest in regression/predictive analyses (only looking at past trends)


## Deliverables
- Final presentation/report describing methodology and findings
- Visualizations of Data Analysis

---

# Repo Admin

# Add Users
To add yourself to the repository, open a Pull Request modifying `COLLABORATORS`, entering your GitHub username in a newline.

All Pull Requests must follow the Pull Request Template, with a title formatted like such `[Project Name]: <Descriptive Title>`
