import re
from sympy import latex
from sympy import sympify, symbols

def ref(string):
	string = string.replace(' ', '').replace('frac', '????').replace('+1&', '+&').replace('&', '*').replace('-+', '-').replace('+-', '-').replace('++', '+').replace('++', '+').replace('+*+', '*').replace(' -', ' - ').replace('+', ' + ').replace('du_du_', 'd^2u_').replace('dwdw', 'd^2w').replace('dw', 'd w').replace('dada', 'da^2').replace('dbdb', 'db^2').replace('dcdc', 'dc^2').replace('a', 'α').replace('b', 'β').replace('c', '\\gamma').replace(' *d', ' d').replace('*u', 'u').replace('u_', 'ū').replace('1*', '').replace('????', 'frac').replace('gαmmα', 'gamma').replace('d', '\partial').replace('pαrtiαl', 'partial').replace('*\\', '\\').replace('v*v', 'v^2').replace('n*n', 'n^2').replace('v', '\\lambda').replace('n', '\\mu').replace('+ *', '*').replace('1 *', '').replace('1ū', 'ū')
	if string[:3] == ' + ':
		string = string[3:]
	return string

def refFractions(string):
	digits = [str(i) for i in range(10)]
	stringSplitted = string.replace('/d', 'od').split()
	for i in range(len(stringSplitted)):
		if 'oda/' in stringSplitted[i] or 'odb/' in stringSplitted[i] or 'odbdb/' in stringSplitted[i] or 'odada/' in stringSplitted[i] or 'odadb/' in stringSplitted[i] or 'odadb/' in stringSplitted[i] or 'u_/' in stringSplitted[i] or ('w/' in stringSplitted[i] and not 'dw/' in stringSplitted[i]) or 'x/' in stringSplitted[i] or 'y/' in stringSplitted[i]:
			parts = stringSplitted[i].split('/')
			if '&' in parts[0]:
				parts[0] = parts[0].split('&')
				parts[0][0] += '/' + parts.pop(-1)
			else:
				char = '+'
				parts[0] = parts[0].split('&')
				if parts[0][0][0] in ['+', '-']:
					char = parts[0][0][0]
					parts[0][0] = parts[0][0][1:]
				parts[0].append(char + '1')
				parts[0] = parts[0][::-1]
				parts[0][0] += '/' + parts.pop(-1)
			char = '+'
			if parts[0][0][0] in ['+', '-']:
				char = parts[0][0][0]
				parts[0][0] = parts[0][0][1:]
			if not parts[0][0][0] in digits:
				if parts[0][0][0] in ['n', 'v']:
					constant = parts[0][0][0]
					parts[0][0] = constant + '*1' + parts[0][0][1:]
				else:
					parts[0][0] = '1' + parts[0][0]
			if parts[0][0][0] in ['n', 'v']:
				if '*' in parts[0][0]:
					parts[0][0] = '*'.join(parts[0][0].split('*')[::-1])
			if 'x' in parts[0][1] or 'y' in parts[0][1]:
				stringSplitted[i] = char + parts[0][0] + '*' + parts[0][1]
			else:
				stringSplitted[i] = char + parts[0][0] + '&' + parts[0][1]
	return ' '.join(stringSplitted).replace('o', '/')

def refChangeFractions(string):
	digits = [str(i) for i in range(10)]
	stringSplitted = string.replace('/d', 'od').split()
	for i in range(len(stringSplitted)):
		if '/' in stringSplitted[i]:
			parts = stringSplitted[i].split('/')
			char = '+'
			if parts[0][0] in ['+', '-']:
				char = parts[0][0]
				parts[0] = parts[0][1:]
			if '*' in parts[0]:
				if parts[0][0] in digits:
					if parts[0].split('*')[-1] in ['n', 'v'] or 'sqrt' in parts[0].split('*')[-1]:
						parts[0] = '*'.join(parts[0].split('*')[::-1])
			elif parts[0][0] in ['n', 'v'] or 'sqrt' in parts[0]:
				parts[0] = parts[0] + '*1'
			parts[0] = char + parts[0]
			stringSplitted[i] = '/'.join(parts)
	return ' '.join(stringSplitted).replace('o', '/')

