
  
  
## Tujuan Laprak:
- Modul 10: 1. Mahasiswa dapat menginvestigasi cara kerja protokol IP menggunakan Wireshark.
  
----------------------------------------------------------------------------------------------------------------------------------
  
## 10.1 Pengantar
  
Di modul ini, kita akan mempelajari protokol IP yang terkenal, dengan fokus pada datagram IPv4 dan IPv6. Modul ini memiliki tiga bagian. Pada bagian pertama, kita akan menganalisis paket dalam jejak datagram IPv4 yang dikirim dan diterima oleh program traceroute (program traceroute itu sendiri dieksplorasi lebih detail di lab Wireshark ICMP). Kita akan mempelajari fragmentasi IP di bagian 2 modul ini, dan melihat sekilas IPv6 di bagian 3 modul ini.
  
## Langkah-langkah Modul 10
  
### 10.1.1 IP Address
IP address itu merupakan alamat unik yang digunakan oleh setiap device untuk dapat saling terhubung dalam suatu jaringan sehingga mereka dapat saling berkomunikasi satu sama lain. berikut contoh dibawah ini merupakan contoh implementasi untuk melakukan pengecekan IP melalui terminal menggunakan syntax "ipconfig" di CMD. Terlihat seperti dibawah ini ip saat ini sedang mendapatkan langsung dari akses point atau DHCP langsung dari ONT. <img width="607" height="610" alt="Cuplikan layar 2026-06-25 142435" src="https://github.com/user-attachments/assets/3974f5c9-f7da-4fef-816d-edae7137d754" />

  
## 10.2 Menangkap paket dari eksekusi traceroute
  
Untuk menghasilkan jejak datagram IPv4 untuk bagian pertama modul ini, kita akan menggunakan program traceroute untuk mengirim datagram ke gaia.cs.umass.edu menggunakan syntax "tracert gaia.cs.umass.edu ".
<img width="833" height="582" alt="Cuplikan layar 2026-06-25 142515" src="https://github.com/user-attachments/assets/c77307f9-32cb-46fb-b78f-2a3c8c5fd4e1" />

  
### 10.2.1 ICMP, MTU dan TTL
  
- ICMP (Message Control Protocol)
    protokol jaringan yang digunakan untuk mengirim pesan kontrol dan informasi kesalahan pada jaringan IP.
- MTU (Maximum Transmission Unit)
    Ukuran maksimum data yang dapat dikirim dalam satu paket/frame tanpa fragmentasi. Pada Ethernet umumnya 1500 byte.
- TTL (Time To Live)
    Batas jumlah hop/router yang dapat dilewati paket. Setiap router mengurangi TTL sebesar 1. Jika TTL mencapai 0, paket dibuang untuk mencegah routing loop.
  
Pertama buka file abc wireshark capture
<img width="833" height="760" alt="Cuplikan layar 2026-06-25 142533" src="https://github.com/user-attachments/assets/2434336b-a215-405e-a8a5-9f343a861921" />

  
Lalu gunakan filter "icmp", disini ttlnya bernilai 1 pada paket pertama.
<img width="838" height="255" alt="Cuplikan layar 2026-06-25 142555" src="https://github.com/user-attachments/assets/5581c46b-f86a-49a8-8824-0e35589b8514" />

  
Pada paket kedua, ttlnya bernilai 11.
<img width="765" height="329" alt="Cuplikan layar 2026-06-25 142703" src="https://github.com/user-attachments/assets/ff94fd51-169b-4812-892e-e310f4d08647" />

<img width="839" height="276" alt="Cuplikan layar 2026-06-25 142712" src="https://github.com/user-attachments/assets/e91ecfda-54b8-4f55-af26-95dbc205b64b" />

  
### 10.2.2 Fragmentasi
  
Selanjutnya adalah memuat contoh untuk fragmentasi dalam wireshark dengan menggunakan fitur filter "ip.frag_offset>0".Bisa dilihat bawah tidak ada fragmentasi yang offset.
![Fragmentasi - 00](../assets/image/week10-07.png)
  
Untuk menampilkan fragmentasi yang offset, kita bisa menggunakan perintah "ping 8.8.8.8 -l 4000" untuk memaksa kita mengirimkan 4000 bytes.
<img width="765" height="329" alt="Cuplikan layar 2026-06-25 142703" src="https://github.com/user-attachments/assets/681010f1-c463-4963-82d4-f153bf198de1" />

  
Lalu kita jalankan perintah "ip.flags.mf == 1" untuk fragmentasi 1 dan 2.
<img width="839" height="276" alt="Cuplikan layar 2026-06-25 142712" src="https://github.com/user-attachments/assets/9531ec4e-e5ef-4c18-aa9a-3219643a2649" />

  
lalu kita jalankan perintah "ip.frag_offset > 0" untuk menampilkan fragmentasi 2 dan 3, fragmentasi 1 tidak ditampilkan karena offset fragmentasi 1 selalu 0.

  <img width="822" height="288" alt="Cuplikan layar 2026-06-25 142723" src="https://github.com/user-attachments/assets/03cdc3c3-074d-422c-b948-a8b1fc2a92ab" />

### 10.2.3 Bagian 3: IPv6
  
Buka file ipv6_sample.pacp di wireshark lalu gunakan filter "ipv6" karena device ssaya tidak menggunakan IPV6 tapi menggunakan IPV4.
<img width="826" height="309" alt="Cuplikan layar 2026-06-25 142739" src="https://github.com/user-attachments/assets/edac68c7-e1e9-4191-b4a8-23410af995da" />


