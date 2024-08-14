import pandas as pd
import numpy as np

def convert_dates_to_mm_yyyy(df, date_columns):
    df[date_columns] = df[date_columns].apply(lambda x: x.dt.strftime('%m/%Y'))
    return df

def age_to_bands(df, age_columns):
    for col in age_columns:
        df[col] = pd.cut(df[col], bins=range(0, 101, 5), right=False, labels=[f'{i}-{i+4}' for i in range(0, 100, 5)])
    return df

def merge_categories(df, column, categories):
    df[column] = df[column].apply(lambda x: x if x in categories else 'Others')
    return df

def transform_categorical_fields(df, object_columns, categories_to_keep):
    for column, categories in categories_to_keep.items():
        df = merge_categories(df, column, categories)
    return df

def map_unique_values_to_categories(df, object_columns):
    for col in object_columns:
        unique_values = df[col].unique()
        category_map = {val: f'{col} {i+1}' for i, val in enumerate(unique_values)}
        df[col] = df[col].map(category_map)
    return df

def drop_unique_columns(df):
    unique_columns = df.columns[df.nunique() == len(df)]
    df = df.drop(columns=unique_columns)
    return df
