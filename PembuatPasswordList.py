import random               
#kode untuk menginport/memasukkan fungsi random yang akan menghasilkan bilangan, huruf, ataupun simbol random pada proses pembuatan password
import string               
#kode untuk menginport fungsi string yang mengandung koleksi string untuk penyusunan password yang formatnya akan berupa string
import PySimpleGUI as sg    
#kode untuk menginport GUI (tampilan)
import pyperclip            
#kode untuk menginport fungsi pyperclip untuk dapat melakukan copy paste pada password yang telah dibuat nantinya


class PembuatPassword:                          
    #penginisialisasian kelas PembuatPassword
    def __init__(self, panjang, kombinasi):     
    #fungsi init yang menginisialisasi metode panjang dan kombinasi
        self.panjang = panjang                  
        #penginisialisasian panjang (panjang password)
        self.kombinasi = kombinasi              
        #penginisialisasian kombinasi (kombinasi password yang dapat terdiri dari beberapa komponen)

    def buat_password(self):                                
    #fungsi untuk memasukkan logika pada pembuatan password
        if self.panjang < 8:                                
            #logika untuk panjang password kurang dari 8, jika benar maka kode akan dijalankan seperti di bawah ini
            sg.popup_ok(                                    
                #untuk menampilkan pop up jika panjang yang diinput < 8
                "Panjang password minimal 8 karakter!",     
                #pop yang muncul apabila logika di atas true
                button_color=("white", "green"),            
                #sebagai warna dari tombol yang akan ditampilkan, yaitu ada warna putih dan hijau
                text_color=("black"),                       
                #sebagai warna dari tulisan yang akan ditampilkan 
                background_color=("lightblue"),             
                #sebagai warna tampilan dari program 
            )
            return      
            #berfungsi untuk mengembalikan nilai

        if self.panjang > 20:                               
        #logika untuk panjang password lebih dari 20, jika benar maka kode akan dijalankan seperti di bawah ini
            sg.popup_ok(                                    
            #untuk menampilkan pop up jika panjang yang diinput > 20
                "Panjang password maksimal 20 karakter!",   
                #pop yang muncul apabila logika di atas true
                button_color=("white", "green"),            
                #sebagai warna dari tombol yang akan ditampilkan, yaitu ada warna putih dan hijau
                text_color=("black"),                       
                #sebagai warna dari tulisan yang akan ditampilkan 
                background_color=("lightblue"),             
                #sebagai warna tampilan dari program 
            )
            return      
        #berfungsi untuk mengembalikan nilai

        kombinasi_terpilih = []                                 
        #penginisialisasian array untuk kombinasi yang terpilih nantinya (dipilih oleh user) dan akan ditampilkan pada kotak yang dapat dicentang
        if self.kombinasi["kapital"]:                           
        #logika pilihan apabila kombinasi yang dipilih berupa huruf kapital
            kombinasi_terpilih.append(string.ascii_uppercase)   
            #apabila logika di atas true, maka akan memunculkan string dengan huruf kapital secara acak
        if self.kombinasi["kecil"]:                             
        #logika pilihan apabila kombinasi yang dipilih berupa huruf kapital
            kombinasi_terpilih.append(string.ascii_lowercase)   
            #apabila logika di atas true, maka akan memunculkan string dengan huruf kecil secara acak
        if self.kombinasi["angka"]:                             
        #logika pilihan apabila kombinasi yang dipilih berupa angka
            kombinasi_terpilih.append(string.digits)            
            #apabila logika di atas true, maka akan memunculkan string angka secara acak
        if self.kombinasi["simbol"]:                            
        #logika pilihan apabila kombinasi yang dipilih berupa simbol
            kombinasi_terpilih.append(string.punctuation)       
            #apabila logika di atas true, maka akan memunculkan string simbol-simbol secara acak

        if not kombinasi_terpilih:      
        #logika jika tidak ada kombinasi yang dipilih (dicentang)
            sg.popup_ok(        
            #penginisialisasian untuk tampilan yang akan dikeluarkan
                "Harap pilih minimal satu kombinasi karakter!",    
                #pop up yang muncul berupa string seperti kode di atas
                button_color=("white", "green"),    
                #sebagai warna dari tombol yang akan ditampilkan, yaitu ada warna putih dan hijau
                text_color=("black"),   
                #sebagai warna dari tulisan yang akan ditampilkan 
                background_color=("lightblue"),  
                #sebagai warna tampilan dari program    
            )
            return      
        #berfungsi untuk mengembalikan nilai

        password = []    
        #Inisialisasi variabel password sebagai sebuah list kosong yang akan digunakan untuk menyimpan karakter-karakter dari password yang dibuat.   
        for _ in range(self.panjang):   
        #Melakukan iterasi sebanyak self.panjang kali, dimana self.panjang adalah variabel yang menentukan panjang dari password yang akan dibuat
            char_pool = random.choice(kombinasi_terpilih)   
            #Memilih secara acak satu dari kombinasi karakter yang terpilih (diasumsikan variabel kombinasi_terpilih berisi daftar kombinasi karakter yang telah ditentukan sebelumnya).
            password.append(random.choice(char_pool))       
            #Memilih secara acak satu karakter dari char_pool (kombinasi karakter terpilih) dan menambahkannya ke dalam list password.

        random.shuffle(password)       
        #Mengacak urutan karakter-karakter dalam list password secara acak.
        password = "".join(password)   
        #Menggabungkan semua karakter dalam list password menjadi sebuah string tunggal.
        return password     
        #Mengembalikan password yang telah dibuat sebagai hasil dari fungsi ini.


