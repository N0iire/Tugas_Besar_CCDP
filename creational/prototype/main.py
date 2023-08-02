from membership_manager import MembershipManager

def main():
    manager = MembershipManager()

    # Tambahkan anggota baru
    manager.add_member("John Doe", 30, "Jl. Jend. Sudirman 123")
    manager.add_member("Jane Smith", 25, "Jl. Gatot Subroto 456")

    # Dapatkan semua anggota
    all_members = manager.get_all_members()
    print("Semua anggota:")
    for member in all_members:
        print(f"{member.name}, {member.age} tahun, {member.address}")

    # Klone anggota pertama
    cloned_member = manager.clone_member(0)
    if cloned_member:
        print("\nAnggota pertama yang diklon:")
        print(f"{cloned_member.name}, {cloned_member.age} tahun, {cloned_member.address}")
    else:
        print("\nAnggota tidak ditemukan")

if __name__ == "__main__":
    main()
