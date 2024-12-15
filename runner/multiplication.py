from fractions import Fraction
from sympy import symbols, sympify, sqrt, expand

def multi(func1, func2):
	du_oda, du_odb, du_odc = symbols('du_oda du_odb du_odc')
	replacements = {
		du_oda * du_oda: symbols('du_du_odada'),
		du_oda * du_odb: symbols('du_du_odadb'),
		du_oda * du_odc: symbols('du_du_odadc'),
		du_odb * du_oda: symbols('du_du_odadb'),
		du_odb * du_odb: symbols('du_du_odbdb'),
		du_odb * du_odc: symbols('du_du_odbdc'),
		du_odc * du_oda: symbols('du_du_odadc'),
		du_odc * du_odb: symbols('du_du_odbdc'),
		du_odc * du_odc: symbols('du_du_odcdc'),
	}
	func1 = func1.replace('•', '*').replace('_/d', '_od').replace('&', '*')
	func2 = func2.replace('•', '*').replace('_/d', '_od').replace('&', '*')
	result = str(expand(sympify(func1) * sympify(func2)).subs(replacements)).replace(' - ', ' -').replace(' + ', ' +').replace('*s', '•s').replace('*', '&').replace('o', '/')
	if not result[0] in ['+', '-']:
		result = '+' + result
	result = result.replace('+d', '+1&d').replace('-d', '-1&d')
	return result