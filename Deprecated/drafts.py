
a = [2,1,4]
a.append(None)
print(a)
raw = pd.DataFrame (a, columns = ['column_name'])

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

missing_values_table(raw)




Changing values to SQL:
import pandas as pd
import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
conn.commit()

data = {'product_name': ['Computer','Tablet','Monitor','Printer'],
        'price': [900,300,450,150]
        }

df = pd.DataFrame(data, columns= ['product_name','price'])
df.to_sql('products', conn, if_exists='replace', index = False)

c.execute('''
SELECT * FROM products
          ''')

for row in c.fetchall():
    print (row)


def recod_genre(column):
    c = []
    a = 0
    b = 0
    for cell in column:
        c.append([])
        for i in cell:
            c[a].append([])
            if i == 'Action':
                c[a][b] = 0
            elif i == 'Adventure':
                c[a][b] = 1
            elif i == 'Animation':
                c[a][b] = 2
            elif i == 'Comedy':
                c[a][b] = 3
            elif i == 'Family':
                c[a][b] = 4
            elif i == 'Sci-Fi':
                c[a][b] == 5
            elif i == 'Drama':
                c[a][b] = 6
            elif i == 'Fantasy':
                c[a][b] = 7
            elif i == 'Romance':
                c[a][b] = 8
            elif i == 'Crime':
                c[a][b] = 9
            elif i == 'Thriller':
                c[a][b] = 10
            elif i == 'Musical':
                c[a][b] = 11
            elif i == 'War':
                c[a][b] = 12
            elif  i == 'Mistery':
                c[a][b] = 13
            elif  i == 'Biography':
                c[a][b] = 14
            elif  i == 'Horror':
                c[a][b] = 15
            else :
                c[a][b] == 16
            b +=1
        a += 1
    return c


#Visualisation de l'ACP
# Utiliser l'ACP sans et avec échelle sur les données X_train
# pour la visualisation.
x_train_transformed = pca.transform(x_train)
scaler = std_clf.named_steps['standardscaler']
x_train_std_transformed = pca_std.transform(scaler.transform(x_train))

# visualiser un ensemble de données standardisé
# ou non standardisé avec l'ACP effectuée
FIG_SIZE = (10, 7)
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=FIG_SIZE)

for l, c, m in zip(range(0, 3), ('blue', 'red', 'green'), ('^', 's', 'o')):
    ax1.scatter(x_train_transformed[y_train == l, 0],
                x_train_transformed[y_train == l, 1],
                color=c,
                label='groupe %s' % l,
                alpha=0.5,
                marker=m
                )

for l, c, m in zip(range(0, 3), ('blue', 'red', 'green'), ('^', 's', 'o')):
    ax2.scatter(x_train_std_transformed[y_train == l, 0],
                x_train_std_transformed[y_train == l, 1],
                color=c,
                label='groupe %s' % l,
                alpha=0.5,
                marker=m
                )

ax1.set_title('données d\'entraînement NON standardisé après l\'ACP')
ax2.set_title('données d\'entraînement standardisé après l\'ACP')

for ax in (ax1, ax2):
    ax.set_xlabel('1er composante principale')
    ax.set_ylabel('2e composante principale')
    ax.legend(loc='upper right')
    ax.grid()

plt.tight_layout()

plt.show()


print(classification_report(y_test, pred_test,
                            target_names=faces.target_names))
