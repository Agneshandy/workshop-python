BAB 8. Errors and Exceptions (Kesalahan errors dan Pengecualian exceptions)

Syntax Error pada Python
Kesalahan sintaks dalam Python terjadi ketika baris kode tidak sesuai dari struktur bahasa Python. Kesalahan ini terindikasi oleh Python sebelum kode dieksekusi.
Kesalahan sintaks tersebut mencegah kode dieksekusi dan umumnya menghasilkan pesan error yang menyoroti yang dimana baris kode yang salah diberitahu.

Exceptions pada Python
Exceptions pada Python adalah jenis kesalahan atau kondisi yang terjadi saat program sedang dieksekusi. Mereka menunjukkan kondisi yang dimana kode tersebut perlu diperbaiki.
Ketika sebuah exception muncul, maka alur dari program tersebut tidak berjalan baik, dan eksekusi beralih ke bagian kode yang ditujukan untuk menangani exception tersebut.

Handling Exceptions pada Python
Handling Exceptions dalam Python adalah proses yang menangani exception yang muncul saat program dieksekusi. Dengan menggunakan mekanisme penanganan exception,
kita dapat mengontrol alur program dan memberikan tindakan atau alur baru yang sesuai ketika exception terjadi, sehingga program tetap dapat berjalan dengan lancar dan mengatasi tersebut.

User-Defined Exceptions pada Python
User-Defined exceptions pada Python yaitu sebuah kemampuan untuk membuat dan mendefinisikan exception khusus yang sesuai dengan kebutuhan dan logika program yang sedang dibuat.
Dengan User-Defined exception, programmer dapat membuat jenis exception baru yang menggunakan kembali kelas exception bawaan Python atau kelas exception lain yang sudah ada.

Define Clean-up Actions pada Python
Tindakan pembersihan (clean up actions) adalah statement dalam sebuah program yang dieksekusi. Pernyataan-pernyataan ini dieksekusi bahkan jika terjadi kesalahan dalam program.
Jika programmer telah menggunakan handling exception dalam programnya, statement ini tetap dieksekusi. Jadi, pada dasarnya dapat dikatakan bahwa jika programmer menginginkan suatu bagian tertentu
selalu berjalan, dapat digunakan clean-up.
Dalam Python, baris kode finally digunakan untuk menentukan bagian dari kode yang akan dieksekusi setiap kali program dijalankan. Artinya, setiap baris kode di bawah finally adalah tindakan pembersihan (clean up action).
