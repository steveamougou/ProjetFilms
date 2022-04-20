import sklearn
import pandas as pd
import numpy as np
import copy
import matplotlib
import seaborn as sns
import os
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import pipeline
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import naive_bayes
from sklearn import preprocessing
from code.traitement import *
from matplotlib import pyplot as plt

path = os.getcwd()
system = ""
if "/" in path:
    system = "/"
if "\\" in path:
    system = "\\"
etape = 5
afficheur = lambda x: str(x)

data = pd.read_excel(path + system + 'Data' + system + 'cleandata.xlsx')

#il est necessaire d'encoder ncertaines variables
data['Distributor'] = encoder(data['Distributor'])
data['Genre'] = encoder(data['Genre'])

#on definit les variables qui serviront a predire les ventes mondiales
x = copy.deepcopy(data[['Distributor', 'Genre', 'Domestic Sales (in $)', 'International Sales (in $)', 'World Sales (in $)']])


x.to_numpy()

#on definit donc la colonne qu'on essaye de predire, les ventes mondiales
#print(data.keys())
y= copy.deepcopy(data[['Group']])
y.to_numpy()



pca = sklearn.decomposition.PCA(n_components=2)
pca.fit(x)
print(pca.components_)
#print(pca.explained_variance_)

projected = pca.fit_transform(x)
#print(x.shape)
#print(projected.shape)


X_data= pd.DataFrame()
X_data['composante PCA 1'] = projected[:, 0]
X_data['composante PCA 2'] = projected[:, 1]
X_data['Vieillesse_film'] = y
sns.lmplot(x = "composante PCA 1", y ="composante PCA 2", hue='Vieillesse_film', data=X_data, fit_reg=False);
plt.show()

print('Vous êtes rendus à étape: ' + afficheur(etape) + '\n Le programme est terminé ' + '\n Veuillez consulter le plan et rapport dans le dossier documentation')
