from datetime import datetime, timedelta

def etl_dates():
    t = datetime.today()
    y = t - timedelta(days=1)
    today = datetime.strptime(t.strftime('%Y-%m-%d'), '%Y-%m-%d')
    yesterday = datetime.strptime(y.strftime('%Y-%m-%d'), '%Y-%m-%d')
    return today, yesterday

def full_load_dates():
    t = datetime.today()
    od = t - timedelta(days=999)
    fd = t + timedelta(days=10)
    future_date = datetime.strptime(fd.strftime('%Y-%m-%d'), '%Y-%m-%d')
    old_date = datetime.strptime(od.strftime('%Y-%m-%d'), '%Y-%m-%d')
    return future_date, old_date
