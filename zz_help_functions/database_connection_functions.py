import pandas as pd


def get_from_oecd(sdmx_query):
    return pd.read_csv(
        f"https://stats.oecd.org/SDMX-JSON/data/{sdmx_query}?contentType=csv"
    )




# data = get_from_oecd('EAG_TRANS_DURUNEMP?COUNTRY=AUS+USA&AGE=T')

# # test = 'https://stats.oecd.org/SDMX-JSON/data/OECD.EDU.IMEP/DSD_EAG_UOE_FIN@DF_UOE_FIN_NATURE_CUR_CAP?contentType=csv'

# https://stats.oecd.org/SDMX-JSON/data/EAG_TRANS_DURUNEMP?COUNTRY=AUS+USA&AGE=T?contentType=csv