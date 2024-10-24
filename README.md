# Final Submission : Machine Learning Pipeline - Online Retail Customer Churn
Nama: Bagas Dwi Santosa

Username dicoding: bagasdwisss


| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Online Retail Customer Churn Dataset](https://www.kaggle.com/datasets/hassaneskikri/online-retail-customer-churn-dataset) |
| Masalah | Dalam industri ritel, churn atau kehilangan pelanggan merupakan masalah signifikan yang dapat berdampak langsung pada pendapatan dan pertumbuhan bisnis. Dataset Online Retail Customer Churn menyediakan informasi tentang transaksi pelanggan, termasuk data demografis dan perilaku pembelian. Analisis churn pelanggan penting untuk memahami faktor-faktor yang mempengaruhi keputusan pelanggan untuk berhenti berbelanja dan membantu perusahaan merumuskan strategi retensi yang lebih baik. |
| Solusi machine learning | Solusi yang akan dibuat adalah model prediksi churn pelanggan menggunakan algoritma machine learning. Model ini akan memanfaatkan data historis untuk mengidentifikasi pelanggan yang berpotensi melakukan churn dan memberikan rekomendasi tindakan pencegahan untuk meningkatkan retensi pelanggan. Metode yang akan digunakan mencakup pengelompokan, klasifikasi, dan analisis faktor. |
| Arsitektur model | Untuk arsitektur model sendiri, untuk tiap layer menggunakan Dense 256, Dense 64, Dense 16 dengan activation relu, kemudian layer terakhir menggunakan Dense 1 dengan activation sigmoid karena akan mengklasifikasi class yang hanya memiliki dua value yaitu churn dan tidak chrun. Untuk model compile menggunakan optimizers Adam dengan learning_rate 0.001, loss binary_crossentropy dengan metrics BinaryAccuracy |
| Metrik evaluasi | Metrik evaluasi yang digunakan yaitu AUC, Precision, Recall, ExampleCount dan BinaryAccuracy |
| Performa model | Untuk performa model, ditinjau dari accuracy dan lossnya, accuracy yang didapatkan terbilang tinggi dengan accuracy 1.0000 pada proses training dan validation, dan loss yang didapatkan pada proses training dan validation yaitu 9.4975.|
| Opsi deployment | Untuk deployment, sistem ini akan dideploy menggunakan platform railway |
| Web app | [customer-model](https://ml-ops-production-021e.up.railway.app/v1/models/customer-model/metadata)|
| Monitoring | Monitoring pada sistem ini dilakukan menggunakan prometheus. Disini hanya dilakukan proses monitoring untuk menampilkan request yang masuk pada sistem yang akan menamplkan status pada tiap request yang dilakukan, pada sistem ini terdapat tiga status yang ditampilkan yaitu apabila proses request pada sistem klasifikasi not found, invalid argument dan proses klasifikasi berhasil ditandakan dengan ok |
