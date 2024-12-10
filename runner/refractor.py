import re

def ref(string):
	return string.replace('+1&', '+&').replace('&', '*').replace(' -', ' - ').replace(' +', ' + ').replace('du_du_', 'd^2u_').replace('dada', 'da^2').replace('dbdb', 'db^2').replace('dcdc', 'dc^2').replace('a', 'α').replace('b', 'β').replace('c', 'ɣ').replace('u_', 'ū').replace(' *d', ' d').replace('+*', '').replace('1*', '').replace('+ *', '+ ').replace('- *', '- ').replace('•sqrt(', '√').replace('*sqrt(', '√').replace(')*', '*')

def refBringSimilar(string):
	stringSplitted = string.replace('*', '•').replace(' + ', ' +').replace(' - ', ' -').replace('+-', '-').replace('-+', '-').split()
	for i in range(0, len(stringSplitted)):
		if not '&du_' in stringSplitted[i]:
			stringSplitted[i] = f"{stringSplitted[i]}&{stringSplitted[i+1].split('&')[1]}"
	newString = ' '.join(stringSplitted)
	pattern = r'(?<!\d•)([+-]sqrt\(.*?\)&\w+/[a-z]+)'
	newStringWithCoefficients = re.sub(pattern, '+1•\\1', newString)
	return newStringWithCoefficients
