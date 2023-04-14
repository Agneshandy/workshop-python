Module

Dalam Python, sebuah modul adalah sebuah berkas yang berisi kode Python, biasanya dengan ekstensi berkas “.py”, yang mendefinisikan fungsi, kelas, dan variabel yang dapat digunakan di program Python lainnya.
Modul digunakan untuk mengorganisir kode ke dalam blok yang dapat digunakan kembali dan meningkatkan keamanan kode. Modul memungkinkan para programmer untuk memecah program besar menjadi bagian-bagian yang lebih kecil
dan dapat diembangkan, diuji, dan dikelola secara terpisah.
Untuk menggunakan modul di Python, pengguna dapat mengimportnya ke dalam program dengan menggunakan pernyataan import. Sebagai contoh, jika pengguna memiliki modul yang bernama math_functions.py yang berisi beberapa fungsi
yang berhubungan dengan matematika.

Modul di Python dapat berisi pernyataan yang dapat dijalankan dan definisi fungsi yang hanya diinisialisasi saat nama modul pertama kali ditemukan dalam pernyataan import. Setiap modul memiliki namespace sendiri yang digunakan
sebagai namespace global oleh semua fungsi yang didefinisikan di dalam modul. Modul juga dapat mengimport modul lain, dan nama modul yang diimport ditambahkan ke namespace global modul tersebut. Selain itu, ada variasi dari
pernyataan import yang mengimport nama langsung ke dalam namespace modul yang mengimport.

“Compiled” Python Files
File Python yang sudah dikompilasi (compiled Python files) adalah file dengan ekstensi .pyc atau .pyo yang berisi bytecode yang sudah dikompilasi dari file sumber Python. Bytecode ini dapat dieksekusi lebih cepat daripada
menginterpretasikan kode sumber aslinya. Interpreter Python akan memeriksa dan memuat file bytecode yang sudah ada, jika lebih baru daripada file sumber, untuk menghemat waktu dan meningkatkan performa. Proses pembuatan file
bytecode sudah dikompilasi berjalan secara otomatis dan transparan bagi pengguna.

Standard Module in Python
Modul standar dalam Python mengacu pada modul bawaan yang disertakan dalam instalasi Python dan dapat digunakan dalam program Python tanpa memerlukan instalasi atau pengaturan tambahan.
Modul-modul ini menyediakan berbagai fungsi yang dapat digunakan untuk mengembangkan aplikasi Python, beberapa fungsi tersebut seperti :
- os: memiliki fungsi yang terkait sistem operasi seperti manipulasi file dan direktori, manajemen proses, dll.
- sys: untuk mengakses parameter dan fungsi khusus sistem.
- math: untuk fungsi dan konstanta matematika.
- random: untuk menghasilkan angka acak dan memilih elemen acak dari urutan.
- datetime: untuk bekerja dengan tanggal dan waktu.
- urllib: untuk mengakses URL dan mengunduh data dari internet.
- json: untuk bekerja dengan data JSON.
- re: untuk bekerja dengan ekspresi reguler.
- argparse: untuk mem-parsing argumen baris perintah.

“Dir” function in Python
Fungsi dir() di Python memunculkan daftar nama-nama yang didefinisikan dalam cakupan lokal atau dalam cakupan objek tertentu. Hal ini dapat digunakan untuk melihat fungsi dan atribut yang tersedia dalam sebuah modul
atau metode yang tersedia dalam sebuah objek. Fungsi ini hanya mengembalikan nama objek dan tidak memberikan informasi tentang cara menggunakan objek tersebut. Untuk informasi lebih lanjut mengenai informasi tersebut, maka dapat digunaakan fungsi help().

Packages in Python
Di Python, package adalah cara untuk mengorganisir modul dan paket terkait ke dalam satu namespace yang sama, sehingga lebih mudah untuk menemukannya dan menggunakannya.
Sebuah package adalah direktori yang berisi satu atau beberapa modul, bersama dengan file khusus yang disebut __init__.py, yang dieksekusi ketika paket diimpor. File __init__.py dapat kosong atau berisi kode Python
yang menginisialisasi paket dan mendefinisikan nama-nama yang akan tersedia bagi pengguna ketika paket diimport.
