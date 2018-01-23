import datetime


def get_slugified_datetime_now():
    time = str(datetime.datetime.now())
    return time.replace('.', ' ').replace(':', ' ')


if __name__ == '__main__':
    print(get_slugified_datetime_now())
