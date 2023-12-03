from datetime import datetime, timedelta

class AntrianRumahSakit:
    def __init__(self):
        self.antrian = []
        self.waktu_pertama_masuk = None
        self.waktu_per_pasien = timedelta(minutes=10)

    def daftar_antrian(self):
        nomor_antrian = len(self.antrian) + 1
        waktu_masuk = datetime.now()

        if not self.waktu_pertama_masuk:
            self.waktu_pertama_masuk = waktu_masuk

        self.antrian.append((nomor_antrian, waktu_masuk))

        print(f"Selamat datang! Nomor Antrian Anda: {nomor_antrian}")
        print(f"Jumlah Antrian Saat Ini: {len(self.antrian)}\n")

    def perkiraan_waktu_tunggu(self, nomor_antrian):
        if nomor_antrian <= len(self.antrian):
            waktu_masuk_pasien_ini = self.antrian[nomor_antrian - 1][1]
            waktu_tunggu = (datetime.now() - waktu_masuk_pasien_ini).total_seconds() / 60.0
            waktu_estimasi = len(self.antrian) * self.waktu_per_pasien.total_seconds() / 60.0

            print(f"Nomor Antrian: {nomor_antrian}")
            print(f"Perkiraan Waktu Tunggu: {waktu_tunggu:.2f} menit")
            print(f"Estimasi Waktu Tunggu Seluruh Antrian: {waktu_estimasi:.2f} menit\n")
        else:
            print("Nomor Antrian tidak valid. Silakan cek nomor antrian Anda.\n")

# Contoh Penggunaan
rumah_sakit = AntrianRumahSakit()

# Pasien 1 mendaftar antrian
rumah_sakit.daftar_antrian()

# Pasien 2 mendaftar antrian
rumah_sakit.daftar_antrian()

# Pasien 3 mendaftar antrian
rumah_sakit.daftar_antrian()

# Cek perkiraan waktu tunggu untuk Pasien 2
rumah_sakit.perkiraan_waktu_tunggu(2)

# Cek perkiraan waktu tunggu untuk Pasien 1
rumah_sakit.perkiraan_waktu_tunggu(1)
