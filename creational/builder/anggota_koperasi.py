# anggota_koperasi.py

class AnggotaKoperasi:
    def __init__(self):
        self.nama = ""
        self.alamat = ""
        self.tanggal_bergabung = ""
        self.saldo_tabungan = 0.0

    def __str__(self):
        return f"Nama: {self.nama}, Alamat: {self.alamat}, Bergabung: {self.tanggal_bergabung}, Saldo: {self.saldo_tabungan}"
