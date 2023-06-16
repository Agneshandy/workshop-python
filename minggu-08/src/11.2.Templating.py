# Modul string mencakup kelas serbaguna Templatedengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
# 'Nottinghamfolk send $10 to the ditch fund.'          output


# Metode substitute() memunculkan a KeyErrorsaat placeholder tidak disediakan dalam kamus atau argumen kata kunci
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)
"""
Traceback (most recent call last):
  ...
KeyError: 'owner'
"""
t.safe_substitute(d)
# 'Return the unladen swallow to $owner.'           output


# Subkelas template dapat menentukan pembatas khusus. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih
# untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f            output

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# img_1074.jpg --> Ashley_0.jpg         output
# img_1076.jpg --> Ashley_1.jpg         output
# img_1077.jpg --> Ashley_2.jpg         output