import sqlite3
import pandas as pd

# Кодировка подобрана вручную с LibreOffice
df = pd.read_csv('vacancies.csv', sep='~', encoding='pt154')

conn = sqlite3.connect('vacancies.db')
df.to_sql('vacancies', conn, index=False, if_exists='replace')

conn.close()