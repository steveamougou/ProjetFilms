import seaborn as sns
import pandas as pd
import matplotlib
import sqlite3
from matplotlib import pyplot as plt

etape = 2
afficheur = lambda x: str(x)

conn = sqlite3.connect('movie_database')

sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM movieSales
                               ''', conn)
df = pd.DataFrame(sql_query, columns=['Distributor', 'DomesticSales', 'InternationalSales', 'WorldSales'])


with sns.axes_style('white'):
    g = sns.catplot(data=df, x='Distributor', y='DomesticSales', aspect=4.0, kind='bar')
    g.set_ylabels('Ventes domestiques')
plt.show()

#  Ces visualisations ne sont plus utiles, pourraient etre utiles pour l'hypothese 2
# # sns.pairplot(df, vars=['Distributor', 'DomesticSales'], kind='reg')
# # plt.show()
# # plt.clf()
# #
# # plt.plot(df['Distributor'], df['Domestic Sales (in $)'])
# # plt.show()
# # plt.clf()

# pd.plotting.scatter_matrix(df[['DomesticSales', 'InternationalSales', 'WorldSales']])
# plt.show()

print('Vous êtes rendus à étape: ' + afficheur(etape) + '\n Allez maintenant à étape: ' + afficheur(etape+1))
