import re
from datetime import datetime
from domain_validation.constants import MONTHS


def parse_date(date):
    pattern = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
    res = re.search(pattern, date, re.I)
    if res:                              # 14 Apr 2018
        day = int(date[0:2])
        month = MONTHS[date[res.start():res.start() + 3]]
        year = int(date[res.end() + 1: res.end() + 5])
    elif '/' in date and date[2] == '/':  # DD/MM/YYY
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    elif '/' in date:                     # YYYY/MM/DD
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
    elif '-' in date and date[2] == '-':  # DD-MM-YYYY
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    elif '-' in date:                     # YYYY-MM-DD
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
    elif '.' in date and date[2] == '.':  # DD.MM.YYYY
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    elif '.' in date:                     # YYYY.MM.DD
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
    else:                                 # YYYYMMDD
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
    date = datetime(year, month, day)
    return date.date()