def refBringSimilar(string, flag = True, w = False):
	stringSplitted = string.replace('*', '•').replace(' + ', ' +').replace(' - ', ' -').replace('+-', '-').replace('-+', '-').split()
	if flag:
		for i in range(0, len(stringSplitted)):
				if not ('&du_' in stringSplitted[i] or '&u_' in stringSplitted[i]):
					stringSplitted[i] = f"{stringSplitted[i]}&{stringSplitted[i+1].split('&')[1]}"
	if w:
		for i in range(0, len(stringSplitted)):
				if not ('&dw' in stringSplitted[i] or '&w' in stringSplitted[i]):
					stringSplitted[i] = f"{stringSplitted[i]}&{stringSplitted[i+1].split('&')[1]}"
	newString = ' '.join(stringSplitted)
	pattern = r'(?<!\d•)([+-]sqrt\(.*?\)&\w+/[a-z]+)'
	newStringWithCoefficients = re.sub(pattern, '+1•\\1', newString)
	return newStringWithCoefficients

def refToMarkdown(string):
	newString = fractions(string.replace(' ', '').replace('-', ' - ').replace('+', ' + ').replace('•', '*').replace('&', '*').replace('*', ' * '))
	for i in newString.split('\\frac'):
		if '}' in i:
			newString = newString.replace(i.split('}')[0][1:] + '\\', '\\')
	for i in newString.split('\\frac'):
		if '{' in i:
			try:
				if i.split('}')[0][1] == '(' and i.split('}')[0][-1] == ')':
					newString = newString.replace(i.split('}')[0], '{' + i.split('}')[0][2:-1])
				if i.split('}')[1][1] == '(' and i.split('}')[1][-2] == ')':
					newString = newString.replace(i.split('}')[1], '{' + i.split('}')[1][2:-1] + '}')
			except:
				pass
	elements = []
	for i in newString.split():
		newElement = i
		while 'sqrt(' in newElement:
			while 'sqrt(' in newElement:
				sqrtpos = newElement.find('sqrt(')
				scopepos = newElement[sqrtpos:].find(')') + len(newElement[:sqrtpos])
				newElement = newElement[:sqrtpos] + '\\' + newElement[sqrtpos:sqrtpos + 4] + '{' + newElement[sqrtpos + 5:scopepos] + '}' + newElement[scopepos + 1:]
		elements.append(newElement)
	return ' + '.join(elements)


def fractions(input_string):
	result = ""
	i = 0
	while i < len(input_string):
		if input_string[i] == '/':
			numerator_start = i - 1
			if input_string[numerator_start] == ')':
				bracket_count = 1
				numerator_start -= 1
				while numerator_start >= 0 and bracket_count > 0:
					if input_string[numerator_start] == ')':
						bracket_count += 1
					elif input_string[numerator_start] == '(':
						bracket_count -= 1
					numerator_start -= 1
				numerator_start += 1
			else:
				while numerator_start >= 0 and input_string[numerator_start] not in " +-*/()":
					numerator_start -= 1
				numerator_start += 1
			numerator = input_string[numerator_start:i]
			denominator_end = i + 1
			if input_string[denominator_end] == '(':
				bracket_count = 1
				denominator_end += 1
				while denominator_end < len(input_string) and bracket_count > 0:
					if input_string[denominator_end] == '(':
						bracket_count += 1
					elif input_string[denominator_end] == ')':
						bracket_count -= 1
					denominator_end += 1
			else:
				while denominator_end < len(input_string) and input_string[denominator_end] not in " +-*/()":
					denominator_end += 1
			denominator = input_string[i + 1:denominator_end]
			fraction = f"\\frac{{{numerator}}}{{{denominator}}}"
			result += fraction
			i = denominator_end - 1
		else:
			result += input_string[i]
		i += 1
	return result