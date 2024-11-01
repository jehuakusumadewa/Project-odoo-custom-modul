# Modul Pemesanan Ruangan

Modul Odoo ini dirancang untuk mengelola pemesanan ruangan secara efektif, mencakup pengaturan master ruangan dan pemesanan ruangan dengan validasi untuk memastikan tidak ada konflik dalam pemesanan ruangan.

## Fitur
1. **Master Ruangan**:
   - Menyimpan informasi tentang ruangan, seperti nama ruangan, tipe ruangan, lokasi, kapasitas, foto, dan deskripsi.
   - Validasi untuk memastikan bahwa setiap nama ruangan unik.

2. **Pemesanan Ruangan**:
   - Menyimpan informasi pemesanan ruangan, termasuk nomor pemesanan otomatis yang terdiri dari tipe pemesanan, tipe ruangan, tanggal, dan sequence unik.
   - Mengelola detail pemesanan seperti nama pemesan, ruangan yang dipesan, tanggal pemesanan, status pemesanan, dan catatan tambahan.
   - Tombol untuk memproses status pemesanan, dari **Draft** ke **On Going** hingga **Done**.
   - Validasi untuk memastikan tidak ada pemesanan pada ruangan dan tanggal yang sama.

## Instalasi

1. **Clone repository ini ke dalam folder `addons` Odoo Anda**:
    ```bash
    git clone  https://github.com/jehuakusumadewa/Project-odoo-custom-modul.git
    ```
2. **Update konfigurasi addons_path pada odoo**:
    - masukkan path clone `contoh` seperti ini `D:\odoo16\dev`.
      
3. **buka di code editor dan jalankan diterminal**:
    ```bash
    python odoo-bin -c odoo_config.CONF
    ```
4. **Update list modul Odoo**:
    - Masuk ke menu `Apps` dalam Odoo, dan klik **Update Apps List** untuk memperbarui daftar modul.

5. **Install Modul**:
    - Cari modul `Pemesanan Ruangan` di halaman Apps, kemudian klik **Install**.

## Penggunaan

1. **Master Ruangan**:
   - Akses menu `Master Ruangan` untuk melihat daftar ruangan yang tersedia.
   - Anda dapat menambahkan ruangan baru dengan mengisi informasi seperti nama, tipe, lokasi, foto, kapasitas, dan deskripsi.

2. **Pemesanan Ruangan**:
   - Akses menu `Pemesanan Ruangan` untuk membuat pemesanan baru.
   - Isi nama pemesanan, pilih ruangan, dan tentukan tanggal pemesanan.
   - Simpan pemesanan, lalu proses statusnya menggunakan tombol **Process** untuk mengubah status menjadi **On Going** atau **Done** sesuai kebutuhan.

## Validasi

- **Nama Pemesanan**: Harus unik, tidak boleh sama dengan pemesanan lain yang sudah ada.
- **Nama Ruangan**: Setiap nama ruangan harus unik dalam data master ruangan.
- **Ruangan dan Tanggal Pemesanan**: Tidak boleh ada pemesanan yang memiliki ruangan dan tanggal yang sama.

## Pengembang

- **Nama Pengembang**: Jehua Kusuma Dewa
- **Email**: docjehua22@gmail.com

## Lisensi

Modul ini berlisensi [MIT License](LICENSE).
