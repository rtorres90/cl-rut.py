def cl_rut(str_rut):
	if str_rut.find("-") < 0:
		return False
	int_multiple = 3
	int_sum_total = 0
	int_max_length = len(str_rut)
	if int_max_length < 10:
		str_rut = "0" * (10 - int_max_length) + str_rut
	for str_number in str_rut:
		if str_number == "-":
			break
		int_number = int(str_number)
		int_sum_total += int_multiple * int_number
		int_multiple -= 1
		if int_multiple == 1:
			int_multiple = 7
	int_module = int_sum_total % 11
	str_verificator_digit = 11 - int_module
	str_rut_verificator_digit = str_rut[int_max_length - 1]
	if (str_verificator_digit == 10) and (str_rut_verificator_digit.upper() != "K"):
		return False
	elif (str_verificator_digit != 10) and not(str_rut_verificator_digit == str(str_verificator_digit)):
		return False
	else:
		return True

if(cl_rut(raw_input())):
	print "Nya!"
else:
	print ":c"