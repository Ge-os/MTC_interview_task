import sqlite3
import requests
import time

def get_work_days(date1, date2):
    date1, date2 = date1.replace('-', ''), date2.replace('-', '')
    
    url = f"https://isdayoff.ru/api/getdata?date1={date1}&date2={date2}&pre=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        # 0 - обычный, 2 - сокращенный, 4 - covid рабочий
        return sum(1 for day in response.text if day in '024')
    return None

conn = sqlite3.connect('vacancies.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT vacancy_id, quota_created_date, hire_date 
    FROM vacancies 
    WHERE hire_date >= quota_created_date
""")

data = cursor.fetchall()

total_work_days = 0
count = 0

for line in data:
    work_days = get_work_days(line[1], line[2])
    if work_days is not None:
        total_work_days += work_days
        count += 1
    # задержка на всякий случай
    time.sleep(0.1)

avg_days = total_work_days / count
print("Средний срок закрытия в рабочих днях:", avg_days)

conn.close()