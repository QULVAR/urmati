from fractions import Fraction
from sympy import symbols, sympify
from .refractor import refFractions

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
	du_oda, du_odb, du_odc = symbols('du_oda du_odb du_odc')
	for component in ud.split():
		componentSplitted = component.split('*')
		component1 = componentSplitted[1]
		componentMain = componentSplitted[0]
		component1 = component1.replace('d', '').split('/')
		number = matrix[stringCases[component1[0]]][columnCases[component1[1]]].replace(' - ', '-').replace(' + ', '+').replace('•', '*')
		if number != '0':
			result = str(sympify(number.replace('•', '*')) * sympify(componentMain.replace('&', '*').replace('_/d', '_od'))).replace('_od', '_/d').replace(' + ', '+').replace(' - ', '-').replace('*sqrt', '•sqrt')
			if '*' in result:
				if result.split('*')[1][0] != 'd':
					result = result.split('*')[1] + '&' + result.split('*')[0]
				else:
					result = result.replace('*', '&')
			else:
				if '-' != result[0]:
					result = '1&' + result
				else:
					result = '-1&' + result[1:]
			if not result[0] in ['+', '-']:
				result = '+' + result
			udNum += ' ' + result
	return refFractions(udNum[1:])