import pandas as pd
import numpy as np
import sklearn
from sklearn import impute
from sklearn import preprocessing
import copy

def outline(a):
    print(a.head())
    print(a.describe(include='all'))
    print(a.corr())

def missing_values_table(df):
    mis_val = df.isnull().sum() # Total missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)  # Percentage of missing values
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1) # Make a table with the results
    mis_val_table_ren_columns = mis_val_table.rename(columns = {0 : 'Missing Values', 1 : '% of Total Values'}) # Rename the columns
    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:,1] != 0].sort_values('% of Total Values', ascending=False).round(1)
    # Print some summary information
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
        "There are " + str(mis_val_table_ren_columns.shape[0]) +
        " columns that have missing values.")
    # Return the dataframe with missing information
    return mis_val_table_ren_columns


#regarder pandas cours 2 comment changer de valeur de cell
class DATE:
    def __init__(self):
        i = 0

    def year(self, column):
        c = []
        for cell in column:
            if type(cell) == str:
                b = int(cell[-4] + cell[-3] + cell[-2] + cell[-1])
                c.append(b)
            else:
                c.append(None)  # on veut s<assurer que dans la colomne on considere encore les valeurs manquantes
        return c

    def group(self, column):
        group = []
        for cell in column:
            if cell <= 2010:
                group.append(0)
            else:
                group.append(1)
        return group



#Fonction qui permet d<isoler les colomnes avec des donnes manquantes, faire le traitement de donnees manquantes et de revenir avec un dataframe complet
def mvalues(df):
    miss_df = copy.deepcopy(df[['Domestic Sales (in $)', 'International Sales (in $)', 'World Sales (in $)', 'Release Date']])
    keys = miss_df.keys()
    df.drop(['Domestic Sales (in $)', 'International Sales (in $)',
       'World Sales (in $)', 'Release Date'], inplace=True, axis=1)
    imp = impute.SimpleImputer(missing_values=np.nan, strategy="mean")
    imp.fit(miss_df)
    miss_df_array = imp.transform(miss_df)
    miss_df_new = pd.DataFrame(miss_df_array, columns=keys)
    df_new = pd.concat([df, miss_df_new], axis=1)
    return df_new

def encoder(column):
    le = preprocessing.LabelEncoder()
    le.fit(column)
    b = le.transform(column)
    return b


def erreur(a, b):
    try:
        reponse = a / b

    except ZeroDivisionError:
        print('division par zero!')

    else:
        print('le résultat:', reponse)

    finally:
        print('execution finale')
