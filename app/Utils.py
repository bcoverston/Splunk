from datetime import date, timedelta, datetime
import pytz

__author__ = 'eMaM'


def startDate():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    return yesterday.replace(hour=00, minute=00, second=00, microsecond=00)


def endDate():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    return yesterday.replace(hour=23, minute=59, second=59, microsecond=00)


def formateDate(date, pattern):
    return date.strftime(pattern)


print(endDate())
