from fractions import Fraction

def multiplyOnNumber(ud, num):
	return multi(ud, f'{num}&./.').replace('.', '')

def multi(func1, func2):
	components1 = func1.split(' ')
	components2 = func2.split(' ')
	result = ''
	for component2 in components2:
		component2SplittedNum = component2.split('&')
		component2Splitted = component2SplittedNum[1].split('/')
		number2 = Fraction(component2SplittedNum[0])
		numerator2 = component2Splitted[0]
		denominator2 = component2Splitted[1]
		for component1 in components1:
			component1SplittedNum = component1.split('&')
			component1Splitted = component1SplittedNum[1].split('/')
			
			number1 = Fraction(component1SplittedNum[0])
			
			numerator1 = component1Splitted[0]
			denominator1 = component1Splitted[1]
			
			number = str(number1 * number2)
			if not number[0] in ['+', '-']:
				number = '+' + number
			numerator = numerator1 + numerator2
			denominators = sorted([denominator1, denominator2])
			denominator = denominators[0] + denominators[1]
			
			result += f' {number}&{numerator}/{denominator}'
	return result[1:]