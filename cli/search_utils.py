import re

def match(value, matchValue, isRegex = False, ignore_case = False):
	if (isRegex):
		if (ignore_case):
			matchValue = matchValue.lower()
			value = value.lower()
		return re.search(matchValue, value)
	else:
		return value == matchValue

