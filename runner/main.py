from .matrix import matrixTrans
from .multiplication import multi, multiplyOnNumber
from .сoeficient import getNums
from .bringSimilar import bringSimilar
from .refractor import ref

def urmati (u, matrixInp):
	output = ''
	#u = input('u: ')
	#u = '+1*uxx +2*uxy +2*uyy +4*uyz +5*uzz +1*ux +1*uy'
	#u = '+2*uxx +2*uxy +1*uyy +2*uxz +2*uz -3*u'
	#matrixInp = input('matrix: ')
	#matrixInp = '1 1 0/0 1 2/0 0 1'
	#matrixInp = '1 1 0/1 0 1/0 0 1'
	matrix = []
	for string in matrixInp.split('/'):
		matrix.append(list(map(int, string.split())))
	matrix = matrixTrans(matrix)
	output += '\n'
	for string in matrix:
		output += f'{string}\n'
	if len(matrix) > 2:
		udxFormula = '+1&du_/da*da/dx +1&du_/db*db/dx +1&du_/dc*dc/dx'
		udyFormula = '+1&du_/da*da/dy +1&du_/db*db/dy +1&du_/dc*dc/dy'
		udzFormula = '+1&du_/da*da/dz +1&du_/db*db/dz +1&du_/dc*dc/dz'
	else:
		udxFormula = '+1&du_/da*da/dx +1&du_/db*db/dx'
		udyFormula = '+1&du_/da*da/dy +1&du_/db*db/dy'
	udx = getNums(udxFormula, matrix)
	udy = getNums(udyFormula, matrix)
	if len(matrix) > 2:
		udz = getNums(udzFormula, matrix)
	else:
		udz = ''
	uddxx = bringSimilar(multi(udx, udx))
	uddxy = bringSimilar(multi(udx, udy))
	uddyy = bringSimilar(multi(udy, udy))
	if len(matrix) > 2:
		uddxz = bringSimilar(multi(udx, udz))
		uddyz = bringSimilar(multi(udy, udz))
		uddzz = bringSimilar(multi(udz, udz))
	else:
		uddxz = ''
		uddyz = ''
		uddzz = ''
	output += f'\nu\'x = {ref(udx)}\n\n'
	output += f'u\'y = {ref(udy)}\n\n'
	output += f'u\'z = {ref(udz)}\n\n'
	output += f'u\'\'xx = {ref(uddxx)}\n\n'
	output += f'u\'\'xy = {ref(uddxy)}\n\n'
	output += f'u\'\'yy = {ref(uddyy)}\n\n'
	output += f'u\'\'xz = {ref(uddxz)}\n\n'
	output += f'u\'\'yz = {ref(uddyz)}\n\n'
	output += f'u\'\'zz = {ref(uddzz)}\n\n'
	expressionsCases = {
		'uxx': uddxx,
		'uxy': uddxy,
		'uxz': uddxz,
		'uyx': uddxy,
		'uyy': uddyy,
		'uyz': uddyz,
		'uzx': uddxz,
		'uzy': uddyz,
		'uzz': uddzz,
		'ux': udx,
		'uy': udy,
		'uz': udz,
		'u': 'u_'
	}
	u1 = ''
	for component in u.split():
		number, key = component.split('*')
		if key != 'u':
			newComponent = multiplyOnNumber(expressionsCases[key], number)
		else:
			newComponent = f'{number}&{expressionsCases[key]}'
			if not newComponent[0] in ['+', '-']:
				newComponent = '+' + newComponent
		u1 += f' {newComponent}'
	u1 = u1[1:]
	u1Refed = ref(u1) + ' = 0'
	u2 = bringSimilar(u1)
	u2Refed = ref(u2) + ' = 0'
	output += f'{u1Refed}\n\n'
	output += f'{u2Refed}'
	return output