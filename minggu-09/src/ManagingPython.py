# Buat lingkungan baru bernama "snakes" yang berisi Python 3.9:
# conda create --name snakes python=3.9

# Aktifkan lingkungan baru:
# conda activate snakes

# Verifikasi bahwa lingkungan ular telah ditambahkan dan aktif:
# conda info --envs
# Conda menampilkan daftar semua lingkungan dengan tanda bintang (*) setelah nama lingkungan aktif:
"""
# conda environments:
#
base                     /home/username/anaconda3
snakes                *  /home/username/anaconda3/envs/snakes
snowflakes               /home/username/anaconda3/envs/snowflakes
"""

# Lingkungan aktif juga ditampilkan di depan prompt Anda di (tanda kurung) atau [tanda kurung] seperti ini:
# (snakes) $

# Verifikasi versi Python mana yang ada di lingkungan Anda saat ini:
# python --version

# Nonaktifkan lingkungan ular dan kembali ke lingkungan dasar:
# conda activate