import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vacancies.csv', sep='~', encoding='cp1251')

df['quota_created_date'] = pd.to_datetime(df['quota_created_date'])
df['hire_date'] = pd.to_datetime(df['hire_date'])

df['duration'] = (df['hire_date'] - df['quota_created_date']).dt.days

df = df[df['duration'] >= 0]

top_vacancies = df.groupby('vacancy_name')['duration'].median()
plt.figure(figsize=(10, 5))
top_vacancies.plot(kind='barh', color='skyblue')
plt.title('Самые быстрые вакансии для закрытия')
plt.xlabel('Медианное время закрытия (дни)')
plt.ylabel('Название вакансии')
plt.tight_layout()
plt.savefig('pics\\vacancies.png')

recruiter_stats = df.groupby('recruiter_name')['duration'].agg(['median', 'count'])
recruiter_stats = recruiter_stats.sort_values('median')

plt.figure(figsize=(12, 6))
recruiter_stats['median'].plot(kind='bar', color='lightgreen')
plt.title('Эффективность рекрутеров')
plt.xlabel('Имя рекрутёра')
plt.ylabel('Медианное время закрытия (дни)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pics\\efficiency.png')

plt.figure(figsize=(10, 6))
plt.hist(df['duration'], bins=30, color='purple', alpha=0.7)
plt.title('Распределение сроков закрытия вакансий')
plt.xlabel('Длительность (дни)')
plt.ylabel('Количество вакансий')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig('pics\\duration.png')