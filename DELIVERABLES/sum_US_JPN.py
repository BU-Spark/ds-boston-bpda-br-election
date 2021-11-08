import pandas as pd
# returns dataframe of file
from IPython.core.display import display


def process(path):
    df = pd.read_csv(path)
    return df


# return array same size as parties of sum of their votes
def sumVotes(countries, df, type):
    votesUSA = 0
    votesJPN = 0

    # For specific years, extract the countries by different municipality names
    if type == '1998' or type == '2002' or type == '2006':
        for country in countries:
            votes = df[df['Municipality Name'] == country]["Number of Votes"].astype({"Number of Votes": 'int32'}).sum()
            if country == "ESTADOS UNIDOS":
                votesUSA = votes
            else:
                votesJPN = votes

    elif type == '2010':
        for country in countries:

            votes = df[df['Municipality Name'].str.contains(country, case=False)]["Number of Votes"].astype({"Number of Votes": 'int32'}).sum()
            if country == "EUA":
                votesUSA = votes
            else:
                votesJPN = votes

    elif type == '2018' or type == '2014':
        for country in countries:
            votes = df[df['country'].str.contains(country, case=False, na=False)]["Number of Votes"].astype({"Number of Votes": 'int32'}).sum()
            if country == "United States":
                votesUSA = votes
            else:
                votesJPN = votes

    return votesUSA, votesJPN


# Reading in CSV to df
df1998 = process('election data/1998-Election.csv')
df2002 = process('election data/2002-Election.csv')
df2006 = process('election data/2006-Election.csv')
df2010 = process('election data/2010-Election.csv')
df2014 = process('election data/2014-Election_test.csv')
df2018 = process('election data/2018-Election_test.csv')

# total votes of each dataset year for USA and JPN -> [USA, JPN]
votes1998 = sumVotes(["ESTADOS UNIDOS", "JAPAO"], df1998, '1998')
votes2002 = sumVotes(["ESTADOS UNIDOS", "JAPAO"], df2002, '2002')
votes2006 = sumVotes(["ESTADOS UNIDOS", "JAPÃO"], df2006, '2006')
votes2010 = sumVotes(["EUA", "JAPA"], df2010, '2010')
votes2014 = sumVotes(["United States", "日本"], df2014, '2014')
votes2018 = sumVotes(["United States", "日本"], df2018, '2018')

# df of party as columns and year as rows
votes_df = pd.DataFrame([votes1998, votes2002, votes2006, votes2010, votes2014, votes2018],
                        index=[1998, 2002, 2006, 2010, 2014, 2018], columns=["USA", "JPN"])
# df to csv file
votes_df.to_csv("election data/sum_votes_US_JPN.csv")
display(votes_df)
