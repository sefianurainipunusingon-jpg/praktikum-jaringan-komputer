# Modul 12 - ICMP dan ICMP Pinger

## Tujuan Praktikum

1. Memahami cara kerja protokol ICMP menggunakan Wireshark.
2. Membuat program sederhana ICMP Pinger.
3. Melakukan asistensi serta melaporkan progres pengerjaan tugas besar.

---

## 12.1 Pengantar

Internet Control Message Protocol (ICMP) merupakan protokol yang digunakan untuk mengirimkan pesan kontrol dan informasi kesalahan pada jaringan komputer. ICMP bekerja bersama protokol IP dan berfungsi membantu proses diagnosis serta pemantauan kondisi jaringan.

Pada praktikum ini dilakukan pengamatan terhadap paket ICMP yang dihasilkan oleh perintah **Ping** dan **Traceroute** menggunakan aplikasi Wireshark.

ICMP umumnya digunakan untuk:

1. Memeriksa ketersediaan host pada jaringan.
2. Mengetahui jalur (hop) yang dilewati paket.
3. Mengirimkan informasi error atau gangguan jaringan.

Hubungan antara IP dan ICMP adalah pesan ICMP dikirim sebagai payload di dalam paket IP.

---

## 12.2 Pengamatan Pesan ICMP dari Ping

Langkah pertama adalah membuka Command Prompt kemudian menjalankan perintah:

```bash
ping -n 10 8.8.8.8
```

Parameter **-n 10** digunakan untuk mengirimkan 10 paket Echo Request ke alamat tujuan. Jika koneksi berjalan normal maka akan diterima 10 Echo Reply tanpa adanya pesan *Request Timed Out*.

Setelah itu dilakukan pengujian ke domain lain menggunakan perintah:

```bash
ping -n 10 www.ust.hk
```

Hasil pengujian menunjukkan bahwa host tujuan dapat diakses dan menghasilkan balasan dari server tujuan.

Ketika proses tersebut diamati menggunakan Wireshark dengan filter **icmp**, terlihat paket **Echo Request** dan **Echo Reply** yang saling berpasangan. Jika dikirim 10 kali ping, maka akan muncul sekitar 20 paket, terdiri dari 10 paket request dan 10 paket reply.

---

## 12.3 Pengamatan Pesan ICMP dari Traceroute

Traceroute digunakan untuk mengetahui jalur yang dilalui paket dari komputer sumber menuju tujuan.

Perintah yang digunakan adalah:

```bash
tracert www.ust.hk
```

Traceroute bekerja dengan mengirim paket menggunakan nilai TTL yang meningkat secara bertahap. Paket pertama dikirim dengan TTL=1, paket kedua TTL=2, dan seterusnya.

Setiap router yang dilewati akan mengurangi nilai TTL. Jika TTL mencapai nol, router akan mengirimkan pesan ICMP *Time Exceeded* ke pengirim. Dengan cara ini, setiap hop yang dilewati paket dapat diketahui.

Untuk mengamati proses tersebut, Wireshark dijalankan dan filter **icmp** diterapkan sehingga seluruh paket ICMP dapat terlihat selama proses traceroute berlangsung.

---

## 12.4 Struktur Header ICMP

| Field          | Panjang  | Fungsi                                                           |
| -------------- | -------- | ---------------------------------------------------------------- |
| Type           | 8 bit    | Menunjukkan jenis pesan ICMP.                                    |
| Code           | 8 bit    | Memberikan informasi tambahan terkait Type.                      |
| Checksum       | 16 bit   | Memverifikasi integritas paket selama transmisi.                 |
| Rest of Header | 32 bit   | Berisi informasi tambahan yang bergantung pada jenis pesan ICMP. |
| Data           | Variabel | Berisi payload atau informasi yang dikirimkan.                   |

---

## Kesimpulan

Berdasarkan praktikum yang dilakukan, dapat disimpulkan bahwa ICMP berperan penting dalam proses diagnosis jaringan. Perintah Ping digunakan untuk menguji konektivitas antara host, sedangkan Traceroute digunakan untuk mengetahui jalur yang dilewati paket data. Dengan bantuan Wireshark, paket ICMP seperti Echo Request, Echo Reply, dan Time Exceeded dapat diamati secara langsung sehingga memudahkan pemahaman mengenai cara kerja komunikasi jaringan.

