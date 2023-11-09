# Job scheduling :
import schedule
from schedule import repeat, every
from datetime import time, timedelta, datetime
import time as tm

@repeat(every(2).seconds, message='Hey')
@repeat(every(5).seconds, message='whats up')
def job(message):
    print('Hello my world ' + message)

# schedule.every(3).seconds.do(job)
# schedule.every().day.at('20:20').do(job)
# schedule.every().hour.unit(time(11, 20, 45)).do(job)
# schedule.every().hour.unit(timedelta=8).do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)
