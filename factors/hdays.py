import datetime
import holidays
import time
import pandas as pd

def daterange(start_date, end_date):
	for n in range(int ((end_date - start_date).days)):
		yield start_date + datetime.timedelta(n)

def get_holidays(day):
	us_holidays = holidays.US()
	start_date = pd.to_datetime(time.strftime("%Y-%m-%d")).date()
	end_date = pd.to_datetime(day).date()
	for single_date in daterange(start_date, end_date):
		if(pd.to_datetime(single_date).date() in us_holidays):
			return single_date;
		else:
			continue