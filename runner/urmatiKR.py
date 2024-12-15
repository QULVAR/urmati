from fractions import Fraction
from sympy import sqrt, I, simplify, Rational, symbols, sympify
from .bringSimilar import bringSimilar
from .refractor import refBringSimilar, refToMarkdown, ref
from .urmatiSR import urmatiSR

def determinant(a):
	for i in range(0, 2):
		for j in range(0, 2):
			a[i][j] = sympify(a[i][j])
	return str(a[0][0] * a[1][1] - a[0][1] * a[1][0])

def urmatiKR(u):
	output = ''
	diffU = u.replace('uxx', '(dy)^2').replace('uxy', 'dxdy').replace('uyx', 'dxdy').replace('uyy', '(dx)^2')
	a11, a12, a21 = 0, 0, 0
	for i in refBringSimilar(bringSimilar(diffU.replace('*', '&')), False).split():
		if '(dy)^2' in i:
			a11 = i.split('&')[0]
		elif 'dxdy' in i:
			a12 = str(Fraction(i.split('&')[0]) * Fraction('1/2'))
		elif '(dx)^2' in i:
			a21 = i.split('&')[0]
	chars = {
		'+': '-',
		'-': '+'
	}
	diffU = diffU.split()
	for i in range(len(diffU)):
		if 'dxdy' in diffU[i]:
			diffU[i] = chars[diffU[i][0]] + diffU[i][1:]
	diffU = ' '.join(diffU)
	output += r'\( ' + diffU[1:diffU.find('(dx)^2') + 6].replace('*', '').replace('1(', '(').replace('1d', 'd').replace(a12, '') + r' = 0 \) <br>'
	d = str(Fraction(a12)*Fraction(a12) - Fraction(a11) * Fraction(a21))
	output += fr'\( d = {a12}^2 - {a11}*{a21} = '.replace('*+', '*')
	if '/' in d:
		char = ''
		numerator, denominator = d.split('/')
		if numerator[0] == '-':
			char = '-'
			numerator = numerator[1:]
		output += char + r'\frac{' + numerator + '}{' + denominator + '} \)'
	else:
		output += fr'{d}'
	diffType = -1
	if d == '0':
		output += r' - \) параболический <br><br>'
		diffType = 0
	elif d[0] == '-':
		output += r' - \) эллиптический <br><br>'
		diffType = 1
	else:
		output += r' - \) гиперболический <br><br>'
		diffType = 2
	dx, dy1, dy2 = -1, -1, -1
	if '/' in d:
		numerator, denominator = d.split('/')
		d = Rational(int(numerator), int(denominator))
	else:
		d = int(d)
	sqrtD = str(simplify(sqrt(d)))
	
	output += '''\\(
\\left[
\\begin{array}{1}
'''
	if a11 == 0:
		dx = 0
		dy1 = str(Fraction(a21) / (Fraction(a12) * 2))
		output += r'dx = 0 \\'
		output += r'dy =  \frac{' + a21 + '}{' + str(Fraction(a12) * 2) + '} = ' + dy1 + '\n'
	else:
		dy1 = str(simplify(f'({a12} + {sqrtD})/{a11}')).replace(' + ', ' +').replace(' - ', ' -')
		dy2 = str(simplify(f'({a12} - {sqrtD})/{a11}')).replace(' + ', ' +').replace(' - ', ' -')
		output += fr'dy = {ref(refToMarkdown(dy1))}'.replace(' +', ' + ').replace(' -', ' - ').replace('I', '\mathit{i}') + r'\\'
		output += fr'dy = {ref(refToMarkdown(dy2))}'.replace(' +', ' + ').replace(' -', ' - ').replace('I', '\mathit{i}') + '\n'
	output += r'''\end{array}
\right.
\) <br><br>'''
	
	x1, y1, y2 = -1, -1, -1
	
	output += '''\\(
\\left[
\\begin{array}{1}
'''
	if dx == 0:
		x1 = 'x=C'
		output += 'x = C \\'
	dy1ToY = ' '.join(map(lambda g: g + '*x', dy1.split()))
	y1 = f'y={dy1ToY} +C'
	output += ref(refToMarkdown(y1.replace(' ', '').replace('=', ' = ').replace('+', ' + ').replace('-', ' - '))).replace('I', '\mathit{i}') + r'\\'
	if dy2 != -1:
		dy2ToY = ' '.join(map(lambda g: g + '*x', dy2.split()))
		y2 = f'y={dy2ToY} +C'
		output += ref(refToMarkdown(y2.replace(' ', '').replace('=', ' = ').replace('+', ' + ').replace('-', ' - '))).replace('I', '\mathit{i}')
	output += r'''\end{array}
\right.
\) <br><br>'''
	x, y = symbols('x y')
	y1 = str(simplify(y1.replace('=', ' -(').replace(' +C', ')')))
	if y2 != -1:
		y2 = str(simplify(y2.replace('=', ' -(').replace(' +C', ')')))
	
	output += '''\\(
\\left[
\\begin{array}{1}
'''
	if x1 == 'x=C':
		output += 'x = C \\'
	yRefed = ref(refToMarkdown(y1.replace('I', '\mathit{i}').replace(' ', '').replace('-',  ' - ').replace('+', ' + ').replace(' + y', ''))).replace('α', 'a')
	if not yRefed[:2] in [' + ', ' - ']:
		if not yRefed[0] in ['+', '-']:
			yRefed = ' + ' + yRefed
	output += 'y' + yRefed + r' = C\\'
	if dy2 != -1:
		yRefed = ref(refToMarkdown(y2.replace('I', '\mathit{i}').replace(' ', '').replace('-',  ' - ').replace('+', ' + ').replace(' + y', ''))).replace('α', 'a')
		if not yRefed[:3] in [' + ', ' - ']:
			if not yRefed[0] in ['+', '-']:
				yRefed = ' + ' + yRefed
		output += 'y' + yRefed + r' = C\\'
	output += r'''\end{array}
\right.
\) <br><br>'''
	
	digits = [str(i) for i in range(0, 10)]
	y1 = y1.replace(' ', '').replace('-', ' -').replace('+', ' +').split()
	for i in range(len(y1)):
		if not y1[i][0] in ['+', '-']:
			y1[i] = '+' + y1[i][0]
		if not y1[i][1] in digits:
			y1[i] = y1[i][0] + '1*' + y1[i][1:]
	y1 = ' '.join(y1)
	if y2 != -1:
		y2 = y2.replace(' ', '').replace('-', ' -').replace('+', ' +').split()
		for i in range(len(y2)):
			if not y2[i][0] in ['+', '-']:
				y2[i] = '+' + y2[i][0]
			if not y2[i][1] in digits:
				y2[i] = y2[i][0] + '1*' + y2[i][1:]
		y2 = ' '.join(y2)
	
	f = 0
	g = 0
	A = [['0', '0'], ['0', '0']]
	#A = [['-3•sqrt(2)-1', '1'], ['+3•sqrt(2)-1', '1']]
	if diffType == 0: #параболический
		f = y1.replace('*s', '•s')
		for i in f.split():
			if 'x' in i:
				A[0][0] += i.split('*')[0]
			else:
				A[0][1] += i.split('*')[0]
		g = []
		for i in range(1, 10):
			if determinant([A[0], [str(i), '0']]) != '0':
				g.extend([str(i), '0'])
				break
		if g == []:
			for i in range(1, 10):
				if determinant([A[0], ['0', str(i)]]) != '0':
					g.extend(['0', str(i)])
					break
			if g == []:
				for i in range(1, 10):
					for j in range(1, 10):
						if determinant([A[0], [str(i), str(j)]]) != '0':
							g.extend([str(i), str(j)])
							break
		A[1] = g.copy()
		g = ''
		for i in A[1][0].split():
			if not i[0] in ['+', '-']:
				g += f' +{i}*x'
			else:
				g += f' {i}*x'
		for i in A[1][1].split():
			if not i[0] in ['+', '-']:
				g += f' +{i}*y'
			else:
				g += f' {i}*y'
		x, y = symbols('x y')
		g = str(simplify(g))
	elif diffType == 1: #эллиптический
		f = ' '.join([i for i in y2.split() if not 'I' in i])
		g = ' '.join(list(map(lambda g: g.replace('I*', ''), [i for i in y2.split() if 'I' in i])))
		for i in f.split():
			if 'x' in i:
				A[0][0] = i.split('*')[0].replace('+', '')
			else:
				A[0][1] = i.split('*')[0].replace('+', '')
		for i in g.split():
			if 'x' in i:
				A[1][0] = i.split('*')[0].replace('+', '')
			else:
				A[1][1] = i.split('*')[0].replace('+', '')
	elif diffType == 2: #гиперболический
		f = y1.replace('*s', '•s')
		g = y2.replace('*s', '•s')
		for i in f.split():
			if 'x' in i:
				A[0][0] += i.split('*')[0]
			else:
				A[0][1] += i.split('*')[0]
		for i in g.split():
			if 'x' in i:
				A[1][0] += i.split('*')[0]
			else:
				A[1][1] += i.split('*')[0]
		for i in range(2):
			for j in range(2):
				if len(A[i][j]) > 1:
					A[i][j] = A[i][j][1:]
					if A[i][j][0] == '+':
						A[i][j] = A[i][j][1:]
	A = list(map(lambda g: list(map(str, g)), A))
	output += r'''\( \begin{equation}
\left\{
\begin{aligned}
\alpha &= '''
	output += ref(refToMarkdown(f)).replace('I', '\mathit{i}') + r'\\'
	output += r'\beta &= ' + ref(refToMarkdown(g)).replace('I', '\mathit{i}') + '\n'
	output += r'''\end{aligned}
\right.
\end{equation} \) <br>'''
	res = urmatiSR(u, '?'.join(map(lambda g: ' '.join(g), A)), False)
	output += res[0].replace('(A^{-1})^{T}', 'A') + '<br>'
	return output