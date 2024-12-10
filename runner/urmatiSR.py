from .matrix import matrixTrans, matrixPrint
from .multiplication import multi, multiplyOnNumber
from .сoeficient import getNums
from .bringSimilar import bringSimilar
from .refractor import ref, refBringSimilar


def urmatiSR (u, matrixInp):
	output = ''
	matrix = matrixTrans(matrixInp)
	output += matrixPrint(matrix)
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
	uddxx = refBringSimilar(bringSimilar(multi(udx, udx)))
	uddxy = refBringSimilar(bringSimilar(multi(udx, udy)))
	uddyy = refBringSimilar(bringSimilar(multi(udy, udy)))
	if len(matrix) > 2:
		uddxz = refBringSimilar(bringSimilar(multi(udx, udz)))
		uddyz = refBringSimilar(bringSimilar(multi(udy, udz)))
		uddzz = refBringSimilar(bringSimilar(multi(udz, udz)))
	else:
		uddxz = ''
		uddyz = ''
		uddzz = ''
	output += f'u\'x = {ref(bringSimilar(udx))}\n\n'
	output += f'u\'y = {ref(bringSimilar(udy))}\n\n'
	output += f'u\'z = {ref(bringSimilar(udz))}\n\n'
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
	print()
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
	u2 = refBringSimilar(bringSimilar(u1))
	u2Refed = ref(u2) + ' = 0'
	output += f'{u1Refed}\n\n'
	output += f'{u2Refed}'
	return output