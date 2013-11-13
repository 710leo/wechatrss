import datetime
import update_list
import model
from apscheduler.scheduler import Scheduler

schedudler = Scheduler(daemonic = False)

@schedudler.cron_schedule(second='*',day_of_week='0-7',hour='1-24')

def quote_send_sh_job():
    account = model.get_wx()
    for info in account:
	update_list.fetch(info.account_id,info.account_addr,info.last_id)
schedudler.start()
