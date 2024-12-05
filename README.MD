# Word Count MapReduce pada Pembukaan UUD 1945

Repository ini berisi implementasi MapReduce menggunakan Hadoop Streaming untuk menghitung frekuensi kata (word count) pada teks Pembukaan UUD 1945.

## Deskripsi
Program ini menggunakan Hadoop Streaming untuk memproses teks Pembukaan UUD 1945 dan menghasilkan perhitungan frekuensi kemunculan setiap kata dalam teks tersebut.

## Prerequisite
- Google Colab
- Python 3.x
- Hadoop 3.3.6
- Java 8

## Struktur File
```
├── mapper.py
├── reducer.py
├── pembukaan_uud1945.txt
├── output_word_count.txt
└── README.md
```

## Langkah Pengerjaan

1. **Persiapan Data Input**
   - Copy teks Pembukaan UUD 1945 dari [website DPR](https://www.dpr.go.id/jdih/uu1945)
   - Simpan dalam file `pembukaan_uud1945.txt`

2. **Setup Environment di Google Colab**
   ```python
   !apt-get install openjdk-8-jdk-headless -qq > /dev/null
   !wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
   !tar xf hadoop-3.3.6.tar.gz
   ```

3. **Set Environment Variables**
   ```python
   import os
   os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
   os.environ["HADOOP_HOME"] = "/content/hadoop-3.3.6"
   os.environ["PATH"] = f"{os.environ['HADOOP_HOME']}/bin:{os.environ['PATH']}"
   ```

4. **Eksekusi MapReduce**
   ```python
   !hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
   -files mapper.py,reducer.py \
   -mapper mapper.py \
   -reducer reducer.py \
   -input pembukaan_uud1945.txt \
   -output output_word_count
   ```

## Output
Output berupa file teks yang berisi daftar kata beserta frekuensi kemunculannya dalam format:
```
Bahwa 1
sesungguhnya 1
Kemerdekaan 1
itu 1
...
```

## Kontributor
[Candra Lorensia A]


---
*Note: Repository ini dibuat sebagai bagian dari homework hadoop DigitalSkola*