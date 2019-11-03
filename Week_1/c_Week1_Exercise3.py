#!/usr/bin/env python
from __future__ import print_function, unicode_literals

first_variable = '2001:4860:4860:8888'
SECOND_VARIABLE = '2001:4860:4860:8844'
the_3rd_Variable = '2001:4860:4860:8888'

print('first_variable: ' + first_variable)
print('SECOND_VARIABLE: ' + SECOND_VARIABLE)
print('the_3rd_Variable: ' + the_3rd_Variable)
print('first_variable = SECOND_VARIABLE: ' + str(first_variable == SECOND_VARIABLE))
print('first_variable != the_3rd_Variable: ' + str(first_variable != the_3rd_Variable))
