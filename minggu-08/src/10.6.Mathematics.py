# Modul ini mathmemberikan akses ke fungsi library C yang mendasari matematika floating point
import math
math.cos(math.pi / 4)
# 0.70710678118654757               output
math.log(1024, 2)
# 10.0                              output


# Modul random menyediakan alat untuk membuat pilihan acak
import random
random.choice(['apple', 'pear', 'banana'])

random.sample(range(100), 10)   # sampling without replacement

random.random()    # random float

random.randrange(6)    # random integer chosen from range(6)


# Modul statistics menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
# 1.6071428571428572                output
statistics.median(data)
# 1.25                              output
statistics.variance(data)
# 1.3720238095238095                output