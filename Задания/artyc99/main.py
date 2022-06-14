import re


__greek_numbers = ['I', 'V']
__pattern = re.compile(r'\D')


def main():
	number_str = input()

	number_int = int(number_str) if not __pattern.search(number_str) else None
	number_int = number_int if number_int and (0 < number_int < 9) else None

	if not number_int:
		return 0
	
	greek_str_buf = ''.join([__greek_numbers[0] for greek_number in range(0, number_int)])
	greek_str = greek_str_buf.replace('IIIII', 'V') if number_int >= 5 else  greek_str_buf.replace('IIII', 'IV')
	print(greek_str)


if __name__ == '__main__':
	main()
