from fractions import Fraction

def multiplyOnNumber(ud, num):
	return multi(ud, f'{num}&./.').replace('.', '')

def multi(func1, func2):
	components1 = func1.split(' ')
	components2 = func2.split(' ')
	result = ''
	for component2 in components2:
		root2 = ''
		component2SplittedNum = component2.split('&')
		component2Splitted = component2SplittedNum[1].split('/')
		if not '•' in component2SplittedNum[0]:
			number2 = Fraction(component2SplittedNum[0])
		else:
			splittedSqrt2 = component2SplittedNum[0].split('•')
			number2, root2 = splittedSqrt2
			if 's' in number2:
				number2, root2 = root2, number2
			number2 = Fraction(number2)
		numerator2 = component2Splitted[0]
		denominator2 = component2Splitted[1]
		for component1 in components1:
			root1 = ''
			component1SplittedNum = component1.split('&')
			component1Splitted = component1SplittedNum[1].split('/')
			if not '•' in component1SplittedNum[0]:
				number1 = Fraction(component1SplittedNum[0])
			else:
				splittedSqrt1 = component1SplittedNum[0].split('•')
				number1, root1 = splittedSqrt1
				if 's' in number1:
					number1, root1 = root1, number1
				number1 = Fraction(number1)
			
			numerator1 = component1Splitted[0]
			denominator1 = component1Splitted[1]
			
			number = str(number1 * number2)
			if not number[0] in ['+', '-']:
				number = '+' + number
			numerator = numerator1 + numerator2
			denominators = sorted([denominator1, denominator2])
			denominator = denominators[0] + denominators[1]
			
			if root1 != '' and root2 != '':
				root1 = f'{root1}*{root2}'
			elif root2 != '':
				root1 = root2
			if root1 == '' and root2 == '':
				result += f' {number}&{numerator}/{denominator}'
			else:
				result += f' {number}•{root1}&{numerator}/{denominator}'
	return result[1:]