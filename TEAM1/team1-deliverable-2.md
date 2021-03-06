# Team 1 - Deliverable 2 - Brazilian Immigrant Participation in Brazil-Held Election Results

## Checklist
- [x] Collect and pre-process a secondary batch of data
- [x] Refine the preliminary analysis of the data performed in PD1
- [x] Answer another key question
- [x] Refine project scope and list of limitations with data and potential risks of achieving project goal
- [x] Submit a PR with the above report and modifications to original proposal

---
## Questions Analyzed and Results


### How Have Voting Patterns Changed Over Time? 
(See [Voting Analysis](https://github.com/BU-Spark/ds-boston-bpda-br-election/blob/team1-deliverable-2/TEAM1/src/votingdata.ipynb) for more Detail)

#### Voting for Political Parties
First, we looked into which political parties parties the Brazilian Immigrant electorate voted for 

*Popularity of Political Parties - All years (1998-2018)*

![alt text](./readme_images/Full_Data_Voting/full_data_votes_by_party_all_years.png)

Above, we can see the number of votes for each party over the 6 election years in the dataset. Overall, the PSDB and PT have received the most votes in the last 6 elections, with the PSL coming in 3rd.

*Popularity of Political Parties - 2006-2018*

![alt text](./readme_images/Full_Data_Voting/alldata_parties_last4elections.png)

Now, if we narrow our focus to the last 4 elections, we can see that while the PSDB and PT were the top two parties in 2006-2014, the PSL emerged as the overwhelming top party in 2018

#### Analysis of Top 10 Countries
To drill deeper into how voting patterns have changed over time, we looked at the same top 10 countries by population (as of 2018) and analyzed how these countries voted for the years 2006-2018.

*2006 - Voting in Top 10 Countries*

![alt text](./readme_images/Top_10_Voting/top10_votes_2006.png)

Above, we plot the voting results for each country for the year 2006. We see a relatively uniform pattern among all countries, with the majority of votes going to the PDSB and PT. Interestingly, a the PT seemed to garner more votes in Portugal, Italy, and France than did the PSDB

*2010 - Voting in Top 10 Countries*

![alt text](./readme_images/Top_10_Voting/top10_votes_2010.png)

Above, we plot the voting results for each country for the year 2010. Again, we see a relatively uniform pattern among all countries, with the majority of votes going to the PDSB and PT. Again, a the PT seemed to garner more votes in Portugal, Italy, and France than did the PSDB and interestingly, the PV garnered a significant number of votes in the US.

*2014 - Voting in Top 10 Countries*

![alt text](./readme_images/Top_10_Voting/top10_votes_2014.png)

In 2014, we see the number of votes for the PT fall dramatically (relative to the PSDB). Meanwhile, votes for the PSB have grown significantly, with the votes for the PSB on par with the PT in the US and votes for the PT outnumbering those for the PT in Japan 

*2018 - Voting in Top 10 Countries*

![alt text](./readme_images/Top_10_Voting/top10_votes_2018.png)

In 2018, the PSL became the most-voted-for party across almost all countries. We also see some small spikes in votes for the new NOVO and PDT parties. Meanwhile, the PSDB has very few votes in all countries, while the PT continues to have some support on par with 2014 (much reduced from 2006 and 2010).


### How Has Educational Attainment Changed Over Time?
(See [Top 10 Analysis in the bottom of the location Analysis for more detail](https://github.com/BU-Spark/ds-boston-bpda-br-election/blob/team1-deliverable-2/TEAM1/src/electorate_location.ipynb) for more Detail)

#### Educational Attainment by Top 10 Countries
The majority of the countries we see an upward trend in the ratio of high school educated and incompletely high school educated voters beginning in 2006. There seems to be a downward trend the ratio of voters who have completed or have not completed college in beginning in 2006, which is likely just due to the ratio for high school education level ratios increasing. In 2010 we see a peak for voters with complete or incomplete elementary education, then a trend downards. We cannot interpret a trends for literate and illiterate voter ratios as their ratios are inconsequentially small.

#### Educational Attainment by Year
When looking at the general trends over all years, we see that the ratio of voters who have a completed college education has actually dropped, especially from 2006 to 2010. The numbers went up again from 2014 to 2018, but they did not return to pre 2006 levels. Likewise, the ratios of voters who have not finished high school or elementary school actaully increased from 2006 to 2010, before dropping a little from 2014 to 2018. The other educational attainments have remained relatively stable. Once again, we cannot interpret trends for literate and illiterate voters because the numbers are too insignificant.

#### Educational Attainment by Gender 

For most countries except for the United States and Canada, where the ratios increased, the ratios of college educated men and women both went down. Similar but opposite patterns appear for high school education, where the ratios of high school educated men and women both increased, except for in the US and Canada, where they decreased. For incomplete college education, the trend is universally downwards for men. For women, the trends are similar except for in the US where the numbers of incompletely college educated men increased. For incomplete high school education, the trends for both men and women are going up as a whole, but significant increases occured in the countries of Japan and Spain. Similarly, the exceptions to this were once again Canada and the US, where the numbers decreased slightly. 

---

## Refined Project Proposal

### Title: Brazilian Immigrant Participation in Brazil-Held Election Results

[Original Project Description](https://docs.google.com/document/d/10svI0F6vJOUjewvWAV4yx70k0brZGpG6pSurwHtmrUM/edit)

## Team Members
- Wiley Hunt (whunt1965)
- John Bestavros (Johannes2755)
- Jerry Zhang (jzhang12)
- Jenna Peters (jennapeters917)

## Meeting Times
*Bi-Weekly Client Meetings:* Fridays 9-10 AM

*Weekly PM Meetings:* Tuesdays 5:30-6 PM

## Project Description
This project seeks to understand the composition of the Brazilian immigrant electorate. By analyzing data on the electorate collected for all Brazilian Presidential elections from 1998???2018, we hope to understand changing patterns among Brazilian immigrants that vote in Brazilian elections. After analyzing the electorate, we hope to conduct additional analysis on Brazilian immigrant voting records to try and determine how community and demographic differences may influence voting patterns.

Pending the success of Brazilian data analysis, we may also look at similar patterns and trends for Haitan immigrants and Haiti-held elections as well as Dominican Republic immigrants and Dominican Republic-held elections.
 
Contextual Note: Immigrants living in the US (or outside their home country) can still vote in national elections.

## Data Sets
For this project, we will primarily focus on the Brazilian electorate dataset, which contains demographic data on Brazilian immigrant voters for the years 1998, 2002, 2006, 2010, 2014, and 2018. The second dataset is the election dataset and it contains voting records for Brazilian immigrant voters for the same years. Our team (team one) will primarily work with the electorate dataset, while team two will do their project primarily focusing on the election dataset. However, after analyzing the electorate, we do plan to examine the election dataset in order to explore how voting patterns may relate to the demographics trends that we have uncovered. 

## Plan for Data Set Cleaning
At this stage, the main cleaning task will be reconciling pre-2010 datasets with post-2010 datasets as there are missing, incomplete, or inconsistent values across the datasets:

- Prior to 2010, the municipality code (location of voter) feature only identified the country of the voter. However, after 2010, the codes were updated to identify the region within a country of the voter. In order to compare data from all years, we will need to develop a mapping function to reconcile the codes for the pre-2010 and post-2010 datasets. 
- From 2002 until 2010, there is an attribute ???educational attainment code??? numerically representing education level along with an ???educational description???. However in 2010 and 2018, this attribute is no longer available and we are left with just an education description. We will need to use past data and their numerical assignments to education description to map this attribute to 2010 and 2018 electorate datasets.
- A good portion of the datasets have some columns with completely missing data (ie. marital status description and code), ranging from a numerical representation to show the lack of data to the words ???no information???. We will need to standardize the absence of data across all sets and columns.
- For 2010 and 2018, there is a representation of age group for the electorate, which is just a string specifying cohort. The past datasets have a ???age group code??? which is -3 for all data entries, signifying it is unavailable information. We can repurpose this attribute, ???age group code??? to create a numeric code for age groups in 2010 and 2018, making it easier to analyze the data. 
- The Year attribute for data points needs to be converted into a Datetime object once we read in our data.

## Plan for Answering Strategic Questions
To begin, we will clean the electorate dataset. Then, we will look at how the composition of the electorate populations have changed over time as well as differences in electorate populations between countries. Looking at age, gender and education of the electorate across the dataset will help provide this insight. After analyzing the electorate, we will examine the Brazilian immigrant voting dataset in order to answer additional questions relating electorate (demographic) information with voting patterns.

## Key Questions to be Answered
- How are electorate populations different among Brazilian immigrants residing in different countries (eg, US vs Japan)?
- How have gender demographics within the electorate populations changed over time?
- How have education-level gender demographics within the electorate populations changed over time?
- How have voting trends changed as the demographics of the electorate (voters) have changed?
- How do communal factors???the environment of immigrant communities in different countries???impact voting patterns?
- How does the intersection of gender and education level impact voting patterns?

## Limitations
- Looking at the data set, it appears that new features (e.g. age, marital status, etc) have been added over time. Thus, the features present in each of the datasets may vary by year, which may make it difficult to analyze how these features have changed over time.
- There appears to be some variance in how "location" (or municipality) of voters is defined in the different datasets (for example, the 1998 dataset appears to only identify the countries in which voters live, but later datasets break down this data into major cities/regions within a country). Likely, we should be able to resolve these differences through some data cleaning, but it is worth noting.
- This is very minor, but some of the earlier datasets contain entries from countries which have since been renamed or split into multiple countries (eg, Yugoslavia). We will need to figure out how to deal with these entries as we analyze trends over time.
- Our client had mentioned that there would be some interest in analyzing what proportion of the populations vote in each country (when compared to the total immigrant population in the country). However, the datasets provided only cover 1 year in our dataset (2014). We may be able to use total population numbers for other years close to a desired year to to approximate the population. For example, we can use 2020 (which we do have) to approximate these proportions for our 2018 dataset.

## Deliverables
- Final presentation/report describing methodology and trends found surrounding electorate demographics and voting patterns. 
- Visualizations of these trends (and how they change over time)


