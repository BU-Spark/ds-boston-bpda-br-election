import pandas as pd
from geopy.geocoders import Nominatim
from unidecode import unidecode

# return df and remove initial row
def process(path, del_init_row):
    df = pd.read_csv(path)

    if del_init_row:
        df = pd.read_csv(path, skiprows=[1])
        column_names = [col.lower().replace(' ', '_') for col in df.columns]
        df.columns = column_names
    else:
        df = pd.read_csv(path)
        column_names = [col.lower().replace(' ', '_') for col in df.columns]
        df.columns = column_names

    return df


# df of each dataset year
df1998 = process('election data/1998-Election.csv', del_init_row=True)
df2002 = process('election data/2002-Election.csv', del_init_row=True)
df2006 = process('election data/2006-Election.csv', del_init_row=True)
df2010 = process('election data/2010-Election.csv', del_init_row=True)
df2014 = process('election data/2014-Election.csv', del_init_row=True)
df2018 = process('election data/2018-Election.csv', del_init_row=True)

def process_df(path):
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


def preprocess_features(df_orig, name_code):
    df = df_orig.copy()

    if name_code:
        # Fill df with pre-2010 muni name and code
        for index in df.index:
            post_code = df.at[index, 'municipality_code']
            # extract pre-2010 muni name and code
            pre_code, muni_name = municipality_dict[post_code]
            # set extracted code and name into df
            df.at[index, 'municipality_code'] = pre_code
            df.at[index, 'municipality_name'] = muni_name

    # Preprocess Municipality Names
    countries = df['municipality_name'].tolist()
    countries = [unidecode(country) for country in countries]
    df['municipality_name'] = countries

    # Preprocess party names
    parties = df["party_name"]
    parties = [unidecode(party) for party in parties]
    df["party_name"] = parties

    return df


# Using GeoCoder to process municipality name
# dfyear = process("election data/2014-Election.csv")
# dfyear.to_csv("election data/2014-Election_test.csv")

