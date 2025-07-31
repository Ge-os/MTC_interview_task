import sqlite3

conn = sqlite3.connect('vacancies.db')
cursor = conn.cursor()

# средний срок закрытия в календарных днях
query = """
SELECT 
    AVG(JULIANDAY(hire_date) - JULIANDAY(quota_created_date))
FROM vacancies
WHERE hire_date >= quota_created_date;
""" # без WHERE другой результат - в строке 9 hire_date < quota_created_date

cursor.execute(query)
result = cursor.fetchone()
print("Средний срок закрытия дней", result[0])
conn.close()
