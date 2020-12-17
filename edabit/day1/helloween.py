def halloween(dt):
	ymd = dt.split('/')
	if (int(ymd[2]) == 31 and int(ymd[1]) == 10):
		return 'Bonfire toffee'
	return 'toffee'