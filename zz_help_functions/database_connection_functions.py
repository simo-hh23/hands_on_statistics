#> define the correct folderpath

def set_folerpath():
    
    import getpass
    
    username = getpass.getuser()
    
    if username == 'simon':
        folderPath = 'C:/Users/simon/Desktop/github_projects/hands_on_statistics/'
    else:
        folderPath = '/Users/tugbasabanoglu/Desktop/hands_on_statistics/'
    
    return folderPath



#> oecd connector function

def get_from_oecd(sdmx_query):

    """
    function to extract data from the OECD API. Input --> indicator's code
    """
    
    import pandas as pd
    
    return pd.read_csv(
        f"https://stats.oecd.org/SDMX-JSON/data/{sdmx_query}?contentType=csv")




