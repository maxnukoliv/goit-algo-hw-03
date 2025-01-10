from datetime import datetime

now = (datetime.today())
date = '2020-10-09'

def get_days_from_today(date, now):
    date2 = datetime.strptime(date, "%Y-%m-%d")
    result = now - date2
    result_final = result.day
    return result_final

print(get_days_from_today(date, now))