# Setel DATABASE_URLvariabel lingkungan ke string koneksi ke klaster Anda:

# $ export DATABASE_URL="{connection-string}"
# Di mana {connection-string}string koneksi yang Anda salin sebelumnya.

# Aplikasi menggunakan string koneksi yang disimpan ke DATABASE_URLvariabel lingkungan untuk terhubung ke klaster Anda dan menjalankan kode.

# Jalankan kode:

# $ cd hello-world-python-psycopg2
# $ python example.py
# Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:

"""
Balances at Thu Aug  4 15:51:03 2022:
account id: 2e964b45-2034-49a7-8ab8-c5d0082b71f1  balance: $1000
account id: 889cb1eb-b747-46f4-afd0-15d70844147f  balance: $250
Balances at Thu Aug  4 15:51:03 2022:
account id: 2e964b45-2034-49a7-8ab8-c5d0082b71f1  balance: $900
account id: 889cb1eb-b747-46f4-afd0-15d70844147f  balance: $350
"""