# Implementasi-Gerak-Jatuh-Bebas-menggunakan-Python

1. Pendahuluan
Pergerakan suatu objek yang ditembakkan dari ketinggian tertentu dapat didekati
dengan menggunakan konsep gerak peluru. Pada kajian yang sederhana, pergerakan
objek pada gerak peluru dapat dihitung dengan mengabaikan hambatan udara. Untuk
kasus tersebut, percepatan gravitasi pada sumbu 𝑥 dan 𝑦 diformulasikan oleh
persamaan (1) dan (2), dimana 𝑔 adalah percepatan gravitasi yang nilainya 9.806 m/s2.
𝑎% = 0 (1)
𝑎( = −𝑔 (2)
Dengan menggunakan nilai percepatan tersebut, posisi objek dan kecepatan dapat
dihitung secara numerik, sebagaimana ditunjukkan pada persamaan (3) – (6), dimana Δ𝑡
merepresentasikan time step. Adapun kecepatan awal pada sumbu 𝑥 dan 𝑦 dihitung
dengan menggunakan persamaan (7) dan (8), dimana 𝛼 merepresentasikan sudut
tembak.
𝑥(𝑡 + Δ𝑡) = 𝑥(𝑡) + 𝑣%(𝑡 + Δ𝑡)Δ𝑡 (3)
𝑦(𝑡 + Δ𝑡) = 𝑦(𝑡) + 𝑣((𝑡 + Δ𝑡)Δ𝑡 (4)
𝑣%(𝑡 + Δ𝑡) = 𝑣%(𝑡) + 𝑎%Δ𝑡 (5)
𝑣((𝑡 + Δ𝑡) = 𝑣((𝑡) + 𝑎(Δ𝑡 (6)
𝑣%(0) = 𝑣(0) cos 𝛼 (7)
𝑣((0) = 𝑣(0) sin 𝛼 (8)
Untuk memvalidasi hasil perhitungan secara numerik, posisi objek yang didapat perlu
dibandingkan dengan posisi objek yang dihitung secara analitik. Perhitungan posisi objek
secara analitik dapat dilakukan dengan menggunakan persamaan (9) – (10).
𝑥(𝑡) = 𝑥(0) + 𝑣%(0) 𝑡 +
1
2
𝑎%𝑡9 (9)
𝑦(𝑡) = 𝑦(0) + 𝑣((0) 𝑡 −
1
2
𝑎(𝑡9 (10)
Pada kasus yang lebih riil, simulasi gerak peluru perlu mempertimbangkan faktor
hambatan udara yang mempengaruhi pergerakan objek. Secara umum, perhitungan
posisi objek pada gerak peluru dengan mengabaikan atau mempertimbangkan hambatan
udara adalah sama. Perbedaan utama untuk kedua kasus tersebut hanyalah ekspresi
yang digunakan pada percepatan sumbu 𝑥 dan 𝑦 . Untuk kasus kedua, percepatan
gravitasi pada sumbu 𝑥 dan 𝑦 diformulasikan oleh persamaan (11) dan (13), dimana 𝐷
dan 𝑚 berturut-turut merepresentasikan konstanta dan massa objek.
𝑎% = −(𝐷/𝑚)𝑣𝑣% (11)
𝑎( = −𝑔 − (𝐷/𝑚)𝑣𝑣( (12)
𝑣 = =𝑣%
9 + 𝑣(
9 (13)
