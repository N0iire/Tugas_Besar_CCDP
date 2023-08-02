from anggota_koperasi import AnggotaKoperasiBuilder

if __name__ == "__main__":
    builder = AnggotaKoperasiBuilder()

    # Membangun objek anggota dengan builder
    anggota1 = builder.set_nama("John Doe").set_alamat("Jl. Raya 123").set_tanggal_bergabung("2023-08-01").set_saldo_tabungan(1000000).build()

    anggota2 = builder.set_nama("Jane Smith").set_alamat("Jl. Jendral Sudirman 456").set_tanggal_bergabung("2023-07-15").set_saldo_tabungan(500000).build()

    # Menampilkan informasi anggota
    print(anggota1)
    print(anggota2)
