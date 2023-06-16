# Skrip utilitas umum seringkali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut sysmodul argv sebagai daftar
import sys
print(sys.argv)
# ['demo.py', 'one', 'two', 'three']            output


# Modul ini argparsemenyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah.
# Skrip berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional untuk ditampilkan
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)