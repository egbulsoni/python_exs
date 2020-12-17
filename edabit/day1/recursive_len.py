def length(txt):
	if txt == "":
		return 0
	return 1 + length(txt[1:])