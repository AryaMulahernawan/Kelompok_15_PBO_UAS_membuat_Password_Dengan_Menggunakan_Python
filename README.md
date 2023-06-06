# Kelompok_15_PBO_UAS_membuat_Password_Dengan_Menggunakan_Python
Program di atas mengimplementasikan konsep OOP (Object-Oriented Programming) dalam bahasa Python. Berikut adalah penjelasan tentang implementasi OOP dalam program tersebut:

Kelas PembuatPassword:

- Kelas ini mewakili objek yang bertanggung jawab untuk membuat password.
- Metode buat_password adalah metode objek yang menerima input panjang password dan kombinasi karakter yang dipilih.
- Metode ini melakukan validasi dan menghasilkan password acak sesuai dengan preferensi pengguna.
- Dalam implementasinya, kelas PembuatPassword mengandalkan metode random.choice() dari library Python untuk menghasilkan karakter acak dari kombinasi karakter yang dipilih.

Kelas GUIPassword:

- Kelas ini mewakili objek yang mengontrol antarmuka pengguna (GUI) untuk aplikasi.
- Konstruktor kelas ini menerima argumen berupa objek PembuatPassword untuk mengakses metode buat_password.
- Metode setup_layout adalah metode objek yang digunakan untuk mengatur tata letak antarmuka pengguna menggunakan library PySimpleGUI.
- Metode setup_callbacks adalah metode objek yang menghubungkan tombol dan peristiwa (event) di antarmuka pengguna dengan fungsi-fungsi yang akan dieksekusi.
- Metode update_password_list digunakan untuk memperbarui daftar password sebelumnya dengan password baru yang dihasilkan.
- Metode copy_selected_password akan menyalin password terpilih ke clipboard pengguna.
- Metode run digunakan untuk menjalankan antarmuka pengguna dengan memanggil metode setup_layout, setup_callbacks, dan window.read() dari library PySimpleGUI.
-Dengan menggunakan pendekatan OOP, program tersebut memisahkan logika pemrosesan password ke dalam kelas PembuatPassword, dan logika antarmuka pengguna ke dalam kelas GUIPassword. Hal ini memungkinkan pengkodean yang lebih terstruktur, memisahkan tanggung jawab, dan memungkinkan kode yang lebih mudah dipelihara. Selain itu, pendekatan OOP juga memungkinkan penggunaan kembali kode dengan cara membuat objek baru dari kelas yang sama.

PySimpleGUI dan pyperclip:

	PySimpleGUI adalah sebuah framework GUI sederhana yang memudahkan pembuatan aplikasi desktop.pyperclip adalah pustaka Python yang memungkinkan kita mengakses clipboard sistem operasi secara lintas-platform.

- Persyaratan
Python 3.x terinstal di sistem . Jika belum, dapat mengunduhnya dari situs resmi Python di python.org.

- Instalasi PySimpleGUI:
1. Buka terminal atau command prompt.
2. Ketik perintah berikut untuk menginstal PySimpleGUI menggunakan pip:
   "pip install PySimpleGUI"
3. Tunggu hingga proses instalasi selesai.

- Instalasi pyperclip
1. Buka terminal atau command prompt.
2. Ketik perintah berikut untuk menginstal pyperclip menggunakan pip:
   "pip install pyperclip"
3. Tunggu hingga proses instalasi selesai.

- Verifikasi Instalasi
 Verifikasi instalasi dengan mengimpor modul PySimpleGUI dan pyperclip ke dalam skrip Python dan menjalankan kode sederhana. 
