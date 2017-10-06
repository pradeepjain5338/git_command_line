def check_bit4(input):
	mas=0b1000
	desired=input & mas
	if desired>0:
		return "om"
	else :
		return "off"


