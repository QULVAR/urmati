from .multiplication import multi
from fractions import Fraction

def getNums(ud, matrix):
	columnCases = {
		'x': 0,
		'y': 1,
		'z': 2
	}
	
	stringCases = {
		'a': 0,
		'b': 1,
		'c': 2
	}
	udNum = ''
	for component in ud.split():
		componentSplitted = component.split('*')
		component1 = componentSplitted[1]
		componentMain = componentSplitted[0]
		component1 = component1.replace('d', '').split('/')
		
		number = matrix[stringCases[component1[0]]][columnCases[component1[1]]]
		if number != '0':
			numberSplit = number.split('•')
			if len(numberSplit) == 1:
				number = Fraction(numberSplit[0])
				componentNum = Fraction(componentSplitted[0].split('&')[0])
				result = componentSplitted[0].replace('+1', str(number * componentNum))
			else:
				
				number = Fraction(numberSplit[0])
				componentNum = Fraction(componentSplitted[0].split('&')[0])
				result = componentSplitted[0].replace('+1', f'{numberSplit[1]}•{str(number * componentNum)}')
			if not result[0] in ['+', '-']:
				result = '+' + result
			
			udNum += ' ' + result
	return udNum[1:]