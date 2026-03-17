

---

**Langkah 1: Awal Mula Proses (Request dari Client)**
Pada gambar Wireshark terlihat bahwa komputer client dengan IP 10.218.8.148 mengirimkan permintaan ke server dengan IP 199.232.210.172 menggunakan metode GET. Permintaan ini bertujuan untuk mengambil file dari server melalui protokol HTTP. Proses ini disebut sebagai HTTP Request, di mana client meminta data tertentu kepada server.

---

**Langkah 2: Respon Server (403 Forbidden)**
Setelah menerima permintaan dari client, server memberikan respon berupa HTTP/1.1 403 Forbidden. Hal ini menunjukkan bahwa server menolak permintaan tersebut. Penolakan ini biasanya terjadi karena client tidak memiliki izin akses, link membutuhkan autentikasi, atau terjadi kesalahan pada parameter permintaan.

---

**Langkah 3: Pengiriman Data Sebagian (206 Partial Content)**
Meskipun sebelumnya terjadi penolakan, pada bagian lain terlihat server mengirimkan respon HTTP/1.1 206 Partial Content. Ini berarti server mengirimkan sebagian data dari file yang diminta. Kondisi ini biasanya terjadi pada proses streaming atau download bertahap, di mana file dikirim tidak sekaligus tetapi dalam beberapa bagian.

---

**Langkah 4: Terjadi Retransmission**
Pada salah satu paket terlihat adanya TCP Retransmission. Ini menandakan bahwa ada paket data yang sebelumnya gagal diterima oleh client, sehingga server mengirim ulang paket tersebut. Hal ini bisa terjadi karena gangguan jaringan atau kehilangan paket saat transmisi.

---

**Langkah 5: Kesimpulan Proses**
Dari hasil analisis tersebut dapat disimpulkan bahwa proses komunikasi dimulai dari client yang mengirim request, kemudian server memberikan respon baik berupa penolakan maupun pengiriman data sebagian. Selain itu, adanya retransmission menunjukkan bahwa komunikasi jaringan tidak selalu sempurna dan bisa mengalami gangguan.

