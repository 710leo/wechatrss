import re
import datetime
import requests
import model
from extract import extract,extract_all
from os.path import dirname,abspath
PREFIX = dirname(abspath(__file__))

def fetch(name,account_url,last_num):
    now = datetime.datetime.now()
    num = 0
    check = 'a'
    if last_num < 10000000:
	last_num = 10000000
    for i in xrange(last_num+1,last_num+500):
	url = account_url + '%s' % i
        r = requests.get(url)
        if r.status_code == 200:
            for title in zip(extract_all('<title>','</title>',r.content)):
                title = ''.join(title)
                if len(title) == 0:
		    num += 1
                    if num == 10:
			return
                else:
                    if check == title:
			pass
                    else:
			check = title
		        for date2 in zip(extract_all('2013-','</span>',r.content)):
			    date = ''.join(date2)
			    #date = now.year +'-'+ date
			    model.add_essay(name,title,url,date)
                            num = 0
		    model.update_account(name,i)
if __name__ == '__main__':
        fetch(name,account_url,last_num)

