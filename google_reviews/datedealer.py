import datetime
import re

today = datetime.date.today()
n_days_be4 = lambda x : today - datetime.timedelta(days=x)
n_weeks_be4 = lambda x : today - datetime.timedelta(days=7*x)
n_months_be4 = lambda x : today - datetime.timedelta(days=31*x)
n_years_be4 = lambda x : today - datetime.timedelta(days=365*x)

def datedealer(_date): # str.

    try: n = int(re.search(r"\d+", _date).group(0))
    except: 
        print("datedealer error.")
        return
    if "天" in _date: return n_days_be4(n)
    if "週" in _date: return n_weeks_be4(n)
    if "月" in _date: return n_months_be4(n)
    if "年" in _date: return n_years_be4(n)
    return today