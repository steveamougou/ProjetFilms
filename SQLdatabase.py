import pandas as pd
import sqlite3

cleandf = pd.read_excel('/home/steveb/Desktop/Universite/PSY4016/Projet/Data/cleandata.xlsx')

conn = sqlite3.connect('movie_database')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS movieSales (Distributor text, DomesticSales number, InternationalSales number, WorldSales number)')
conn.commit()
# , Domestic_Sales_(in $) number, International_Sales (in $) number), World_Sales_(in $) number, Release_Date number
# data = {'product_name': ['Computer','Tablet','Monitor','Printer'],
#         'price': [900,300,450,150]
#         }

smalldf= pd.DataFrame()
smalldf['Distributor'] = cleandf['Distributor']
smalldf['DomesticSales']= cleandf['Domestic Sales (in $)']
smalldf['InternationalSales'] = cleandf['International Sales (in $)']
smalldf['WorldSales'] = cleandf['World Sales (in $)']
# print(columns)
smalldf.to_sql('movieSales', conn, if_exists='replace', index=False)

c.execute('''
SELECT * FROM 'movieSales'
          ''')
