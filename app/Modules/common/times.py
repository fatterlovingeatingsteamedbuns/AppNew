import time
import datetime
from functools import wraps


def timestamp():
    return time.time()

def dt_strftime(fmt='%Y-%m-%d-%H-%M'):
    return datetime.datetime.now().strftime(fmt)

def time_delta(days,fmt):
    now=datetime.datetime.now()
    delta=datetime.timedelta(days)
    n_days=now+delta
    return n_days.strftime(fmt)




if __name__ == '__main__':
    print(dt_strftime())