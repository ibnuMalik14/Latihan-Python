class Transaksi:
    def __init__(self) :
        self.daftar_transaksi = []
    
    def input_transaksi(self, nama_pelanggan, total_harga, dp, status):
        data_transaksi = {
            'nama_pelanggan' : nama_pelanggan,
            'total_harga' : total_harga,
            'dp' : dp,
            'status' : status
        }
        self.daftar_transaksi.append(data_transaksi)
        print(f"Data transaksi {status} berhasil ditambahkan. \n")
    def proses_data(self, status='Lunas', nama_pelanggan=None):
        if nama_pelanggan:
            transaksi_tertentu = [transaksi for transaksi in self.daftar_transaksi
                                  if transaksi['nama_pelanggan'] == nama_pelanggan and transaksi['status'] == status]
            if transaksi_tertentu:
                print(f"Proses data transaksi {status} untuk pelanggan {nama_pelanggan}: ")
                for transaksi in transaksi_tertentu:
                    print(transaksi)
                print()
            else:
                print(f"tidak ada data transaksi {status} untuk pelanggan {nama_pelanggan}")
        else:
            transaksi_status = [transaksi for transaksi in self.daftar_transaksi if transaksi['status'] == status]
            if transaksi_status:
                print(f"Proses data transaksi {status}: ")
                for transaksi in transaksi_status:
                    print(transaksi)
                print()
            else:
                print(f"Tidak ada ddata transaksi {status}.\n")

transaksi_online_shop = Transaksi()

#Input DP untuk pelanggan A
transaksi_online_shop.input_transaksi('Pelanggan A', 5000000, 2000000, 'Belum lunas')

#Input pelunasan untuk pelanggan B
transaksi_online_shop.input_transaksi('Pelanggan B', 8000000, 8000000, 'Lunas')

#Proses data transaksi yang sudah lunas
transaksi_online_shop.proses_data(status='Lunas')

# Proses data transaksi untuk pelanggan A
transaksi_online_shop.proses_data(nama_pelanggan='Pelanggan A')



























