PEP 249
Python Enhancement Proposal 249 atau yang biasa dikenal dengan PEP 249 adalah suatu API database yang berada pada Python yang merupakan suatu interface dasar untuk berinteraksi dengan database relasional menggunakan Python.
Tujuan Utama dari PEP 249 adalah sebagai penyedia antarmuka yang seragam sehingga memungkinkan program Python terhubung ke berbagai sistem yang mengelola database seperti MySQL, PostgreSQL, SQLite, Oracle, dll.
Pada API PEP 249, serangkaian metode didefinisikan sehingga sesuai dengan modul pada database. Beberapa komponen utama dari API ini yaitu :
• Connection Objects : yaitu sebuah objek yang digunakan untuk menghubungkan dengan database dan mengelola data transfer.
• Cursor Object : Digunakan untuk menjalankan statement SQL dan mengambil hasil dari database.
• Error Handling : Yaitu sebuah objek yang digunakan untuk mendefinisikan serangkaian kelas untuk menangani error yang mungkin terjadi selama pengoperasian.

Psycopg
Psycopg adalah sebuah modul Python yang menyediakan interface untuk berinteraksi dengan database PostgreSQL. Modul ini juga mengimplementasikan PEP 249 API yang sebelumnya pernah dibahas pada materi PEP 249. Hal ini membuat operasi seperti koneksi ke database, menjalankan statement SQL, mengambil hasil, dan sebagainya dapat dilakukan.
Psycopg dirancang agar menjadi modul yang efisien, mudah digunakan, dan kompatibel dengan standar DB-API. Pengembang Python dapat dengan mudah berkomunikasi dengan database PostgreSQL dengan menggunakan Psycopg dan perintah perintah simpel Python.
Bebarapa fitur dan keunggulan Psycopg diantaranya :
• Mendukung fitur-fitur khusus PostgreSQL: Psycopg memungkinkan penggunaan fitur-fitur khusus dari PostgreSQL, seperti tipe data kompleks (array, JSON, HSTORE).
• Performa yang baik: Psycopg dirancang untuk memberikan kinerja yang baik dan efisien saat berinteraksi dengan database PostgreSQL.
• Koneksi yang aman: Psycopg menyediakan dukungan untuk koneksi yang aman ke database PostgreSQL melalui SSL/TLS.

Mongo Python Driver
Mongo Python Driver adalah modul Python resmi yang disediakan oleh MongoDB yang digunakan untuk berinteraksi dengan database MongoDB menggunakan bahasa pemrograman Python. Driver ini menyediakan interface yang compact untuk melakukan operasi pada database MongoDB, seperti menyambungkan ke server MongoDB, menjalankan query, mengubah data, dan mengelola indeks.
Driver ini juga mendukung fitur-fitur yang berada pada MongoDB, seperti :
• Koneksi ke server MongoDB: Driver ini memungkinkan pengguna untuk membuat koneksi ke server MongoDB, baik melalui URI koneksi atau menggunakan parameter host dan port.
• Operasi CRUD: Driver menyediakan metode untuk melakukan operasi Create, Read, Update, dan Delete (CRUD) pada MongoDB collection.
• Indeks: Driver memungkinkan pengguna untuk membuat, mengelola, dan menggunakan indeks di collection pada MongoDB. Indeks dapat meningkatkan kinerja query dengan mempercepat pencarian dan pengurutan data.

SQLAlchemy
SQLAlchemy adalah sebuah library Python bersifat Open Source yang menyediakan toolkit Object-Relational Mapping (ORM) tingkat tinggi dan sejumlah utilitas untuk bekerja dengan database. Ini membuat interaksi dengan database menjadi lebih sederhana dengan mengabstraksi sintaks SQL dan memungkinkan pengembang untuk bekerja dengan objek database sebagai objek Python.
