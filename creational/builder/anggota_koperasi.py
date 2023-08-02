class AnggotaKoperasi:
    def __init__(self):
        self.nama = None
        self.alamat = None
        self.tanggal_bergabung = None
        self.saldo_tabungan = 0

    def __str__(self):
        return f"Anggota: {self.nama}, Alamat: {self.alamat}, Bergabung pada: {self.tanggal_bergabung}, Saldo: {self.saldo_tabungan}"

class AnggotaKoperasiBuilder:
    def __init__(self):
        self.anggota = AnggotaKoperasi()

    def set_nama(self, nama):
        self.anggota.nama = nama
        return self

    def set_alamat(self, alamat):
        self.anggota.alamat = alamat
        return self

    def set_tanggal_bergabung(self, tanggal):
        self.anggota.tanggal_bergabung = tanggal
        return self

    def set_saldo_tabungan(self, saldo):
        self.anggota.saldo_tabungan = saldo
        return self

    def build(self):
        return self.anggota
