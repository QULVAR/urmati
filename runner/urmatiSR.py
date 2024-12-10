from .matrix import matrixTrans, matrixPrint
from .multiplication import multi, multiplyOnNumber
from .сoeficient import getNums
from .bringSimilar import bringSimilar
from .refractor import ref, refBringSimilar, refToMarkdown, refSignes


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
	
	output += r"\( u'_{x} = " + ref(refToMarkdown(ref(bringSimilar(udx)))) + r'\)    ' + '<br>'
	output += r"\( u'_{y} = " + ref(refToMarkdown(ref(bringSimilar(udy)))) + r'\)    ' + '<br>'
	if len(matrix) == 3:
		output += r"\( u'_{z} = " + ref(refToMarkdown(ref(bringSimilar(udz)))) + r'\)    ' + '<br>'
	output += r"\( u''_{xx} = " + ref(refToMarkdown(ref(bringSimilar(uddxx)))) + r'\)    ' + '<br>'
	output += r"\( u''_{xy} = " + ref(refToMarkdown(ref(bringSimilar(uddxy)))) + r'\)    ' + '<br>'
	output += r"\( u''_{yy} = " + ref(refToMarkdown(ref(bringSimilar(uddyy)))) + r'\)    ' + '<br>'
	if len(matrix) == 3:
		output += r"\( u''_{xz} = " + ref(refToMarkdown(ref(bringSimilar(uddxz)))) + r'\)    ' + '<br>'
		output += r"\( u''_{yz} = " + ref(refToMarkdown(ref(bringSimilar(uddyz)))) + r'\)    ' + '<br>'
		output += r"\( u''_{zz} = " + ref(refToMarkdown(ref(bringSimilar(uddzz)))) + r'\)    ' + '<br>'

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
		if component[1] == 'u':
			number, key = list(component)
			number += '1'
		else:
			number, key = component.split('*')
		if key != 'u':
			newComponent = multiplyOnNumber(expressionsCases[key], number)
		else:
			newComponent = f'{number}&{expressionsCases[key]}'
			if not newComponent[0] in ['+', '-']:
				newComponent = '+' + newComponent
		u1 += f' {newComponent}'
	u1 = u1[1:]
	u1Refed = ref(u1)
	u2 = refBringSimilar(bringSimilar(u1))
	u2Refed = ref(u2)
	output += rf"\({refSignes(ref(refToMarkdown(ref(u1Refed))))} = 0\) <br>"
	output += rf"\({refSignes(ref(refToMarkdown(ref(u2Refed))))} = 0\) <br>"
	return output