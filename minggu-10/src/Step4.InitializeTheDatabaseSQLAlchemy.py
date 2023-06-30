# 1. Setel DATABASE_URLvariabel lingkungan ke string koneksi untuk klaster Anda:

# $ export DATABASE_URL="{connection-string}"

# Di mana {connection-string}string koneksi yang Anda salin sebelumnya.

# 2. Untuk menginisialisasi database contoh, gunakan cockroach sqlperintah untuk mengeksekusi pernyataan SQL dalam dbinit.sqlfile:

# $ cat dbinit.sql | cockroach sql --url $DATABASE_URL

# Pernyataan SQL dalam file inisialisasi harus dijalankan:

"""
CREATE TABLE

Time: 102ms
"""