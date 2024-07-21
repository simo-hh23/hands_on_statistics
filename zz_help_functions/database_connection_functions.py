#> oecd connector function

def get_from_oecd(sdmx_query):

    """
    function to extract data from the OECD API. Input --> indicator's code
    """
    
    import pandas as pd
    
    return pd.read_csv(
        f"https://stats.oecd.org/SDMX-JSON/data/{sdmx_query}?contentType=csv")



def get_from_oecd_v2(dataset_location, dataset_tag, datasets_filters, start_period):

    """
    function to extract data from the OECD API. Input --> indicator's location, tag, filters, start period
    """
    
    import pandas as pd
    import requests
    from io import StringIO

    extr = requests.get('https://sdmx.oecd.org/public/rest/data/' +
                        dataset_location + '@' +
                        dataset_tag + '/' +
                        datasets_filters + '?' +
                        'startPeriod=' + start_period +
                        '&format=csv')
    
    extr_text = StringIO(extr.text)
    
    extr_df = pd.read_csv(extr_text,
                             sep = ',',
                             header = 0)

    return extr_df
