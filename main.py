print('Program Toko Premium Orlando')

print('+============================+')

#nama Awal
member = ['Abi, Abu, Avi, Hassan, Sinta, Frida']

print('Halo, Selamat datang di toko kue Kami')
nama = input('Silahkan Masukkan Nama anda : ')
print()
print('++' + '-' * 5,'=' * 20,'-' * 5 + '++')
print('Terimakasih telah Memasukkan Nama anda, dengan ini anda sudah masuk ke dalam Daftar Pembeli')
print('++' + '-' * 5,'=' * 20,'-' * 5 + '++')
print()
member.append(nama)
print(member)

print('Untuk Keamanan silahkan Type nama anda Sekali Lagi')
namaVerivy = input()

if namaVerivy in member:

    #deklarasi Variabel
    pil1 = 'Es Teh Bintang Lima'
    pil2 = 'Ayam Tepung Sultan'
    pil3 = 'Kopi Hitam Jon Santana'
    pil4 = 'Indomie King Arthur'
    pil5 = 'Ketoprak Hijau'
    pil6 = 'Air Putih Queen Elizabeth'
    pil7 = 'Sandal Michael jackson'
    pil8 = 'Sorban Saddam Husin'
    pil9 = 'Sapu Ajaib'
    pil10 = 'Sandal Hermes'

    #Print Menu
    print('Nama Terverifikasi, Silahkan Pilih Menu yang anda inginkan')
    print('+' + '=' * 20 + '+')
    print('1). Es Teh Bintang Lima      \t 15000')
    print('2). Ayam Tepung Sultan       \t 25000')
    print('3). Kopi Hitam Jon Santana   \t 10000')
    print('4). Indomie King Arthur      \t 30000')
    print('5). Ketoprak Hijau           \t 12000')
    print('6). Air Putih Queen Elizabeth \t 15000')
    print('7). Sandal Michael jackson   \t 100000')
    print('8). Sorban Saddam Husin      \t 100000')
    print('9). Sapu Ajaib               \t 150000')
    print('10). Sandal Hermes            \t 150000')
    print('+' + '=' * 20 + '+')

#while True:
    pilihan = input('Pilih Nomor Barang yang anda Inginkan: ')
    print('-----------------------------------------------------------')

    if pilihan == '1':
        print('Anda Membeli ' + pil1)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil1)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 15000:
            print('Terimakasih Telah Membeli ' + pil1)

        else:
            print('anda Salah Menginput Harga ' + pil1)

#        break

    elif pilihan == '2':
        print('Anda Membeli ' + pil2)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil2)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 25000:
            print('Terimakasih Telah Membeli ' + pil2)

        else:
            print('anda Salah Menginput Harga ' + pil2)

    elif pilihan == '3':
        print('Anda Membeli ' + pil3)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil3)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 10000:
            print('Terimakasih Telah Membeli ' + pil3)

        else:
            print('anda Salah Menginput Harga ' + pil3)

    elif pilihan == '4':
        print('Anda Membeli ' + pil4)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil4)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 30000:
            print('Terimakasih Telah Membeli ' + pil4)

        else:
            print('anda Salah Menginput Harga ' + pil4)

    elif pilihan == '5':
        print('Anda Membeli ' + pil5)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil5)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 12000:
            print('Terimakasih Telah Membeli ' + pil5)

        else:
            print('anda Salah Menginput Harga ' + pil5)

    elif pilihan == '6':
        print('Anda Membeli ' + pil6)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil6)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 15000:
            print('Terimakasih Telah Membeli ' + pil6)

        else:
            print('anda Salah Menginput Harga ' + pil6)

    elif pilihan == '7':
        print('Anda Membeli ' + pil7)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil7)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 100000:
            print('Terimakasih Telah Membeli ' + pil7)

        else:
            print('anda Salah Menginput Harga ' + pil7)

    elif pilihan == '8':
        print('Anda Membeli ' + pil8)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil8)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 100000:
            print('Terimakasih Telah Membeli ' + pil8)

        else:
            print('anda Salah Menginput Harga ' + pil8)


    elif pilihan == '9':
        print('Anda Membeli ' + pil9)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil9)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 150000:
            print('Terimakasih Telah Membeli ' + pil9)

        else:
            print('anda Salah Menginput Harga ' + pil9)

    elif pilihan == '10':
        print('Anda Membeli ' + pil10)
        print('Harap Bayar dengan Menuliskan Harga Barang ' + pil10)
        harga = int(input())

        print('|' + '=' * 35 + '|')
        if harga == 100000:
            print('Terimakasih Telah Membeli ' + pil10)

        else:
            print('anda Salah Menginput Harga ' + pil10)

    else:
        print('Maaf, Menu yang anda Pilih tidak ada di dalam Daftar Menu')

else:
    print(f'Nama Anda Belum ada di List member, harap Ulang Kembali Program')