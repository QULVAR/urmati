from fractions import Fraction
from sympy import symbols, sympify, sqrt, expand
from .refractor import refFractions

def multi(func1, func2, flag=True):
	du_oda, du_odb, du_odc, zwoda, zwodb, w, n, v = symbols('du_oda du_odb du_odc zwoda zwodb w n v')
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
		zwoda * zwoda: symbols('zwzwodada'),
		zwoda * zwodb: symbols('zwzwodadb'),
		zwodb * zwodb: symbols('zwzwodbdb'),
		zwodb * zwoda: symbols('zwzwodadb')
	}
	func1 = func1.replace('•', '*').replace('_/d', '_od').replace('&', '*').replace('w/d', 'wod').replace('dw', 'zw')
	func2 = func2.replace('•', '*').replace('_/d', '_od').replace('&', '*').replace('w/d', 'wod').replace('dw', 'zw')
	result = str(expand(sympify(func1) * sympify(func2)).subs(replacements)).replace(' - ', ' -').replace(' + ', ' +').replace('*s', '•s').replace('o', '/')
	if flag:
		result = result.replace('*', '&')
	else:
		result = result.replace('z', 'd').replace('*d', '&d').replace('*w', '&w')
	if not result[0] in ['+', '-']:
		result = '+' + result
	result = result.replace('+d', '+1&d').replace('-d', '-1&d').replace('+u', '+1&u').replace('-u', '-1&u').replace('+w', '+1&w').replace('-w', '-1&w')
	return refFractions(result)