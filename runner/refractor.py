import re
from sympy import latex

def ref(string):
	string = string.replace(' ', '').replace('frac', '????').replace('+1&', '+&').replace('&', '*').replace('-+', '-').replace('+-', '-').replace('++', '+').replace('++', '+').replace('+*+', '*').replace(' -', ' - ').replace('+', ' + ').replace('du_du_', 'd^2u_').replace('dada', 'da^2').replace('dbdb', 'db^2').replace('dcdc', 'dc^2').replace('a', 'α').replace('b', 'β').replace('c', '\\gamma').replace(' *d', ' d').replace('*u', 'u').replace('u_', 'ū').replace('1*', '').replace('????', 'frac').replace('gαmmα', 'gamma').replace('d', '\partial').replace('pαrtiαl', 'partial').replace('*\\', '\\')
	if string[:3] == ' + ':
		string = string[3:]
	return string

def refBringSimilar(string, flag = True):
	stringSplitted = string.replace('*', '•').replace(' + ', ' +').replace(' - ', ' -').replace('+-', '-').replace('-+', '-').split()
	if flag:
		for i in range(0, len(stringSplitted)):
				if not ('&du_' in stringSplitted[i] or '&u_' in stringSplitted[i]):
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