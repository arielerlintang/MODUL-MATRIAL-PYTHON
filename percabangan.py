6. PERCABANGAN
6.1 If sederhana
nilai = 80

if nilai >= 75:
    print("Lulus")
6.2 If Else
nilai = 60

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
6.3 If Elif Else
nilai = 82

if nilai >= 85:
    print("A")
elif nilai >= 75:
    print("B")
elif nilai >= 65:
    print("C")
else:
    print("D")
6.4 Nested If

Nested if adalah if di dalam if.

Contoh 1
nilai = 85
kehadiran = 90

if nilai >= 75:
    if kehadiran >= 80:
        print("Lulus")
    else:
        print("Tidak lulus karena kehadiran kurang")
else:
    print("Tidak lulus karena nilai kurang")
Contoh 2: penentuan grade kuliah lebih detail
nilai = 88
kehadiran = 85

if kehadiran >= 75:
    if nilai >= 85:
        print("Grade A")
    elif nilai >= 75:
        print("Grade B")
    elif nilai >= 65:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Tidak dapat grade karena kehadiran kurang")
Contoh 3: studi kasus mahasiswa
nilai = 78
kehadiran = 82
tugas = 80

if kehadiran >= 75:
    if tugas >= 70:
        if nilai >= 85:
            print("Nilai Akhir: A")
        elif nilai >= 75:
            print("Nilai Akhir: B")
        elif nilai >= 65:
            print("Nilai Akhir: C")
        else:
            print("Nilai Akhir: D")
    else:
        print("Tugas belum memenuhi syarat")
else:
    print("Kehadiran belum memenuhi syarat")
