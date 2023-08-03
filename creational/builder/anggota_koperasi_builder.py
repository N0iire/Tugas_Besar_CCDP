# anggota_koperasi_builder.py
from anggota_koperasi import AnggotaKoperasi

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
