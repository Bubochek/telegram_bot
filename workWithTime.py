import datetime

def find_time():
    import time
    time = time.localtime()
    result = time.tm_hour * 3600 + time.tm_min * 60 + time.tm_sec

    return result


def convert_seconds(seconds):
    return str(datetime.timedelta(seconds=seconds))

def convert_seconds(seconds):
    return str(datetime.timedelta(seconds=seconds))


