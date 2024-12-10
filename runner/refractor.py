import re

def ref(string):
	return string.replace('  ', ' ').replace('+ -', '- ').replace('- +', '- ').replace('+ +', '+ ').replace('frac', '????').replace('+1&', '+&').replace('&', '*').replace('-+', '-').replace('+-', '-').replace('++', '+').replace('+ +', '+').replace(' -', ' - ').replace(' +', ' + ').replace('du_du_', 'd^2u_').replace('dada', 'da^2').replace('dbdb', 'db^2').replace('dcdc', 'dc^2').replace('a', 'α').replace('b', 'β').replace('c', '\\gamma').replace('u_', 'ū').replace(' *d', ' d').replace('+*', '').replace('1*', '').replace('+ *', '+ ').replace('- *', '- ').replace('•sqrt(', '√').replace('*sqrt(', '√').replace(')*', '*').replace('????', 'frac').replace('gαmmα', 'gamma').replace('d', '\partial').replace('pαrtiαl', 'partial')

def refSignes(string):
	return string.replace(' ', '').replace('++', '+').replace('-+', '-').replace('+-', '-').replace('+', ' + ').replace('-', ' - ')

def refBringSimilar(string):
	stringSplitted = string.replace('*', '•').replace(' + ', ' +').replace(' - ', ' -').replace('+-', '-').replace('-+', '-').split()
	newString = ' '.join(stringSplitted)
	pattern = r'(?<!\d•)([+-]sqrt\(.*?\)&\w+/[a-z]+)'
	newStringWithCoefficients = re.sub(pattern, '+1•\\1', newString)
	return newStringWithCoefficients

def refToMarkdown(string):
	elements = []
	for i in string.replace(' + ', ' +').replace(' - ', ' -').split():
		number = ''
		root = ''
		fraction = i
		if '*' in i:
			isplitted = i.split('*')
			splittedNumber = isplitted[0]
			if '√' in splittedNumber:
				splittedNumberForRoot = splittedNumber.split('√')
				root = r'\sqrt{' + splittedNumberForRoot[1] + '}'
				splittedNumber = splittedNumberForRoot[0]
			if '/' in splittedNumber:
				numerator, denominator = splittedNumber.split('/')
				number = r'\frac{' + numerator + '}{' + denominator + '}'
			else:
				number = splittedNumber
			fraction = isplitted[1]
		if '/' in fraction:
			numerator, denominator = fraction.split('/')
			fraction = r'\frac{' + numerator + '}{' + denominator + '}'
		elements.append(number + root + fraction)
	return ' + '.join(elements)