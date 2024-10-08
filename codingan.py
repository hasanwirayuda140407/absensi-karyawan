
# Data absensi (nama: kehadiran)
absensi = {}

# Daftar karyawan
karyawan_list = ['Alif', 'Faris', 'Yuda', 'Farid', 'Alfin']

# Menginput kehadiran dari pengguna
for karyawan in karyawan_list:
    kehadiran = input(f"Apakah {karyawan} hadir? (ya/tidak): ").strip().lower()
    if kehadiran == 'ya':
        absensi[karyawan] = True
    else:
        absensi[karyawan] = False

# Menghitung jumlah kehadiran dan total karyawan
jumlah_hadir = sum(absensi.values())
total_karyawan = len(absensi)

# Menghitung persentase kehadiran
persentase_hadir = (jumlah_hadir / total_karyawan) * 100

# Menampilkan hasil
print(f"\nJumlah Karyawan Hadir: {jumlah_hadir}/{total_karyawan}")
print(f"Persentase Kehadiran: {persentase_hadir:.2f}%")

if jumlah_hadir == total_karyawan:
    print("Semua Karyawan Hadir")
elif jumlah_hadir == 0:
    print("Semua Karyawan Tidak Hadir")
else:
    print("Sebagian Karyawan Tidak Hadir")
