🧠 Ekran Süresi ve Zihinsel İyi Oluş İlişkisi Analizi
Bu proje, bir veri setini kullanarak Ekran Süresi, Stres Seviyesi, Uyku Kalitesi ve diğer yaşam tarzı faktörleri ile Zihinsel İyi Oluş Endeksi arasındaki korelasyonları ve ilişkileri inceleyen kapsamlı bir veri analiz çalışmasıdır. Projenin temel amacı, zihinsel sağlık üzerinde en güçlü ve anlamlı etkiye sahip olan faktörleri bilimsel yöntemlerle keşfetmektir.

⚙️ Proje Ortamı ve Kütüphaneler
Bu analiz, Python programlama dili ve veri bilimi için endüstri standardı olan aşağıdaki kütüphaneler kullanılarak gerçekleştirilmiştir:

Pandas: Veri çerçeveleri (DataFrame) ile hızlı veri yükleme, temizleme ve manipülasyonu için.

NumPy: Yüksek performanslı sayısal hesaplamalar ve dizi (array) işlemleri için.

Matplotlib: Grafiklerin temel çizim altyapısını sağlar.

Seaborn: Matplotlib üzerine kurulu olup, istatistiksel görselleştirmeleri daha estetik ve bilgilendirici bir şekilde oluşturmayı sağlar.

📁 Proje Yapısı
Proje dosyaları aşağıdaki temel yapıda düzenlenmiştir. mental_wellness_analysis.py betiği çalıştırıldığında görsel çıktılar otomatik olarak .png formatında kaydedilecektir.

.
├── ScreenTime vs MentalWellness.csv  # Analizin yapıldığı ham veri seti
├── mental_wellness_analysis.py       # Tüm analiz, görselleştirme ve bulguları içeren ana Python kodu
├── README.md                         # Şu an okumakta olduğunuz dosya
└── Görseller/                        # Kod çalıştırıldığında oluşan tüm grafik çıktıları bu klasöre taşınabilir.
    ├── 2_1_temel_degisken_dagilimlari.png
    ├── 3_1_korelasyon_heatmap.png
    └── ... (Diğer tüm grafik çıktıları)


📈 Analiz Adımları ve Temel Bulgular
Proje, mental_wellness_analysis.py dosyasında 4 ana aşamada ilerlemektedir:

1. Veri Ön İşleme (Preprocessing)
Veri seti yüklendi ve Unnamed: 15 gibi gereksiz (boş) sütunlar temizlendi.

describe() ve info() metotları ile sayısal ve kategorik verilerin temel istatistikleri ve veri tipleri kontrol edildi.

İlk Kritik Gözlem: Ortalama Zihinsel İyi Oluş Endeksi'nin düşük (yaklaşık 20) ve Stres Seviyesi'nin ise yüksek (yaklaşık 8.15) olduğu tespit edildi.

2. Keşifçi Veri Analizi (EDA)
Dağılım Analizleri: histplot ve countplot kullanılarak Zihinsel İyi Oluş, Stres Seviyesi ve Uyku Kalitesi gibi değişkenlerin sıklık dağılımları görselleştirildi.

Bu analizler, verinin çarpık yapısını ve çoğu kullanıcının düşük iyi oluş, yüksek stres ve düşük uyku kalitesi bildirdiğini ortaya çıkardı.

3. Korelasyon ve İlişki Analizi
3.1. Korelasyon Matrisi (Heatmap)
Korelasyon analizi ile Zihinsel İyi Oluş Endeksi'ni etkileyen faktörler sayısal olarak belirlendi:

| Değişken | Korelasyon (R) | İlişkinin Yönü ve Gücü |
| Stres Seviyesi | -0.89 | Çok Güçlü Negatif (Stres arttıkça İyi Oluş azalır) |
| Uyku Kalitesi | -0.89 | Çok Güçlü Negatif (Kalite azaldıkça İyi Oluş azalır) |
| Üretkenlik | +0.75 | Güçlü Pozitif (Üretkenlik arttıkça İyi Oluş artar) |
| Toplam Ekran Süresi | -0.74 | Güçlü Negatif (Ekran süresi arttıkça İyi Oluş azalır) |

3.2. Regresyon ve Kutu Grafikleri
Regresyon Grafikleri (regplot): Güçlü ilişkiler (Stres vs. İyi Oluş) grafiksel olarak teyit edildi. Regresyon doğrusunun eğimi, ilişkinin doğrusal olduğunu gösterdi.

Uyku Kalitesi (Boxplot): Uyku Kalitesi puanı 1'den 4'e yükseldikçe, Zihinsel İyi Oluş Endeksi'nin ortanca değerinde dramatik bir artış gözlemlenmiştir. Bu, uyku kalitesinin en güçlü müdahale noktası olduğunu gösteren kritik bir bulgudur.

4. Bulgular Özeti
Kodun son bloğunda, yukarıdaki tüm analizlere dayanarak elde edilen en güçlü pozitif ve negatif korelasyonlar konsola özet tablo olarak yazdırılmıştır.

🚀 Betiği Yerelde Çalıştırma
Projeyi kendi bilgisayarınızda çalıştırmak ve görsel çıktıları üretmek için aşağıdaki adımları izleyin:

Gerekli kütüphaneleri Python ortamınıza kurun:

pip install pandas numpy matplotlib seaborn


ScreenTime vs MentalWellness.csv ve mental_wellness_analysis.py dosyalarını aynı klasöre indirin.

Komut satırında o klasöre gidin ve betiği çalıştırın:

python mental_wellness_analysis.py


Tüm grafikler 7 ayrı .png dosyası olarak klasörünüze kaydedilecektir.