class GUIPassword:      
#penginisialisasian kelas GUIPassword
    def __init__(self): 
    #penginisialisasian metode init untuk kelas GUIPassword  
        self.layout = [     
        #Inisialisasi variabel layout sebagai sebuah list yang berisi elemen-elemen tampilan antarmuka pengguna menggunakan library PySimpleGUI.
            [sg.Text("Panjang Password :", text_color=("black"), background_color=("lightblue")), sg.Input(key="PANJANG")],     
            #Membuat elemen teks "Panjang Password" dan elemen input yang digunakan untuk mengambil panjang password dari pengguna. Key "PANJANG" digunakan untuk mengidentifikasi elemen ini dalam program.
            [sg.Checkbox("Huruf Kapital", key="kapital", text_color=("black"), background_color=("lightblue"), pad=((100, 10), (10, 10))), sg.Checkbox("Huruf Kecil", key="kecil", text_color=("black"), background_color=("lightblue"), pad=((25, 10), (10, 10)))],    
            #Membuat dua elemen checkbox untuk memungkinkan pengguna memilih apakah password harus mengandung huruf kapital atau huruf kecil.
            [sg.Checkbox("Angka", key="angka", text_color=("black"), background_color=("lightblue"), pad=((100, 10), (10, 10))), sg.Checkbox("Simbol", key="simbol", text_color=("black"), background_color=("lightblue"), pad=((62, 10), (10, 10)))],  
            #Membuat dua elemen checkbox untuk memungkinkan pengguna memilih apakah password harus mengandung angka atau simbol.
            [sg.Button("Buat Password", button_color=("white", "green"), pad=((170, 10), (0, 10)))],    
            #Membuat tombol "Buat Password" yang akan digunakan untuk memulai pembuatan password.
            [sg.Text("Password :", text_color=("black"), background_color=("lightblue"), pad=((55, 10), (10, 10))), sg.Input(key="PASSWORD", disabled=True, pad=((0, 10), (10, 10)))],  
            #Membuat elemen teks "Password" dan elemen input yang akan menampilkan password yang dibuat dan diaktifkan agar tidak dapat diedit oleh pengguna.
            [sg.Text("Daftar Password", text_color=("black"), background_color=("lightblue"), pad=((160, 0), (0, 0)))],     
            #Membuat elemen teks "Daftar Password" untuk menampilkan label daftar password yang telah dibuat sebelumnya.
            [sg.Listbox([], size=(40, 4), key="PASSWORD_LIST", pad=((70, 0), (0, 0)))],         
            #Membuat elemen listbox kosong yang akan menampilkan daftar password yang telah dibuat sebelumnya. Key "PASSWORD_LIST" digunakan untuk mengidentifikasi elemen ini dalam program.
            [sg.Button("Salin", button_color=("white", "blue"), pad=((200, 10), (10, 10)))],    
            #Membuat tombol "Salin" yang akan digunakan untuk menyalin password yang dipilih dari daftar password.
            [sg.Button("Keluar", button_color=("white", "firebrick"), pad=((370, 10), (10, 10)))],      
            #Membuat tombol "Keluar" yang akan digunakan untuk keluar dari program.
        ]
        self.window = sg.Window("Pembuat Password", self.layout, size=(450, 390), background_color=("lightblue"))       
        #Membuat jendela aplikasi dengan judul "Pembuat Password" menggunakan PySimpleGUI dengan menggunakan layout yang telah didefinisikan sebelumnya. Jendela memiliki ukuran 450x390 piksel dan latar belakang berwarna biru muda (light blue).
        self.daftar_password = []       
        #Inisialisasi variabel daftar_password sebagai sebuah list kosong yang akan digunakan untuk menyimpan daftar password yang telah dibuat sebelumnya.

    def update_daftar_password(self, password):
    #Deklarasi metode/fungsi update_daftar_password yang digunakan untuk memperbarui daftar password dengan password baru yang diberikan.
        self.daftar_password.append(password)
        #Menambahkan password baru ke dalam list daftar_password menggunakan metode append(). Dengan demikian, password baru akan ditambahkan ke akhir daftar.
        self.window["PASSWORD_LIST"].update(values=self.daftar_password)
        #Memperbarui nilai dari elemen listbox "PASSWORD_LIST" pada jendela dengan menggunakan metode update() dari objek self.window. Nilai elemen listbox diupdate dengan menggunakan list self.daftar_password sehingga daftar password yang ditampilkan akan diperbarui dengan password baru yang telah ditambahkan.

    def jalankan(self):
    #Deklarasi metode jalankan yang akan menjalankan aplikasi dan menangani interaksi pengguna.
        while True:
        #kondisi apabila true, maka akan program akan menjalankan kode di bawah ini
            event, values = self.window.read()
            #Membaca input pengguna dari jendela aplikasi menggunakan metode read() dari objek self.window. event berisi event yang terjadi (misalnya, tombol yang ditekan) dan values berisi nilai-nilai dari elemen-elemen dalam jendela.
            if event == "Keluar" or event == sg.WINDOW_CLOSED:
            #Memeriksa apakah event yang terjadi adalah "Keluar" (tombol "Keluar" ditekan) atau event sg.WINDOW_CLOSED (jendela ditutup). Jika ya, maka loop akan dihentikan dengan menggunakan break, sehingga program keluar dari loop dan berhenti.
                break
                #menghentikan program apabila kondisi sudah memenuhi (menekan tombol "keluar")
            elif event == "Buat Password":
            #Memeriksa apakah event yang terjadi adalah "Buat Password" (tombol "Buat Password" ditekan).
                input_panjang = values["PANJANG"]
                #jika bernilai true, maka nilai input_panjang akan diisi dengan nilai dari input pengguna pada elemen dengan key "PANJANG". 
                kombinasi = {
                #penginisialisasian variabel kombinasi yang berisi dictionary yang berisi nilai-nilai dari checkbox-checkbox 
                    "kapital": values["kapital"],
                    #key kapital
                    "kecil": values["kecil"],
                    #key kecil
                    "angka": values["angka"],
                    #key angka
                    "simbol": values["simbol"],
                    #key simbol
                }

                if not input_panjang:
                #kondisi jika pengguna tidak menginputkan panjang password yang diinginkan, maka kode akan berjalan seperti di bawah ini.
                    sg.popup_ok(
                    #kode untuk menampilkan pop up pesan
                        "Harap masukkan panjang password!",
                        #pesan yang ditampilkan
                        button_color=("white", "green"),
                        #warna tombol yang digunakan, yaitu hijau
                        text_color=("black"),
                        #warna font yang digunakan, yaitu hitam
                        background_color=("lightblue"),
                        #warna background,yaitu light blue
                    )
                    continue
                    #Melanjutkan iterasi berikutnya dalam loop while saat ini yang akan membawa program kembali ke awal loop dan menunggu input pengguna berikutnya.
                try:
                    panjang = int(input_panjang)
                    #menginput nilai panjang dengan tipe data int (bilangan bulat)
                except ValueError:
                #Jika terjadi ValueError saat mencoba mengubah nilai input_panjang menjadi bilangan bulat, artinya karakter yang dimasukkan oleh pengguna tidak valid, maka program akan menjalankan program di bawah ini.
                    sg.popup_ok(
                    #kode untuk menampilkan pop up pesan
                        "Karakter yang dimasukkan tidak valid!",
                        #pesan yang ditampilkan
                        button_color=("white", "green"),
                        #warna tombol yang digunakan, yaitu hijau
                        text_color=("black"),
                        #warna font yang digunakan, yaitu hitam
                        background_color=("lightblue"),
                        #warna background,yaitu light blue
                    )
                    continue
                    #Melanjutkan iterasi berikutnya dalam loop while saat ini yang akan membawa program kembali ke awal loop dan menunggu input pengguna berikutnya.

                generator = PembuatPassword(panjang, kombinasi)
                #Membuat objek PembuatPassword dengan menggunakan nilai panjang (panjang password) dan kombinasi (dict yang menunjukkan jenis karakter apa yang harus ada dalam password) sebagai argumen. Objek generator akan digunakan untuk membuat password baru.
                password = generator.buat_password()
                #Menggunakan objek generator untuk memanggil metode buat_password(), yang akan menghasilkan password baru berdasarkan panjang dan kombinasi yang telah ditentukan. Password tersebut akan disimpan dalam variabel password.
                if password:
                #Memeriksa apakah password tidak kosong (berarti password berhasil dibuat). Jika true, maka kode di dalam blok ini akan dieksekusi.
                    self.window["PASSWORD"].update(password)
                    #metode update() digunakan untuk memperbarui nilai elemen input "PASSWORD" pada jendela dengan nilai password baru yang dibuat.
                    self.update_daftar_password(password)
                    #metode update_daftar_password() dipanggil untuk memperbarui daftar password dengan password baru yang telah dibuat menggunakan objek self.daftar_password.
            elif event == "Salin":
            #kondisi jika tombol salin ditekan, maka kode di bawah ini akan berjalan
                password_terpilih = self.window["PASSWORD_LIST"].get()
                #Mengambil nilai yang terpilih dari elemen listbox "PASSWORD_LIST" pada jendela menggunakan metode get() dari objek self.window. Nilai yang terpilih akan disimpan dalam variabel password_terpilih.
                if password_terpilih:
                #Memeriksa apakah password_terpilih tidak kosong (berarti ada password yang terpilih).
                    password_terpilih = password_terpilih[0]
                    #Mengambil password yang terpilih dari list password_terpilih. Karena password_terpilih adalah list, maka akan mengambil elemen pertama (indeks 0) dari list tersebut.
                    pyperclip.copy(password_terpilih)
                    #Menggunakan modul pyperclip untuk menyalin password yang terpilih ke clipboard sistem.

        self.window.close()
        #Menutup jendela aplikasi menggunakan metode close() dari objek self.window, yang akan menghentikan eksekusi program dan menutup jendela aplikasi.


if __name__ == "__main__":
#pengecekan yang dilakukan untuk memastikan bahwa kode di bawahnya hanya akan dieksekusi jika file ini dijalankan langsung sebagai program utama, bukan sebagai modul yang diimpor oleh file lain.
    gui = GUIPassword()
    #Membuat objek gui dari kelas GUIPassword yang telah didefinisikan sebelumnya.
    gui.jalankan()
    #Memanggil metode jalankan() pada objek gui untuk menjalankan aplikasi, yang akan memulai loop yang terus berjalan hingga pengguna menekan tombol "Keluar" atau menutup jendela aplikasi.

#    Nama Anggota Kelompok :
# 1. Rana Qonitah Helida    (G1A022017)
# 2. Arya Mulahernawan      (G1A022029)
# 3. David Thimotius Rarung (G1A022045)