Tur Singkat Perpustakaan Standar Part 1
10.1. Antarmuka Sistem Operasi
	Modul ini os menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi
	Pastikan untuk menggunakan gaya alih-alih . Ini akan mencegah membayangi fungsi bawaan yang beroperasi jauh berbeda
	import osfrom os import *os.open()open()
10.2. File Wildcards
	Modul ini globmenyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori
10.3. Command Line Arguments
	Skrip utilitas umum seringkali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut sysmodul argv sebagai daftar
	Modul ini argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah
10.4. Error Output Redirection and Program Termination
	Modul ini sysjuga memiliki atribut untuk stdin , stdout , dan stderr . Yang terakhir berguna untuk memancarkan peringatan dan pesan
	kesalahan agar terlihat bahkan ketika stdout telah dialihkan
10.5. String Pattern Matching
	Modul ini remenyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut.
	Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug.
10.6. Mathematics
	Modul math memberikan akses ke fungsi library C yang mendasari matematika floating point.
	Modul random menyediakan alat untuk membuat pilihan acak.
	Modul ini statistics menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik.
10.7. Internet Access
	Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request
	untuk mengambil data dari URL dan smtplibuntuk mengirim email.
10.8. Dates and Times
	Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara sederhana dan kompleks.
	Sementara aritmatika tanggal dan waktu didukung, fokus penerapannya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran.
	Modul ini juga mendukung objek yang sadar zona waktu
10.9. Data Compression
	Pengarsipan data umum dan format kompresi didukung langsung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfiledan tarfile.
10.10. Performance Measurement
	Misalnya, mungkin tergoda untuk menggunakan fitur packing dan unpacking tuple daripada pendekatan tradisional untuk bertukar argumen.
	Modul timeit dengan cepat menunjukkan keunggulan kinerja sederhana.
	Berbeda dengan timeit tingkat perincian yang halus, modul profile dan pstats menyediakan alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.
10.11. Quality Control
	Modul doctest menyediakan alat untuk memindai modul dan memvalidasi pengujian yang disematkan dalam dokumen program. Konstruksi pengujian semudah memotong-dan-menempelkan panggilan
	biasa beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap sesuai dengan dokumentasi.
	Modul unittest tidak semudah modul doctest, tetapi memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah.
10.12. Batteries Included
	Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kemampuan canggih dan tangguh dari paket-paketnya yang lebih besar. Misalnya:

	    1. Modul xmlrpc.clientand xmlrpc.servermembuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama modul, tidak diperlukan pengetahuan langsung atau penanganan XML.

	    2. Paket tersebut emailadalah pustaka untuk mengelola pesan email, termasuk MIME dan lainnyaDokumen pesan berbasis RFC 2822 . Tidak sepertismtplibdan poplibyang benar-benar mengirim dan menerima pesan,
	       paket email memiliki perangkat lengkap untuk membangun atau mendekode struktur pesan yang rumit (termasuk lampiran) dan untuk mengimplementasikan protokol penyandian dan header internet.

	    3. Paket ini jsonmemberikan dukungan kuat untuk mem-parsing format pertukaran data populer ini. Modul ini csvmendukung pembacaan dan penulisan file secara langsung dalam format Comma-Separated Value,
               umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh xml.etree.ElementTree, xml.domdan xml.saxpaket. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara
               aplikasi Python dan alat lainnya.

	    4. Modul ini sqlite3adalah pembungkus pustaka database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

	    5. Internasionalisasi didukung oleh sejumlah modul termasuk gettext, locale, dan codecspackage.


Tur Singkat Perpustakaan Standar Part 2
11.1. Output Formatting
	Modul reprlib menyediakan versi yang repr()disesuaikan untuk tampilan singkat wadah besar atau bersarang dalam.
	Modul pprint menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan yang ditentukan pengguna dengan cara yang dapat dibaca oleh juru bahasa.
	Modul textwrap memformat paragraf teks agar pas dengan lebar layar tertentu.
	Modul locale mengakses database format data khusus budaya.
11.2. Templating
	Modul string mencakup kelas serbaguna Templatedengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.
	Metode substitute() memunculkan a KeyErrorsaat placeholder tidak disediakan dalam kamus atau argumen kata kunci.
11.3. Working with Binary Data Record Layouts
	Modul struct menyediakan pack()dan unpack()fungsi untuk bekerja dengan format catatan biner panjang variabel. Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan zipfilemodul.
	Kemas kode "H"dan "I"masing-masing mewakili dua dan empat byte angka yang tidak ditandatangani.
11.4. Multi-threading
	Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima input pengguna saat tugas lain berjalan di latar belakang.
	Kasus penggunaan terkait sedang menjalankan I/O secara paralel dengan perhitungan di utas lainnya.
	Tantangan utama dari aplikasi multi-utas adalah mengoordinasikan utas yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronisasi termasuk kunci, peristiwa, variabel kondisi, dan semaphore.
11.5. Logging
	Modul logging menawarkan sistem logging berfitur lengkap dan fleksibel. Secara default, pesan informasi dan debug disembunyikan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk merutekan pesan melalui email,
	datagram, soket, atau ke Server HTTP. Filter baru dapat memilih perutean yang berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL.
11.6. Weak References
	Modul weakrefmenyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, secara otomatis dihapus dari tabel ref lemah dan panggilan balik dipicu untuk objek ref lemah.
	Aplikasi umum termasuk objek caching yang mahal untuk dibuat.
11.7. Tools for Working with Lists
	Modul array menyediakan array() objek yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih kompak. Contoh berikut menunjukkan larik angka yang disimpan sebagai dua byte bilangan biner
	tak bertanda (typecode "H") daripada 16 byte biasa per entri untuk daftar reguler objek int Python.
	Modul collections menyediakan deque()objek yang seperti daftar dengan penambahan dan kemunculan yang lebih cepat dari sisi kiri tetapi pencarian yang lebih lambat di tengah.
	Modul heapq menyediakan fungsi untuk mengimplementasikan tumpukan berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol.
11.8. Decimal Floating Point Arithmetic
	Modul ini decimal menawarkan Decimaltipe data untuk aritmatika floating point desimal. Dibandingkan dengan implementasi built-in float dari floating point biner, kelas ini sangat membantu.