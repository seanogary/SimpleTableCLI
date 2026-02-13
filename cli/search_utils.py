import re

def match(value, matchValue, isRegex = False):
	if (isRegex):
		return re.search(matchValue, value)
	else:
		return value == matchValue

