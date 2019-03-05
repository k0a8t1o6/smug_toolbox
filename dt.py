import random
import datetime


# generate random date and time between now and the additional days entered
def random_datetime_genrator(period):
	k = 1000000
	now = datetime.datetime.now()
	_now = int(now.timestamp()*k)
	alt_now = int(((now + datetime.timedelta(period)).timestamp())*k)
	if period >= 0:
		randdt = datetime.datetime.fromtimestamp(random.randrange(_now, alt_now)/k)
	else:
		randdt = datetime.datetime.fromtimestamp(random.randrange(alt_now, _now)/k)
	return randdt
