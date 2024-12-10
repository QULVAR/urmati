import sympy as sp

def bringSimilar(expression):
    terms = expression.split(' ')
    grouped_terms = {}
    for term in terms:
        coeff, variable = term.split('&')
        coeff = sp.sympify(coeff.replace('•', '*').replace('+', ''))
        if variable in grouped_terms:
            grouped_terms[variable] += coeff
        else:
            grouped_terms[variable] = coeff
    # Формируем итоговую строку
    simplified_terms = []
    for variable, coeff in grouped_terms.items():
        simplified_coeff = sp.simplify(coeff)
        if simplified_coeff != 0:  # Убираем нулевые члены
            simplified_terms.append(f'{simplified_coeff}&{variable}')
    return ' +'.join(simplified_terms)