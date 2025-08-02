import pandas as pd

# Для Power BI сохраняю чистый датасет, который он распознает
df = pd.read_csv('vacancies.csv', sep='~', encoding='pt154')
df.to_csv("vacancies_clean.csv")