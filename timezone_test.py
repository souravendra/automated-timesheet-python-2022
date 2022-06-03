from time import time
from pytz import timezone
from datetime import date, datetime, time

ind_datetime = datetime.now(timezone("Asia/Kolkata"))
ind_time = time.now(timezone("Asia/Kolkata"))
print(ind_time)
