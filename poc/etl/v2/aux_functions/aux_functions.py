from datetime import datetime, timedelta

def etl_dates():
    t = datetime.today()
    y = t - timedelta(days=1)
    today = datetime.strptime(t.strftime('%Y-%m-%d'), '%Y-%m-%d')
    yesterday = datetime.strptime(y.strftime('%Y-%m-%d'), '%Y-%m-%d')
    return today, yesterday
