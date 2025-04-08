from scipy import stats
import numpy as np
from scipy.stats import mstats
import pandas as pd


###### Manejo de Outliers ######

#Eliminación
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return filtered_df


#Winsorización
def winsorize_outliers(s, limits=(0.01, 0.01)):  # Limita el 1% inferior y superior
    winsorized_s = mstats.winsorize(s, limits=limits)
    return pd.Series(winsorized_s, index=s.index)

