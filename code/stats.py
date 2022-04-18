import pandas
import scipy
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels
from statsmodels.formula.api import ols
import sklearn


data = pandas.read_excel('/home/steveb/Desktop/Universite/PSY4016/Projet/Data/cleandata.xlsx')

#ici, pour boir la distribution des vente mondiale, ce code s<affiche sur jupyter notebook
#on voit ici les donnees descriptives de mon dataset
#print(data.describe())

#On teste ici la normalite de ma variable d<interet
#print(stats.skew(data['Domestic Sales (in $)']), stats.kurtosis(data['Domestic Sales (in $)']))

# On voit que la distribution n<est pas normale dans ce dataset donc on va standardiser
def standardiser(column):
    scaler = sklearn.preprocessing.StandardScaler()
    x_one = column.to_numpy()
    x_one = x_one[:, np.newaxis]
    scaled_one = scaler.fit(x_one)
    transformed = scaler.transform(x_one)
    return transformed


#on vient ici tester l<hypothese 1
def analysis(df):
    new_df = pandas.DataFrame()
    new_df['Sales'] = df['Domestic Sales (in $)']
    new_df['Distributor'] = df['Distributor']
    model = ols("Sales ~ Distributor + 1", new_df).fit()
    regression = model.summary()
    return regression
