import pandas as pd
import numpy as np


def identify_data_types(df):
    numeric_columns = [col for col in df.columns if np.issubdtype(df[col].dtype, np.number)]
    object_columns = [col for col in df.columns if df[col].dtype == 'object']
    date_columns = [col for col in df.columns if df[col].dtype == 'datetime64[ns]']
    
    return numeric_columns, object_columns, date_columns
