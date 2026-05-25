# PRAKTIKUM KECERDASAN BUATAN - ALGORITMA GENETIKA

Repositori ini berisi implementasi algoritma genetik yang dikerjakan pada Praktikum Kecerdasan Buatan. Program ini bertujuan untuk menyelesaikan permasalahan optimasi menggunakan algoritma genetik. Program ini mencakup inisialisasi populasi, evaluasi fitness, seleksi, crossover, dan mutasi.

## Struktur Direktori
- `main.py` : Main program yang berisi implementasi algoritma genetik.
- `populasi.py` : Inisialisasi populasi.
- `evaluasiFitness.py` : Evaluasi fitness untuk setiap individu dalam populasi menggunakan metode fitness evaluation.
- `selection.py` : Seleksi menggunakan tournament selection menggunakan metode tournament selection.
- `crossover.py` : Crossover dengan probabilitas tertentu menggunakan metode one point crossover.
- `mutation.py` : Mutasi dengan probabilitas tertentu menggunakan metode uniform mutation.

## Parameter
Parameter dapat diubah pada fungsi `run_ga` di file `main.py`. Parameter yang dapat diubah adalah sebagai berikut:

- `jumlah_generasi`: Jumlah generasi yang akan dievaluasi. Default: 100.
- `jumlah_populasi`: Jumlah populasi. Default: 50.
- `prob_crossover`: Probabilitas crossover. Default: 0.8.
- `prob_mutasi`: Probabilitas mutasi. Default: 0.03.
- `max_gudang`: Kapasitas maksimum gudang. Default: 15.

## Hasil Uji Coba
![image](/img/Figure_1.png)

Grafik menunjukkan perkembangan nilai fitness pada setiap generasi dalam proses optimasi menggunakan Genetic Algorithm.

- Fitness Tertinggi (biru) stabil pada nilai maksimum 10, menunjukkan algoritma berhasil menemukan dan mempertahankan solusi optimal hingga akhir generasi.
- Fitness Rata-rata (merah) berada di kisaran tinggi mendekati 10, menandakan mayoritas individu dalam populasi memiliki kualitas solusi yang baik dan proses konvergensi berjalan stabil.
- Fitness Terendah (kuning) beberapa kali turun hingga 0 akibat proses mutasi dan eksplorasi populasi yang menghasilkan individu dengan fitness rendah.

Secara keseluruhan, hasil ini menunjukkan bahwa algoritma genetika mampu mencapai solusi optimal dengan cepat, menjaga kualitas populasi secara konsisten, serta tetap mempertahankan keberagaman solusi selama proses evolusi berlangsung.

## Cara Menjalankan Program
1. Clone repository

```bash
git clone https://github.com/kmuiii/H1D024053-PraktikumKB-Pertemuan10.git
```
2. Install library yang dibutuhkan

```bash
pip install numpy matplotlib
```
3. Jalankan program

```bash
python main.py
```