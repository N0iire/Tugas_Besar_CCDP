from individual_member import IndividualMember
from group_member import GroupMember

# Membuat anggota individual
individual1 = IndividualMember("John Doe", 5000)
individual2 = IndividualMember("Jane Smith", 7000)

# Membuat anggota kelompok
group1 = GroupMember("Group A")
group2 = GroupMember("Group B")

# Menambahkan anggota individual ke dalam kelompok
group1.add_member(individual1)
group1.add_member(individual2)

# Menambahkan anggota kelompok ke dalam kelompok lain
group2.add_member(group1)

# Menampilkan data anggota
group2.display()
