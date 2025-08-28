limit = 0
data_name = []
data_tugas = []
data_UTS = []
data_UAS = []
data_nilai_akhir = []
data_status = []
status = ""
number = 0
no = 0
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "python123":
        print("Password benar")
        print("="*10,"SELAMAT DATANG","="*10)
        break
    else:
        print("password salah")
        limit += 1
        print(f"sisa percobaan {limit}/10")
        if limit == 10:
            print("Silahkan coba lagi nanti")
            break
        continue

jumlah_siswa = int(input("Masukkan jumlah siswa : "))

for i in range(jumlah_siswa):
    name = input(f"Masukkan nama Mahasiswa {number+1} : ").upper()
    number +=1
    data_name.append(name)
    while True:    
        nilai_tugas = float(input("Masukkan nilai tugas: "))
        data_tugas.append(nilai_tugas)
        nilai_UTS = float(input("Masukkan nilai UTS : "))
        data_UTS.append(nilai_UTS)
        nilai_UAS = float(input("Masukkan nilai UAS : "))
        data_UAS.append(nilai_UAS)
        if nilai_tugas >100 or nilai_UTS >100 or nilai_UAS >100:
            print("Nilai hanya bisa 0-100")
        else:
            break

    nilai_akhir = 0.3*nilai_tugas + 0.3*nilai_UTS + 0.4*nilai_UAS
    data_nilai_akhir.append(nilai_akhir)
    if nilai_akhir >= 80:
        status = "LULUS SEMPURNA\033[92m"
    elif nilai_akhir >= 60:
        status = "LULUS\033[33m"
    else:
        status = "GAGAL\033[91m"

    data_status.append(status)
print("""
+----+----------------------+-------+-------+-------+-------+-------+
| NO | NAMA MAHASISWA       | TUGAS |  UTS  |  UAS  |  NA   | STATUS |
+----+----------------------+-------+-------+-------+-------+-------+""")
for Name,Tgs,UTS,UAS,NA,ST in zip(data_name,data_tugas,data_UTS,data_UAS,data_nilai_akhir,data_status):
    print(f"""| {str(no).ljust(2)} | {Name.ljust(20)} | {str(Tgs).center(5)} | {str(UTS).center(5)} | {str(UAS).center(5)} | {str(NA).center(5)} | {ST.ljust(10)} |""")
    print("+----+----------------------+-------+-------+-------+-------+-------+")
    no += 1
print(f"Total mahasiswa {no}")
ans = sum(data_nilai_akhir)
nilai_rata_rata = (ans)/ jumlah_siswa
print(f"Nilai rata rata akhir seluruh mahasiswa adalah {nilai_rata_rata}")
print(f"""
Mahasiswa yang lulus sempurna : {data_status.count("LULUS SEMPURNA\033[92m")} Mahasiswa
Mahasiswa yang lulus : {data_status.count("LULUS\033[33m")} Mahasiswa
Mahasiswa yang gagal : {data_status.count("GAGAL\033[91m")} Mahasiswa
""")