## Team 2: Final Deliverable - Brazilian Immigrant Participation in Brazil-Held Election Results

---
## Document Links
* Final Report: [Document](https://docs.google.com/document/d/1UlbZXTUHx7HcR5ONZXqrkxYcVryihC_Knry517Y_Ylo/edit?usp=sharing)
* Final Presentation: [Slides](https://docs.google.com/presentation/d/1xA7zLP8ly3901dhuaoxi88QKLmJ5Tvf9XrSBtBj6y24/edit?usp=sharing)
* Technical README is in DELIVERABLES folder
---

## Project Proposal

### Title: Brazilian Immigrant Participation in Brazil-Held Election Results

## Team Members
- Chen Feng (cefeng9988)
- Marco Raigoza (marco-raigoza)
- Wangkai Zhu (wzhu8410)
- Jiaru Li (Jiaru-Li)

## Project Description
This project seeks to understand voting patterns of Brazilian immigrants in Brazil elections and the composition of the Brazilian immigrant electorate. By analyzing the election and electorate data, we hope to understand changing patterns among Brazilian immigrants that vote in Brazilian elections by analyzing how community and demographic differences influence voting patterns.

Pending the success of Brazilian data analysis, look at similar patterns and trends for Haitan Immigrants and Haiti-held elections as well as Dominican Republic Immigrants and Dominican Republic-held elections.

Contextual Note: Immigrants living in the US (or outside their home country) can still vote in national elections.

## Data Sets
For our project, we have been given 2 main datasets, each with 6 separate files (excel worksheets). The first dataset contains demographic data on Brazilian immigrant voters for the years 1998, 2002, 2006, 2010, 2014, and 2018. The second dataset contains voting records for Brazilian immigrant voters for the same years.
Our team (Team 2) is working with the election data to extract voting trends over the span of the two decades (1998-2018).

## Plan for Data Set Cleaning
At this stage, the main cleaning task will be reconciling pre-2010 datasets with post-2010 datasets as there are missing, incomplete, or inconsistent values across the datasets:

- Prior to 2010, the municipality code (location of voter) feature only identified the country of the voter. However, after 2010, the codes were updated to identify the region within a country of the voter. In order to compare data from all years, we will need to develop a mapping function to reconcile the codes for the pre-2010 and post-2010 datasets.

## Plan for Answering Strategic Questions
To begin, we will clean the datasets and examine each separately. For the voting records dataset, we will look at how voting patterns — popularity of political parties and voter turnout — have changed over time as well as differences in voting patterns between countries the electorate votes from. 

## Key Questions to be Answered
Overarching Question: How have voting patterns changed over time
- Key Question 1: What are some social-political activities that have influenced voting patterns? Which factors appear to be the most impactful?
- Key Question 2: How are voting patterns different among Brazilian immigrants residing in different countries (eg, US vs Japan)?
- Key Question 3: How have voting turnout changed over time across different political parties?
- Key Question 4: What are the top political parties from the top voting countries?

## Limitations
- There appears to be some variance in how "location" (or municipality) of voters is defined in the different datasets (for example, the 1998 dataset appears to only identify the countries in which voters live, but later datasets break down this data into major cities/regions within a country). Likely, we should be able to resolve these differences through some data cleaning, but it is worth noting.
- This is very minor, but some of the earlier datasets contain entries from countries which have since been renamed or split into multiple countries (eg, Yugoslavia). We will need to figure out how to deal with these entries as we analyze trends over time.
- We have been advised by the client to avoid making causal inferences, i.e. inferences that aren’t ground in statistical analysis.
- We have been advised by the client that there is limited interest in regression/predictive analyses (only looking at past trends)



## Deliverables
- Final presentation/report describing methodology, trends found in trends in voting patterns.
- Visualizations of trends over time


---

# Repo Admin

# Add Users
To add yourself to the repository, open a Pull Request modifying `COLLABORATORS`, entering your GitHub username in a newline.

All Pull Requests must follow the Pull Request Template, with a title formatted like such `[Project Name]: <Descriptive Title>`
