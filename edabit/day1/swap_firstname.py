def name_shuffle(txt):
	full = txt.split(' ')
	s = ' '
	full[0], full[-1] = full[-1], full[0]
  # side note, the join method in python is weeeird
	return s.join(full)