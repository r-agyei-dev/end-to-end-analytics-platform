import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Loads dataset from CSV file.
    """
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans dataset by:
    - Converting release_date to datetime
    - Dropping missing financial values
    """
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df.dropna(subset=['budget', 'revenue', 'vote_average'])
    return df
