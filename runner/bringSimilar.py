import re
from fractions import Fraction
from collections import defaultdict

def bringSimilar(expression):
    # Разбиваем строку на отдельные термы
    terms = re.findall(r'([+-]?[0-9./]+)&(\S+)', expression)

    # Используем defaultdict для суммирования коэффициентов
    term_dict = defaultdict(Fraction)

    for coeff, variable in terms:
        # Преобразуем дроби в Fraction
        value = Fraction(coeff)
        term_dict[variable] += value
        
    # Формируем итоговую строку
    simplified_terms = []
    for variable, coeff in term_dict.items():
        if coeff != 0:  # Пропускаем термы с нулевым коэффициентом
            # Используем str() для преобразования Fraction в строку
            simplified_terms.append(f'{"+" if coeff > 0 else "-"}{str(abs(coeff))}&{variable}')
        
    # Объединяем термы в строку
    return ' '.join(simplified_terms)