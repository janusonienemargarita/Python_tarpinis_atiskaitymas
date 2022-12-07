# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos


# Kitų failų ir žemiau esančio kodo nekeiskite


from modules.numbers.numbers import *

from modules.math.composition import composition as addition

from modules.math.division import division

from modules.math.subtraction import *

from modules.math.multiplication import *
# a = addition(one, four);
# b = divivsion(four, two);       keiciau i division, pamaniau kad rasybos klaida
# c = substraction(three, two);   keiciau i subtraction, , pamaniau kad rasybos klaida
# d = multiplication(five, two);



a = addition(one, four)
# a = composition(one, four)
b = division(four, two)
c = subtraction(three, two)
d = multiplication(five, two)
print(a)
print(b)
print(c)
print(d)
