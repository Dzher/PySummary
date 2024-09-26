import datetime


def get_today_date_str():
    today = datetime.date.today()
    return today.strftime('%Y-%m-%d')


def get_precise_time_now():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

