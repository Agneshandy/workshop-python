Virtual Environment dan Packages

Pengertian dari Virtual Environment dan Packages, dan cara membuatnya.
Virtual environment adalah sebuah alat untuk menjaga ruang terpisah yang digunakan sebagai sebuah proyek dengan pustaka dan dependensi di satu tempat. Environment ini spesifik ke proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya.
Paket-paket, dalam konteks Python, merujuk pada kumpulan modul dan skrip yang telah dikemas bersama-sama untuk memberikan fungsionalitas tambahan. Paket-paket ini dapat berisi script code Python, file konfigurasi, data, dan sumber daya lainnya yang diperlukan oleh program atau proyek yang lebih besar.
Cara untuk membuat Virtual Environment tersebut adalah dengan cara sebagai berikut :
1. Buat Folder untuk proyek, misalnya python-dasar bisa dengan command mkdir python-dasar atau dari jendela lebih mudah
2. Masuk kedalam folder yang dibuat tadi cd python-dasar
3. Membuat virtualenv dengan nama env perintahnya python3 -m venv env
4. Selesai tanpa error, akan ada folder baru bernama env didalam folder python-dasar.
5. Aktifkan dengan perintah source env/bin/activate dan untuk menonaktifkan deactivate

Conda 

Conda merupakan sebuah sistem manajemen packages, environment, dan dependency yang dirancang khusus untuk bahas pemrograman Python. Conda adalah alat yang populer dalam dunia yang berhubungan dengan data dan pengembangan perangkat lunak, terutama untuk proyek-proyek yang melibatkan analisis data (Data Analytics) dan pembelajaran mesin (Machine Learning).
Berikut adalah langkah dalam menggunakan Conda :
1. Pada start menu, cari sebuah aplikasi dengan nama "Anaconda Prompt".
2. Kemudian Lakukan verifikasi apakah conda telah terinstall dan berjalan pada system dengan menggunakan perintah "conda --version".
3. Jika terjadi error, maka dapat dilakukan update pada conda yang sedang dijalankan dengan menggunakan perintah "conda update conda"

