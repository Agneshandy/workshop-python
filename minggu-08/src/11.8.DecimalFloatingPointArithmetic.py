# Modul decimal menawarkan Decimaltipe data untuk aritmatika floating point desimal.
# Dibandingkan dengan implementasi built-in float dari floating point biner, kelas ini sangat membantu
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
# Decimal('0.74')           output
round(.70 * 1.05, 2)
# 0.73                      output


# Representasi yang tepat memungkinkan Decimal kelas untuk melakukan kalkulasi modulo dan uji kesetaraan yang tidak cocok untuk floating point biner
Decimal('1.00') % Decimal('.10')
# Decimal('0.00')           output
1.00 % 0.10
# 0.09999999999999995       output

sum([Decimal('0.1')]*10) == Decimal('1.0')
# True                      output
sum([0.1]*10) == 1.0
# False                     output


# Modul decimal menyediakan aritmatika dengan presisi sebanyak yang diperlukan
getcontext().prec = 36
Decimal(1) / Decimal(7)
# Decimal('0.142857142857142857142857142857142857')         output