Teori workshop pertemuan 3

Struktur Data

5.1 Struktur Data Pada Python
Struktur data adalah cara untuk menyimpan dan mengorganisasi data dalam suatu program komputer. Di Python, ada beberapa tipe struktur data yang umum digunakan, antara lain:
1.	Lists: tipe data yang berisi kumpulan nilai atau objek yang diurutkan dan dapat diakses menggunakan indeks.
2.	Tuples: tipe data yang mirip dengan lists, tetapi bersifat immutable (tidak dapat diubah setelah dibuat).
3.	Sets: tipe data yang berisi kumpulan nilai yang tidak memiliki urutan dan tidak dapat memiliki elemen yang duplikat.
4.	Dictionaries: tipe data yang terdiri dari kumpulan pasangan key-value yang diindeks oleh key.
Setiap jenis struktur data ini memiliki metode dan fungsi yang berbeda-beda untuk memanipulasi dan mengakses datanya. Memahami struktur data pada Python adalah penting untuk membuat program yang efektif dan efisien.
Terdapat beberapa method list objek yang tersedia, yaitu :
list.append, list.extend, list.insert, list remove, list.pop, list.clear, list.index, list.count, list.sort, list.reverse, dan list.copy.

5.2 Statement Del pada python
Statement del merupakan sebuah keyword pada Python yang digunakan untuk menghapus sebuah objek dari memori komputer. Objek yang dapat dihapus menggunakan del antara lain variabel, list, tuple, set, dictionary, atau bahkan fungsi.
Penggunaan del harus dilakukan dengan hati-hati, karena objek yang dihapus dengan del tidak dapat dipulihkan dan akan mengosongkan memori yang digunakan oleh objek tersebut. Oleh karena itu, pastikan untuk hanya menghapus objek yang tidak diperlukan lagi atau yang tidak akan digunakan dalam program.

5.3 Tuples dan Sequence pada Python
Tuple pada Python adalah salah satu jenis tipe data sekuen yang digunakan untuk menyimpan sekumpulan nilai yang tidak dapat diubah setelah didefinisikan. Dalam Python, tuple ditulis dengan tanda kurung () dan elemen-elemennya dipisahkan dengan koma.
Sequence pada Python adalah tipe data yang dapat menyimpan sekumpulan nilai yang diurutkan. Selain tuple, tipe data sequence lainnya adalah list dan range. Tipe data sequence dapat diindeks dan di-slicing seperti halnya list.
Perbedaan utama antara tuple dan list adalah tuple bersifat immutable, artinya elemen-elemennya tidak dapat diubah setelah didefinisikan, sedangkan list bersifat mutable, artinya elemen-elemennya dapat diubah setelah didefinisikan.
Pada dasarnya, tipe data sequence pada Python digunakan untuk menyimpan data yang diurutkan, sehingga memudahkan dalam melakukan pengolahan data seperti sorting, searching, dan filtering.

5.4 Sets pada Python
Sets pada Python adalah salah satu jenis tipe data koleksi yang digunakan untuk menyimpan sekumpulan nilai unik (tidak ada duplikat) dalam urutan yang tidak terdefinisi. Sets dalam Python ditulis dengan tanda kurung kurawal atau brace {} dan elemen-elemennya dipisahkan dengan koma.
Set memiliki beberapa sifat atau karakteristik sebagai berikut:
1.	Set hanya dapat menyimpan nilai unik, sehingga jika terdapat nilai duplikat, hanya akan disimpan satu kali.
2.	Set tidak memiliki indeks, sehingga tidak dapat diakses menggunakan indeks.
3.	Set bersifat mutable, artinya elemen-elemennya dapat ditambahkan atau dihapus setelah dibuat.
4.	Set mendukung operasi matematika seperti union, intersection, difference, dan symmetric difference.
Sets pada Python sering digunakan untuk menghilangkan nilai duplikat pada sebuah list atau sequence, dan untuk melakukan operasi matematika pada himpunan seperti penggabungan, irisan, atau selisih.

5.5 Dictionaries pada Python
Dictionary pada Python adalah salah satu jenis tipe data koleksi yang digunakan untuk menyimpan pasangan key-value atau kunci-nilai dalam urutan yang tidak terdefinisi. Dalam Python, dictionary ditulis dengan tanda kurung kurawal atau brace {} dan pasangan key-value dipisahkan dengan tanda titik dua : dan koma.
Setiap key pada dictionary harus unik dan hanya dapat terdiri dari tipe data yang tidak dapat diubah seperti string atau tuple. Sedangkan nilai atau value pada dictionary dapat berupa tipe data apapun, termasuk list, tuple, atau bahkan dictionary lain.
Dictionary pada Python bersifat mutable, artinya elemen-elemennya dapat ditambahkan atau dihapus setelah dibuat. Selain itu, dictionary juga mendukung operasi-operasi seperti pencarian nilai berdasarkan key, penghapusan elemen berdasarkan key, atau pengulangan untuk mendapatkan seluruh pasangan key-value pada dictionary.
Dictionary pada Python sering digunakan untuk menyimpan data yang memerlukan akses berdasarkan kunci (key) yang unik dan tidak terurut. Contohnya adalah data mahasiswa dengan NIM sebagai kunci dan data yang berkaitan sebagai nilai, atau data produk dengan kode produk sebagai kunci dan data produk lainnya sebagai nilai.

Apa yang membedakan Sequence dengan Objek yang lain?
Sequence pada Python adalah salah satu jenis tipe data koleksi yang digunakan untuk menyimpan sekumpulan nilai dalam urutan tertentu, seperti list, tuple, dan string. Yang membedakan sequence dengan objek lain adalah kemampuannya untuk diakses menggunakan indeks. Setiap elemen dalam sequence memiliki indeks yang unik, dimulai dari 0 untuk elemen pertama, 1 untuk elemen kedua, dan seterusnya.

Selain itu, sequence pada Python juga memiliki sifat yang berbeda dengan tipe data koleksi lainnya, seperti set dan dictionary. Sequence bersifat terurut, artinya urutan elemen dalam sequence dapat diprediksi dan dikontrol. Sementara itu, set dan dictionary tidak bersifat terurut dan elemen-elemennya tidak memiliki indeks.