import pandas as pd
from geopy.geocoders import Nominatim

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


dfyear = process("election data/2014-Election.csv")
dfyear.to_csv("election data/2014-Election_test.csv")