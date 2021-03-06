import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import matplotlib
import sqlite3
import os
from matplotlib import pyplot as plt
from code.traitement import *
from code.stats import *
from sklearn import impute
path = os.getcwd()
system = ""
if "/" in path:
    system = "/"
if "\\" in path:
    system = "\\"
data = pd.read_excel(path + system + 'Data' + system + 'rawdata.xlsx')

etape = 1
afficheur = lambda x: str(x)
# outline(df)
# missing = missing_values_table(data)
# print(missing) #permet d<avoir une cllone montrant les variables manquantes

# On enleve les colonnes qui ne seront pas necessaires pour les analyses futures
# Elles sont choisies en fonction de nos hypoth'ses

data.drop('License', inplace=True, axis=1)
data.drop('Movie Runtime', inplace=True, axis=1)

# On va garder seulement les annees pour les dates de parution
mod = DATE()
data['Release Date'] = mod.year(data["Release Date"])

# On va aussi creer une colonne groupe qui sera utile pour l<apprentissage Machine
data['Group'] = mod.group(data['Release Date'])

#print(data['Release Date']

#on va ici regler le probleme de valeurs manquantes
cleandf = mvalues(data)
cleandf.to_excel(path + system + 'Data' + system + 'cleandata.xlsx', index=False)

# Le choix a ete fait de ne pas standardiser les donnes, pour faciliter la visualisation
# cleandf['Domestic Sales (in $)'] = standardiser(cleandf['Domestic Sales (in $)'])
# cleandf['International Sales (in $)'] = standardiser(cleandf['International Sales (in $)'])
# cleandf['World Sales (in $)'] = standardiser(cleandf['World Sales (in $)'])


regression = analysis(cleandf)
print(regression)




#on sauvegarde le r/sultat de l'analyse sous format csv
with open( path + system + 'Data' + system + 'analyses.csv', 'w') as fh:
    fh.write(regression.as_csv())


#Pour visualiser cette distribution des groupes
#
# with sns.axes_style('white'):
#     g = sns.catplot(data=cleandf, x='Distributor', y='Domestic Sales (in $)', aspect=4.0, kind='bar')
#     g.set_ylabels('Ventes domestiques')
# plt.show()
#
# sns.pairplot(cleandf, vars=['Distributor', 'Domestic Sales (in $)'], kind='reg')
# plt.show()



print('Vous ??tes rendus ?? ??tape: ' + afficheur(etape) + '\n Allez maintenant ?? ??tape: ' + afficheur(etape+1))
