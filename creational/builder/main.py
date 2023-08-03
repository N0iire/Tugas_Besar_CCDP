# main.py
from anggota_koperasi_builder import AnggotaKoperasiBuilder

def main():
    builder = AnggotaKoperasiBuilder()

    anggota1 = builder.set_nama("John Doe")\
                     .set_alamat("Jl. Contoh No. 123")\
                     .set_tanggal_bergabung("2023-08-01")\
                     .set_saldo_tabungan(5000000)\
                     .build()

    builder = AnggotaKoperasiBuilder()  # Buat objek builder baru untuk anggota kedua

    anggota2 = builder.set_nama("Jane Smith")\
                     .set_alamat("Jl. Akses No. 456")\
                     .set_tanggal_bergabung("2022-12-15")\
                     .set_saldo_tabungan(7500000)\
                     .build()

    print("Data Anggota Koperasi:")
    print(anggota1)
    print(anggota2)

if __name__ == "__main__":
    main()
