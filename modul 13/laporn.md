
  
  
## Tujuan Laprak:
- Modul 13: 1. Mahasiswa dapat menginvestigasi cara kerja Ethernet dan ARP menggunakan Wireshark.
  
----------------------------------------------------------------------------------------------------------------------------------
  
## 13.1 Pengantar
  
Di lab ini, kami akan menyelidiki protokol Ethernet dan protokol ARP. RFC 826 (ftp://ftp.rfceditor.org/in-notes/std/std37.txt) berisi detail mengerikan dari protokol ARP, yang digunakan oleh perangkat IP untuk menentukan alamat IP dari antarmuka jarak jauh yang alamat Ethernetnya diketahui.
  
## Langkah-langkah Modul 13
  
Buka CMD sebagai Administrator, lalu ketik syntax "arp -d *".
<img width="443" height="204" alt="week13-00" src="https://github.com/user-attachments/assets/38e3d65e-c4b0-4ce7-8240-b9e280d6352b" />

  
Kemudian buka Wireshark, klik Analyze, klik Enabled Protocols.
<img width="758" height="561" alt="week13-01" src="https://github.com/user-attachments/assets/d5870f02-b464-49be-8c07-8b0c42cad2d5" />

  
Lalu cari IPv4, kemudian unchecklist, lalu klik ok.
<img width="902" height="730" alt="week13-02" src="https://github.com/user-attachments/assets/90b5cefa-91ff-4a2d-b5ea-7eea09089084" />
<img width="1223" height="763" alt="week13-03" src="https://github.com/user-attachments/assets/4f11cdd3-b388-4a1c-a5e0-bf38f8c7832c" />

  
Lalu buka modul dan salin URL berikut: [Bill of Right AS](http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html), kemudian akan menampilkan tampilan seperti dibawah ini:

  <img width="1916" height="961" alt="week13-04" src="https://github.com/user-attachments/assets/a0a56d7e-ea72-4cdc-b050-c9d99ce83a17" />

Kemudian kembali ke Wireshark dan klik stop.
<img width="1165" height="613" alt="week13-05" src="https://github.com/user-attachments/assets/2d14fabc-28e4-441f-9e21-8d9f343bd25b" />

  
Gunakan filter "arp" untuk mencari protocol ARP, disini terdapat 2 packet protocol ARP dan salah satunya destination berupa Broadcast, dapat dilihat disini bahwa arp akan bertanya seperti siapa yang punya ip 10.211.192.1? beritau pada 10.211.240.9 agar dapat berkomunikasi lebih lanjut, kita juga dapat melihat semua alamat MAC yang tersedia.
<img width="1365" height="419" alt="week13-06" src="https://github.com/user-attachments/assets/2c8f684b-e911-4e7e-9d97-6942c25b0dfd" />
