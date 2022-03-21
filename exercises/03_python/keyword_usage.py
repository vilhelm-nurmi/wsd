def keyword_usage(a, b):
	a = a.split()
	list = []
	for i in b:
		if i in a:
			list.append(True)
		else:
			list.append(False)
	return tuple(list)
	
