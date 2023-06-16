# Modul reprlib menyediakan versi yang repr()disesuaikan untuk tampilan singkat wadah besar atau bersarang dalam
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
# "{'a', 'c', 'd', 'e', 'f', 'g', ...}"         output


# Modul pprint menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan yang ditentukan pengguna dengan cara yang dapat dibaca oleh juru bahasa
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)
"""
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
"""


# Modul textwrap memformat paragraf teks agar pas dengan lebar layar tertentu
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))
"""
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
"""


# Modul locale mengakses database format data khusus budaya
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# 'English_United States.1252'          output
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)
# '1,234,567'                           output
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
# '$1,234,567.80'                       output