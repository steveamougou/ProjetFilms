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
etape = 3
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

#On va donc ici separer nos groupes en test et train
x_train, x_test, y_train, y_test =sklearn.model_selection.train_test_split(x, y, test_size=0.30, random_state=0)

#Etait necessaire pour la comprehension mais n'est plus necessaire
#x_train = x_train.astype('int')
#x_test = x_test.astype('int')
#y_train = y_train.astype('int')
#y_test = y_test.astype('int')


#on utilise l'ACP acp ici pour retirer les meilleurs composantes
model = pipeline.make_pipeline(decomposition.PCA(n_components=2), naive_bayes.GaussianNB())
model.fit(x_train, y_train)
pred_test = model.predict(x_test)


print(f'Prediction accuracy for the gaussien algorithm: \
      {sklearn.metrics.accuracy_score(y_test, pred_test):.2%}')
print(classification_report(pred_test, y_test))

mat = confusion_matrix(y_test, pred_test)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label');
plt.show()

print('Vous êtes rendus à étape: ' + afficheur(etape) + '\n Allez maintenant à étape: ' + afficheur(etape+1))
