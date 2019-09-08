# _*_ coding=utf-8 _*_
"""
Chapter.1
线性代数中的线性方程组
"""

#  为了简单起见,
#  我们仅仅考虑最简单的化简后的线性方程,即,a_1*x_1+a_2*x_2+a_3*x_3+....+a_n*x_n=b 的形式
# 1. a_n 为 整数或浮点,可正可负可为零
# 2. 若 a_n 为 +1(或-1),则 a_n*x_n 可简写为 x_n 或 (-x_n)
# 3. x 不分大小写
# 4. x_n 不重复在方程组中出现多次
import re


class Item(object):
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def __str__(self):
        return ('-' if self.a == -1 else '') + 'x_{}'.format(self.n)


class LinearEquation(object):
    def __init__(self, items, result):
        self.items = sorted(items, key=lambda i: i.n)
        self.result = result


class LinearEquations(object):
    def __init__(self, equations):
        self.equations = equations


def linear_equ_str2obj(linear_eq_string):
    linear_eq_string = linear_eq_string.replace(' ', '').replace('X', 'x')
    eq_left = linear_eq_string[:linear_eq_string.index('=')]
    eq_right = int(linear_eq_string[linear_eq_string.index('=') + 1:])
    # ([+-])?([\d]*)?\*?
    eq_left_pattern = re.compile('([+-])?(\d*)\*?x_([\d]*)')
    idx_of_sign_bit = 0
    idx_of_x_coefficient_bit = 1
    idx_of_x_appendix_bit = 2

    items = []
    for group in eq_left_pattern.findall(eq_left):
        print(group)
        # for example
        # ('', '', '1') <=> x_1
        # ('-', '2', '2') <=> -2*x_2
        # ('+', '', '3') <=> +x_3
        sign = -1 if group[idx_of_sign_bit] == '-' else 1
        coefficient = group[idx_of_x_coefficient_bit]
        coefficient = coefficient if coefficient != '' else '1'
        coefficient_of_variable = sign * int(coefficient)
        x_appendix = group[idx_of_x_appendix_bit]
        # print(coefficient_of_variable, 'x_{}'.format(x_appendix))
        items.append(Item(a=coefficient_of_variable, n=x_appendix))

    linear_equation = LinearEquation(items=items, result=int(eq_right))
    return linear_equation


equations_str_array = [
    "x_1-2*x_2+x_3=0",
    "2*x_2-8*x_3=8",
    "5*x_1-5*x_3=10"
]
eqs = list()
max_x_appendix = 0
for eq_string in equations_str_array:
    eq = linear_equ_str2obj(eq_string)
    eqs.append(eq)
    max_x_appendix = eq.items[-1].n

print(max_x_appendix)
linear_equations = LinearEquations(equations=eqs)
row_num = len(equations_str_array)
col_num = max_x_appendix + 1

