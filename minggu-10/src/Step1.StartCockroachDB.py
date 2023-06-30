#Use CockroachDB Serverless
"""
1. Jika Anda belum melakukannya, daftar akun Cloud CockroachDB.
2. Masuk ke akun Cloud CockroachDB Anda.
3. Di laman Gugus, klik Buat Gugus.
4. Di laman Buat kluster Anda, pilih Tanpa Server.
5. Klik Buat kluster.

Cluster Anda akan dibuat dalam beberapa detik dan dialog Create SQL user akan ditampilkan.

**Buat pengguna SQL**
Dialog Buat pengguna SQL memungkinkan Anda membuat pengguna dan kata sandi SQL baru.
1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik Buat & simpan kata sandi.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.
4. Klik Berikutnya.

Saat ini, semua pengguna SQL baru dibuat dengan hak admin. Untuk informasi selengkapnya dan untuk mengubah pengaturan default, lihat [ Kelola pengguna SQL di kluster .

**Dapatkan sertifikat root**
Dialog Sambungkan ke klaster menampilkan informasi tentang cara menyambungkan ke klaster Anda.
1. Pilih string koneksi Umum dari dropdown Pilih opsi.
2. Buka terminal baru di mesin lokal Anda, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.

**Dapatkan string koneksi**
Buka bagian String koneksi umum , lalu salin string koneksi yang disediakan dan simpan di lokasi yang aman.
"""

"""
Catatan: 
String koneksi sudah diisi sebelumnya dengan nama pengguna, kata sandi, nama cluster, dan detail lainnya.
Kata sandi Anda, khususnya, hanya akan diberikan sekali . 
Simpan di tempat yang aman (Cockroach Labs merekomendasikan pengelola kata sandi) untuk terhubung ke cluster Anda di masa mendatang. 
Jika Anda lupa kata sandi, Anda dapat mengatur ulang dengan membuka halaman Pengguna SQL.
"""

#Use a Local Cluster
"""
1. Jika Anda belum melakukannya, unduh binary CockroachDB .
2. Jalankan cockroach start-single-nodeperintah:
"""
# $ cockroach start-single-node --advertise-addr 'localhost' --insecure

"""
3. Catat informasi koneksi berikut dalam teks selamat datang SQL shell:
CockroachDB node starting at 2021-08-30 17:25:30.06524 +0000 UTC (took 4.3s)
build:               CCL v21.1.6 @ 2021/07/20 15:33:43 (go1.15.11)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257?sslmode=disable
"""

"""
Peringatan:
Bendera --insecureyang digunakan dalam tutorial ini hanya ditujukan untuk pengujian non-produksi. Untuk menjalankan CockroachDB dalam produksi, gunakan cluster yang aman sebagai gantinya.
"""