

from datetime import datetime
from pytz import timezone

time_date= "27/04/94 08:43:40"
format_date = "%d/%m/%y %H:%M:%S"

date = datetime.strptime(time_date, format_date)

now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))


if __name__ == "__main__":
    print(date)
    print(date.hour)
    print(date.minute)
    print()
    print(now_asia.strftime(format_date))


