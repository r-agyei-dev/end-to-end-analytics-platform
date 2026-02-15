# src/feature_engineering.py

import numpy as np
import pandas as pd

def add_financial_features(df: pd.DataFrame) -> pd.DataFrame:
    df['profit'] = df['revenue'] - df['budget']
    df['profit_ratio'] = df['revenue'] / df['budget']
    df['decade'] = (df['release_date'].dt.year // 10) * 10
    return df


def add_log_features(df: pd.DataFrame) -> pd.DataFrame:
    df['log_budget'] = np.log1p(df['budget'])
    df['log_revenue'] = np.log1p(df['revenue'])
    return df


def explode_genres(df: pd.DataFrame) -> pd.DataFrame:
    df_exploded = df.assign(
        genre=df['genre'].str.split(',')
    ).explode('genre')
    df_exploded['genre'] = df_exploded['genre'].str.strip()
    return df_exploded

