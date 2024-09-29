from datetime import datetime, date
from dacite import Config

def encode_date(dt):
    return datetime.strptime(dt, '%Y-%m-%d').date()

def encode_datetime(dt):
    return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

config=Config(type_hooks={date: encode_date, datetime: encode_datetime})