# Preprocessing for consistency
# Mapping of municipality codes and names for pre- and post- 2010 data
# Key is from post-2010 data and Value is code and name for pre-2010 data
municipality_dict = {
    29483: (98086, "EGITO"),
    39187: (39187, "REPUBLICA DO CONGO"),
    29874: (29874, "REPUBLICA DEMOCRATICA DO CONGO"),
    99341: (99341, "MALAWI"),
    29394: (98027, "GUINE BISSAU"),
    29408: (11185, "COLOMBIA"),
    29416: (11266, "ESTADOS UNIDOS"),
    29424: (98663, "BARBADOS"),
    29432: (98922, "BELGICA"),
    29440: (98647, "ROMENIA"),
    29459: (29238, "HUNGRIA"),
    29467: (11142, "ARGENTINA"),
    29602: (11142, "ARGENTINA"),
    11142: (11142, "ARGENTINA"),
    11568: (11568, "URUGUAI"),
    98540: (98540, "CHINA"),
    29092: (29092, "ZIMBABWE"),
    11800: (11800, "BOLIVIA"),
    98361: (98361, "NIGERIA"),
    98043: (98043, "GANA"),
    29246: (29246, "HAITI"),
    98302: (98302, "PAQUISTAO"),
    11460: (11460, "PERU"),
    11762: (11762, "UCRANIA"),
    29092: (29092, "ZIMBABWE"),
    29661: (29033, "IRLANDA"),
    29670: (11444, "PARAGUAI"),
    29688: (98744, "SUECIA"),
    30961: (11509, "PORTUGAL"),
    29696: (11100, "ALEMANHA"),
    29700: (11525, "SUICA"),
    29718: (11304, "GUIANA"),
    98000: (98000, "GUATEMALA"),
    29742: (11380, "JAPAO"),
    29750: (2800, "VIETNA"),
    29769: (29092, "ZIMBABWE"),
    30902: (11266, "ESTADOS UNIDOS"),
    29777: (98868, "CUBA"),
    29785: (98426, "FINLANDIA"),
    29793: (29025, "HONG KONG"),
    29807: (11266, "ESTADOS UNIDOS"),
    29815: (29220, "REPUBLICA DOS CAMAROES"),
    29823: (11460, "PERU"),
    29831: (98302, "PAQUISTAO"),
    39306: (98108, "TURQUIA"),
    29840: (29211, "INDONESIA"),
    29858: (11762, "UCRANIA"),
    99430: (29190, "JAMAICA"),
    29882: (29157, "KUWAIT"),
    29890: (29130, "MALASIA"),
    29904: (11800, "BOLIVIA"),
    29912: (98361, "NIGERIA"),
    99422: (11304, "GUIANA"),
    29939: (98060, "GABAO"),
    29947: (11460, "PERU"),
    29955: (11509, "PORTUGAL"),
    29963: (98167, "TOGO"),
    29971: (98841, "INGLATERRA"),
    29980: (11266, "ESTADOS UNIDOS"),
    29998: (98965, "ANGOLA"),
    30104: (11428, "MEXICO"),
    30066: (11240, "ESPANHA"),
    30074: (98838, "NICARAGUA"),
    30082: (98442, "FILIPINAS"),
    30090: (29116, "MOCAMBIQUE"),
    39004: (11142, "ARGENTINA"),
    30112: (11266, "ESTADOS UNIDOS"),
    30120: (11363, "ITALIA"),
    30147: (11568, "URUGUAI"),
    30155: (98906, "CANADA"),
    30163: (98760, "RUSSIA"),
    30171: (98825, "INDIA"),
    30180: (11100, "ALEMANHA"),
    30198: (11380, "JAPAO"),
    30201: (29165, "KENIA"),
    30210: (98825, "INDIA"),
    30228: (11266, "ESTADOS UNIDOS"),
    30244: (98345, "NORUEGA"),
    30252: (98906, "CANADA"),
    30260: (98329, "PANAMA"),
    30279: (11541, "SURINAME"),
    30287: (11282, "FRANCA"),
    30295: (11142, "ARGENTINA"),
    30309: (11444, "PARAGUAI"),
    30317: (98540, "CHINA"),
    30325: (98140, "TRINIDAD TOBAGO"),
    30341: (11509, "PORTUGAL"),
    30333: (29246, "HAITI"),
    30368: (98604, "CABO VERDE"),
    30376: (98787, "AFRICA DO SUL"),
    99155: (11142, "ARGENTINA"),
    99236: (11800, "BOLIVIA"),
    39160: (39160, "ESLOVENIA"),
    99287: (99287, "ZAMBIA"),
    39102: (39102, "OMA"),
    99180: (99180, "COMUNIDADE DAS BAHAMAS"),
    39322: (39322, "CHIPRE"),
    30350: (30350, "REPUBLICA CHECA"),
    30414: (30414, "PALESTINA"),
    39225: (39225, "SAO TOME E PRINCIPE"),
    30988: (30988, "BOSNIA E HERZEGOVINA"),
    99317: (99317, "ESTONIA"),
    99104: (99104, "GEORGIA"),
    39284: (39284, "BURQUINA FASSO"),
    99376: (99376, "MYANMAR"),
    39020: (39020, "CROACIA"),
    38881: (38881, "BELIZE"),
    39263: (39263, "GUINE EQUATORIAL"),
    99350: (99350, "MALI"),
    29491: (98981, "AUSTRALIA"),
    30651: (98540, "CHINA"),
    30481: (11169, "CHILE"),
    30538: (11207, "COREIA"),
    29548: (98523, "CINGAPURA"),
    30473: (11800, "BOLIVIA"),
    30562: (98981, "AUSTRALIA"),
    30627: (11380, "JAPAO"),
    30570: (2828, "TAIWAN"),
    30597: (29203, "IRA"),
    30600: (29076, "HONDURAS"),
    30619: (11347, "ISRAEL"),
    30635: (98906, "CANADA"),
    30686: (29149, "LIBIA"),
    30708: (98124, "TUNISIA"),
    39063: (98906, "CANADA"),
    30740: (11487, "POLONIA"),
    30767: (98949, "AUSTRIA"),
    30783: (11266, "ESTADOS UNIDOS"),
    30805: (29050, "NOVA ZELANDIA"),
    30821: (29068, "NAMIBIA"),
    30848: (98540, "CHINA"),
    30864: (11525, "SUICA"),
    30139: (11380, "JAPAO"),
    30554: (11380, "JAPAO"),
    30589: (11380, "JAPAO"),
    30643: (11380, "JAPAO"),
    30724: (11380, "JAPAO"),
    30236: (11380, "JAPAO"),
    29726: (98000, "GUATEMALA"),
    29866: (29190, "JAMAICA"),
    30880: (98540, "CHINA"),
    30384: (11800, "BOLIVIA"),
    29378: (29378, "SERVIA"),
    99406: (99406, "SERRA LEOA"),
    39241: (39241, "CAZAQUISTAO"),
    30669: (30669, "BOTSWANA"),
    39209: (39209, "ESLOVAKIA"),
    30929: (30929, "SRI LANKA"),
    38903: (38903, "GUINE"),
    38920: (38920, "BENIM"),
    38962: (38962, "TANZANIA"),
    29653: (29653, "CATAR"),
    29254: (98582, "COSTA DO MARFIM"),
    29262: (98728, "EMIRADOS ARABES"),
    29270: (98043, "GANA"),
    29289: (29181, "JORDANIA"),
    29297: (98108, "TURQUIA"),
    29300: (98701, "ARGELIA"),
    29319: (11568, "URUGUAI"),
    29327: (11444, "PARAGUAI"),
    29505: (11584, "VENEZUELA"),
    29513: (11266, "ESTADOS UNIDOS"),
    29521: (11568, "URUGUAI"),
    29530: (98787, "AFRICA DO SUL"),
    29556: (11444, "PARAGUAI"),
    29564: (11584, "VENEZUELA"),
    29572: (11800, "BOLIVIA"),
    29580: (11444, "PARAGUAI"),
    29599: (98485, "DINAMARCA"),
    29610: (98248, "SENEGAL"),
    29637: (98221, "SIRIA"),
    29360: (11401, "LIBANO"),
    29386: (11100, "ALEMANHA"),
    30392: (11223, "EQUADOR"),
    30406: (29122, "MARROCOS"),
    30422: (11126, "ARABIA SAUDITA"),
    30430: (11568, "URUGUAI"),
    30449: (11363, "ITALIA"),
    30457: (29009, "PAISES BAIXOS"),
    30490: (98280, "REPUBLICA DOMINICANA"),
    30503: (11266, "ESTADOS UNIDOS"),
    30511: (98507, "COSTA RICA"),
    30520: (98469, "EL SALVADOR"),
    30546: (98620, "BULGARIA"),
    29475: (11320, "GUIANA FRANCESA"),
    29645: (29645, "TIMOR-LESTE"),
    38989: (38989, "ARMENIA"),
    29173: (0, "NEPAL"),
    30465: (11444, "PARAGUAI"),
    29335: (11827, "GRECIA"),
    39080: (11266, "ESTADOS UNIDOS"),
    29343: (98205, "TAILANDIA"),
    29351: (11240, "ESPANHA"),
}

# Call helper functions here to preprocess df and write to csv files
preprocess_features(df1998,name_code=False).to_csv('./election data/1998_Election_processed.csv')
preprocess_features(df2002,name_code=False).to_csv('./election data/2002_Election_processed.csv')
preprocess_features(df2006,name_code=False).to_csv('./election data/2006_Election_processed.csv')
preprocess_features(df2010,name_code=False).to_csv('./election data/2010_Election_processed.csv')
preprocess_features(df2014,name_code=False).to_csv('./election data/2014_Election_processed.csv')
preprocess_features(df2018,name_code=False).to_csv('./election data/2018_Election_processed.csv')