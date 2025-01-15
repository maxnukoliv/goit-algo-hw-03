from datetime import datetime

date = '2020-10-09'

def get_days_from_today(date):
    now = (datetime.today())
    date2 = datetime.strptime(date, "%Y-%m-%d")
    result = now - date2
    result_final = result.days
    return result_final

print(get_days_from_today(date))