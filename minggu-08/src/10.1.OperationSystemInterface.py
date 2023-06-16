# Modul ini osmenyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi
import os
os.getcwd()      # Return the current working directory
# 'C:\\Python311'       output
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
# o         output


# Fungsi bawaan dir()dan help()berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os
import os
dir(os)
# <returns a list of all module functions>      output
help(os)
# <returns an extensive manual page created from the module's docstrings>       output


# Untuk tugas manajemen file dan direktori harian, shutilmodul ini menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan
import shutil
shutil.copyfile('data.db', 'archive.db')
# 'archive.db'          output
shutil.move('/build/executables', 'installdir')
# 'installdir           output