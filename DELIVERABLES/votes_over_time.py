import pandas as pd
# returns dataframe of file
from IPython.core.display import display


def process(path):
    df = pd.read_csv(path)
    return df
# return array same size as parties of sum of their votes
def sumVotes(parties, df):
    votes = {}
    for party in parties:
        df = df[1:]
        sum = df[df['party_name']==party]["number_of_votes"].astype({"number_of_votes":'int32'}).sum()
        votes[party] = sum
    return votes
# df of each dataset year
df1998 = process('election data/1998_Election_processed.csv')
df2002 = process('election data/2002_Election_processed.csv')
df2006 = process('election data/2006_Election_processed.csv')
df2010 = process('election data/2010_Election_processed.csv')
df2014 = process('election data/2014_Election_processed.csv')
df2018 = process('election data/2018_Election_processed.csv')
# unique ndarray of party name from each dataset year
parties1998 = df1998['party_name'].unique()[1:]
parties2002 = df2002['party_name'].unique()[1:]
parties2006 = df2006['party_name'].unique()[1:]
parties2010 = df2010['party_name'].unique()[1:]
parties2014 = df2014['party_name'].unique()[1:]
parties2018 = df2018['party_name'].unique()[1:]
# Sum votes of each year in dict type
votes1998 = sumVotes(parties1998, df1998)
votes2002 = sumVotes(parties2002, df2002)
votes2006 = sumVotes(parties2006, df2006)
votes2010 = sumVotes(parties2010, df2010)
votes2014 = sumVotes(parties2014, df2014)
votes2018 = sumVotes(parties2018, df2018)

# df of party as columns and year as rows
votes_df = pd.DataFrame([votes1998, votes2002, votes2006, votes2010, votes2014, votes2018], index=[1998, 2002, 2006, 2010, 2014, 2018])
# df to csv file
votes_df.to_csv("election data/sum_party_votes.csv")
display(votes_df)