import sklearn
import pandas as pd
import numpy as np
import copy
import matplotlib
from sklearn import model_selection
from sklearn import pipeline
from sklearn import decomposition
from sklearn import naive_bayes
from sklearn import preprocessing
from code.traitement import *
from matplotlib import pyplot as plt

data = pd.read_excel('/home/steveb/Desktop/Universite/PSY4016/Projet/Data/cleandata.xlsx')

#il est necessaire d'encoder ncertaines variables
data['Distributor'] = encoder(data['Distributor'])
data['Genre'] = encoder(data['Genre'])

#on definit les variables qui serviront a predire les ventes mondiales
x = copy.deepcopy(data[['Distributor', 'Genre', 'Domestic Sales (in $)', 'International Sales (in $)', 'Release Date']])

#print(x.keys())
#x.drop(columns = ['Column1', 'Title', 'Movie Info', 'World Sales (in $)'])
#print(x.keys())
x.to_numpy()

#on definit donc la colonne qu'on essaye de predire, les ventes mondiales
#print(data.keys())
y= copy.deepcopy(data[['World Sales (in $)']])
y.to_numpy()

#On va donc ici separer nos groupes en test et train
x_train, x_test, y_train, y_test =sklearn.model_selection.train_test_split(x, y, test_size=0.30, random_state=0)
x_train = x_train.astype('int')
x_test = x_test.astype('int')
y_train = y_train.astype('int')
y_test = y_test.astype('int')
