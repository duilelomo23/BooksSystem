from datetime import datetime, date
from dacite import Config

def encode_date(dt):
    return datetime.strptime(dt, '%Y-%m-%d').date()

def encode_datetime(dt):
    return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

config=Config(type_hooks={date: encode_date, datetime: encode_datetime})

#遇到日期或時間字串，dacite 通過 type_hooks 使用定義的函數來解析並轉換，確保資料類中的 date 和 datetime 欄位能正確匹配輸入的字串格式。
