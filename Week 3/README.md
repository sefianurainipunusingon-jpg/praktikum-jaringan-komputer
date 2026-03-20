📄 Laporan Praktikum: Analisis Protokol HTTP Menggunakan Wireshark (Versi 2)
3.2 Interaksi Dasar HTTP GET dan Response

Pada bagian ini dilakukan pengamatan terhadap proses komunikasi antara client (browser) dan server melalui protokol HTTP.

Langkah Percobaan
1. Menyiapkan Wireshark

Buka aplikasi Wireshark, lalu masukkan filter http pada kolom filter untuk menampilkan hanya paket HTTP.

2. Melakukan Capture dan Akses Website

Mulai proses capture, kemudian buka browser dan akses URL berikut:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html

3. Mengamati Tampilan Halaman

Browser akan menampilkan halaman sederhana sebagai tanda bahwa file berhasil diambil. Setelah itu, hentikan proses capture.

4. Analisis Paket

Pada Wireshark terlihat adanya permintaan HTTP GET dari client dan balasan HTTP 200 OK dari server.

Hasil Pengamatan

Request Method: GET

Response Status: 200 OK

Client IP: IP perangkat pengguna

Server IP: 128.119.245.12

Kesimpulan

Proses komunikasi HTTP berjalan dengan pola request-response, di mana client meminta data dan server memberikan respon berupa file HTML.

3.2.1 HTTP Conditional GET

Bagian ini membahas bagaimana browser menggunakan cache untuk menghemat bandwidth.

Langkah Percobaan

Menghapus cache browser

Memulai capture di Wireshark

Mengakses URL:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html

Melakukan refresh halaman

Menghentikan capture dan melihat hasil

Analisis
Request Pertama

Server mengirim respon 200 OK beserta isi file.

Request Kedua

Browser mengirim header If-Modified-Since.

Respon Server

Server mengirim 304 Not Modified karena file tidak berubah.

Kesimpulan

Teknik Conditional GET membantu mengurangi penggunaan data karena file tidak dikirim ulang jika belum berubah.

3.3 Pengambilan Dokumen Berukuran Besar

Bagian ini menjelaskan bagaimana HTTP menangani file berukuran besar melalui TCP.

Langkah Percobaan

Menghapus cache

Memulai capture tanpa filter

Mengakses URL:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html

Mengamati paket di Wireshark

Analisis
Segmentasi Data

File besar dipecah menjadi beberapa segmen TCP.

Reassembly

Wireshark menyatukan kembali segmen tersebut menjadi satu data utuh.

Kesimpulan

File besar tidak dikirim sekaligus, tetapi dibagi menjadi beberapa bagian untuk efisiensi transmisi.

3.4 HTML dengan Objek Tambahan

Bagian ini membahas halaman HTML yang memiliki gambar atau objek tambahan.

Langkah Percobaan

Menghapus cache

Memulai capture

Mengakses URL:
http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html

Analisis
Permintaan HTML

Browser meminta file utama HTML.

Permintaan Gambar

Browser otomatis meminta file gambar tambahan.

Respon Server

Semua permintaan dibalas dengan status 200 OK.

Kesimpulan

Satu halaman web dapat terdiri dari banyak file yang diminta secara terpisah oleh browser.

3.5 HTTP Authentication

Bagian ini menjelaskan mekanisme login menggunakan HTTP Basic Authentication.

Langkah Percobaan

Menghapus cache

Memulai capture

Mengakses URL:
http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html

Memasukkan:

Username: wiresharkstudents

Password: network

Analisis
Respon Awal

Server mengirim 401 Unauthorized.

Permintaan Kedua

Browser mengirim ulang request dengan header Authorization.

Respon Akhir

Server mengirim 200 OK jika login berhasil.

Kesimpulan

Autentikasi HTTP membutuhkan dua kali proses komunikasi dan tidak aman jika tanpa HTTPS.

🔚 Penutup

Praktikum ini menunjukkan bagaimana protokol HTTP bekerja dalam berbagai kondisi, mulai dari request sederhana hingga autentikasi, serta peran Wireshark dalam menganalisis lalu lintas jaringan.
