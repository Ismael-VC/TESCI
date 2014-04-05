#!/usr/bin/env python
#coding: utf-8


__author__ = 'Ismael Venegas Castelló' + '\t' + 'ismael.vc1337@gmail.com'
__date__ = '04 / Abril / 2014'


from fractions import Fraction  as F
from textwrap  import dedent    as dd


def calc(expresión=0, precisión=1000):
    '''
    Calculadora de expresiones con números complejos.

    expresión: expresión númerica válida.
    precisión: precisión de la simplificación.

    Uso:
    >>> from calc_comp import calc
    >>> from numpy import conjugate as c
    >>> z1 =  3-2j
    >>> z2 = -5-6j
    >>> z3 = -4+2j
    >>> exp = ((z1 - c(z2)) / z2) * ((2*z1) / z3)
    >>> calc(exp)
    (-0.49836065573770494-2.281967213114754j) =
         -152             -696
    ------------- + ------------- i
         305             305
    '''
    z = expresión
    frac_real = F.from_float(z.real).limit_denominator(precisión)
    frac_imag = F.from_float(z.imag).limit_denominator(precisión)
    print(dd('''\
                 {0} =
                      {1}             {2}
                 ------------- + ------------- i
                      {3}             {4}       '''.format(expresión,
                                                    frac_real.numerator,
                                                    frac_imag.numerator,
                                                    frac_real.denominator,
                                                    frac_imag.denominator)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
