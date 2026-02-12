import re

def match(value, matchValue, isRegex):
	if (isRegex):
		return re.search(matchValue, value)
	else:
		return value == matchValue

