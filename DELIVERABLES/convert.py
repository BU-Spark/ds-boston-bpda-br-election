import pandas as pd
# import pip
# pip.main(['install', 'geopy'])
from geopy.geocoders import Nominatim


# Because you need to access the network, please run it when the network is normal and it takes a long time to run
# I tested 2018-election. CSV and generated 2018-election_test.csv with country of origin


# returns dataframe of file
def process(path):
    df = pd.read_csv(path)
    # print(df['Municipality Code'])
    df['country'] = df['Municipality Code']
    df['country'] = df['country'].fillna(0)
    # count = 0
    for row in df.iterrows():
        row[1][10] = convert_city_to_country(row[1][4])
    return df


def convert_city_to_country(place):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(place)
    return location


df2018 = process("election data/2018-Election.csv")
df2018.to_csv("election data/2018-Election_test.csv")
